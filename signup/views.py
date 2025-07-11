from django.shortcuts import render
from django.views import View
from .forms import UserForm
from supabase import create_client
import bcrypt

url = "https://your url.supabase.co"
key = "your KEY"
supabase = create_client(url, key)

class User(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'signup/index.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            data = {
                "name": name,
                "email": email,
                "password": hashed_pw,
            }
            supabase.table("auth").insert(data).execute()
        return render(request, 'signup/index.html', {'form': form})    
