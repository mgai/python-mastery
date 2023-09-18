import ex2_1 as readrides

rows = readrides.read_file(readrides.DATA_FILE, readrides.read_into_dict)

# How many bus routes exist in Chicago?
routes = {r["route"] for r in rows}
print(f"There are {len(routes)} bus routes exist in Chicago.")

# How many people rode the number 22 bus on February 2, 2011?
rides = sum(
    [r["rides"] for r in rows if r["date"] == "02/02/2011" and r["route"] == "22"]
)
print(f"There were {rides} people who rode 22 bus on Feb 2nd, 2011")


# What about any route on any date of your choosing?
def count_rides(route, day):
    rides = sum([r["rides"] for r in rows if r["date"] == day and r["route"] == route])
    print(f"There were {rides} people who rode {route} bus on {day}")


count_rides("11", "01/01/2003")

# What is the total number of rides taken on each bus route?
from collections import Counter

totals = Counter()
for r in rows:
    totals[r["route"]] += r["rides"]
from pprint import pprint

pprint(totals)

# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

totals_2001 = Counter()
for r in rows:
    if r["date"].split("/")[2] == "2001":
        totals_2001[r["route"]] += r["rides"]

totals_2011 = Counter()
for r in rows:
    if r["date"].split("/")[2] == "2011":
        totals_2011[r["route"]] += r["rides"]

totals_diff = totals_2011 - totals_2001
print(
    "The top five bus routes had the greatest ten-year increase in ridership from 2001 to 2011."
)
pprint(totals_diff.most_common(5))
