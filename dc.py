#!/usr/bin/env python

import sys
from core.DeepCatcher import *
from optparse import OptionParser

from colorama import init, Fore, Back, Style
init()


def banner():        
        print Fore.RED
        print "\r[+] DeepCatcher\r"
        print "[-] Find your Domains Fast & Easy.\r"
        print "[-] Author: Deyaa Muhammad\r"
        print "[-] Email: contact@deyaa.me\r"
        print "[-] Website: deyaa.me\r"
        print Fore.WHITE


def main():

    # Set Options with Default values.

    parser = OptionParser(usage="usage: %prog [options]",
                          version="DeepCatcher v0.1")

    parser.add_option("-d",
                    # "--domain",
                    action="store",
                    dest="domain",
                    help="Check a single domain name")

    parser.add_option("-w",
                    # "--whois",
                    action="store",
                    dest="whois",
                    help="Find the domain owner information")

    parser.add_option("-k",
                    # "--words",
                    action="store",
                    dest="keywords",
                    help="Keywords in domain name separated by comma")

    parser.add_option("-f",
                    # "--file",
                    action="store",
                    dest="file",
                    # default="keywords.txt",
                    help="Load keywords from a file separated by comma, line or space")

    parser.add_option("-l",
                    # "--ltds",
                    action="store",
                    dest="ltds",
                    default='.com',
                    help="LTD extensions separated by comma")


    parser.add_option("-c",
                    # "--comb",
                    action="store",
                    dest="comb",
                    default=2,
                    type="int",
                    help="Number of keywords in domain name combination")

    parser.add_option("-p",
                    # "--popular",
                    action="store_true",
                    dest="popular",
                    default=False,
                    help="Use popular keywords with given words")


    (options, args) = parser.parse_args()

    # Recognize Options
    if len(sys.argv) == 1:
        banner()
        parser.parse_args(['--help'])


    if options.ltds == "all":
        options.ltds = "com,net,org,info,cc,io,biz,app"

    elif not options.ltds:
        options.ltds = "com"

    if options.keywords and options.popular:
        options.keywords = options.keywords+"group,network,online,get,hub,support,blog,business"

    if not options.comb:
        options.comb = 1


    # Call core.DeepCatch
    DeepCatcher(options = options)


if __name__ == '__main__':
    main()
