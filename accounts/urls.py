from django.urls import path
from .views import login_page, register_page, activate_email

urlpatterns = [
    path('login/', login_page, name='login' ),
    path('register/', register_page, name='register' ),
    path('activate-email/<email_token>/', activate_email, name='activate-email' ),
]

