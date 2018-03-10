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
                    help="Check a specific domain name")

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

    parser.add_option("-e",
                    # "--extensions",
                    action="store",
                    dest="extensions",
                    default='.com',
                    help="LTD extensions separated by comma")


    parser.add_option("-c",
                    # "--comb",
                    action="store",
                    dest="comb",
                    # default=2,
                    type="int",
                    help="Number of keywords in domain name combination")

    parser.add_option("-l",
                    # "--log",
                    action="store_true",
                    dest="log",
                    default=False,
                    help="Logging operation results")


    (options, args) = parser.parse_args()

    # Recognize Options
    if len(sys.argv) == 1:
        banner()
        parser.parse_args(['--help'])


    if options.extensions == "all":
        options.extensions = "com,net,org,info,cc,io,biz,app,co,xyx,club,design,shop,site,online,me,us,ca,ac,academy,accountant,actor,adult,ae,ai,am,apartment,art,at,bar,be,beer,bet,bid,blog,cam,cab,city,cl,cool,country,cx,cz,de,dating,zone,yt,wtf,ws,win,work,wiki,wf,watch,vote,vip,video,vg,vet,vc,vegas,uno,uk,tv,tube,toys,town,top,today,to,tl,tk,tf,tech,black,build,buzz,cafe,ch,chat,click,cm,"

    elif options.extensions == "basic":
        options.extensions = "com,net,org"

    elif not options.extensions:
        options.extensions = "com"

    if not options.comb:
        options.comb = 2


    # Call core.DeepCatch
    DeepCatcher(options = options)


if __name__ == '__main__':
    main()
