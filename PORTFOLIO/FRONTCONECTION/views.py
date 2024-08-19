from django.shortcuts import render, redirect
from . import data_git
from .models import Project, Contact, corosel, posts, services_des
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from . import webscriping






# Create your views here.
#

def crosol_view():
    return corosel.objects.all()


def index(request):
    webscriping.get_posts()
    corosel_data = crosol_view()#item from database
    context = {
        'posts': posts.objects.all(),
        'carousel': corosel_data,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    # emplement the mail sending function here to send the mail to the admin
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        position = request.POST['position']
        message = request.POST['message']
        phone_number = request.POST['phone']

        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            position=position,
            message=message)
        try:
            send_mail(
                subject='This is computer generated mail for response',
                message=f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible.\n\nBest Regards,\n\n{settings.EMAIL_HOST_USER}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )
            contact.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect('contact')

        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later')
            return redirect('contact')

    return render(request, 'contact.html')



def projects(request):
    data_git.main()
    projects = Project.objects.all()
    if len(projects) == 0:
        return render(request, 'projects.html')

    return render(request, 'projects.html', {'projects': projects} )

def services(request):
    service=services_des.objects.all()
    if len(service) == 0:
        return render(request, 'service.html')
    context = {
        'services': service
    }
    return render(request, 'service.html', context)
