from django.shortcuts import render

# Create your views here.

def test_view(request):
    return render(request, 'my_app/vue_test.html')