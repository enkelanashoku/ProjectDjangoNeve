from django.db import migrations, models


PRODUCTS = [
    ("velvet-cleanser", "Velvet Cream Cleanser", "Skincare", "A gentle daily cleanser for a soft, refreshed feel.", "18.00", "image/produkti2.jpeg"),
    ("daily-glow-serum", "Daily Glow Serum", "Skincare", "A lightweight serum for a dewy-looking complexion.", "26.50", "image/produkti2.jpeg"),
    ("rosewater-toner", "Rosewater Balancing Toner", "Skincare", "A refreshing toner to complete your cleansing routine.", "16.00", "image/produkti2.jpeg"),
    ("hydration-cloud-cream", "Hydration Cloud Cream", "Skincare", "A comforting moisturiser for everyday hydration.", "24.00", "image/produkti2.jpeg"),
    ("overnight-repair-mask", "Overnight Repair Mask", "Skincare", "A rich overnight mask for a relaxed evening ritual.", "29.00", "image/produkti2.jpeg"),
    ("daily-shield-spf", "Daily Shield SPF 30", "Skincare", "A lightweight daily sunscreen for your morning routine.", "22.00", "image/produkti2.jpeg"),
    ("silk-hair-oil", "Silk Finish Hair Oil", "Haircare", "A smoothing hair oil that adds shine to dry ends.", "21.00", "image/produkt1.jpeg"),
    ("repair-hair-mask", "Nourish & Repair Hair Mask", "Haircare", "A weekly conditioning mask for softer-feeling hair.", "25.00", "image/produkt1.jpeg"),
    ("curl-defining-cream", "Soft Curl Defining Cream", "Haircare", "A flexible styling cream for defined, touchable curls.", "19.50", "image/produkt1.jpeg"),
    ("scalp-care-serum", "Scalp Care Serum", "Haircare", "A lightweight leave-in serum for a balanced scalp routine.", "23.00", "image/produkt1.jpeg"),
    ("heat-protect-spray", "Heat Protect Mist", "Haircare", "A fine mist to use before heat styling.", "17.00", "image/produkt1.jpeg"),
    ("daily-volume-shampoo", "Daily Volume Shampoo", "Haircare", "A gentle shampoo for a fresh, lightweight finish.", "18.50", "image/produkt1.jpeg"),
    ("lash-conditioning-serum", "Lash Conditioning Serum", "Lash & Brow", "A conditioning step for your evening lash routine.", "27.00", "image/produkti3.jpeg"),
    ("brow-shaping-gel", "Clear Brow Shaping Gel", "Lash & Brow", "A clear styling gel to keep brows neatly in place.", "14.00", "image/produkti3.jpeg"),
    ("lash-cleanser", "Gentle Lash Cleanser", "Lash & Brow", "A gentle cleanser for lash extension aftercare.", "13.50", "image/produkti3.jpeg"),
    ("brow-conditioning-oil", "Brow Conditioning Oil", "Lash & Brow", "A nourishing oil for a simple brow care ritual.", "16.50", "image/produkti3.jpeg"),
    ("lash-brush-set", "Lash Care Brush Set", "Lash & Brow", "A set of soft brushes for daily lash grooming.", "9.00", "image/produkti3.jpeg"),
    ("brow-defining-pencil", "Soft Definition Brow Pencil", "Lash & Brow", "A fine-tip pencil for softly defined brows.", "15.00", "image/produkti3.jpeg"),
    ("body-glow-lotion", "Body Glow Lotion", "Body Care", "A silky body lotion for a smooth, radiant-looking finish.", "20.00", "image/makeup.jpeg"),
    ("calming-body-balm", "Calming Body Balm", "Body Care", "A rich balm to make your post-shower routine feel special.", "22.50", "image/makeup.jpeg"),
]


def seed_products(apps, schema_editor):
    Product = apps.get_model("aplikacion", "Product")
    Product.objects.bulk_create([
        Product(
            product_slug=slug,
            product_name=name,
            category=category,
            description=description,
            price=price,
            image_path=image_path,
        )
        for slug, name, category, description, price, image_path in PRODUCTS
    ])


def remove_seed_products(apps, schema_editor):
    Product = apps.get_model("aplikacion", "Product")
    Product.objects.filter(product_slug__in=[item[0] for item in PRODUCTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("aplikacion", "0004_studioinformation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("product_slug", models.SlugField(unique=True)),
                ("product_name", models.CharField(max_length=160)),
                ("category", models.CharField(max_length=80)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("image_path", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["-created_at", "-pk"]},
        ),
        migrations.RunPython(seed_products, remove_seed_products),
    ]
