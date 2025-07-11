from django.shortcuts import render,redirect
from django.views import View
from .forms import AuthForm
from supabase import create_client
from django.contrib.auth import authenticate, login

url = "https://your url.supabase.co"
key = "your KEY"

supabase = create_client(url, key)

class Auth(View):
    def get(self, request):
        form = AuthForm()
        return render(request, 'login/login.html', {'form': form})

    def post(self, request):
        form = AuthForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            raw_password = request.POST.get('password')
            user = authenticate(request, emailA=email, passwordA=raw_password)
            if user:
                login(request, user)
            return redirect('question')
        return render(request, 'login/login.html', {'form': form})    
