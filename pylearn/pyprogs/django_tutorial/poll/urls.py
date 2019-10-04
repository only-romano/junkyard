from django.urls import path

from . import views

app_name = 'poll'      # Namespaces added to URLconf.
urlpatterns = [
    # /poll/
    path('', views.index, name='index'),
    # /poll/<question_id>/ (example: /poll/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /poll/<question_id>/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /poll/<question_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]