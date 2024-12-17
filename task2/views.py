from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.

# Функциональное представление
def function_based_view(request):
    return render(request, 'second_task/function_based_view.html')


# Классовое представление
class ClassBasedView(TemplateView):
    template_name = 'second_task/class_based_view.html'


