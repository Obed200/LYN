from django.urls import path
from . import views
from .views import home, gallery, contact, admin_dashboard, upload_image, delete_image, site_settings, download_image, download_hero_video, about_page_edit

app_name = 'gallery'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/message/',views.message, name='message'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('delete-image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('site-settings/', views.site_settings, name='site_settings'),
    path('download-image/<int:image_id>/', views.download_image, name='download_image'),
    path('download-hero-video/', views.download_hero_video, name='download_hero_video'),
    path('dashboard/about-page/', about_page_edit, name='about_page_edit'),
    path('dashboard/about-features/', views.about_features_manage, name='about_features_manage'),
    path('dashboard/about-features/delete/<int:feature_id>/', views.about_feature_delete, name='about_feature_delete'),
    path('about/', views.about, name='about'),
]