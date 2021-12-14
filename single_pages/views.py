from django.shortcuts import render
from item.models import Item

# Create your views here.
def home_page(request):
    #recent_posts = Post.objects.order_by('-pk')[:3] #최신순 정렬
    #return render(request, 'single_pages/landing.html',
                  #{'recent_posts' : recent_posts}
                  #)
    return render(request, 'single_pages/home_page.html')

def company_page(request):
    return render(request, 'single_pages/company_page.html')