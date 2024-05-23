from django.shortcuts import render, HttpResponse

# Create your views here.
def add(request):
    if request.method=='POST':
        eno= request.POST.get('eno', '')
        add= Studentdata(eno=eno)
        add.save()
    return render(request, 'administrator/add.html')
