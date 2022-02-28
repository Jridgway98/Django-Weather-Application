"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views as board_views
from data import views as data_views
from graphs import views as graph_views

urlpatterns = [
    url(r'^$', board_views.BoardListView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', board_views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', board_views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
            ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', board_views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', board_views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        board_views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^cities/$', data_views.CityList.as_view(), name='cities'),
    url(r'^cities/(?P<pk>\d+)/$', data_views.city_vehicle, name='city_vehicle'),
    url(r'^vehicles/$', data_views.VehicleList.as_view(), name='vehicles'),
    url(r'^powerplants/$', data_views.PowerplantList.as_view(), name='powerplants'),
    url(r'^graphs/$', graph_views.GraphView, name='graphs'),
    url(r'^graphs/citygraph/$', graph_views.CityGraphView, name='CityGraphView'),
    url(r'^graphs/pollutantchart/$', graph_views.PollutantChartView, name='PollutantChartView'),
    url(r'^graphs/pm25hourlychart/$', graph_views.PM25HourlyChartView, name='PM2.5HourlyChartView'),
    url(r'^graphs/pm25yearlychart/$', graph_views.PM25YearlyChartView, name='PM2.5YearlyChartView'),
    url(r'^graphs/highestamount/$', graph_views.HighestAmountsChartView, name='HighestAmountsChartView'),
    url(r'^graphs/vehiclechart/$', graph_views.VehicleChartView, name='VehicleChartView'),
    url(r'^graphs/directionchart/$', graph_views.DirectionChartView, name='DirectionChartView'),

    #url(r'^main/$', graph_views.ShowCities, name='ShowCities'),





    ]
