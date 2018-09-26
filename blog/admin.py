from django.contrib import admin
from .models import Post

# Register your models here.


class ModelAdminPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'details', 'author']


admin.site.register(Post, ModelAdminPost)


