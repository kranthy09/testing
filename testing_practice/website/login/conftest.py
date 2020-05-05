import pytest
from .models import User

@pytest.fixture
def user():
    user = User.objects.create(username='jimpak_jest', is_superuser=True)
    return user