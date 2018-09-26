import requests
#import json
import flask # web app libary


lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

def company_search(string):
	r = requests.get(lookup_url+string)
	print(r)
	print(type(r))
	try:
		company_details = r.json()
		print(type(company_details))
		return company_details
	except ValueError:
		return 0

def get_quote(string):
		r = requests.get(quote_url+string)
		try:
		#r.json().get("LastPrice"):
		# to access json object by key use .get
			quote = (r.json())
			print(quote)
			print("**********")
			return quote["LastPrice"]
		except ValueError:
			return 0
#print(company_search("AAPL"))
print(get_quote("AMZN"))