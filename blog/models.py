from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

TAG_CHOICES = [
    ("SP", "Spot"),
    ("SE", "Session"),
    ("PR", "Progress"),
    ]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=20, choices = TAG_CHOICES, default="PR")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


VENUE_CHOICES = [
    ("LN", "London"),
    ("VG", "Vegas"),
    ("WD", "World"),
]

class Session(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="session_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.TextField(max_length=10, unique=True, blank=True)
    venue = models.TextField(choices=VENUE_CHOICES, default="LN")
    length = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    profit_loss = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    notes = models.TextField(blank=True)
    link = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.name