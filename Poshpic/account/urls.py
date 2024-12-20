from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", views.RegisterUserView.as_view()),
    path("otp_verify/", views.Verify_OTP.as_view()),
    path("resend_otp/", views.ResntOtp.as_view()),
    path("login/", views.LoginUserView.as_view()),
    path("apitoken/", TokenObtainPairView.as_view()),
    path("refreshtoken/", TokenRefreshView.as_view()),
    path("forgotpassword/", views.ForgotpasswordView.as_view()),
    path("resetpassword/<str:uidb64>/<str:token>/", views.ResetPasswordView.as_view()),
    path("userprofile/", views.UserProfileView.as_view()),
    path("phtotgrapher/", views.PhtotgrapherApiview.as_view()),
    path("phtotgraphersearch/",views.PhtotgrapherSearchAPIView.as_view(),name="photographer-list"),
]
