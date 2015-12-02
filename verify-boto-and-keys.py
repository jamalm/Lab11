#separate the amazon key into 2 variables
import boto
import requests
import urllib2

def main():
	verify()
	version()
def verify():
	#curl command retrived key
	key = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	response = key.read()		
	#character to look for when splitting key
	split = ':'
	i = response.find(split)
	# splits key in half
	word1 = response[:i]
	word2 = response[i+len(split):]
	# Prints two new variables 
	print word1
	print word2
def version():
	# prints current version of boto
	print boto.Version

if __name__ == '__main__':
	main()
