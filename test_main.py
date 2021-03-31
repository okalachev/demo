import main

def test_return_greeting():
    assert main.return_greeting('foobar') == 'hello foobar'
    assert main.return_greeting('bob') == 'hello bob'
    assert main.return_greeting('') == 'hello'
