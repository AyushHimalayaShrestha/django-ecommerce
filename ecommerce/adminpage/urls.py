from django.urls import path
from . import views
urlpatterns =[

    path('category/add/', views.add_category, name='add_category'),
    path('product/add/',views.add_product, name='add_product'),
    path('product/lists',views.products, name="dashboard_product_lists"),
    path('product/update/<int:product_id>/',views.update_product,name='update_product'),
    path('product/delete/<int:product_id>/',views.delete_product,name='delete_product'),
    path('category/list/',views.category,name='dashboard_category_lists')
   
    
]