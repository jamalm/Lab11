#separate the amazon key into 2 variables
import boto
import requests

def main():
	verify()
	version()
def verify():
	#curl command retrived key and put into a file previously called key(in same directory)
	f = open('key','r')
	key = f.read()
	#character to look for when splitting key
	split = ':'
	i = key.find(split)
	# splits key in half
	word1 = key[:i]
	word2 = key[i+len(split):]
	# Prints two new variables 
	print word1
	print word2
	##close key file
	f.close()
def version():
	# prints current version of boto
	print boto.Version

if __name__ == '__main__':
	main()
