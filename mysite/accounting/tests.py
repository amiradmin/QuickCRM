from django.test import TestCase
from django.contrib.auth.models import User
from training.models import Product
import pytest
from nplusone.core.profiler import Profiler
from django.db import connection

@pytest.fixture()
def make_data():
    for i in range(10):
        Product.objects.create( name=f"Song {i + 1}")

@pytest.mark.django_db()
def test_print_product(make_data):
    print(len(connection.queries))


@pytest.mark.django_db()
def test_users_query_performances():
    User.objects.all()


@pytest.mark.django_db()
def test_products_query_performances():
    Product.objects.all()

#
# @pytest.fixture(autouse=True)
# def record_query_count(request):
#     from django.test.utils import CaptureQueriesContext
#     from django.db import connection
#
#     with CaptureQueriesContext(connection) as context:
#         yield
#     num_performed = len(context)
#
#     if not hasattr(request.config, "query_counts"):
#         request.config.query_counts = dict()
#     request.config.query_counts[request.node.nodeid] = num_performed