import pytest
from programs import example

def test_endsPy():
    assert example.endsPy("ilovepy") == True
    assert example.endsPy("welovepy") == True
    assert example.endsPy("welovepyforreal") == False
    assert example.endsPy("pyiscool") == False
    assert example.endsPy("hurrayforpY") == True
    
    
def test_one():
    assert example.one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) == {'apple':3, 'orange':2, 'banana':1}
    assert example.one(['tic', 'tac', 'toe']) == {'tic':1, 'tac':1, 'toe':1}
    assert example.one([]) == {}
    assert example.one(['bert']*1000) == {'bert':1000}

def test_two():
    for a, b in [ (5, 3), (3, 1.5), (-5, 7) , (0, 1) ]:
        for operator in ['+', '-', '*', '/']:
            assert example.two(a, b, operator) == eval(f'{a} {operator} {b}')

def test_three():
    assert example.three(7) == 4
    assert example.three(64) == 64
    assert example.three(32) == 25
    assert example.three(1) == example.three(2) == 1

def test_four():
    assert example.four(32, 24) == 8
    assert example.four(18, 11) == 1
    assert example.four(10, 50) == 10
    assert example.four(1, 1) == 1
    assert example.four(2, 2048) == 2

def test_five():
    assert example.five('wxyz') == 'vwxy'
    assert example.five('abc') == 'zab'
    assert example.five('aAbB') == 'zZaA'
    assert example.five('abcabcABCABC') == 'zabzabZABZAB'
    assert example.five('hello world') == 'gdkkn vnqkc'
    assert example.five('54321') == '54321'
