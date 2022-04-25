from django.shortcuts import render
from .models import Faq

# Create your views here.
def faq(request):
    context = dict(faqs=Faq.objects.all())
    return render(request, 'faq/faq.html', context)