from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import GalleryImage, Category, ContactMessage, SiteSettings, AboutPage
from .forms import GalleryImageForm, ContactForm, SiteSettingsForm, AboutPageForm

def home(request):
    featured_images = GalleryImage.objects.filter(is_featured=True)[:6]
    categories = Category.objects.all()[:4]
    context = {
        'featured_images': featured_images,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = GalleryImage.objects.all()
    categories = Category.objects.all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        images = images.filter(category_id=category_id)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        images = images.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_id,
        'search_query': search_query,
    }
    return render(request, 'gallery.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('gallery:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

@staff_member_required
def admin_dashboard(request):
    total_images = GalleryImage.objects.count()
    total_categories = Category.objects.count()
    total_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    
    recent_images = GalleryImage.objects.all()[:5]
    recent_messages = ContactMessage.objects.all()[:5]
    
    context = {
        'total_images': total_images,
        'total_categories': total_categories,
        'total_messages': total_messages,
        'unread_messages': unread_messages,
        'recent_images': recent_images,
        'recent_messages': recent_messages,
    }
    return render(request, 'admin/dashboard.html', context)

@staff_member_required
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = request.user
            image.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('gallery:admin_dashboard')
    else:
        form = GalleryImageForm()
    
    return render(request, 'admin/upload_image.html', {'form': form})

@staff_member_required
def delete_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('gallery:admin_dashboard')
    return render(request, 'admin/confirm_delete.html', {'object': image})

# TODO: Create 'admin/site_settings.html' template for site settings management
@staff_member_required
def site_settings(request):
    settings_obj, created = SiteSettings.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        if 'delete_video' in request.POST and settings_obj.hero_video:
            settings_obj.hero_video.delete(save=False)
            settings_obj.hero_video = None
            settings_obj.save()
            messages.success(request, 'Hero video deleted successfully!')
            return redirect('gallery:site_settings')
        form = SiteSettingsForm(request.POST, request.FILES, instance=settings_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Site settings updated successfully!')
            return redirect('gallery:site_settings')
    else:
        form = SiteSettingsForm(instance=settings_obj)
    
    return render(request, 'admin/site_settings.html', {'form': form})

@staff_member_required
def about_page_edit(request):
    about_obj, created = AboutPage.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AboutPageForm(request.POST, request.FILES, instance=about_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'About page updated successfully!')
            return redirect('gallery:about_page_edit')
    else:
        form = AboutPageForm(instance=about_obj)
    return render(request, 'admin/about_page_edit.html', {'form': form})

def download_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    response = HttpResponse(image.image.read(), content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{image.title}.jpg"'
    return response

def download_hero_video(request):
    settings_obj = SiteSettings.objects.first()
    if not settings_obj or not settings_obj.hero_video:
        messages.error(request, 'No video available for download.')
        return redirect('gallery:home')
    video_file = settings_obj.hero_video
    response = HttpResponse(video_file.open('rb'), content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename="{video_file.name.split("/")[-1]}"'
    return response
