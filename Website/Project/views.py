from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from typing import Text
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Certifications, Project, Tag

# Create your views here.


def projects(request):
    projectobj = Project.objects.all()

    context = {'projects': projectobj}
    return render(request, 'Project/projects.html', context)


def about(request):
    tagobj = Tag.objects.all()
    certificationobj = Certifications.objects.all()
    context = {'tag': tagobj, 'certificationobj': certificationobj}
    return render(request, 'Project/profile.html',  context)


def search(request):

    if request.method == "POST":
        searched = request.POST['text']
        projectobj = Project.objects.filter(title__contains=searched)

        context = {'projects': projectobj, 'searched': searched}
        return render(request, 'Project/search.html', context)
    else:
        projectobj = Project.objects.all

        context = {'projects': projectobj}
        return render(request, 'Project/search.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'kumu199633@gmail.com',
                          ['kumu199633@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("about")
    form = ContactForm()
    return render(request, "Project/contact.html", {'form': form})


def SingleProject(request, pk):
    projectobj = Project.objects.get(id=pk)

    tags = projectobj.tags.all()
    context = {'project': projectobj, 'tags': tags}
    return render(request, 'Project/single-project.html', context)
