import sys
import numpy as np
import pandas as pd

def main():
    d = [["$229.2", 2017, 123000, "$1100", "Cupertino, US"],
         ["$211.9", 2017, 320671, "$284", "Suwon, South Korea"],
         ["$177.8", 2017, 566000, "$985",  "Seattle, US"],
         ["$154.7", 2017, 1300000, "$66", "New Taipei City, Taiwan"],
         ["$110.8", 2017, 80110, "$834", "Mountain View, US"]]

    comps = ["apple", "samsung", "amazon", "foxconn", "alphabet"]
    cols = ["revenue", "fy", "employees", "mcap", "location"]

    c = pd.DataFrame(d, index=comps, columns=cols)

    print(c.dropnull())


if __name__ == "__main__":
    main()