"""
A function to check if a string is in valid ISO 8601 format.

Author: AERivas
Date: 06-02-2022
"""

def iso_8601(time_string: str) -> bool:
    """
    Returns True if s is a string in ISO 8601 format, False otherwise

    ISO 8601 format the form 'hh:mm:ss' where h, m, and s are digits.  There must be
    exactly two digits each for minutes and seconds, so they are padded with 0s when
    necessary. The hours may either be 1 or 2 digits. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not accept time zones, abbreviated formats, or decimals

    Parameter time: The string to check
    Precondition: time is a string
    """
    try:
        pos1 = time_string.index(":")
        pos2 = time_string.index(":",pos1+1)
        hour = int(time_string[:pos1])
        mins = int(time_string[pos1+1:pos2])
        secs = int(time_string [pos2+1:])
        # Check times in range
        correct = 0 <= hour < 24 and 0 <= mins < 60 and 0 <= secs < 60
        # Check digits correct
        correct = correct and pos2 == pos1+3 and len(time_string) == pos2+3 and pos1 <= 2
        return correct
    except:
        return False

if __name__ == '__main__':
    print(iso_8601('00:00:00'))