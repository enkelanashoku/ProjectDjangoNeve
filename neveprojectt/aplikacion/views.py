
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

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
@never_cache
def services(request):
    services = Service.objects.all()

    return render(request, 'services.html', {
        'services': services
    })


# PRODUCTS
def products(request):
    products = Product.objects.filter(is_active=True).order_by("-created_at", "-pk")
    return render(request, 'products.html', {'products': products})


# PRODUCT DETAIL
def product_detail(request, product_slug):
    product = get_object_or_404(
        Product,
        product_slug=product_slug,
        is_active=True
    )

    related_products = list(
        Product.objects.filter(is_active=True, category=product.category)
        .exclude(pk=product.pk)
        .order_by("-created_at", "-pk")[:3]
    )
    if len(related_products) < 3:
        related_products.extend(
            Product.objects.filter(is_active=True)
            .exclude(pk=product.pk)
            .exclude(pk__in=[item.pk for item in related_products])
            .order_by("-created_at", "-pk")[:3 - len(related_products)]
        )

    product_copy = {
        'calming-body-balm': {
            'benefits': [('fa-droplet', 'Deep nourishment', 'Softens dry-feeling skin.'), ('fa-feather', 'Comforting feel', 'Leaves skin smooth and comfortable.')],
            'how_to_use': 'Massage a small amount into clean, dry skin, focusing on dry areas.',
            'who_for': 'For dry-feeling skin that needs a comforting step after showering.',
        },
        'body-glow-lotion': {
            'benefits': [('fa-droplet', 'Everyday hydration', 'Helps keep skin feeling hydrated.'), ('fa-sun', 'Soft glow', 'Leaves skin soft, smooth and radiant-looking.')],
            'how_to_use': 'Massage generously into clean, dry skin, especially after showering.',
            'who_for': 'For anyone who wants everyday moisture with a soft, radiant-looking finish.',
        },
        'brow-defining-pencil': {
            'benefits': [('fa-wand-magic-sparkles', 'Natural definition', 'Shapes brows with a soft finish.'), ('fa-pen', 'Precise detail', 'Fills sparse-looking areas with control.')],
            'how_to_use': 'Use light, short strokes to fill sparse areas, then blend with a spoolie.',
            'who_for': 'For anyone who wants softly defined brows or a little extra shape in sparse areas.',
        },
        'lash-brush-set': {
            'benefits': [('fa-eye', 'Neat grooming', 'Helps separate and groom lashes and brows.'), ('fa-heart', 'Easy routine', 'Makes daily touch-ups simple.')],
            'how_to_use': 'Gently brush lashes and brows in the direction of hair growth; clean brushes regularly.',
            'who_for': 'For lash and brow lovers who want an easy tool for everyday grooming.',
        },
        'brow-conditioning-oil': {
            'benefits': [('fa-droplet', 'Conditioning care', 'Helps keep brow hairs feeling soft.'), ('fa-leaf', 'Simple ritual', 'Adds a nourishing step to brow care.')],
            'how_to_use': 'Apply a small amount to clean brows and gently distribute through the hairs.',
            'who_for': 'For anyone looking to add a simple conditioning step to their brow routine.',
        },
        'lash-cleanser': {
            'benefits': [('fa-soap', 'Gentle cleanse', 'Lifts everyday buildup from the lash area.'), ('fa-wind', 'Fresh feel', 'Leaves lashes feeling clean and refreshed.')],
            'how_to_use': 'Apply with a suitable brush or cotton pad and gently cleanse without rubbing or pulling.',
            'who_for': 'For lash-extension wearers looking for a gentle aftercare cleanse.',
        },
        'brow-shaping-gel': {
            'benefits': [('fa-wand-magic-sparkles', 'Soft definition', 'Shapes brows for a naturally defined look.'), ('fa-check', 'Stays in place', 'Helps keep brow hairs neatly styled.')],
            'how_to_use': 'Brush through clean brows in short upward strokes and let the gel set.',
            'who_for': 'For anyone who likes tidy, softly shaped brows that stay in place.',
        },
        'lash-conditioning-serum': {
            'benefits': [('fa-eye', 'Lash care', 'Conditions the appearance of lashes.'), ('fa-moon', 'Evening ritual', 'An easy step for a delicate lash-care routine.')],
            'how_to_use': 'Apply a thin line to the clean, dry upper lash line and let it dry completely.',
            'who_for': 'For anyone wanting a simple conditioning step in their evening lash routine.',
        },
        'daily-volume-shampoo': {
            'benefits': [('fa-soap', 'Fresh cleanse', 'Gently cleanses hair and scalp.'), ('fa-wind', 'Lightweight volume', 'Leaves hair feeling fresh and full.')],
            'how_to_use': 'Massage into wet hair and scalp, rinse thoroughly, and repeat if needed.',
            'who_for': 'For hair that needs a fresh, lightweight cleanse and a fuller-looking finish.',
        },
        'heat-protect-spray': {
            'benefits': [('fa-temperature-half', 'Heat styling care', 'Helps protect hair during heat styling.'), ('fa-feather', 'Smooth finish', 'Leaves hair feeling manageable and soft.')],
            'how_to_use': 'Mist evenly over damp or dry hair before using heat tools.',
            'who_for': 'For anyone who regularly styles their hair with heat tools.',
        },
        'scalp-care-serum': {
            'benefits': [('fa-droplet', 'Scalp comfort', 'Supports a comfortable-feeling scalp.'), ('fa-leaf', 'Lightweight care', 'Refreshes without weighing down your routine.')],
            'how_to_use': 'Apply in small sections directly to the scalp and massage gently with fingertips.',
            'who_for': 'For anyone who wants a lightweight, focused step in their scalp-care routine.',
        },
        'curl-defining-cream': {
            'benefits': [('fa-wand-magic-sparkles', 'Defined curls', 'Helps bring out your natural curl shape.'), ('fa-feather', 'Soft movement', 'Leaves curls flexible and touchable.')],
            'how_to_use': 'Work a small amount through damp hair and scrunch to encourage curl definition.',
            'who_for': 'For naturally wavy or curly hair that could use definition with a soft feel.',
        },
        'repair-hair-mask': {
            'benefits': [('fa-droplet', 'Extra nourishment', 'Helps care for dry-looking lengths.'), ('fa-feather', 'Softer feel', 'Leaves hair feeling smooth and cared for.')],
            'how_to_use': 'After shampooing, apply to damp lengths and ends for 5–10 minutes, then rinse.',
            'who_for': 'For dry-feeling lengths and ends that need an extra weekly care step.',
        },
        'silk-hair-oil': {
            'benefits': [('fa-sun', 'Glossy finish', 'Adds a soft-looking shine.'), ('fa-feather', 'Smoother lengths', 'Helps smooth the look of frizz.')],
            'how_to_use': 'Warm a few drops between your palms and smooth through mid-lengths and ends.',
            'who_for': 'For anyone who wants to smooth dry ends and add a polished finish.',
        },
        'daily-shield-spf': {
            'benefits': [('fa-sun', 'SPF 30', 'Helps protect skin from UVB rays.'), ('fa-feather', 'Lightweight wear', 'An easy finish to your morning routine.')],
            'how_to_use': 'Apply generously to face and neck as the final morning step; reapply every two hours.',
            'who_for': 'For daily skincare routines that need broad daytime sun protection.',
        },
        'overnight-repair-mask': {
            'benefits': [('fa-moon', 'Overnight care', 'Nourishes skin while you rest.'), ('fa-heart', 'Morning softness', 'Leaves skin feeling soft and comforted.')],
            'how_to_use': 'Smooth an even layer over clean skin as the last step of your evening routine.',
            'who_for': 'For dry-feeling skin that would love a comforting overnight step.',
        },
        'hydration-cloud-cream': {
            'benefits': [('fa-droplet', 'Daily hydration', 'Helps keep skin feeling hydrated.'), ('fa-feather', 'Comfortable finish', 'Leaves skin soft with a lightweight feel.')],
            'how_to_use': 'Massage a small amount over clean face and neck morning and evening.',
            'who_for': 'For anyone looking for a lightweight moisturiser for everyday use.',
        },
        'rosewater-toner': {
            'benefits': [('fa-spa', 'Fresh feel', 'Refreshes skin after cleansing.'), ('fa-leaf', 'Ready for skincare', 'Prepares skin for the next steps.')],
            'how_to_use': 'Sweep over clean skin with a cotton pad or gently press in with your palms.',
            'who_for': 'For anyone who enjoys a refreshing step between cleansing and moisturising.',
        },
        'daily-glow-serum': {
            'benefits': [('fa-sun', 'Healthy-looking glow', 'Brightens the look of dull skin.'), ('fa-feather', 'Smooth feel', 'Leaves skin feeling fresh and soft.')],
            'how_to_use': 'Apply 2–3 drops to clean, dry skin before moisturiser, morning or evening.',
            'who_for': 'For complexions that could use a fresh, dewy-looking boost.',
        },
        'velvet-cleanser': {
            'benefits': [('fa-soap', 'Gentle cleanse', 'Removes everyday impurities.'), ('fa-feather', 'Soft finish', 'Leaves skin feeling clean and comfortable.')],
            'how_to_use': 'Massage a small amount over damp skin, avoiding the eye area, then rinse well.',
            'who_for': 'For anyone who prefers a gentle first step that leaves skin feeling soft.',
        },
    }
    selected_copy = product_copy.get(product.product_slug, {})
    category_icons = {
        'Body Care': 'fa-spa',
        'Lash & Brow': 'fa-eye',
        'Haircare': 'fa-wand-magic-sparkles',
        'Skincare': 'fa-droplet',
    }
    benefit_points = [
        (category_icons.get(product.category, 'fa-heart'), benefit.strip().lstrip('-• ').strip(), '')
        for benefit in product.benefits.splitlines()
        if benefit.strip()
    ][:5]
    if not benefit_points and product.description:
        benefit_points = [(category_icons.get(product.category, 'fa-heart'), product.description.strip(), '')]

    extra_touches = {
        'calming-body-balm': 'A soft, soothing finish to your post-shower ritual.',
        'body-glow-lotion': 'Let daily body care end with a touch of radiance.',
        'brow-defining-pencil': 'Your natural brow shape, softly brought into focus.',
        'lash-brush-set': 'A simple finishing touch for lashes and brows.',
        'brow-conditioning-oil': 'A little care for beautifully groomed brows.',
        'lash-cleanser': 'Keep lash aftercare feeling fresh and considered.',
        'brow-shaping-gel': 'A polished brow finish, made effortless.',
        'lash-conditioning-serum': 'A delicate final note in your evening lash ritual.',
        'daily-volume-shampoo': 'Freshly cleansed hair, ready for the day ahead.',
        'heat-protect-spray': 'Style with care, then enjoy the finishing touch.',
        'scalp-care-serum': 'Make a little room for focused scalp care.',
        'curl-defining-cream': 'Let your natural texture take the spotlight.',
        'repair-hair-mask': 'Give lengths and ends a moment of weekly care.',
        'silk-hair-oil': 'A few drops bring a polished finish to your lengths.',
        'daily-shield-spf': 'A thoughtful finishing step for bright mornings.',
        'overnight-repair-mask': 'End the day with a soft moment of skincare.',
        'hydration-cloud-cream': 'A light, comforting close to your daily ritual.',
        'rosewater-toner': 'A refreshing pause between cleanse and care.',
        'daily-glow-serum': 'A dewy moment to brighten your routine.',
        'velvet-cleanser': 'Begin your routine with a gentle, considered cleanse.',
    }
    how_to_use = product.usage_instructions or selected_copy.get('how_to_use', '')
    if '\ufffd' in how_to_use:
        how_to_use = selected_copy.get('how_to_use', how_to_use)
    who_for = selected_copy.get(
        'who_for',
        f"For anyone looking to add a thoughtful step to their {product.category.lower()} routine."
    )

    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products,
        'benefit_points': benefit_points,
        'how_to_use': how_to_use,
        'who_for': who_for,
        'key_ingredients': 'Ingredient information has not been provided for this product. Please refer to its packaging for the complete ingredient list.',
        'extra_touch': extra_touches.get(product.product_slug, 'A thoughtful addition to your everyday ritual.'),
    })


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
