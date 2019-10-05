"""
Name: Kennard Fung

Module: EconStat

Description: Gives relevant economic data based on what gets pushed to it.

import requests
import json
from urllib3.exceptions import ProtocolError"""

import json
import ast
import requests


def main():
	pass

def inflation():
	#Use the CPI data
	pass

def interest():
	pass

def loans():
	pass

def historical_data(ticker, timeframe = '1Y'):
	history_url = "https://financialmodelingprep.com/api/v3/historical-price-full/" + str(ticker) + "?serietype=line"
	history_results = requests.get(history_url)
	history_json = history_results.json()
	historical = history_json.get("historical")
	latest_date = history_json.get("historical")[-1].get("date")
	#YYYY-MM-DD format
	latest_year = int(latest_date[0:4])
	latest_month = int(latest_date[5:7])
	latest_day = int(latest_date[8:10])

	timeframe = '4M'

	if timeframe[-1] == 'Y':
		old_year = latest_year - int(timeframe[0:-1])
	elif timeframe[-1] == 'M':
		old_year = latest_year
		old_month = latest_month - int(timeframe[0:-1])
	if old_month < 1:
		old_year = latest_year - 1
		old_month = 12 - (int(timeframe[0:-1]) - latest_month)

	if old_month < 10:
		old_month_final = str("0") + str(old_month)
	else:
		old_month_final = old_month

	if latest_day < 10:
		latest_day_final = str("0") + str(latest_day)
	else:
		latest_day_final = latest_day

	#If you tracked back into a public holiday/weekend, just use data from the next dictionary
	historical_to_push = []
	print(str(old_year) + "-" + str(old_month) + "-" + str(latest_day))

	date_found = False

	while date_found is False:
		for x in range(len(historical)):
			if (str(old_year) + "-" + str(old_month) + "-" + str(latest_day)) == historical[x].get("date"):
			# if (int(historical[x].get("date")[0:4]) == old_year) and (int(historical[x].get("date")[5:7]) == old_month) and (int(historical[x].get("date")[8:10]) == latest_day):
				print(historical[x].get("close"))
				date_found = True
			else:
				latest_day += 1

	return(latest_day, old_month, old_year)

print(historical_data("AAPL"))
