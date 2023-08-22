
from django.urls import path
from.import views


urlpatterns = [
    path('',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('regsave',views.regsave,name='regsave'),
    path('loginsave',views.loginsave,name='loginsave'),
    path('dataentry',views.dataentry,name='dataentry'),
    path('table',views.table,name='table'),
    path('datasave',views.datasave,name='datasave'),
    path('delete',views.delete,name='delete'),
    path('logout',views.logout,name='logout'),
    path('allluser',views.allluser,name='allluser'),
    path('deleteuser',views.deleteuser,name='deleteuser'),
    path('login_view',views.login_view,name='login_view'),
]
