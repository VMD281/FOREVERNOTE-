from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.index, name='forevernote_app'),  # This will map the home URL to the `index` view
    path('del/<str:item_id>', views.remove, name='del'),  # For deleting a to-do item
    path('edit/<int:item_id>/', views.edit, name='edit'),  # Maps to the `edit` view with an integer ID

]