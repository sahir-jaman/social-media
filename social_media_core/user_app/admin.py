from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import PostModel, PostLikeModel, PostCommentModel


# # Register your models here.
admin.site.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "description", "updated_at", "created_at"]
    list_filter = ["uid"]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["title", "description"],
            },
        ),
    ]
    search_fields = ["title"]
    filter_horizontal = []

admin.site.register(PostLikeModel)
class PostLikeModelAdmin(admin.ModelAdmin):
    list_display = ["user", "is_liked"]
    list_filter = ["user"]
    search_fields = ["user"]
    filter_horizontal = []

admin.site.register(PostCommentModel)
class PostCommentModelAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "slug"]
    list_filter = ["user"]
    search_fields = ["user"]
    filter_horizontal = []


# admin.site.register(PostModel, PostModelAdmin)
# admin.site.register(PostLikeModel, PostLikeModelAdmin)
# admin.site.register(PostCommentModel, PostCommentModelAdmin)
