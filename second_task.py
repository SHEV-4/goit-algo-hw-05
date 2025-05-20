from typing import Callable

def is_number(text:str)->bool:
    try:
        float(text)
        return True
    except ValueError:
        return False
def generator_numbers(text:str):
    for word in text.split(' '):
        if is_number(word):
            yield float(word)

def sum_profit(text:str,func:Callable[[str],None]):
    total = 0
    for num in func(text):
        total += num
    return total