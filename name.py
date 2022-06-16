import sys

#if len(sys.argv) < 2:
#    sys.exit("Too few argument")
#elif len(sys.argv) > 2:
#    sys.exit("Too many argument")
#
#print("hello, my name is", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too few argument")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)