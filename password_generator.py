"""
 a basic random password generator using pythons built-in secrets and string 

 1) upon running script you are presented 5 options:
 [lower] => a-z
 [upper] => A-Z
 [digits] => 0-9
 [puncts] => !@#$^...
 [kitchen_sink] => io1_2TR@#$

 choose one of the 5.

 2) you will be asked to enter a length for the password: 8-65556

 3) the locksmith will create the key and display it for you

 Author: AERivas
 Date: 12/12/2022
"""
import string
import secrets
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def password_response_handler():
    ACCEPTABLE_CHOICES: list[str] = [
        "lower",
        "upper",
        "digits",
        "punct",
        "kitchen_sink",
    ]
    kitchen_sink: str = ""

    while True:
        response = input("Enter an option:")
        if response in ACCEPTABLE_CHOICES:
            if response == 'lower':
                kitchen_sink += string.ascii_lowercase
            elif response == 'upper':
                kitchen_sink += string.ascii_uppercase
            elif response == 'digits':
                kitchen_sink += string.digits
            elif response == 'punct':
                kitchen_sink += string.punctuation
            elif response == 'kitchen_sink':
                kitchen_sink += string.ascii_letters + string.digits + string.punctuation
            break

        if not response in ACCEPTABLE_CHOICES:
            logger.error("That wasn't an acceptable option, please try again.")
            continue
    return kitchen_sink


def password_length_handler():
    password_length: int = 0
    while True:
        try:
            password_length = int(input("Enter a length for the passphrase minimum 8 maximum 65556: "))
            if password_length < 8:
                logger.error("That value wasn't within range.")
                continue
        except ValueError:
            logger.error(f"That isn't a numerical value.")
            continue
        else:
            break
    return password_length


def the_locksmith():
    welcome_message: str = f"""
        Options:
            [lower] => {string.ascii_lowercase}
            [upper] => {string.ascii_uppercase}
            [digits] => {string.digits}
            [punct] => {string.punctuation}
            [kitchen_sink] => a mixture of all of the above 
            > """

    print(welcome_message)
    response = password_response_handler()
    length = password_length_handler()
    the_key: str = ''.join(secrets.choice(response) for i in range(length))
    print(the_key)


if __name__ == '__main__':
    the_locksmith()
