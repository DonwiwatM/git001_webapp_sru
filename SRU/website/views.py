from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category  
from .form import PostForm, EditForm
from django.urls import reverse_lazy

class PostView(ListView):
    model = Post
    template_name = 'postpage.html'
    cats = Category.objects.all()
    ordering = ['-post_date']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',''))
    return render(request, 'categories.html', {'cats': cats.replace('-','').title(), 'category_post': category_posts})

def CategoryListView(request, cats):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_postpage.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('postpage')
  

def home(request):
    return render(request, 'home.html', {})

# def login_user(request):
#     #Check to see if logginf in
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # Authenticate
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "You have been logged in")
#             return redirect('home')
#         else:
#             messages.success(request, "There was an error logging in, Please try again..")
#             return redirect('home')
#     else:
#         return render(request, 'home.html', {})


# def logout_user(request):
#     pass