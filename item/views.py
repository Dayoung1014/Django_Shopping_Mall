from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Item, Category
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.
class ItemList(ListView):
    model = Item
    ordering = 'pk' #게시된 순서대로
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        return context

class ItemSearch(ItemList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        item_list = Item.objects.filter(
            Q(name__contains=q)
        ).distinct()
        return item_list

    def get_context_data(self, **kwargs):
        context = super(ItemSearch, self).get_context_data()
        q  = self.kwargs['q']
        context['search_info'] = f'{q}({self.get_queryset().count()})'
        return context

class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

def new_comment(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Item, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.item = item
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(item.get_absolute_url())

    else:
        raise PermissionDenied

def category_page(request, slug):
    if slug == 'no_category' :
        category = '미분류'
        item_list = Item.objects.filter(category=None) #일치하는

    else:
        category = Category.objects.get(slug=slug)
        item_list = Item.objects.filter(category=category)

    return render(request, 'item/item_list.html',
            {
                'item_list' : item_list,
                'categories' : Category.objects.all(),
                'no_category_post_count' : Item.objects.filter(category=None).count(),
                'category' : category
            }
        )

class ItemCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): # 템플릿 : 모델명_form
    model = Item
    fields = ['name', 'description', 'image', 'price', 'company', 'category', 'stock', 'delivery_date']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser) :
            #form.instance.author = current_user
            response =  super(ItemCreate, self).form_valid(form)
            return response
        else :
            return redirect('/item/')

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'description', 'image', 'price', 'company', 'category', 'stock', 'delivery_date']

    template_name = 'item/item_update_form.html'
    def dispatch(self, request, *args, **kwargs):
        current_user = self.request.user
        if request.user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            return super(ItemUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

