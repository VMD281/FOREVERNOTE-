from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .forms import Notesform
from .models import Note
from django.shortcuts import render, get_object_or_404, redirect
def index(request):
    item_list = Note.objects.order_by("-date")
    if request.method == 'POST':
        form = Notesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forevernote_app')
    form = Notesform()
    page = {
        "form" : form,
        "list" : item_list,
        "Title" : "FOREVERNOTE",
        }
    return render(request, 'forevernote_app/index.html', page)

def remove(request, item_id):
    item = Note.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!!!")
    return redirect('forevernote_app')

def edit(request, item_id):
    note = get_object_or_404(Note, id=item_id)
    if request.method == 'POST':
        form = Notesform(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully!")
            return redirect('forevernote_app')
    else:
        form = Notesform(instance=note)
    
    page = {
        'form': form,
        'note': note,
        'Title': 'Edit Note',
    }
    return render(request, 'forevernote_app/edit.html', page)
