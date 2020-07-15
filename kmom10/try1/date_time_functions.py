#!/usr/bin/env python3
"""
Date time
"""
import datetime

def datetest(textfile):
    """
    date
    """
    with open(textfile, "r") as filehandle:
        lines = filehandle.read()
        words = lines.split()
        date_format = "%Y-%m-%d"
        dates = []
        for word in words:
            word = word.rstrip(".,'")
            if len(word) == 10:
                try:
                    date_obj = datetime.datetime.strptime(word, date_format)
                    date_obj = date_obj.date().strftime("%Y-%m-%d")
                    dates.append(str(date_obj))
                except ValueError:
                    continue
    return ", ".join(dates)

def timetest(textfile):
    """
    time
    """
    with open(textfile, "r") as filehandle:
        lines = filehandle.read()
        words = lines.split()
        date_format = "%H:%M"
        times = []
        for word in words:
            word = word.rstrip(".,'")
            try:
                if len(word) == 5:
                    date_obj = datetime.datetime.strptime(word, date_format)
                    date_obj = date_obj.time().strftime("%H:%M")
                    times.append(str(date_obj))
            except ValueError:
                continue
    return ", ".join(times)
