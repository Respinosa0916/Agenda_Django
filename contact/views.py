from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse

def index(request, letter = NULL):
    if letter != NULL:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__contains = request.GET.get('search', ''))
    return render(request, 'contact/index.html', {
        'contacts': contacts
    })

def view(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact/detail.html', {
        'contact': contact
    })

def edit(request, id):
    contact = Contact.objects.get(id=id)

    if(request.method == 'GET'):
        form = ContactForm(instance = contact)
        return render(request, 'contact/edit.html', {
            'form' : form,
            'id' : id
            })
    
    if(request.method == 'POST'):
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        messages.success(request, "Contacto actualizado")
        return render(request, 'contact/edit.html', {
            'form' : form,
            'id' : id
            })
    
def create(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact/create.html', {
            'form': form
        })
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('contact')
    
def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')