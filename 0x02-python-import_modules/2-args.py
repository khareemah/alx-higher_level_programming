#!/usr/bin/python3
import sys
no_of_args = len(sys.argv) - 1
if no_of_args == 1:
    print("{} argument".format(no_of_args))
else:
    print("{} arguments".format(no_of_args))

for i in  range(1, no_of_args + 1):
  print("{:d}: {}".format(i, sys.argv[i]))
