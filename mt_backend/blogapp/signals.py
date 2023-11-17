from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment


@receiver(post_save, sender=Comment)
def update_blog_on_comment_save(sender, instance, created, **kwargs):
    if created:  # Only perform this for newly created comments
        if instance.blog:
            instance.blog.comments.add(instance)
