from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Outfit, Shoe
from .forms import AccessoriesForm


# Create your views here.
def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def outfits_index(request):
    outfits = Outfit.objects.order_by('season')
    return render(request, 'outfits/index.html', {'outfits':outfits})

def outfits_detail(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    accessories_form = AccessoriesForm()
    # find all shoes NOT associated with this outfit
    shoes_outfit_doesnt_have = Shoe.objects.exclude(id__in=outfit.shoes.all().values_list('id'))
    return render(request, 'outfits/detail.html', {
        'outfit': outfit,
        'accessories_form' : accessories_form,
        'shoes': shoes_outfit_doesnt_have,
    })

class OutfitCreate(CreateView):
    model = Outfit
    fields = ['name','number_items','season','color_theme','dress_code','description']
   

class OutfitUpdate(UpdateView):
    model = Outfit
    fields = ['name','number_items','season','color_theme','dress_code','description']
    

class OutfitDelete(DeleteView):
    model = Outfit
    success_url = '/outfits/'


def add_accessories(request, outfit_id):
    # create a ModelForm instance using the data in request.POST
    form = AccessoriesForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the object_id assigned
        new_accessories = form.save(commit=False)
        new_accessories.outfit_id = outfit_id
        new_accessories.save()
    return redirect('outfits_detail', outfit_id=outfit_id)

class ShoeList(ListView):
      model = Shoe

class ShoeDetail(DetailView):
  model = Shoe

class ShoeCreate(CreateView):
  model = Shoe
  fields = '__all__'

class ShoeUpdate(UpdateView):
  model = Shoe
  fields = '__all__'

class ShoeDelete(DeleteView):
  model = Shoe
  success_url = '/shoes/'

def assoc_shoe(request, outfit_id, shoe_id):
    outfit = Outfit.objects.get(id=outfit_id)
    outfit.shoes.add(shoe_id)
    return redirect('outfits_detail', outfit_id=outfit_id)