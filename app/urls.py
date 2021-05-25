from django.urls import path
from .views import landingview, supplierlistview, productlistview, addsupplier, deletesupplier

urlpatterns = [
    path('landing/', landingview),
    path('suppliers/', supplierlistview),
    path('products/', productlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier)
]
