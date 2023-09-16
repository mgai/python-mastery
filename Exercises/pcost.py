import sys
import os

DEFAULT_FILE = os.sep.join(["..", "Data", "portfolio.dat"])


def parse_file(input_file):
    with open(input_file, "r") as f:
        total_amount = 0
        total_stocks = 0
        for line in f.readlines():
            try:
                stock, amount, price = line.split(" ")
                total_stocks += 1
                total_amount += int(amount) * float(price)
            except ValueError:
                print(f"Error passing line [{line}]")
                print("skipped")
        return (total_stocks, total_amount)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {__file__} [Input_File]")
        print(f"Using default data file: {DEFAULT_FILE}")
        input_file = DEFAULT_FILE
    else:
        input_file = sys.argv[1]
        if not os.path.isfile(input_file):
            print(f"{input_file} is not detected as a file, please check.")
            exit(1)

    total_stocks, total_amount = parse_file(input_file)
    print(f"Total Amount: ${total_amount}, for {total_stocks} stocks.")
