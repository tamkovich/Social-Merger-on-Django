from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    def post_info(self, obj):
        return obj.post

    post_info.short_description = 'Content'


admin.site.register(Post, PostAdmin)
