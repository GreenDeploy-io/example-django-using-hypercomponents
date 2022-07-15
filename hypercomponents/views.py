from django.shortcuts import render


# Create your views here.
def base_for_django_components(request):
    return render(request, 'django_components/base.html')
