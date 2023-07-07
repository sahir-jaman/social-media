from django.contrib import admin
from django.urls import path, include
from user_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.PrivateUserProfileViewDetail.as_view(), name='profile'),
    # path('profile/', include('user_app.urls')),
]
