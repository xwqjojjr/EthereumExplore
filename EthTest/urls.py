from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Blocks/',views.ShowBlocks),
    path('Tx_Block/',views.Show_number_tx_in_block),
]