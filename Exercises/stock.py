import csv


def read_portfolio(file):
    shares = []
    with open(file) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip the headers.
        for row in rows:
            shares.append(Stock(row[0], row[1], row[2]))
    return shares


# Python does not have overloading, so this functional will NOT be called.
def print_portfolio(portfolio):
    format = "%10s %10d %10.2f"
    header_format = "%10s %10s %10s"
    # Header
    print(header_format % ("name", "shares", "price"))
    print(header_format % (10 * "-", 10 * "-", 10 * "-"))
    # Body
    for p in portfolio:
        print(format % (p.name, p.shares, p.price))


def print_portfolio(portfolio, fields):
    # Header
    print(" ".join(["%10s" % (f) for f in fields]))
    print(" ".join(["-" * 10] * len(fields)))
    # Body
    for p in portfolio:
        print_fields = []
        for f in fields:
            if type(getattr(p, f)) == str:
                print_fields.append("%10s" % (getattr(p, f)))
            elif type(getattr(p, f)) == int:
                print_fields.append("%10d" % (getattr(p, f)))
            else:
                print_fields.append("%10.2f" % (getattr(p, f)))
        print(" ".join(print_fields))


class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = int(shares)
        self.price = float(price)

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        if self.shares > shares:
            self.shares -= shares
        else:
            raise ValueError("Not enough shares available to sell.")

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)


def test_row_creation():
    row = ["AA", "100", "32.20"]
    s = Stock.from_row(row)
    print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
