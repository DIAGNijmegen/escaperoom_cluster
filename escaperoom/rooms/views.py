from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return render(request, 'main.html')

def check_code(code):
    # Dummy function to check code
    # Replace with your actual code validation logic
    valid_codes = ["code1", "code2", "code3", "code4"]
    return code in valid_codes

def page1(request):
    code = request.GET.get('code', '')
    success = check_code(code)
    context = {'success': success}
    return render(request, 'assignment1.html', context)

def page2(request):
    code = request.GET.get('code', '')
    success = check_code(code)
    context = {'success': success}
    return render(request, 'assignment1.html', context)

def page3(request):
    code = request.GET.get('code', '')
    success = check_code(code)
    context = {'success': success}
    return render(request, 'assignment1.html', context)

def page4(request):
    code = request.GET.get('code', '')
    success = check_code(code)
    context = {'success': success}
    return render(request, 'assignment1.html', context)