from django.urls import path, include
from .views import (
  
    IndexView,
    donation,  
    VideosView,
    category_video,    
    VideoCategoryView,
    AudiosView,
    subscribe,
    faq,
    live_view,
    odds_view,
    privacy_policy,
    tandc,
    contact,
    Youtube,
    vid_json,
    VideosTestView

)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    

    path('videos/', VideosView.as_view(), name='videos'),
    path('videostest/', VideosTestView.as_view(), name='videostest'),
    path('podcast/', AudiosView.as_view(), name='podcast'),
    
    
    path('videos-category/<int:id>/<slug:slug>',
         VideoCategoryView.as_view(), name='category_video'),
    
    
    
    path('subscribe/', subscribe, name='subscribe'),
    path('frequently-asked-questions/', faq, name='faq'),
    path('livescores/', live_view, name='live_view'),
    path('odds/', odds_view, name='odds_view'),
    path('donate/', donation, name='donate'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', tandc, name='tandc'),
    path('contact/', contact, name='contact'),
    path('youtube-json/', Youtube.as_view(), name='youtube-json'),
    path('vid-json/<int:num_posts>/', vid_json, name='vid-json'),
    




]
