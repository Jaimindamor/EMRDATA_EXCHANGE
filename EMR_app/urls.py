from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns=[

    path('PatientAPI/',views.PatientAPI.as_view(),name="doctor"),
    path('ProcedureAPI/',views.ProcedureAPI.as_view(),name="None"),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token_refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
    
]