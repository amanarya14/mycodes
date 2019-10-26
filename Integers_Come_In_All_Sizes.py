#Link https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?h_r=next-challenge&h_v=zen
#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = pow(a, b) + pow(c, d)
sys.stdout.write(str(e))