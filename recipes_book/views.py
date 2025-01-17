from django.shortcuts import render,redirect
from .models import Recipe
import logging
# Create your views here.

logger = logging.getLogger('recipe_book')

def add_recipe(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']
        data = {
            'name':name,
            'description':description,
            'image':image
        }
        Recipe.objects.create(**data)
        return redirect('recipe')

    payload = Recipe.objects.all()

    if request.GET.get('search'):
        payload = Recipe.objects.filter(name__icontains = request.GET.get('search'))

    return render(request,'recipe.html',context={"payload":payload})


def update(request,id):
    queryset={}
    try:
        queryset = Recipe.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            queryset.name = name
            queryset.description = description
            if image:
                queryset.image = image
            queryset.save()        
            return redirect('recipe')
    except:
        logger.error('Invalid Object Id')
    return render(request,'update_recipe.html',context={"payload":queryset})


def delete(request,id):
    print(request.POST)
    data = Recipe.objects.get(id=id)
    data.delete()
    print(data)
    return redirect('recipe')