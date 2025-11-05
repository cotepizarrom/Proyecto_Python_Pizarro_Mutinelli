from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import Message
from .forms import MessageForm

@login_required
def inbox_view(request):
    # Inbox simple: últimos recibidos primero
    msgs = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messaging/inbox.html', {'messages_list': msgs})

@login_required
def thread_view(request, username):
    other = get_object_or_404(User, username=username)
    qs = Message.objects.filter(
        Q(sender=request.user, receiver=other) | Q(sender=other, receiver=request.user)
    ).order_by('created_at')

    # marcar como leídos los que me enviaron
    Message.objects.filter(sender=other, receiver=request.user, is_read=False).update(is_read=True)

    # formulario para responder en el mismo hilo
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.receiver = other
            msg.save()
            messages.success(request, 'Mensaje enviado.')
            return redirect('msg_thread', username=other.username)
    else:
        form = MessageForm(user=request.user, initial={'receiver': other.id})

    return render(request, 'messaging/thread.html', {'other': other, 'messages_thread': qs, 'form': form})

@login_required
def compose_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, 'Mensaje enviado.')
            return redirect('msg_inbox')
    else:
        form = MessageForm(user=request.user)
    return render(request, 'messaging/compose.html', {'form': form})
