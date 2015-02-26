# surveydog

A simple Django app for survey. 

Use django's admin to post a survey.

##Usage
1. Add 'surveydog' app in the 'INSTALLED_APPS' in settings.py:

	```
	INSTALLED_APPS = (
    	...
   		'surveydog',
		...
	)
	```

2. Add the surveydog's url to your site's urls.py:

	```
	urlpatterns = patterns('',

   		 url(r'^admin/', include(admin.site.urls)),
    	 ...
   		 url(r'^surveydog/', include('surveydog.urls', namespace="surveydog")),
    )
	```
3. Syncdb through migrate.
4. Runserver. 
