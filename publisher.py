import csv
import paho.mqtt.publish as publish
import sys


msgs = []

if(len(sys.argv)!=2):
    print('Wrong number of arguments!')
    exit(0)

path = sys.argv[1]

try:
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            msgs.append({'topic': 'test', 'payload':', '.join(row)})
except:
    print("File reading failed!")
    exit(0)
    
try:
    publish.multiple(msgs, hostname="localhost")
except:
    print("Publishing failed!")