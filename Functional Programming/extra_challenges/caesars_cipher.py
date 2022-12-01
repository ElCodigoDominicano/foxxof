"""
A module to encode with Caesar-style substitution ciphers.

Early (pre-20th century) encrypted messages letter substitution techniques.  To encrypt
a message like this:
    
    Attack at dawn!

you first removed all punctuation, spaces, and capitalization, like this:
    
    attackatdawn
    
The idea is that the reader can add all that information just inferring it from the text.

Now that the message only has letters, you then substitute each letter for another.  In 
Caesar's original cipher, each letter was shifted 3 positions, wrapping around at the end.  
So 'a' became 'd', 'b' become 'e',...,'w' became 'z', 'x' became 'a', 'y' became 'b' and 
'z' became 'c'. So this message becomes 
    
    dwwdfndwgdzq

To decrypt the message, you simply shift back in the reverse direction.  Or, you can just 
shift 26-3 = 23 spots and you will wrap back around to the original message.  Because of
this, rot-13 (shifting by 13 positions instead of 3) is another popular technique. 
Encoding a message with rot-13 twice gives you the original message.

This way of encoding messages is no longer used for secure communication, because it
is so easy to break.  But rot-13 can still be found on some Internet message boards
where people use it to hide movie spoilers and for other light-hearted topics.

Author: AERivas
Date: 06-04-2021
Updated: 06-05-2022
latest: 11-30-2022
"""
def encode(text: str, n: int) -> str:
    """
    Returns the text encoded by shifting each letter by n positions.
    
    Letters at the end of the alphabet wrap back around.  So if n is 3, 'x' becomes 'a'.
    
    Examples:
        encode('attackatdawn',3) returns 'dwwdfndwgdzq'
        encode('dwwdfndwgdzq',23) returns 'attackatdawn'
        encode('attackatdawn',13) returns 'nggnpxngqnja'
        encode('',13) returns ''
    
    Parameter text: the text to encode
    Precondition: text is a string
    
    Parameter n: the number of positions to shift
    Precondition: n is an int between 0 and 25 (inclusive)
    """
    assert isinstance(text, str), f'Parameter text must be a string not ->{repr(text)}.'
    assert isinstance(n, int), f'Parameter n: must be an integer not -> {repr(n)}.'
    assert 0 <= n < 26, 'This exceeds the maximum number allowed.'

    result: str = ''
    alpha: str = 'abcdefghijklmnopqrstuvwxyz'
    for i in text.replace(" ",""):
        if i.isalpha():
            i = i.lower()
            result += alpha[alpha.index(i)]
        else:
            result = "Nope."
    return result


def decode(text: str, n: int):
    """ Reversing the steps for the encode function """
    assert isinstance(text, str), f'Parameter text must be a string not ->{repr(text)}.'
    assert isinstance(n, int), f'Parameter n: must be an integer not -> {repr(n)}.'
    assert 0 <= n < 26, 'This exceeds the maximum number allowed.'
    
    result: str = ""
    alpha: str = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        result += alpha[alpha.index(i) - n ]
    return result

if __name__ == '__main__':
    first_message =  encode("land of the free",3)
    second_message = encode("home of the brave",13)
    third_message = encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",23)
    
    print(first_message)
    print(decode(first_message,3))
    
    print(second_message)
    print(decode(second_message,3))

    print(third_message)
    print(decode(third_message,3))
