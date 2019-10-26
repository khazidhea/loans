from django.urls import path
import loans.views as views


urlpatterns = [
    path('', views.LoanListView.as_view(), name='loan-list'),
    path('create', views.LoanCreateView.as_view(), name='loan-create'),
    path('api/day/', views.api_day),
]
