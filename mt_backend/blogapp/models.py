from django.db import models
from authentication.models import Customer

# Create your models here.


class Comment(models.Model):
    content = models.TextField()
    written_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Mention field - upcoming
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    title = models.CharField(max_length=1023, null=True, blank=True)
    content = models.TextField()
    uploaded_by = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='uploaded_by')
    tagged_to = models.ManyToManyField(
        Customer, related_name='tagged_user', blank=True)
    comments = models.ManyToManyField(
        Comment, related_name='blog_comment', blank=True, through='BlogCommentRelation')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.JSONField(null=True, blank=True)


class BlogCommentRelation(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
