from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('nutritional_facts.apps.nutrition.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^list/', include('nutritional_facts.apps.nutrition.urls')),
    url(r'^single/', include('nutritional_facts.apps.nutrition.urls')),
]
