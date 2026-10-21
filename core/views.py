from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm, MembershipApplicationForm
from .models import GalleryImage, HomePageHero, NewsArticle, ProductCategory


def home(request):
    hero = HomePageHero.objects.first()
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
    stats = hero.stats if hero else [
        {'value': '6', 'label': 'Core services'},
        {'value': '100%', 'label': 'Member-centered'},
        {'value': '24/7', 'label': 'Support mindset'},
    ]
    news_items = NewsArticle.objects.all()[:3]
    gallery_items = GalleryImage.objects.all()[:4]
    return render(request, 'home.html', {'service_highlights': service_highlights, 'stats': stats, 'news_items': news_items, 'gallery_items': gallery_items, 'hero': hero})


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
    product_categories = ProductCategory.objects.filter(is_active=True)
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
