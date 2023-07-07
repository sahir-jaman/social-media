from django.db import models
import uuid
from autoslug import AutoSlugField
from authentication.models import User, UserManager

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
