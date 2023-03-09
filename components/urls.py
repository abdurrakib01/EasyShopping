from django.urls import path
from .views import (
    ProductView, 
    ProductDetailView, 
    MobileView, 
    AddToCartView, 
    ShowCartsView,
    plus_cart,
    minus_cart,
    buy_now,
    delete_cart,
    checkout_view,
    order_done,
    order,
    orderplaced)
from django.conf import settings
from django.conf.urls.static import static
app_name = 'components'
urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('detial/<int:pk>', ProductDetailView.as_view(),name='detail'),
    path('mobile/', MobileView.as_view(), name="mobile"),
    path('mobile/<slug:data>/', MobileView.as_view(), name="mobile-data"),
    path('add-to-cart/', AddToCartView.as_view(), name="addtocart"),
    path('carts/', ShowCartsView.as_view(), name='carts'),
    path('pluscart/', plus_cart),
    path('minuscart/', minus_cart),
    path('buy-now/', buy_now, name="buy_now"),
    path('delete-cart/', delete_cart, name='delete_cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('orderdone/', order_done, name="order_done"),
    path('order/', order, name="order"),
    path('orderplaced/', orderplaced, name='orderplaced'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
