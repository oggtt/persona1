from django.shortcuts import render
from django.views import View
from .forms import QuestionForm
from supabase import create_client
import os
url = "https://your url.supabase.co"
key = "your KEY"
supabase = create_client(url, key)

class question(View):
    def get(self, request):
        form = QuestionForm()
        return render(request, 'question/question.html', {'form': form})

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            selected_radio = form.cleaned_data['radio']

            all_options = ['question1', 'question2', 'question3']

            radio_status = {q: q == selected_radio for q in all_options}
            data = {
                "name": name,
                "gender": gender,
                "question1": radio_status['question1'],
                "question2": radio_status['question2'],
                "question3": radio_status['question3']
            }
            supabase.table("users").insert(data).execute()
        return render(request, 'question/question.html', {'form': form})
