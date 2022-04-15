from django.urls import path

from location_app import views


urlpatterns = [
    #GET: Available units
    path('unidades-disponibles', views.AvailableUnits.as_view(), name='available_units'),
    #GET: Unit location
    path('ubicacion-de-unidad/<int:label>', views.UnitLocation.as_view(), name='unit_location'),
    #GET: Available localities
    path('alcaldias-dosponibles', views.AvailableLocalities.as_view(), name='available_locality'),
    #GET: Units inside a locality
    path('unidades-en-alcaldia', views.UnitsInLocality.as_view(), name='units_in_locality'),
    #POST: Load data with pipeline into the database
    path('fetch-data', views.FetchData.as_view(), name='fetch_data'),
]
