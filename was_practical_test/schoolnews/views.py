from django.shortcuts import render
from schoolnews.models import Page

# Create your views here.
def index(request):
    page_list = Page.objects.all()

    context_dict = {}
    context_dict['pages'] = page_list

    return render(request, 'schoolnews/index.html', context=context_dict)