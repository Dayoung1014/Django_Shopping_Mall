from django.shortcuts import render
from item.models import Item, Comment

# Create your views here.
def home_page(request):
    new_products = Item.objects.order_by('-pk')[:3] #최신순 정렬
    return render(request, 'single_pages/home_page.html',
                  {'new_products' : new_products}
                  )

def company_page(request):
    return render(request, 'single_pages/company_page.html')

def mypage(request):
    comment_list = Comment.objects.all()
    return render(request, 'single_pages/mypage.html',
                  {'comment_list' :  comment_list}
                  )

