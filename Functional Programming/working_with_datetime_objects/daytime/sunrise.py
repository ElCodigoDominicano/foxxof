"""
Functions for parsing time values and determining daylight hours.

Author: AERivas
Date: 06-23-2022
"""
from dateutil.parser import parse
import pytz
import datetime
import itertools

def str_to_time(timestamp, tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and 
    tz if not None, this this function will assign that timezone to the datetime 
    object. 
    
    The value for tz can either be a string or a time OFFSET. If it is a string, 
    it will be the name of a timezone, and it should localize the timestamp. If 
    it is an offset, that offset should be assigned to the datetime object.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    if isinstance(tz, str):
            tz = pytz.timezone(tz)
            parsed = parse(timestamp)
            return tz.localize(parsed)
    try:
        parsed = parse(timestamp)
        timezone_info = parsed.tzinfo
        if timezone_info is None and tz is None:
            return parsed
        if timezone_info is not None and tz is not None:
            return parsed.replace(tzinfo=timezone_info) 
        if timezone_info is not None and tz is None:
            return parsed.replace(tzinfo=timezone_info)
        if timezone_info is None and tz is not None:
            return parsed.replace(tzinfo=tz)
        else:
            return parsed.replace(tzinfo=tz)
    except:
        return None 

def daytime(time,daycycle):
    """
    Returns True if the time takes place during the day.
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.
    
    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    tz = pytz.timezone(daycycle["timezone"])
    years = list(daycycle.keys())[5:]
    mnthday_list_of_dict = list(daycycle.values())[5:]
    list_of_mnthsdays = list(mnthday_list_of_dict[0].keys())
    for year, string in itertools.product(years, list_of_mnthsdays):
        seperator = string.find("-")
        year = int(year)
        months = int(string[:seperator])
        days = int(string[seperator+1:])
        rise_set_dict = mnthday_list_of_dict[0][string]
        sunrise_time = rise_set_dict["sunrise"]
        sunset_time = rise_set_dict["sunset"]      
        rise_str = str(year)+'-'+str(months)+'-'+str(days)+'-'+'T'+sunrise_time
        set_str = str(year)+'-'+str(months)+'-'+str(days)+'-'+'T'+sunset_time
        rise_obj = str_to_time(rise_str)
        set_obj = str_to_time(set_str)
        rise_zone = tz.localize(rise_obj)
        set_zone = tz.localize(set_obj)
        if time.year == year and time.month == months and time.day == days: 
            return True if rise_zone <= time <= set_zone else False
