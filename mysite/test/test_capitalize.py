import pytest
import os
import sys
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.contrib.auth.models import User
from django.conf import settings


def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='amiradmin')
    assert me.is_superuser