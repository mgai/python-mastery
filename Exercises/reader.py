import os, csv

# Treating functions as the 1st class data
coltypes = [str, int, float]
FILE = os.path.sep.join(["..", "Data", "portfolio.csv"])


def main():
    cta_rows = read_csv_as_dicts(
        os.path.sep.join(["..", "Data", "ctabus.csv"]), [str, str, str, int]
    )
    routes = {row["route"] for row in cta_rows}
    print(f"There are {len(routes)} unique routes.")
    route_ids = {id(row["route"]) for row in cta_rows}
    print(f"There are {len(route_ids)} unique route_ids.")

    # Use the intern type for internal representation of the constant strings
    # So that we can better cache the common strings for memory optimization.
    from sys import intern
    import tracemalloc

    tracemalloc.start()
    cta_rows_optimized = read_csv_as_dicts(
        os.path.sep.join(["..", "Data", "ctabus.csv"]), [intern, str, str, int]
    )
    route_ids = {id(row["route"]) for row in cta_rows_optimized}
    print(f"There are {len(route_ids)} unique route_ids with intern.")
    print(tracemalloc.get_traced_memory())
    cta_rows_optimized2 = read_csv_as_dicts(
        os.path.sep.join(["..", "Data", "ctabus.csv"]), [intern, intern, str, int]
    )
    route_ids = {id(row["route"]) for row in cta_rows_optimized2}
    print(f"There are {len(route_ids)} unique route_ids with intern.")
    print(tracemalloc.get_traced_memory())
    cta_rows_optimized3 = read_csv_as_dicts(
        os.path.sep.join(["..", "Data", "ctabus.csv"]), [intern, intern, intern, int]
    )
    route_ids = {id(row["route"]) for row in cta_rows_optimized3}
    print(f"There are {len(route_ids)} unique route_ids with intern.")
    print(tracemalloc.get_traced_memory())

    """It is recommended to have intern when duplicated constants are there."""


def read_csv_as_dicts(file_name, coltypes):
    f = open(file_name)
    rows = csv.reader(f)
    headers = next(rows)
    return [
        ({name: func(val) for name, func, val in zip(headers, coltypes, row)})
        for row in rows
    ]


if __name__ == "__main__":
    main()
