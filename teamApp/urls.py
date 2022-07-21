from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MemberListView.as_view(), name='member_list'),
	path('add/', views.AddMemberView.as_view(), name='member_create'),
    path('<int:pk>/edit/', views.EditMemberView.as_view(), name='member_edit'),
    path('<int:pk>/delete/', views.MemberDeleteView.as_view(), name='member_delete'),
]
