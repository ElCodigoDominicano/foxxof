"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Alfredo Elias Rivas
Date:   03/21/2021
"""


import introcs

APIKEY = 'XfkqLkp6B4H4k1GO8wwWsBUxiDOrq3mXEQx7vSizDkMe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    
    assert type(s) == str, 'The Value '+repr(s)+' is not a string.'
    #assert ' ' in s, repr(s)+'Atleast one space is required'
    
    pos = introcs.find_str(s, ' ')
    result = s[:pos]

    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    
    assert type(s) == str, 'The Value '+repr(s)+' is not a string.'
    assert ' ' in s, repr(s)+'Atleast one space is required'
    
    pos = introcs.find_str(s, ' ',0)
    result = s[pos+1:]
    
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """   
    
    assert type(s) == str, 'The Value '+repr(s)+' is not a string.'
    
    first = introcs.find_str(s,'"')
    second = introcs.find_str(s,'"',first+1)
    assert second != -1,'Missing 1 more double quote'
    result = s[first+1:second]
    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    assert type(json) == str, 'The Value '+repr(json)+' is not a valid string.'
    src = introcs.find_str(json,'src')
    result = json[src+4:]
    return first_inside_quotes(result)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    assert type(json) == str, 'The Value '+repr(json)+' is not a valid string.'
    src = introcs.find_str(json,'dst')
    result = json[src+4:]
    return first_inside_quotes(result)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    assert type(json) == str, 'The Value '+repr(json)+' is not a valid string.'
    sc = introcs.find_str(json,'error')
    result = json[sc+6:]
    error = first_inside_quotes(result)
    return len(error) > 4


def service_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

    '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert introcs.find_str(src, ' ') <= 0 and introcs.find_str(dst, ' ') <= 0, +\
    repr(src)+'Precondition Violated ; not the proper "3" letter format...'
    assert introcs.isspace(src) <= 0 and introcs.isspace(dst) <= 0, src+'Precon' +\
    'dition Violated ; string is empty.'
    assert len(src) and len(dst) < 4 and not 0 , src+dst+\
    'Precondition Violated ; "3" characters needed.'
    assert introcs.isalpha(src) and introcs.isalpha(dst) == True, ' Only' +\
     'Letters are Allowed.'
    #assert type(amt) == int or type(amt) == float, 'The amount 
    #entered isnt represented as a numerical amount.'
    
    s = str(amt)
    url = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='+src+\
    '&dst='+dst+'&amt='+s+'&key='+APIKEY+''
    result = introcs.urlread(url)
    return result


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert type(currency) == str, 'Must be a string'
    
    helper1 = service_response(currency,'USD', 1) 
    helper2 = has_error(helper1) 
    return helper2 == False 


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    helper1 = service_response(src,dst,amt)
    result = get_dst(helper1)
    return float(before_space(result))