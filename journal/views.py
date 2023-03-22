from django.shortcuts import render
from .models import JournalBlog

def home(request):
    data = JournalBlog.objects.all()
    return render(request, 'home.html', {'journal_entries': data})

