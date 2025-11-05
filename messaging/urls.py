from django.urls import path
from .views import inbox_view, compose_view, thread_view

urlpatterns = [
    path('', inbox_view, name='msg_inbox'),
    path('compose/', compose_view, name='msg_compose'),
    path('t/<str:username>/', thread_view, name='msg_thread'),
]
