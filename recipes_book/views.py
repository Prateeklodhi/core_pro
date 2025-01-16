from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.
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
    return render(request,'recipe.html',context={"payload":payload})

def delete(request,id):
    print(request.POST)
    data = Recipe.objects.get(id=id)
    data.delete()
    print(data)
    return redirect('recipe')