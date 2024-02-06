from django.urls import path
from . import views

urlpatterns = [
    path('user-stadium/', views.UserStadiumList.as_view(), name='user-stadium-list'),
    #  path('user/stadiums/', views.UserStadiumListView.as_view(), name='user_stadiums'),
    path('owner-stadium/', views.OwnerFieldList.as_view(), name='owner-stadium-list'),
    path('owner-stadium/<int:pk>/', views.OwnerFieldDetail.as_view(), name='owner-field-detail'),
    path('owner-bookings/', views.OwnerBookingList.as_view(), name='owner-booking-list'),
    path('owner-bookings/<int:pk>/', views.OwnerBookingDetail.as_view(), name='owner-booking-detail'),
    path('stadiums/<int:stadium_id>/book/', views.BookingsCreateView.as_view(), name='book-stadium'),
]