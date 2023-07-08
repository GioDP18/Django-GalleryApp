from django.shortcuts import render, redirect
from .models import Picture
from .forms import PictureForm



def pictures(request):
    pictures = Picture.objects.all()
    return render(request, 'pictures.html', {'pictures': pictures})

def members(request):
    return render(request, 'members.html')

def view(request, pk):
    picture = Picture.objects.get(id=pk)
    return render(request, 'view.html', {'picture': picture})

def create(request):
    form = PictureForm()

    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'create.html', {'form': form})


def details(request, pk):
    picture = Picture.objects.get(id=pk)
    return render(request, 'details.html', {'picture': picture})

def update(request, pk):
    picture = Picture.objects.get(id=pk)
    form = PictureForm(instance=picture)

    if request.method == 'POST':
        form = PictureForm(request.POST, instance=picture, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        'picture': picture
    }

    return render(request, 'update.html', context)


def delete(request, pk):
    picture = Picture.objects.get(id=pk)
    picture.delete()
    return redirect('/')
