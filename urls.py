from django.urls import path
from . import views

urlpatterns = [
    # route for insert/create operation. its for get and post request for insert operation
    path('', views.employee_form, name='insert'),

    # route for update operation. Its for get and post request for update operation
    path('<int:id>/', views.employee_form, name='update'),

    # route for display/retrieve records or operation. Get req. to retrieve and display all records
    path('list/', views.employee_list, name='retrieve'),

    # url for delete operation
    path('delete/<int:id>', views.employee_delete, name='delete')
]