"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Alfredo Elias Rivas
Date:   03/21/2021
"""


import introcs
import currency


def test_before_space():
    """
    Test procedure for before_space
    """
    print('Testing before_space')

    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello',result)

    result = currency.before_space('He llo World')
    introcs.assert_equals('He',result)

    result = currency.before_space(' Hello World')
    introcs.assert_equals('',result)

    result = currency.before_space('Hel loWor ld')
    introcs.assert_equals('Hel',result)

    result = currency.before_space('Hello  World')
    introcs.assert_equals('Hello',result)

    result = currency.before_space(' Hello')
    introcs.assert_equals('',result)


def test_after_space():
    """
    Test procedure for after_space
    """
    print('Testing after_space')

    result = currency.after_space('Hello World')
    introcs.assert_equals('World',result)

    result = currency.after_space('He llo World')
    introcs.assert_equals('llo World',result)

    result = currency.after_space(' Hello World')
    introcs.assert_equals('Hello World',result)

    result = currency.after_space('Hel loWor ld')
    introcs.assert_equals('loWor ld',result)

    result = currency.after_space('Hello  World')
    introcs.assert_equals(' World',result)

    result = currency.after_space(' Hello')
    introcs.assert_equals('Hello',result)

    result = currency.after_space('HelloWorld ')
    introcs.assert_equals('',result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """
    print('Testing first_inside_quotes')

    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result)

    result = currency.first_inside_quotes('A "B C D "E F" G')
    introcs.assert_equals('B C D ',result)

    result = currency.first_inside_quotes('""A B C D "E F" G')
    introcs.assert_equals('',result)

    result = currency.first_inside_quotes('"A B C" D "E F" "G H I"')
    introcs.assert_equals('A B C',result)

    result = currency.first_inside_quotes('"Can\'t Be this?"')
    introcs.assert_equals("Can't Be this?",result)


def test_get_src():
    """
    Test procedure for get_src
    """
    print('Testing get_src')
    result = currency.get_src('{"success": true, "src": "2 United States Dollar'+
    's", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Sour'+
    'ce currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_src('{"success":true, "src":"2 United States Dollars",'+
    ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":true, "src":      "2 United States '+
    'Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":false,"src": "","dst":"","error":"'+
    'Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print('Testing get_dst')

    result = currency.get_dst('{"success": true, "src": "2 United States Dollars"'+
    ', "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success":false,"src":"","dst": "","error":'+
    '"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_dst('{"success":true, "src":"2 United States Dollars",'+
    ' "dst": "1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success":true, "src":"2 United States Dollars",'+
    ' "dst":        "1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success":false,"src": "","dst":"","error":"Sou'+
    'rce currency code is invalid."}')
    introcs.assert_equals('',result)


def test_has_error():
    """
    Test procedure for has_error
    """
    print('Testing has_error')

    result = currency.has_error('{"success":false,"src":"","dst": "","error":'+
    '"Source currency code is invalid."}')
    introcs.assert_true(True)

    result = currency.has_error('{"success":false,"src": "","dst":"","error":'+
    '"Source currency code is invalid."}')
    introcs.assert_true(True)

    result = currency.has_error('{"success":true, "src":"2 United States '+
    'Dollars", "dst": "1.772814 Euros", "error":""}')
    introcs.assert_false(False)

    result = currency.has_error('{"success":true, "src":"2 United States Doll'+
    'ars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(False)

    result = currency.has_error('{"success":false,"src": "","dst":"","error":'+
    '      "Source currency code is invalid."}')
    introcs.assert_true(True)


def test_service_response():
    """
    Test procedure for service_response
    """
    print('Testing service_response')

    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars",'+
    ' "dst": "2.2160175 Euros", "error": ""}',result)

    result = currency.service_response('USD','ER',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '+
    '"The rate for currency ER is not present."}',result)

    result = currency.service_response('US','DOP', 2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'+
    ' "The rate for currency US is not present."}',result)

    result = currency.service_response('USD','EUR', 0)
    introcs.assert_equals('{"success": true, "src": "0.0 United States Dollars"'+
    ', "dst": "0.0 Euros", "error": ""}',result)

    result = currency.service_response('USD','EUR',-100)
    introcs.assert_equals('{"success": true, "src": "-100.0 United States '+
    'Dollars", "dst": "-88.6407 Euros", "error": ""}',result)


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print('Testing iscurrency')

    result = currency.iscurrency('DOP')
    introcs.assert_true(True)

    result = currency.iscurrency('DO')
    introcs.assert_false(False)


def test_exchange():
    """
    Test procedure for exchange
    """
    print('Testing exchange')

    result = currency.exchange('USD','DOP', 2.5)
    introcs.assert_floats_equal('127.4375', '127.4375')

    result = currency.exchange('DOP','USD', -2.5)
    introcs.assert_floats_equal('-127.4375', '-127.4375')


test_before_space()
test_after_space()
test_first_inside_quotes()
test_has_error()
test_get_src()
test_get_dst()
test_service_response()
test_iscurrency()
test_exchange()


print('All tests completed successfully')
