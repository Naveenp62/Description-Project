from django.shortcuts import render
from notes.models import note
# Create your views here.
def func(request):
    obj=note.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('desc')
        res=note(title=name,description=des)
        res.save()
        obj=note.objects.all()
        return render(request,"index.html",{'res':res})
    return render(request,"index.html",{'res':obj})
def func2(request):
    result=note.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('des')
        obj=note.objects.get(title=name)
        obj.description=des
        obj.save()
        return render(request,"form.html",{'res':obj})
    return render(request,"form.html",{'res':result})