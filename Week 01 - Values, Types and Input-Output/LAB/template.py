"""
RECORD CHECK  -  my version
===========================

Name  : Shahta Jaraf
Lane  :  AI      
Date  : 2026-09-25

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label = input("Enter Name/Hostname/IP: ")    
first = float(input("Enter the first number: "))    
second = float(input("Enter the second number: "))   


difference = second - first
percent = (first / second) * 100


print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  first:  {first:>10.2f}")
print(f"  second: {second:>10.2f}")
print(f"  difference: {difference:>+10.2f}")
print(f"  percent: {percent:>10.2f}")

print("=" * 34)

