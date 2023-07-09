import uuid
from django.db import models
from autoslug import AutoSlugField
from authentication.models import User

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostModel(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", null=True)


class PostCommentModel(BaseModel):
    user = models.ForeignKey(PostModel, null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="comment", null=True)



class PostLikeModel(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    is_liked = models.BooleanField(default=False)

