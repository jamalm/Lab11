# This script Counts the number of messages in a queue
#
# Author - Jamal Mahmoud Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

url = 'http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
key = res.read()
split = ':'
i = key.find(split)
word1 = key[:i]
word2 = key[i+len(split):]
res.close()

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = word1
secret_access_key = word2

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Gets a queue and prints a message along side it 
student_no = 'c13730921-'

q_name = student_no + sys.argv[1]

queue = conn.get_queue(q_name)

print "Number of messages in queue ", queue, ": ", str(queue.count())
