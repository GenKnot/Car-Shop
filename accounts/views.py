from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth


# Create your views here.
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Username Or Password Error')
            return render(request, 'accounts/login.html')

    elif request.user.is_authenticated:
        return redirect(reverse('home'))

    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if first_name.isspace() or last_name.isspace() or username.isspace():
                messages.error(request, "Your name can not be space")
                return render(request, 'accounts/signup.html')

            elif first_name is None or last_name is None or username is None:
                messages.error(request, "Your have to enter something on name")
                return render(request, 'accounts/signup.html')

            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken")
                    return render(request, 'accounts/signup.html')

                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, "Email already taken")
                        return render(request, 'accounts/signup.html')

                    else:
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            password=password,
                            email=email
                        )
                        auth.login(request, user)
                        user.save()
                        return redirect(reverse('home'))

        else:
            messages.error(request, "Your password are not match")
            return render(request, 'accounts/signup.html')

    elif request.user.is_authenticated:
        return redirect(reverse('home'))

    else:
        return render(request, 'accounts/signup.html')


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect(reverse('home'))
    return redirect(reverse('home'))


@login_required
def dashboard(request):
    user = request.user
    user_contacts = Contact.objects.order_by('-create_date').filter(user_id=user.id)
    context = {
        'inquiries': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
