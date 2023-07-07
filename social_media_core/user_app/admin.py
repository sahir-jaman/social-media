from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import PostModel

# Register your models here.
# class PostModelAdmin(admin.ModelAdmin):
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserModelAdmin
#     # that reference specific fields on auth.User.
#     list_display = ["uid", "titile", "description", "user_id", "updated_at", "created_at"]
#     list_filter = ["uid"]
#     fieldsets = [
#         ("Post Credential", {"fields": ["uid", "title"]}),
#         ("Personal info", {"fields": ["description"]}),
#         ("Permissions", {"fields": ["user_id"]}),
#     ]
#     # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["uid", "title", "description", "user_id"],
#             },
#         ),
#     ]
#     search_fields = ["title"]
#     # ordering = ["email","id"]
#     filter_horizontal = []

admin.site.register(PostModel)
