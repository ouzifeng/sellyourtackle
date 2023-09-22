from django.shortcuts import render, redirect
from .forms import CustomUserSignupForm

def signup(request):
    return render(request, 'signup.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Here you can also log the user in or send a confirmation email if needed
            return redirect('/')  # Redirect to a success page or login page
    else:
        form = CustomUserSignupForm()
    return render(request, 'auth_app/signup.html', {'form': form})