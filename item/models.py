from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30) # 상품명
    description = models.TextField() # 상품 설명
    image = models.ImageField(upload_to='item/images/%Y/%m/%d/') # 상품 이미지
    price = models.IntegerField(default=0, blank=True) # 상품 가격
    # 제조사
    # 카테고리
    # 재고 갯수
    # 배송 도착 예정 날짜

    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return f'/item/{self.pk}'