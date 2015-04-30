from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
               url(r'^$', 'nutritional_facts.apps.nutrition.views.index_view'),
               url(r'^(?P<nutrition_id>\d+)/$', 'nutritional_facts.apps.nutrition.views.single'),
               )