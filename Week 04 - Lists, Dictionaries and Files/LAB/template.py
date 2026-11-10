"""
RECORD CHECK  -  my version
===========================

Name  :  Shahta Jaraf
Lane  :  AI 
Date  :  28/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

from matplotlib.pylab import record


def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"



label = input("Enter label")     
value = float(input("Enter value"))     
limit = float(input("Enter limit"))   

def check(value, limit):
    """Calculate the difference and percentage of value against limit."""
    difference = limit - value
    percent = (value / limit) * 100 if limit != 0 else 0
    return difference, percent


difference, percent = check(value, limit)
status = status_of(percent)         


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
# your report lines go here
print(f"  Used: {value:6.2f}")
print(f"  Total: {limit:6.2f}")
print(f"  Free: {difference:6.2f}")
print(f"  Percent: {percent:6.2f}%")
print(f"  Status: {status}")
print("=" * 34)

def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(',')
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }
            records.append(record)
    return records

records = load_records(r"C:\Users\HP\Documents\CST1510\Week 04 - Lists, Dictionaries and Files\LAB\records_sample.txt")  # replace with your code


for item in records:
    difference, percent = check(item["value"], item["limit"])
    status = status_of(percent)
    print(item["label"], item["value"], item["limit"], difference, percent, status)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
