from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Session
from .forms import CommentForm, SessionForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def CategoryTag(request, tag):
    context ={}
    context["spot_list"] = Post.objects.all().filter(tag = tag)
    context["tag"] = tag
         
    return render(request, "category_tag.html", context)


class SessionDetail(View):

    def get(self, request):
        context ={}
        context["sessions"] = Session.objects.order_by("-created_on").all()
        context["session_form"] = SessionForm()
        context["session_added"] = False
         
        return render(request, "session_detail.html", context)

    def post(self, request, *args, **kwargs):
        context ={}
        context["sessions"] = Session.objects.order_by("-created_on").all()
        context["session_form"] = SessionForm()
        context["session_added"] = True

        session_form = SessionForm(data=request.POST)
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.save()
        else:
            session_form = SessionForm()
         
        return render(request, "session_detail.html", context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))