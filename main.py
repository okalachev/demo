def return_greeting(who):
    if (not who):
        return 'hello'
    return 'hello ' + who


print(return_greeting('world'))
