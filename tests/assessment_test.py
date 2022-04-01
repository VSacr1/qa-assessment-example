import pytest
from programs import example

def test_endsPy():
    assert example.endsPy("ilovepy") == True
    assert example.endsPy("welovepy") == True
    assert example.endsPy("welovepyforreal") == False
    assert example.endsPy("pyiscool") == False
    assert example.endsPy("hurrayforpY") == True
    
    
def test_one():
    assert python2.one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) == {'apple':3, 'orange':2, 'banana':1}
    assert python2.one(['tic', 'tac', 'toe']) == {'tic':1, 'tac':1, 'toe':1}
    assert python2.one([]) == {}
    assert python2.one(['bert']*1000) == {'bert':1000}

def test_three():
    for a, b in [ (5, 3), (3, 1.5), (-5, 7) , (0, 1) ]:
        for operator in ['+', '-', '*', '/']:
            assert python2.two(a, b, operator) == eval(f'{a} {operator} {b}')

def test_four():
    assert python2.three(7) == 4
    assert python2.three(64) == 64
    assert python2.three(32) == 25
    assert python2.three(1) == python2.three(2) == 1

def test_five():
    assert python2.four(32, 24) == 8
    assert python2.four(18, 11) == 1
    assert python2.four(10, 50) == 10
    assert python2.four(1, 1) == 1
    assert python2.four(2, 2048) == 2

def test_six():
    assert python2.five('wxyz') == 'vwxy'
    assert python2.five('abc') == 'zab'
    assert python2.five('aAbB') == 'zZaA'
    assert python2.five('abcabcABCABC') == 'zabzabZABZAB'
    assert python2.five('hello world') == 'gdkkn vnqkc'
    assert python2.five('54321') == '54321'
