from django.shortcuts import render, redirect


# Create your views here.
def showpage(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if not request.user.is_authenticated:
            return redirect('auth_page')
    return render(request, 'comments/main.html')