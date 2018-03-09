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
		self.log_file_reserved = "reserved.txt"
		self.log_file_available = "available.txt"

		# Set Options
		self.__ltds = options.ltds
		self.__file = options.file
		self.__comb = options.comb
		self.__whois = options.whois
		self.__domain = options.domain
		self.__popular = options.popular
		self.__keywords = options.keywords

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
	def ltds(self):
		return self.split(self.__ltds.strip('.') )


	@property
	def comb(self):
		return self.__comb


	@property
	def popular(self):
		return self.__popular


	@property
	def whois(self):
		if self.__whois:
			return self.split(self.__whois)


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


		if self.ltds:

			domains = []

			for ltd in self.ltds:
				domain = self.checkName(name,ltd)
				domains.append(domain)

			return domains

		else:

			domain = self.checkName(name)

			return domain


	def checkDomain(self,domain='hackerinit.com'):

		try:
			socket.gethostbyname(domain)
			print Fore.RED+"%s is Reserved" %domain
			self.log(domain, self.log_file_reserved)
			return False

		except:
			print Fore.GREEN+"%s is Available" %domain
			self.log(domain, self.log_file_available)
			return True


	def checkName(self,name,ltd=None):
		if validators.domain(name):
			return name
		else:

			name = re.sub(r'\W+', '', name)
			return name+'.'+ltd


	def checkWhois(self,domain):
		print Fore.RED
		print "Domain : %s \r" %domain
		
		print Fore.WHITE
		record = whois.whois(domain)
		print record


	def split(self,option):
		return re.split(';|,| |\n', option)


	def log(self,content,file):
		f = open(file,'a')
		f.write(content+'\r')
		f.close()

