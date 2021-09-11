from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Contact, About
from django.http import HttpResponse
from .forms import ContactForm


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'category.html', context)

def contact_register(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['phone']
            mg = fm.cleaned_data['message']
            reg = Contact(name=nm, email=em, phone=ph, message=mg)
            reg.save()
            return HttpResponse('Message Sent, Thanks for contacting us')
    else:
        fm = ContactForm()
    stud = Contact.objects.all()
    return render(request, 'contact.html', {'form':fm, 'stu': stud,})

def about_page(request):
    abouts = About.objects.all()
    context = {'abouts': abouts}
    return render(request, 'about.html', context)

def mission_page(request):
    return render(request, 'mission.html')

def vision_page(request):
    return render(request, 'vision.html')

def location_page(request):
    return render(request, 'location.html')

  