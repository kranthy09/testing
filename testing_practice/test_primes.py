from primes import is_prime
import pytest

def test_is_prime_for_prime_numbers_returns_true():
    
    #Arrange
    number_to_check = 3
    
    #Act
    result = is_prime(number_to_check)
    
    #Assert
    assert result is True
    
def test_is_prime_for_zero_prime_numbers_returns_false():
    
    #Arrange
    number_to_check = 0
    
    #Act
    result = is_prime(number_to_check)
    
    #Assert
    assert result is False

def test_is_prime_for_one_prime_numbers_returns_true():
    
    #Arrange
    number_to_check = 1
    
    #Act
    result = is_prime(number_to_check)
    
    #Arrange
    assert result is False
    

def test_is_prime_for_float_prime_numbers_returns_False():
    
    #Arrange
    number_to_check = 4.0
    
    #Act
    with pytest.raises(Exception):
        is_prime(number_to_check)
    
def test_is_prime_for_negative_numbers_returns_False():
    
    #Arrange
    number_to_check = -5
    
    #Act
    result = is_prime(number_to_check)
    
    #Assert
    assert result is False
    
def test_is_prime_for_string_input_is_given():
    
    #Arrange
    number_to_check = '1'
    
    #Act
    with pytest.raises(Exception):
        is_prime(number_to_check)