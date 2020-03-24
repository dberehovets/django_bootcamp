from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'practice_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING
            print("VALIDATION SUCCESS!")
            print("Name: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'practice_app/form_page.html', {'form': form})
