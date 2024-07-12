# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('register/', signup_view, name="register"),
    path('signup/', signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_view, name='login'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('profile/', profile, name='profile'),
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
    path('loans/', loans, name='loans'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
