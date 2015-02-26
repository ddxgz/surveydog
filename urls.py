from django.conf.urls import patterns, url

from surveydog import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # ex: /surveydog/5/
    # url(r'^(?P<survey_id>\d+)/$', views.detail, name='detail'),
    # # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # url(r'^(?P<survey_id>\d+)/vote/$', views.vote, name='vote'),
    # url(r'^login/$', views.login, name='login'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^allusers/$', views.allusers, name='allusers'),
    # url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/$', views.post_survey, name='post_survey'),
    url(r'^post_success/$', views.post_success, name='post_success'),
    # url(r'^admin_vote/$', views.admin_vote, name='admin_vote'),

    url(r'^(?P<survey_id>\d+)/$', views.admin_detail, name='admin_detail'),
    url(r'^(?P<survey_id>\d+)/admin_results/$', views.admin_results, name='admin_results'),
    url(r'^(?P<survey_id>\d+)/admin_vote/$', views.admin_vote, name='admin_vote'),

    url(r'^modelform/$', views.modelform, name='modelform'),

#    (r'^pages/', include('django.contrib.flatpages.urls')),
)
