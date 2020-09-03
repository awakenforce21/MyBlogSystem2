"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic.base import TemplateView

# http://localhost:8000 요청이 들어왔을 때 우리 전체 project의 홈페이지로
# 이동시킬 거예요!
# Django는 elegant URL을 지원해요!
# 정규표현식(regular expression)
# 시작 => ^, 끝 => $
# [0-9] : 1글자를 지칭
# {3,5}: 3번 반복
# [0-9]{4}
# r(raw)은 escape 문자를 한번 더 사용하지 않도록 처리
# r"^[0-9]{1,3}$"
# r"^010[1-9]\d{6,7}$"

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name = 'index.html'), name = "home"),
    path('admin/',admin.site.urls),
    path('posts/', include('posts.urls'))
]
