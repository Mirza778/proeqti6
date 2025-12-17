from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.get_all),
    path("cars/<int:car_id>/", views.get),
    path("cars/make/<str:make>/", views.get_by_make),
    path("cars/price/<float:min_price>/<float:max_price>/", views.get_by_price_range),
    path("cars/filter/<float:price>/<int:stock>/", views.get_by_price_less_or_stock_less_then_price),
]
