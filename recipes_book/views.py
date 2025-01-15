from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.
def add_recipe(request):
    print(request)
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
    return render(request,'recipe.html')
