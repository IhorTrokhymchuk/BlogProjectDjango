from django.contrib import admin

# Register your models here.
# products/admin.py
from django.contrib import admin
from .models import Post, Comment
admin.site.register(Post)
admin.site.register(Comment)