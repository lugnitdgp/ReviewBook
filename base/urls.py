from django.urls import path

from base.views import(
    base,
    search,
    home,
    select_category,
    
)

app_name='base'

urlpatterns = [
    path('', home, name="home"),
    path('search/',search,name="search"),
    path('selectcategory/', select_category, name="select_category"),
    ]
