"""
 Random password generator

 using pythons built-in secrets and string 
 Author: AERivas
 Date: 12/12/2022
"""
import string
import secrets

def the_maker(choice: str, length: int):
    assert isinstance(length, int), f"The length must be an integer [0-9] not {repr(length)}."
    assert isinstance(choice, str), f"The choice must be a string not {repr(choice)}."
    assert 8 <= length < 65556, f"The length must be any value from 8-65555" 

    kitchen_sink: str = '' 
    if choice == 'lower':
        kitchen_sink += string.ascii_lowercase
    elif choice == 'upper':
        kitchen_sink += string.ascii_uppercase
    elif choice == 'digits':
        kitchen_sink += string.digits
    elif choice == 'punct':
        kitchen_sink += string.punctuation
    elif choice == 'kitchen_sink':
        kitchen_sink += string.ascii_letters + string.digits + string.punctuation
    try: 
        the_key = ''.join(secrets.choice(kitchen_sink) for i in range (length))
    except:
        raise RuntimeError("Please use one of the approved options") from None
    return the_key


if __name__ == '__main__':
    message = (f"""
        Options:
            [lower] => {string.ascii_lowercase}
            [upper] => {string.ascii_uppercase}
            [digits] => {string.digits}
            [punct] => {string.punctuation}
            [kitchen_sink] => a mixture of all of the above 
            > """)

    time_to_choose = str(input(message))
    length = int(input("Enter the length of the password you want generated [ 8 - 65555 ]: "))
    der_wille_zur_macht = the_maker(time_to_choose, length)
    print(der_wille_zur_macht)
