from django.urls import path
from .views import UserAPI, UpdateProfileView, ChangePasswordsView, RegistrationView, LogoutAPIView, SetNewPasswordAPIView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail

urlpatterns = [
    # path('register/', UserAPI.as_view(), name="register"),
    # path('login/', LoginAPIView.as_view(), name="login"),
    # path('logout/', LogoutAPIView.as_view(), name="logout"),
    # path('api/getUserDetail/', UserAPI.as_view(), name='user'),
    # path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    # #     path('request-reset-email/', RequestPasswordResetEmail.as_view(),
    # #          name="request-reset-email"),
    # #     path('password-reset/<uidb64>/<token>/',
    # #          PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # #     path('password-reset-complete', SetNewPasswordAPIView.as_view(),
    # #          name='password-reset-complete'),
    # path('changePassword', ChangePasswordsView.as_view(), name='changePassword'),
    # path('update_profile/<int:pk>/', UpdateProfileView.as_view(),
    #      name='auth_update_profile'),
]