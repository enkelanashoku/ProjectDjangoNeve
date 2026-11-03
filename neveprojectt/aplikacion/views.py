
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import AppointmentForm, ContactForm
from .models import Service, About, GalleryPost, Product, StudioInformation


# HOME
def home(request):
    services = Service.objects.all()
    products = Product.objects.filter(is_active=True).order_by("-created_at", "-pk")[:3]
    studio_info = StudioInformation.objects.first()

    return render(request, 'home.html', {
        'services': services,
        'products': products,
        'studio_info': studio_info
    })


# ABOUT
def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})


# CONTACT
def contact(request):
    studio_info = StudioInformation.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your message has been sent. We will contact you soon.'
            )

            return redirect('contact')
    else:
        product_name = request.GET.get('product', '').strip()
        service_name = request.GET.get('service', '').strip()
        subject = product_name or service_name
        initial = {'contact_comment': f"I'm interested in {subject}."} if subject else None
        form = ContactForm(initial=initial)

    return render(request, 'contact.html', {
        'form': form,
        'studio_info': studio_info
    })


# GALLERY
def gallery(request):
    posts = GalleryPost.objects.filter(is_published=True)
    return render(request, 'gallery.html', {
        'gallery_posts': posts,
        'gallery_categories': GalleryPost.Category.choices,
    })


# SERVICES

def services(request):
    services = Service.objects.all()

    return render(request, 'services.html', {
        'services': services
    })


# PRODUCTS
def products(request):
    products = Product.objects.filter(is_active=True).order_by("-created_at", "-pk")
    return render(request, 'products.html', {'products': products})


# APPOINTMENT
def book(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your appointment request was sent. The studio will contact you to confirm it.'
            )

            return redirect('appointment')
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})
