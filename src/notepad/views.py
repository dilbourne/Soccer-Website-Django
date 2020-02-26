from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Note
from .forms import NoteModelForm
# Create your views here.

def create_view(request):
    # if this view is being called with GET dont call the form
    # form also takes FILES
    # THIS WILL BE SKIPPED WHEN USER FIRST DOEST GET REQUEST FOR notes/create
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # assigned the user who send the request to the model field 'user'
        form.instance.user = request.user
        form.save()
        return redirect('/')
    # SKIPPED FIRST TIME
    context = {
        'form': form
    }
    # this view renders using the 'create.html' template
    # that template gets passed the form as context
    return render(request,"notepad/create.html",context)

def list_view(request):
    notes = Note.objects.all()
    context = {
        'object_list': notes,
        'user': request.user
    }
    return render(request,"notepad/list.html",context)

def delete_view(request, id):
    item_to_delete = Note.objects.filter(pk=id) #return as list
    #should only be one item
    if item_to_delete.exists():
        # the person calling this function is the owner
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()

    return redirect('/notes/list/')

def update_view(request, id):
    # grab specific note here from db
    # get_object_or_404(queryset,pk)
    unique_note = get_object_or_404(Note, pk=id)
    # note instance in form means prepopulated from that instance
    form = NoteModelForm(request.POST or None, request.FILES or None, instance = unique_note)
    if form.is_valid():
        # assigned the user who send the request to the model field 'user'
        form.instance.user = request.user
        form.save()
        return redirect('/notes/list/')
    # SKIPPED FIRST TIME
    context = {
        'form': form
    }
    # this view renders using the 'create.html' template
    # that template gets passed the form as context
    return render(request,"notepad/create.html",context)