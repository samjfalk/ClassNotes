import sys

for line in sys.stdin:
    line = line.strip()
    elements = line.split(",")
    try:
        print '%s\t%s' % (elements[0],int(elements[2])+int(elements[3]))
    except:
        print 'State, Sum of Math and Reading'