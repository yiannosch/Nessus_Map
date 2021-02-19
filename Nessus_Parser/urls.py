from django.urls import path, include
from . import views

app_name = 'nessus'

urlpatterns = [
    path('vulnerabilities/', views.parse_XML, name='nessusparse'),
    path('upload/', views.upload_file, name='upload'),
    path('services/', views.do_port_filter, name='services'),
    path('parseOS/', views.do_parse_os, name='parseos'),
    path('executive-report/', views.generate_executive_report, name='executive-report'),
    path('gen-html/', views.generate_html_report, name="gen-html-report"),
    path('gen-json/', views.generate_json_file, name="gen-json"),
    path('load-json/', views.load_json_file, name="load-json")
]
