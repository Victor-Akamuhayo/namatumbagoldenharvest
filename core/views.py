from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm, MembershipApplicationForm
from .models import GalleryImage, NewsArticle


def home(request):
    service_highlights = [
        {
            'icon': '🌾',
            'title': 'Agriculture Loans',
            'description': 'Funding support for farming activities, business growth, and productive agricultural investments.',
        },
        {
            'icon': '🚜',
            'title': 'Extension Services',
            'description': 'Practical farmer guidance, productivity support, and improved agricultural practices.',
        },
        {
            'icon': '🧪',
            'title': 'Farm Inputs',
            'description': 'Access to fertilizers, pesticides, supplements and other quality agricultural inputs.',
        },
        {
            'icon': '🌱',
            'title': 'Seedlings & Planting Materials',
            'description': 'Support for quality seedlings and planting material to strengthen production.',
        },
        {
            'icon': '📦',
            'title': 'Marketing & Trading',
            'description': 'Market access and trade opportunities that help farmers get better value for their produce.',
        },
        {
            'icon': '💰',
            'title': 'Savings & Cash Flow Support',
            'description': 'Savings culture and reliable financial planning to help members build resilience.',
        },
    ]
    stats = [
        {'value': '6', 'label': 'Core services'},
        {'value': '100%', 'label': 'Member-centered'},
        {'value': '24/7', 'label': 'Support mindset'},
    ]
    news_items = NewsArticle.objects.all()[:3]
    gallery_items = GalleryImage.objects.all()[:4]
    return render(request, 'home.html', {'service_highlights': service_highlights, 'stats': stats, 'news_items': news_items, 'gallery_items': gallery_items})


def about(request):
    return render(request, 'about.html')


def services(request):
    service_items = [
        {
            'icon': '💳',
            'title': 'Agriculture Loans',
            'description': 'Flexible financial support for farming and agricultural enterprise development.',
            'points': ['Production financing', 'Business expansion support', 'Repayment planning'],
        },
        {
            'icon': '👨‍🌾',
            'title': 'Extension Services',
            'description': 'Knowledge sharing and guidance for improved productivity and better farm management.',
            'points': ['Training and advisory', 'Best crop practices', 'Farm productivity improvements'],
        },
        {
            'icon': '🌿',
            'title': 'Farm Inputs & Supplements',
            'description': 'Quality inputs that strengthen production outcomes for members.',
            'points': ['Fertilizer access', 'Pesticide support', 'Farm supplements'],
        },
        {
            'icon': '🌼',
            'title': 'Seedlings & Planting Materials',
            'description': 'Reliable planting support for healthier crop establishment and growth.',
            'points': ['Seedling supply', 'Planting materials', 'Growth support'],
        },
        {
            'icon': '📈',
            'title': 'Marketing & Trading',
            'description': 'Opportunities that help members connect better with buyers, markets and trade networks.',
            'points': ['Market linkages', 'Trade opportunities', 'Price advantage'],
        },
        {
            'icon': '🏦',
            'title': 'Savings & Cash Flow Support',
            'description': 'Sustainable financial planning for households, farmers and traders.',
            'points': ['Savings culture', 'Financial planning', 'Cashflow resilience'],
        },
    ]
    return render(request, 'services.html', {'service_items': service_items})


def products(request):
    product_categories = [
        {
            'name': 'Maize',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/16/Maize_%28Cone%29_seeds_07.jpg/500px-Maize_%28Cone%29_seeds_07.jpg',
            'image_alt': 'Maize kernels on a corn cob',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Maize_(Cone)_seeds_07.jpg',
        },
        {
            'name': 'Groundnuts',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4e/Groundnut_Seed.jpg/500px-Groundnut_Seed.jpg',
            'image_alt': 'Groundnut seeds',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Groundnut_Seed.jpg',
        },
        {
            'name': 'Beans',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a7/Beans_seeds_1.jpg/500px-Beans_seeds_1.jpg',
            'image_alt': 'Bean seeds',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Beans_seeds_1.jpg',
        },
        {
            'name': 'Sunflower',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/32/Sunflower_seeds._img_004.jpg/500px-Sunflower_seeds._img_004.jpg',
            'image_alt': 'Sunflower seeds',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Sunflower_seeds._img_004.jpg',
        },
        {
            'name': 'Soybeans',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/87/Soybean_Seed_in_Soil_%289621475751%29.jpg/500px-Soybean_Seed_in_Soil_%289621475751%29.jpg',
            'image_alt': 'Soybean seed germinating in soil',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Soybean_Seed_in_Soil_(9621475751).jpg',
        },
        {
            'name': 'Cassava',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/31/Cassava_stems_cut_for_planting.jpg/500px-Cassava_stems_cut_for_planting.jpg',
            'image_alt': 'Cassava stem cuttings prepared for planting',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Cassava_stems_cut_for_planting.jpg',
        },
        {
            'name': 'Rice',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/35/Rice_grains_for_seeds.jpg/500px-Rice_grains_for_seeds.jpg',
            'image_alt': 'Rice grains selected for seed',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Rice_grains_for_seeds.jpg',
        },
        {
            'name': 'Sorghum',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7b/Sorghum_Seeds_%2805410446%29_%2852995387780%29.jpg/500px-Sorghum_Seeds_%2805410446%29_%2852995387780%29.jpg',
            'image_alt': 'Sorghum seeds',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Sorghum_Seeds_(05410446)_(52995387780).jpg',
        },
        {
            'name': 'Millet',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/81/Finger_millet_seeds.jpg/500px-Finger_millet_seeds.jpg',
            'image_alt': 'Finger millet seeds',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Finger_millet_seeds.jpg',
        },
        {
            'name': 'Vegetables & More',
            'image_url': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ed/Seeds_%281899%29_%2820525046926%29.jpg/500px-Seeds_%281899%29_%2820525046926%29.jpg',
            'image_alt': 'A selection of vegetable and field seeds',
            'image_source': 'https://commons.wikimedia.org/wiki/File:Seeds_(1899)_(20525046926).jpg',
        },
    ]
    return render(request, 'products.html', {'product_categories': product_categories})


def membership(request):
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your membership enquiry has been received. Our team will contact you soon.')
            return redirect('membership')
    else:
        form = MembershipApplicationForm()
    return render(request, 'membership.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def news(request):
    articles = NewsArticle.objects.all()[:10]
    return render(request, 'news.html', {'articles': articles})


def gallery(request):
    images = GalleryImage.objects.all()[:12]
    return render(request, 'gallery.html', {'images': images})


def governance(request):
    governance_points = [
        'Founding owner and initiating members provide the community basis for the SACCO.',
        'The Board / authorised governing body provides strategic oversight and governance.',
        'Management and the Director supervise implementation, operations and service delivery.',
        'Executives and programme teams coordinate member services, agriculture support and operations.',
        'Field staff and representatives deliver services to members and communities.',
        'Members remain the core owners and beneficiaries of the SACCO model.',
    ]
    return render(request, 'governance.html', {'governance_points': governance_points})
