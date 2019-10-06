"""
Name: Kennard Fung
File: historical.py
Date: 10/05/2019
Description: The historical data function that grabs historical stock
data from FinancialModellingPrep. It returns a json, based on the timeframe
input in historical_data.
"""
import json
import requests

def historical_data(ticker, timeframe = '1Y'):
	history_url = "https://financialmodelingprep.com/api/v3/historical-price-full/" + str(ticker) + "?serietype=line"
	history_results = requests.get(history_url)
	history_json = history_results.json()
	historical = history_json.get("historical")
	latest_date = history_json.get("historical")[-1].get("date")
	#YYYY-MM-DD format
	#First, grab the latest year, month and day
	latest_year = int(latest_date[0:4])
	latest_month = int(latest_date[5:7])
	latest_day = int(latest_date[8:10])

	#For testing purposes
	timeframe = '6M'

	#Check if the request is a month or a year
	if timeframe[-1] == 'Y':
		old_year = latest_year - int(timeframe[0:-1])
	elif timeframe[-1] == 'M':
		old_year = latest_year
		old_month = latest_month - int(timeframe[0:-1])

	if old_month < 1:
		old_year = latest_year - 1
		old_month = 12 - (int(timeframe[0:-1]) - latest_month)

	#put a 0 in front of the month or the day if they are less than 10
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
	#print(str(old_year) + "-" + str(old_month) + "-" + str(latest_day))

	date_found = False
	specific_area = int()
	print(str(old_year))
	print(str(old_month_final))
	print(str(latest_day_final))
	print(str(old_year) + "-" + str(old_month_final) + "-" + str(latest_day_final))


	for x in range(len(historical)):
		if (str(old_year) + "-" + str(old_month_final) + "-" + str(latest_day_final)) == historical[x].get("date"):
			print(historical[x].get("close"))
			specific_area = x
			break

	print(specific_area)
	print(len(historical))
	for x in range(specific_area, len(historical)):
		historical_to_push.append(historical[x])

	historical_to_push = json.dumps(historical_to_push)
			# else:
			# 	#If the old date does not exist, add one to the latest day
			# 	#If the day > 31, add one to the old_month
			# 	#If the month > 12, add one to the old_year
			# 	#Go back up to the top
			# 	latest_day += 1
			# 	if latest_day > 31:
			# 		old_month = old_month + 1
			# 	if old_month > 12:
			# 		old_year = old_year + 1
			#
			# 	#put a 0 in front of the month or the day if they are less than 10
			# 	if old_month < 10:
			# 		old_month_final = str("0") + str(old_month)
			# 	else:
			# 		old_month_final = old_month
			#
			# 	if latest_day < 10:
			# 		latest_day_final = str("0") + str(latest_day)
			# 	else:
			# 		latest_day_final = latest_day

	return(historical_to_push)

print(historical_data("AAPL"))
