from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at', 'is_read')
    search_fields = ('sender__username', 'receiver__username', 'body')
    list_filter = ('is_read', 'created_at')