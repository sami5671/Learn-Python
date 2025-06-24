from django.contrib import admin
from django.urls import path
from  .import views
# from views import home
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home),
]


# MVT
# URL ===> views ===> Template/Text
