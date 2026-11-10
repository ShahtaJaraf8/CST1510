# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, percent):
        self.label = "R-001"
        self.value = percent
        self.limit = 100
    def status(self):  # this parameter should be self
        return self.value

r = Record(95)
print(r.status())
