from django.conf.urls import patterns, url

urlpatterns = patterns('postreply.views',
                        
                       (r'^postreply/$','home'),
                       (r'^post/$','post'),
                       (r'^reply/$','reply'),


                     
                       )