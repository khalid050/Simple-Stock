"""
Name: Kennard Fung

Module: EconStat

Description: Gives relevant economic data based on what gets pushed to it.

import requests
import json
from urllib3.exceptions import ProtocolError"""

import json
import ast


def main():
	pass

def inflation():
	#Use the CPI data
	pass

def interest():
	pass

def loans():
	pass

def investment(stock_ticker):
	stock = str(stock_ticker)

	#Open up the list of stocks
	main_stock_list = list(open("stock_symbol_file", 'r'))
	print(main_stock_list)
	print(type(main_stock_list))

	
	#Check if the stock ticker exists in the overall list, if not return an error.
	if stock not in main_stock_list:
		return("Stock does not exist in this server!")

	else:

		#First, collect the data for the three main financial statements
		balance_sheet_base = "https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/"
		balance_sheet_url = balance_sheet_base + str(ticker)
		balance_sheet_results = requests.get(balance_sheet_url)
		balance_sheet_json = balance_sheet_results.json()

		cash_flow_base = "https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/"
		cash_flow_url = cash_flow_base + str(ticker)
		cash_flow_results = requests.get(cash_flow_url)
		cash_flow_json = cash_flow_results.json()

		income_statement_base = "https://financialmodelingprep.com/api/v3/financials/income-statement/"
		income_statement_url = income_statement_base + str(ticker)
		income_statement_results = requests.get(income_statement_url)
		income_statement_json = income_statement_results.json()

		IS_financials = income_statement_json.get("financials")
		CF_financial = cash_flow_json.get("financials")
		
		#Then, collect the data for the big five criteria
		#CAGR Revenue
		#Try getting the CAGR for eight years, if not available, then five, if not, three, if not the company can screw itself
		IS_length = len(IS_financials)
		last_revenue = float(IS_financials[0].get("Revenue")) 
		if IS_length >= 8:			
			first_revenue = float(IS_financials[7].get("Revenue"))
			year_count = 7
		elif IS_length >= 5:
			first_revenue = float(IS_financials[4].get("Revenue"))
			year_count = 4
		elif IS_length >= 3:
			first_revenue = float(IS_financials[2].get("Revenue"))
			year_count = 2

		#Do the CAGR calculation

		CAGR_Revenue = (((last_revenue - first_revenue) ^ (1/year_count)) - 1) * 100
		CAGR_Revenue_rounded = round(CAGR_Revenue, 2)

		return(CAGR_Revenue_rounded)



		#CAGR CAPEX



		#CAGR Dividends

		#Short-Term Debt Ratio

		#Current Ratio

		#Capital Acquisition Ratio

		#Quality of Income Ratio


	

if __name__ == '__main__':
	investment("AAPL")

