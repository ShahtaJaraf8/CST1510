"""
RECORD CHECK  -  my version
===========================

Name  :  Shahta Jaraf
Lane  :  AI
Date  :  01/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

from numpy import record
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
    def percent(self):
            return (self.value/ self.limit)*100
    def status(self):
            current_percent = self.percent()
            if current_percent >= 100:
                return f"Over Limit"
            elif current_percent >= 90:
                return f"Warning"
            else:
                return f"OK"
    def is_over(self):
        return self.value > self.limit
records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 45.0, 100.0)
]
for r in records:
    over_count = 0
    if r.is_over():
        over_count += 1


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print(f"  RECORD VALUE  :  {record.value}")
    print(f"  RECORD LIMIT  :  {record.limit}")
    print(f"  RECORD STATUS :  {record.status()}")
    print(f"{over_count} of {len(records)} records are OVER LIMIT")
    print("=" * 34)

    # your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
