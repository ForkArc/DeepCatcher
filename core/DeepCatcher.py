#!/usr/bin/env python

import re
import whois
import socket
import pprint
import requests
import itertools
import validators

from colorama import init, Fore, Back, Style
init()


class DeepCatcher(object):

	def __init__(self,options):

		# Basic Settings
		self.log_whois = "whois.log"
		self.log_reserved = "reserved.log"
		self.log_available = "available.log"

		# Set Options
		self.__log = options.log
		self.__file = options.file
		self.__comb = options.comb
		self.__whois = options.whois
		self.__domain = options.domain
		self.__keywords = options.keywords
		self.__extensions = options.extensions

		# Call Main
		self.main()

	@property
	def domain(self):
		if self.__domain:
			return self.split(self.__domain)


	@property
	def keywords(self):

		if self.__keywords:
			keywords = self.split(self.__keywords)

		if self.__file:
			fcontent =  open(self.__file).read()
			keywords = self.split(fcontent)

		try:

			return keywords

		except NameError:

			return False

	@property
	def extensions(self):
		return self.split(self.__extensions.strip('.') )


	@property
	def comb(self):
		return self.__comb


	@property
	def whois(self):
		if self.__whois:
			return self.split(self.__whois)


	@property
	def log(self):
		return self.__log


	def main(self):

		if self.domain:
			for domain in self.catchDomains(self.domain):
				self.checkDomain(domain)

		if self.keywords:
			keywords = self.catchKeywords(self.keywords)
			for domain in self.catchDomains(keywords):
				self.checkDomain(domain)

		if self.whois:
			for w in self.catchWhois(self.whois):
				self.checkWhois(w)

	def catchWhois(self,domain):

		if isinstance(domain, list):
			records = []

			for d in domain:
				record = self.catchWhois(d)
				records.append(record)

			return records


		record = domain

		return record


	def catchKeywords(self,keyword):

		combos = list(itertools.permutations(self.keywords, self.comb))

		names = []

		for comb in combos:
			name = "".join([keywords for keywords in comb])
			names.append(name)

		return names


	def catchDomains(self,name):

		if isinstance(name, list):
			domains = []

			for n in name:
				domain = self.catchDomains(n)
				domains.extend(domain)

			return domains


		if self.extensions:

			domains = []

			for ext in self.extensions:
				domain = self.checkName(name,ext)
				domains.append(domain)

			return domains

		else:

			domain = self.checkName(name)

			return domain


	def checkDomain(self,domain='hackerinit.com'):

		try:
			socket.gethostbyname(domain)
			print Fore.RED+"%s is Reserved" %domain
			self.write(domain, self.log_reserved)
			return False

		except:
			print Fore.GREEN+"%s is Available" %domain
			self.write(domain, self.log_available)
			return True


	def checkName(self,name,ext=None):
		if validators.domain(name):
			return name
		else:
			name = re.sub(r'\W+', '', name)
			return name+'.'+ext


	def checkWhois(self,domain):

		try:	
			record = whois.whois(domain)
			print Fore.RED
			print "Domain : %s" %domain
			print Fore.WHITE
			print record
			self.write(record, self.log_whois)
			return True

		except:
			print Fore.RED
			print "Can't get whois record for %s" %domain
			return False


	def split(self,option):
		return re.split(';|,| |\n', option)


	def write(self,content,file):
		if self.log:
			f = open(file,'a')
			f.write(content+'\r')
			f.close()

