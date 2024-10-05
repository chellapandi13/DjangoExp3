from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to the success page upon successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Success page view
def success(request):
    return render(request, 'success.html')  # Render the success.html page
