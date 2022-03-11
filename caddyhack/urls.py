"""caddyhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from caddyhackapi.views import (login_user, register_user, CommentView, GolfCourseView, GolferView, PostView, FinalScoreView, NumOfHolesView, HoleByHoleView, IndividualHoleView)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'comments', CommentView, 'comment')
router.register(r'golf_courses', GolfCourseView, 'golf_course')
router.register(r'golfers', GolferView, 'golfer')
router.register(r'posts', PostView, 'post')
router.register(r'final_scores', FinalScoreView, 'final_score')
router.register(r'num_of_holes', NumOfHolesView, 'num_of_hole')
router.register(r'hole_by_holes', HoleByHoleView, 'hole_by_hole')
router.register(r'individual_holes', IndividualHoleView, 'individual_hole')

urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user)
]
