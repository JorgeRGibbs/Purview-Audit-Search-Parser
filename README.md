# Purview-Audit-Search-Parser
This Python script parses the export from a Microsoft Purview Audit Search.  It will parse the JSON data in the AuditData column and append it to the rest of  the csv to make it more readable. It may need some tweaking, depending  on your needs. 

All you need to do is run the python script and pass the export csv as a paremeter:
  $ python3 audit_parser.py audit_search_export.csv

Version: 0.1
