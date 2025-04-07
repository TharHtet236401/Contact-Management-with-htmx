from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ContactForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@login_required
def index(request):
    contacts = request.user.contacts.all().order_by("-created_at")
    context = {
        "contacts": contacts,
        "form": ContactForm()
    }
    return render(request, 'contacts.html', context)


@login_required
def search_contacts(request):  
    import time
    time.sleep(2)
    search_query = request.GET.get('search')
    q_object = Q()
    if search_query:
        try:
            q_object = Q(name__icontains=search_query) | Q(email__icontains=search_query)
            contacts = request.user.contacts.filter(q_object).order_by("-created_at")
        except Exception as e:
            contacts = request.user.contacts.all().order_by("-created_at")
            # Optionally log the exception e
    context = {
        "contacts": contacts
    }
    return render(request, 'partials/contacts-list.html', context)



@login_required
@require_http_methods(['POST'])
def add_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        context = {
            "contact": contact
        }
        return render(request, 'partials/contact-row.html', context)
    
