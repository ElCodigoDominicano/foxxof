"""
 Random password generator using pythons built-in secrets and string

 1) upon running script you are presented 5 options:
 [lower] => a-z
 [upper] => A-Z
 [digits] => 0-9
 [puncts] => !@#$^...
 [kitchen_sink] => io1_2TR@#$

 choose one of the 5.

 2) you will be asked to enter a length for the password: 8-65537

 3) the locksmith will create the key and display it for you

 Author: AERivas
 Date: 12/12/2022
"""
import string
import secrets
import logging

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s")


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
        response = input("Enter an option: ")
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
    loop = True
    while loop:
        try:
            password_length = int(input("Enter a length for the passphrase minimum 8 maximum 65537: "))
            # if negative value
            if password_length < 0:
                logger.error("Positive numbers only")
                continue
            # elif within range of 0 to 7
            elif 0 <= password_length < 8:
                logger.error("That value wasn't within range.")
                continue
            # elif within range of 8 to 65537
            elif 8 <= password_length < 65538:
                loop = False
            # elif over the maximum 65537
            elif password_length >= 65538:
                logger.error(f"The value was greater then the maximum allowed.")
                continue
        except ValueError:
            logger.error(f"That isn't a numerical value.")
            continue
    return password_length


def the_locksmith():
    random_example = ''.join(secrets.choice(string.ascii_letters+string.digits+string.punctuation)for i in range(8))
    welcome_message: str = f"""
        Options:
            [lower] => {string.ascii_lowercase}
            [upper] => {string.ascii_uppercase}
            [digits] => {string.digits}
            [punct] => {string.punctuation}
            [kitchen_sink] => {random_example} 
            > """

    logger.info(welcome_message)
    response = password_response_handler()
    length = password_length_handler()
    the_key: str = ''.join(secrets.choice(response) for i in range(length))
    logger.info(the_key)


if __name__ == '__main__':
    the_locksmith()

