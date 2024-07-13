from django.urls import path

from customer.views.auth import login_page, logout_page, register_page
from customer.views.customers import export_data, CustomersTemplateView, AddCustomerView, DeleteCustomerView, \
    EditCustomerView

urlpatterns = [
    path('customer-list/', CustomersTemplateView.as_view(), name='customers'),
    path('add-customer/', AddCustomerView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', DeleteCustomerView.as_view(), name='delete'),
    path('customer/<int:pk>/update', EditCustomerView.as_view(), name='edit'),
    # Authentication path
    path('login-page/', login_page, name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', register_page, name='register'),
    path('export-data/', export_data, name='export_data')
]
