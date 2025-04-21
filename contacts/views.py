from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ContactForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Contact
from django.shortcuts import redirect

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
    form = ContactForm(request.POST,request.FILES,initial={'user': request.user})
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        context = {
            "contact": contact
        }
        response = render(request, 'partials/contact-row.html', context)
        response['HX-Trigger'] = 'success'
        return response
    else:
       response = render(request, 'partials/add-contact-modal.html', {'form': form})
       response['HX-Retarget'] = '#contact_modal'
       response['HX-Reswap'] = 'outerHTML'
       response['HX-Trigger-After-Settle'] = 'fail'
       return response
    
    

@login_required
@require_http_methods(['DELETE'])
def delete_contact(request, pk):
    try:
        contact = get_object_or_404(Contact, pk=pk, user=request.user)
        
        # Delete the file from S3 if it exists
        if contact.document:
            contact.document.delete(save=False)
        
        # Delete the contact
        contact.delete()
        response = HttpResponse(status=204)
        response['HX-Trigger'] = 'contact-deleted'
        return response
    except Exception as e:
        print(f"Error deleting contact: {e}")
        return HttpResponse(status=500)


@login_required
@require_http_methods(['GET', 'POST'])
def edit_contact(request, pk):
    try:
        contact = get_object_or_404(Contact, pk=pk, user=request.user)
        if request.method == 'POST':
            form = ContactForm(request.POST, request.FILES, instance=contact)
            if form.is_valid():
                contact = form.save(commit=False)
                
                # Handle file removal if checkbox is checked
                if request.POST.get('remove_document') == 'true':
                    if contact.document:
                        contact.document.delete(save=False)
                        contact.document = None
                
                contact.save()
                return redirect('index')
        else:
            form = ContactForm(instance=contact)
        
        context = {
            "contact": contact,
            "form": form
        }
        return render(request, 'edit_contact.html', context)
    except Exception as e:
        print(f"Error editing contact: {e}")
        return HttpResponse(status=500)



