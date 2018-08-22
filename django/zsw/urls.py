from django.conf.urls import url
from zsw import views
from zsw.action import user

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # url(r'^.*\.html', views.gentella_html, name='gentella'),
    #
    # # The home page
    # url(r'^$', views.index, name='index'),

    url(r'^$', views.hello),
    url(r'^user/login', user.login),
    url(r'^notice_del_confirm', views.notice_del_confirm),

]


