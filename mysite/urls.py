"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
#include() : 다른 URLconf를 참조하게 함
#django가 함수 include()를 만나면 URL의 시점까지 일치하는 부분을 잘라내고 남은 문자열 부분을 include된 URLconf로 전달

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

]

'''
ex : 
예시
127.00.0.1/polls/ 이 들어온다면 이 url을 파싱한 후 polls를 파싱한 후 
polls에 url로 연결해주는것
'''
