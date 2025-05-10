from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.core.mail import send_mail
import random
from cars.models import Car
from contacts.models import Contact


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        w_car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if (w_car_id is None or w_car_id == '') or (w_car_id.isspace()) or \
                (car_title is None or car_title == '') or (car_title.isspace()):
            return redirect(reverse('cars:cars'))

        try:
            Car.objects.get(id=w_car_id)
            car_id = w_car_id
        except:
            items = list(Car.objects.all())
            random_car = random.choice(items)
            car_id = random_car.id

        if request.user.is_authenticated:
            a_user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=a_user_id)
            if has_contacted:
                return redirect(reverse('accounts:dashboard'))

        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message
        )

        mail_title = f'{car_title} From CarShop'
        mail_context = f'Dear Admin\n Someone Just Send Contact On Our Site, You Can Check Now'
        admin_emails = []
        admin_info = User.objects.filter(is_superuser=True)
        for i in admin_info:
            admin_emails.append(i.email)

        send_mail(
            mail_title,
            mail_context,
            'carlib.north@gmail.com',
            admin_emails,
            fail_silently=False
        )

        if request.user.is_authenticated:
            user_id = request.user.id
            contact.user_id = user_id

        contact.save()
        if request.user.is_authenticated:
            return redirect(reverse('accounts:dashboard'))
        else:
            return redirect(reverse('home'))

    else:
        return redirect(reverse('home'))
