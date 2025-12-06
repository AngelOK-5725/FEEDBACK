from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import Feedback

# Create your views here.
from .forms import review_form

class ReviewView(View):
    def get(self, request):
        form = review_form()
        return render(request, 'feedback_app/index.html', {
            'form': form})
    
    def post(self, request):
        form = review_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thankyou/')
        return render(request, 'feedback_app/index.html', {
            'form': form})


# def index(request):
#     if request.method == 'POST':
#         form = review_form(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data['user_name']) #проверка
#             # rewiw = Feedback(user_name=form.cleaned_data['user_name'],
#             #                     review_text=form.cleaned_data['review_text'],
#             #                     rating=form.cleaned_data['rating'])
#             # rewiw.save()
#             form.save()
#             return HttpResponseRedirect('/thankyou/')
#             # return thankyou(request)
#     else:
#         form = review_form()
        
#     return render(request, 'feedback_app/index.html',
#             {'form': form})

def thankyou(request):
    return HttpResponse('Thank you for your feedback!') 
