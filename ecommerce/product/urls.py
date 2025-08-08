from django.urls import path
from . import views
urlpatterns =[

    path('lists/', views.products, name='product_lists'),
    path('<int:product_id>/',views.product_details,name='product_details')
    
]