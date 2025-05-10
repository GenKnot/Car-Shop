from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from cars.models import Car
from pages.models import Team


# Index Page Here
def home(req):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    year_fields = Car.objects.values_list('year', flat=True).distinct()
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    body_fields = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'teams': teams,
        'featured_car': featured_car,
        'all_cars': all_cars,
        'years': year_fields,
        'models': model_fields,
        'citys': city_fields,
        'bodys': body_fields
    }
    return render(req, 'pages/home.html', context)


def about(req):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(req, 'pages/about.html', context)


def services(req):
    return render(req, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        if name.isspace() or subject.isspace() or phone.isspace() or message.isspace():
            return redirect(reverse('home'))

        if (name is None) or (subject is None) or (phone is None) or (message is None):
            return redirect(reverse('home'))

        mail_title = f'{subject} From CarShop'
        mail_context = f'Dear Admin\n' \
                       f'My Name is {name}, Here is my Email: {email}\n' \
                       f'My Phone Number Is: {phone}\n' \
                       f'Message: \n{message}'
        admin_emails = []
        admin_info = User.objects.filter(is_superuser=True)
        for i in admin_info:
            admin_emails.append(i.email)

        send_mail(
            mail_title,
            mail_context,
            'genknot@gmail.com',
            admin_emails,
            fail_silently=False
        )
        return redirect(reverse('home'))

    else:
        return render(request, 'pages/contact.html')
