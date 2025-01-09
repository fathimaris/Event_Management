from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Event_App import views, User_views, Admin_views

urlpatterns=[
    path('', views.Index, name='index'),
    path('Gallery',views.Gallery,name='Gallery'),
    path('Testimonials',views.Testimonials,name='Testimonials'),
    path('Cooperative_Event',views.Cooperative_Event,name='Cooperative_Event'),
    path('Wedding_Venue',views.Wedding_Venue,name='Wedding_Venue'),
    path('Customer_Registration/',views.Customer_Registration,name='Customer_Registration'),
    path('Login/',views.Login,name='Login'),
    path('Logout_view/',views.Logout_view,name='Logout_view'),
    path('UserBase/',User_views.UserBase,name='UserBase'),
    path('User_details/',User_views.User_details,name='User_details'),
    path('Edit_Profile/', User_views.Edit_Profile, name='Edit_Profile'),
    path('Booking_Event/',User_views.Booking_Event,name='Booking_Event'),
    path('View_Booked_Event/',User_views.View_Booked_Event,name='View_Booked_Event'),

    path('create-checkout-session/', User_views.create_checkout_session, name='create_checkout_session'),
    # Create checkout session
    path('success/', User_views.payment_success, name='payment_success'),
    path('cancel/', User_views.payment_cancel, name='payment_cancel'),  # Payment cancel page
    path('AdminBase/',Admin_views.AdminBase,name='AdminBase'),
    path('view_registered_users/', Admin_views.view_registered_users, name='view_registered_users'),
    path('Delete_customer/<int:user_id>/', Admin_views.Delete_customer, name='Delete_customer'),
    path('AdminBase/view-registered-events/', Admin_views.view_registered_events, name='view_registered_events'),
    path('approve/<int:id>/',Admin_views.approve_event, name='approve_event'),
    path('reject/<int:id>/',Admin_views.reject_event, name='reject_event'),
    path('calendar_view/', Admin_views.calendar_view, name='calendar_view'),
    path('calendar/<int:year>/<int:month>/', Admin_views.calendar_view, name='calendar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)