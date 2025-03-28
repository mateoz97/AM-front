"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web_project.views import SystemView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('app.authentication.urls')),
    path("", include("app.dashboards.urls")),
    path("", include("app.pages.urls")),
    path("", include("app.layouts.urls")),
    path("", include("app.cards.urls")),
    path("", include("app.ui.urls")),
    path("", include("app.extended_ui.urls")),
    path("", include("app.icons.urls")),
    path("", include("app.forms.urls")),
    path("", include("app.form_layouts.urls")),
    path("", include("app.tables.urls")),
]

handler404 = SystemView.as_view(template_name="pages_misc_error.html", status=404)
handler400 = SystemView.as_view(template_name="pages_misc_error.html", status=400)
handler500 = SystemView.as_view(template_name="pages_misc_error.html", status=500)
