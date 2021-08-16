from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import SignUpForm
from .tokens import account_activation_token
from .models import Users

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if Users.objects.filter(email__iexact=email).count() == 1:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Активируйте вашу учетную запись.'
                message = render_to_string('accounts/acc_active_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        })
                to_email = form.cleaned_data.get('email')
                send_mail(mail_subject, message, 'n.chistyak0v322@gmail.com', [to_email])
                print(send_mail)
                return HttpResponse('Пожалуйста, подтвердите свой адрес электронной почты, чтобы завершить регистрацию')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signInUp.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Спасибо за подтверждение. Теперь вы можете войти в свою учетную запись.')
    else:
        return HttpResponse('Ссылка для активации недействительна!')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'shared/site.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'accounts/signInUp.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/signInUp.html', {'form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('index')
