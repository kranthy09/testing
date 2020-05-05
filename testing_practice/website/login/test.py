from .models import User
from django.test import TestCase
import pytest
# Create your tests here.import pytest

@pytest.mark.django_db
def test_my_user(user):
    #Arrange
    
    #Act
    me = User.objects.get(username='jimpak_jest')
    
    #Assert
    assert me.is_superuser is True