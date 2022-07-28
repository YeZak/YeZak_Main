
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemList, ItemDetail

app_name='posts'
 
urlpatterns = [
    # path('detail/<int:pk>/', views.item_detail, name='posts_detail'),
    # path('create/', views.create, name='create'),
    # path('upload/', views.item_upload, name='posts_upload'),
    # path('', views.item_list, name='posts_list'),
    # path('update/<int:item_id>/', views.update, name='posts_update'),
    # path('delete/', views.item_delete),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
