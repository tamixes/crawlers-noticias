from datetime import datetime


def string_to_date_processor(string):
    """Convert a string with the format Y-M-DTH:M:S to a datetime"""

    if type(string) == list:
        string = string[0]
    string = string.replace('T', ' ')
    date = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return date
