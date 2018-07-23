import os.path
import urllib
import datetime
import csv

def csv_read(csv_file):
	reader = csv.DictReader(csv_file)
	for record in reader:
		nameTuple = (record["Name"]),
		url = (record["URL"])
		name = "".join(nameTuple)
		print name
		print url
		rightNow = datetime.datetime.now().strftime("%y%m%d%H%M")
		today = datetime.datetime.now().strftime("%y%m%d")
		time = datetime.datetime.now().strftime("%H%M")
		directory = "/path/to/directory/" + name + "/" + today
		if not os.path.exists(directory):
			os.makedirs(directory)
		filename = "%s.jpg" % time
		savePath = "%s%s" % (directory, filename)
		urllib.urlretrieve("http://example.com/images/path/to/static/name.jpg", savePath)

with open("/path/to/file.csv", "rb") as csv_file:
	csv_read(csv_file)
