from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name ='about'),
    # 'outfits/' - Outfits Index Route
    path('outfits/', views.outfits_index, name='outfits_index'),
    # 'outfits/<int:outfit_id>/' Outfits Details Route
    path('outfits/<int:outfit_id>/', views.outfits_detail, name = "outfits_detail"),
    # 'outfits/create/' Outfits Create Route
    path('outfits/create', views.OutfitCreate.as_view(), name='outfits_create'),
    # 'outfits/<int:pk>/update/'
    path('outfits/<int:pk>/update/', views.OutfitUpdate.as_view(), name='outfits_update'),
    # 'outfits/<int:pk>/delete/'
    path('outfits/<int:pk>/delete/', views.OutfitDelete.as_view(), name='outfits_delete'),
    # 'outfits/<int:outfit_id>/add_accessories/'
    path('outfits/<int:outfit_id>/add_accessories/', views.add_accessories, name="add_accessories"),
    path('outfits/<int:outfit_id>/assoc_shoe/<int:shoe_id>/', views.assoc_shoe, name='assoc_shoe'),
    path('shoes/', views.ShoeList.as_view(), name='shoes_index'),
    path('shoes/<int:pk>/', views.ShoeDetail.as_view(), name='shoes_detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),

]

