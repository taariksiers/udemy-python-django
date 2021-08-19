from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View

from blog.forms import CommentForm, PostForm
from blog.models import Comment, Post


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post

    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post

    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    success_url = reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin, ListView):
    model = Post

    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("-created_at")

####


@login_required(login_url='/accounts/login/')
def add_comments_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/comments_form.html", context={"form": form})


@login_required(login_url='/accounts/login/')
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect("blog:post_detail", pk=comment.post.pk)


@login_required(login_url='/accounts/login/')
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("blog:post_detail", pk=post_pk)


@login_required(login_url='/accounts/login/')
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("blog:post_detail", pk=pk)
