from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import AccountCreationForm, LoginForm


def login_view(request):
    # prevent authenticated user from accessing this view
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                messages.warning(request, "Account Not Activated. Check Your Email for Activation code!")
                return redirect("activate")
            messages.error(request, "Wrong Email or Password!")
            return redirect("login")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


def signup(request):
    # prevent authenticated user from accessing this view
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.verification_code = user.generate_verification_code()
            user.save()
    
            #Email New user verification code            
            mail_subject = "Verification Code"
            message = render_to_string("registration/verification_email.html", {
                "user": user,
                "verification_code": user.verification_code,
            })
            email = EmailMessage(mail_subject, message, from_email="Team@MicroFocusInc.com", to=[user.email])
            email.content_subtype="html"
            email.send()
            messages.info(request=request, message="Kindly check your Email for your Account verification code!")
            return redirect("activate")
    else:
        form = AccountCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def account_verification(request):
    if request.method == "POST":
        verification_code = request.POST.get("verification_code")
        try:
            user = User.objects.get(verification_code=verification_code)
        except (TypeError, ValueError, User.DoesNotExist):
            user = None
            
        if user is not None:
            user.is_active = True
            user.verification_code = None
            user.save()
            messages.success(request, "Account successfully activated. Kindly Login")
            return redirect("login")
        else:
            messages.error(request, "Invalid verification code.")  
    return render(request, "registration/account_verification.html")


def resend_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                messages.info(request, "Account Already Activated.Kindly Login")
                return redirect("login")
            user.verification_code = user.generate_verification_code()
            user.save()
            
            # Send the activation code to the user's email
            mail_subject = "Verification Code"
            message = render_to_string("registration/verification_email.html", {
                "user": user,
                "verification_code": user.verification_code,
            })
            email = EmailMessage(mail_subject, message, from_email="Team@MicroFocusInc.com", to=[user.email])
            email.content_subtype = "html"
            email.send()
            messages.success(request, "Activation code has been resent. Please check your email.")
            return redirect("activate")
        except User.DoesNotExist:
            messages.error(request, "The provided email does not exist!")
            return redirect("activate")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")