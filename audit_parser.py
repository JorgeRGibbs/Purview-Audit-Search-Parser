'''
Name: Purview audit search parser.
Description: This script parses the export from a Microsoft Purview Audit Search. 
It will parse the JSON data in the AuditData column and append it to the rest of 
the csv to make it more readable. This script may need some tweaking, depending 
on your needs.
#Version: 0.1
#Author: Jorge R Gibbs
'''

import csv
import json
import sys


lines = []
json_data = []
fields = []
clean_fields = []

def parse_data():
#Open purview export file and load the lines of the file into a list.
	file = sys.argv[1]
	print("Reading file:",file)
	with open(file, 'r' ) as theFile:
		reader = csv.DictReader(theFile)
		for line in reader:
			lines.append(line)

#Parse the Audit Data in JSON. 	
	for i in lines:
		json_dict = json.loads(i['AuditData'])

		#Remove empty fields and the original AuditData column.
		del i['AuditData']
		del i['AssociatedAdminUnitsNames']
		del i['AssociatedAdminUnits']
		
		#Append all the JSON data to the other columns.
		i.update(json_dict)
		
		# Extract data from the nested AppAccessContext object and append it to the
		# rest of the JSON data.
		if 'AppAccessContext' in json_dict:
			access_context = json_dict['AppAccessContext']
			del json_dict['AppAccessContext']
			i.update(access_context)

	#Get the fields from all the extracted data and put them in a list
	for i in lines:
		fields.append(i.keys())
	for i in fields:
		for j in i:
			#Insert fields that are not in the list.
			if j not in clean_fields:
				clean_fields.append(j)

	#Write the headers and data to a csv.
	output = 'parsed_'+file
	with open(output, 'w', newline='') as f:
		writer = csv.DictWriter(f, fieldnames=clean_fields)
		writer.writeheader()
		for i in lines:
			writer.writerow(i)
		print('Output written to: '+output)


if __name__ == '__main__':
	parse_data()