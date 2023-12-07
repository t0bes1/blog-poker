from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

def post_summary(request):
    """View function for home page of site."""

    mydata = Post.objects.values_list('excerpt')

    context = {
        'data_dump': mydata,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)