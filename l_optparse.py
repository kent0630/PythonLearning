#!/usr/bin/python
# encoding=utf-8
from optparse import OptionParser
def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename", type="string",
            action="store", help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    ar = ["-f", "foo.txt", "-v", "ftt"]
    (options, args) = parser.parse_args(ar)
    print "filename %s" % options.filename
    print "lenthofargs %d" % len(args)
    print "tst %s" % args[0]
    if len(args) != 1:
         parser.error("incorrect number of arguments")
    if options.verbose:
        print "reading %s..." % options.filename

if __name__ == "__main__":
    main()
