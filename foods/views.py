from django.shortcuts import render , redirect
from .models import Foods
from .forms import FoodsForm
from django.http import HttpResponse
# Create your views here.
def food_list(request):
    foods_list =Foods.objects.all()
    context = {
        'foods': foods_list
    }
    return render(request,'foods/index.html',context=context)

def food_detail(request,pk):
    food = Foods.objects.get(pk=pk)
    context = {
        'food' : food
    }
    return render(request,'foods/detail.html',context=context)

def post_create(request):
    if request.method == 'POST':
        form = FoodsForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()  # Use form.save() for ModelForm
            return redirect('food_list')
    else:
        form = FoodsForm()
    # Render the form for both GET and invalid POST cases
    return render(request, 'foods/create_post.html', {'form': form})