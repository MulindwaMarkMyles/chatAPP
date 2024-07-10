from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.user_list_view, name='home'),
    path('send-message/', views.send_message_view, name='send_message'),
    path('send-message/<int:id>/', views.send_message, name='send_message_post'),
    path('inbox/', views.inbox_view, name='inbox'),
]
