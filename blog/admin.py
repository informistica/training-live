from django.contrib import admin
from .models import BlogPostModel, BlogCommentModel
# Register your models here.

admin.site.register(BlogPostModel,BlogCommentModel)
