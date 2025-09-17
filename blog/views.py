from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from blog.models import Post
from .forms import PostForm



class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list_view.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status = 'pub').order_by('-datetime_modified')



class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'




class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'




class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'




class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')


# if request.method == 'POST':
#     post_title = request.POST.get('title')
#     post_text = request.POST.get('text')
#
#     user = User.objects.all()[0]
#     Post.objects.create(title = post_title, text = post_text , author = user , status = 'pub')
#     return redirect('post_list')
#
# else :
#     return render(request,'blog/add_post.html')

# def post_list_view(request):
#     posts_list = Post.objects.filter(status = 'pub').order_by('-datetime_modified')
#     return render(request,'blog/posts_list_view.html',{'posts_list':posts_list})

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html',{'post':post})


# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form=PostForm()
#             return redirect('post_list')
#
#     else:
#         form = PostForm()
#
#     return render(request,'blog/add_post.html',{'form':form})

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None ,instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request,'blog/add_post.html',{'form':form})
# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#
#     return render(request,'blog/post_delete.html',{'post':post})
