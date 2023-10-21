import csv
import paho.mqtt.publish as publish


msgs = []

with open('/home/rosario/py/policumbert/file.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        msgs.append({'topic': 'test', 'payload':', '.join(row)})
        

publish.multiple(msgs, hostname="localhost")
