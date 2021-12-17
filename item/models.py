from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from django.contrib.auth.models import User

# Create your models here.

# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/item/category/{self.slug}'

    class Meta:
        verbose_name_plural = "Categories"


# 제조사
class Company(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="제조사 이름")
    address = models.CharField(max_length=200, unique=True, verbose_name="제조사 주소")
    contact_number = PhoneNumberField(unique=True, verbose_name="제조사 연락처")
    contact_email = models.EmailField(max_length=100, verbose_name="제조사 이메일")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


# 상품
class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name="상품 이름")
    description = MarkdownxField()
    image = models.ImageField(upload_to='item/images/%Y/%m/%d/', verbose_name="상품 이미지")
    price = models.IntegerField(default=0, verbose_name="상품 가격")
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE, verbose_name="제조사")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="카테고리")
    stock = models.IntegerField(default=0, verbose_name="상품 재고 갯수")
    delivery_date = models.DateTimeField(default=datetime.now() + timedelta(days=2),
                                         verbose_name="상품 배송 도착 예정 날짜")  # default : 현재 시간부터 2일 뒤

    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return f'/item/{self.pk}'

    def get_description_markdown(self):
        return markdown(self.description)
    
# 댓글
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.item.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/434/9bc8058cdec56c97/svg/{{self.author.email}}'


