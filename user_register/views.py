from django.shortcuts import render, redirect
from .models import user_prof


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        print(name, image)
        user = user_prof.objects.create(name=name, image=image)
        user.save()
        return redirect('home')

    all_user = user_prof.objects.all()
    return render(request, 'user_details.html', locals())


def delete(request, id):
    user = user_prof.objects.get(id=id)
    user.delete()
    return redirect('home')


def test():
    pass