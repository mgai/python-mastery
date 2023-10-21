import os
import tracemalloc

DATA_FILE = os.path.sep.join(["..", "Data", "ctabus.csv"])


# A tuple
# row_tup = (route, date, daytype, rides)
def read_into_tuple(route, date, daytype, rides):
    return (route, date, daytype, rides)


# A dictionary
# row_dict = {"route": route, "date": date, "daytype": daytype, "rides": rides}
def read_into_dict(route, date, daytype, rides):
    return {"route": route, "date": date, "daytype": daytype, "rides": rides}


# A class
class RowClass:
    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_into_class(route, date, daytype, rides):
    return RowClass(route, date, daytype, rides)


# A named tuple
from collections import namedtuple

RowNamedTuple = namedtuple("Row", ["route", "date", "daytype", "rides"])

# A named tuple with Typing
import typing


class RowClassTyping(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


def read_into_named_tuple(route, date, daytype, rides):
    return RowNamedTuple(route=route, date=date, daytype=daytype, rides=rides)


# A class with slots
class RowClassSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides) -> None:
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_into_class_with_slots(route, date, daytype, rides):
    return RowClassSlots(route, date, daytype, rides)


def read_file(file, method):
    with open(DATA_FILE, "r") as f:
        next(f)
        tracemalloc.start()
        my_array = []
        for line in f.readlines():
            row = line.strip().split(",")
            my_array.append(method(row[0], row[1], row[2], int(row[3])))
        current, peak = tracemalloc.get_traced_memory()
        print(
            f"{len(my_array)} records read. Current memory: {current:.2f}, Peak: {peak:.2f}."
        )
    return my_array


# Per test, the memory footprint is as below for peak
# Class > Named Tuple > Tuple > Class with Slots


# Ex 2.5
def read_rides_as_columns(filename):
    """
    Read the bus ride data into 4 lists, representing columns.
    """
    import csv

    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(row[3])
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
