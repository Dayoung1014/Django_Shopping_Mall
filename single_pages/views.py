from django.shortcuts import render, redirect
from item.models import Item, Comment, Company, Category
from django.shortcuts import get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def home_page(request):
    new_products = Item.objects.order_by('-pk')[:3] #최신순 정렬
    return render(request, 'single_pages/home_page.html',
                  {'new_products' : new_products}
                  )

def company_page(request):
    company_list = Company.objects.all()
    category_list = Category.objects.all()
    item_list = Item.objects.all()
    return render(request, 'single_pages/company_page.html',
                  {'company_list' : company_list,
                   'category_list' : category_list,
                   'item_list' : item_list}
                  )

def mypage(request):
    item_list = Item.objects.all()
    comment_list = Comment.objects.all()

    return render(request, 'single_pages/mypage.html',
                  {'comment_list' :  comment_list,
                   'item_list' : item_list,}
                  )

def likes_mypage(request, pk): #마이페이지 좋아요 처리
    like_item = get_object_or_404(Item, pk=pk)
    if request.user in like_item.like.all():
        like_item.like.remove(request.user)
        like_item.save()
    else:
        like_item.like.add(request.user)
        like_item.save()
    return redirect('/mypage/')

