from django.conf.urls import url
from django.contrib import admin
from . import view, testdb, search

urlpatterns = [
    url(r'^ajax$', view.ajax),
    url(r'^ajaxPost$', view.ajaxPost),
	url(r'^$', view.hello),
    url(r'^testdb$', testdb.insertData),
    url(r'^getUser$', testdb.getData),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search.search_post),
    url(r'^admin/', admin.site.urls),
    url(r'^data$', view.getGeojson),
]
