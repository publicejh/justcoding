from django.urls import path, include
from .views import BandList, BandDetail, BandMemberDetail, BandCreate, BandParticipateCreateView,\
    BandParticipateListView, BandInvitationTokenCreateView, BandInvitationTokenRetrieveView, BandUpdateView

urlpatterns = [
    path('', BandList.as_view()),
    path('<int:pk>/', BandDetail.as_view()),
    # path('<int:pk>/member', BandMemberDetail.as_view()),
    path('create/', BandCreate.as_view()),
    path('<int:pk>/update/', BandUpdateView.as_view()),
    path('<int:band_id>/invite/', BandParticipateCreateView.as_view()),
    path('<int:band_id>/member/', BandParticipateListView.as_view()),
    path('<int:band_id>/invitation-token/', BandInvitationTokenCreateView.as_view()),
    path('n/<token>', BandInvitationTokenRetrieveView.as_view()),
]