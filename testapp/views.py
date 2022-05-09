from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='sonam'
    return render(request, 'testapp/setsession.html')