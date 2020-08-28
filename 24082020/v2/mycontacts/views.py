from django.shortcuts import render
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import AddForm


def show(request):
   contact_list = Contact.objects.all()
   return render(request, 'mycontacts/show.html',{'contacts': contact_list})

def add(request):
 context ={} 

 if request.method == 'POST':
      django_form = AddForm(request.POST)
      if django_form.is_valid():

        """ Assign data in Django Form to local variables """
        new_member_name = django_form.data.get("name")
        new_member_relation = django_form.data.get("relation")
        new_member_phone = django_form.data.get('phone')
        new_member_email = django_form.data.get('email')

        """ This is how your model connects to database and create a new member """
        Contact.objects.create(
           name = new_member_name,
           relation = new_member_relation,
           phone = new_member_phone,
           email = new_member_email,
           )
        contact_list = Contact.objects.all()
        return render(request, 'mycontacts/show.html',{'contacts': contact_list})

      else:
        """ redirect to the same page if django_form goes wrong """
        context['form']= AddForm() 
        return render(request, 'mycontacts/add.html',context)

        return render(request, 'mycontacts/add.html')
 else:
     context['form']= AddForm() 
     return render(request, 'mycontacts/add.html',context)
     return render(request, 'mycontacts/add.html')
