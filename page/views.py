from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile

# Create your views here.
def home(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'profiles' : profiles})

def detail(request, profile_id):
    profile = get_object_or_404(Profile, pk = profile_id)
    return render(request, 'detail.html', {'profile' : profile})

def introduce(request):
    return render(request, 'introduce.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Profile()
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()
        
        return redirect('/profile/' + str(post.id))

def update(request, profile_id):
    post = get_object_or_404(Profile, pk = profile_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()
        return redirect('/profile/' + str(post.id))
    
    else:
        return render(request, 'update.html', {'profile':post})

def delete(request, profile_id):
    post = get_object_or_404(Profile, pk = profile_id)
    post.delete()

    return redirect('home')