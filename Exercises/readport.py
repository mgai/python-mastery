import csv


# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio


if __name__ == "__main__":
    import os

    FILE = os.path.sep.join(["..", "Data", "portfolio.csv"])
    from pprint import pprint

    portfolio = read_portfolio(FILE)
    pprint(portfolio)

    pprint([s for s in portfolio if s["shares"] > 100])
    print(sum([s["shares"] * s["price"] for s in portfolio]))

    pprint({s["name"] for s in portfolio})

    # Count the total shares of each stock.
    totals = {s["name"]: 0 for s in portfolio}
    for s in portfolio:
        totals[s["name"]] += s["shares"]
    pprint(totals)

    # Collections
    # Counter
    from collections import Counter

    totals_counter = Counter()
    for s in portfolio:
        totals_counter[s["name"]] += s["shares"]
    pprint(totals_counter.most_common(2))
