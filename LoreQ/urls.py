from django.urls import path
from LoreQ import views

urlpatterns = [
   path('',views.welcome, name='welcome'), # path(pathname, process) if pathname == '', it's mean main website
   
   path('main', views.index, name='main'),
   path('inmain/<userNAME>/<TableNo>', views.index_in, name='inmain'),
   path('inmain/<userNAME>/<TableNo>/search', views.search, name='search'),

   path('UserTable/<userNAME>/<TableNo>', views.UserTable, name='userTable'),
   path('plus_minus/<menu_id>', views.plus_minus, name='plus_minus'),
   path('delete_menu/<menu_id>', views.delete_menu, name='delete_menu'),
   path('create_queue/<ttprice>/<Uname>/<Tno>/<paymentmethod>', views.create_queue, name='create_queue'),
   path('paymentsuccess/<next_queue_id>/<ttprice>/<paymentmethod>', views.paymentsuccess, name='paymentexample'),

   path('UserQ/<userNAME>/<TableNo>', views.UserQ, name='userQ'), 

   path('reportListAllQueue', views.reportListAllQueue, name='reportListAllQueue'),
   path('controlnextqueue', views.controlnextqueue, name='controlnextqueue'),
   path('next_queue', views.next_queue, name='next_queue')
]
