from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Token based auth
    # Do a request to login_social_token_user with provider name to grant the access
    url(r'^login/', include('rest_social_auth.urls_token')),
    # Use jwt auth for micro-services
    # Do a request to login_social_jwt_user with provider name to grant the access
    url(r'^login/', include('rest_social_auth.urls_jwt')),
    # Get the current user details and token to access app resources
    url(r'^token/', views.UserTokenDetailView.as_view(), name="current_user_token"),
    # Get current user details and jwt token to access app resources
    url(r'^jwt/', views.UserTokenDetailView.as_view(), name="current_user_jwt"),
]