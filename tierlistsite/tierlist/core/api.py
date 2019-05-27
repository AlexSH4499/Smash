from django.conf.urls import url

from models import views as FighterReadView
from fighters import views as fighters_views

urlpatterns = [
    #{%url "api:fighters"%}
    url(
        regex=r"fighters/$",
        view=
    )

]
