# conftest.py
import pytest
from nplusone.core.profiler import Profiler

@pytest.fixture(autouse=True)
def _raise_nplusone(request):
    if request.node.get_closest_marker("skip_nplusone"):
        yield
    else:
        with Profiler():
            yield