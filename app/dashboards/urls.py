from django.urls import path
from .views import DashboardsView



urlpatterns = [
    path(
        "main/",
        DashboardsView.as_view(template_name="dashboard_analytics.html"),
        name="index",
    )
]
