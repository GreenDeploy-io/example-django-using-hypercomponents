from django.shortcuts import render


# Create your views here.
def demo_calendar(request):
    return render(request, 'django_components/demo_calendar.html')

def demo_calendar_slots(request):
    return render(request, 'django_components/demo_calendar_slots.html')

def demo_calendar_slots_with_super(request):
    return render(request, 'django_components/demo_calendar_slots_with_super.html')

def tagify_demo_00_basic(request):
    return render(request, 'tagify/demo_00_basic.html')


