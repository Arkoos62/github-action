def test_fizzbuzz():
    result = fizzbuzz(5)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizzbuzz_up_to_15():
    result = fizzbuzz(15)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizzbuzz_up_to_0():
    result = fizzbuzz(0)
    assert result == []

def test_fizzbuzz_negative():
    result = fizzbuzz(-5)
    assert result == []