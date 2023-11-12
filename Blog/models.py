from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.views.generic import CreateView


def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField()


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'create_blog.html'  # Replace with the actual template name
    success_url = 'create_posts/'  # Replace with the actual URL where you want to redirect after creating a post


def __str__(self):
    return self.title


@receiver(pre_save, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiver(instance):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "_" + instance.title)

    pre_save.connect(pre_save_blog_post_receiver, sender=Post)
