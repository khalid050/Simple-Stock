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

def investment(ticker):


	#Open up the list of stocks
	stock_list = list(open("stock_symbol_file", 'r'))
	actual_stock_list = stock_list[0]
	# print(type(main_stock_list))


	#Check if the stock ticker exists in the overall list, if not return an error.
	if ticker not in actual_stock_list:
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
		CF_financials = cash_flow_json.get("financials")

		#Then, collect the data for the big five criteria
		#CAGR Revenue
		#Try getting the CAGR for eight years, if not available, then five, if not, three
		IS_length = len(IS_financials)
		last_revenue = float(IS_financials[0].get("Revenue"))

		if IS_length >= 5:
			first_revenue = float(IS_financials[4].get("Revenue"))
			year_count = 4
		else:
			first_revenue = float(IS_financials[CF_length - 1].get("Revenue"))
			year_count = CF_length

		CAGR_Revenue = (((last_revenue/first_revenue) ** (1/year_count)) - 1) * 100
		CAGR_Revenue_rounded = str(round(CAGR_Revenue, 2)) + "%"

		#CAGR CAPEX
		CF_length = len(CF_financials)
		last_capex = float(CF_financials[0].get("Capital Expenditure"))
		last_dividends = float(CF_financials[0].get("Dividend payments"))

		if CF_length >= 5:
			first_capex = float(CF_financials[4].get("Capital Expenditure"))
			first_dividends = float(CF_financials[4].get("Dividend payments"))
			year_count = 4
		else:
			first_capex = float(CF_financials[CF_length - 1].get("Capital Expenditure"))
			first_dividends = float(CF_financials[CF_length - 1].get("Dividend payments"))
			year_count = CF_length


		#CAGR Dividends
		CAGR_Dividends = (((last_dividends/first_dividends) ** (1/year_count)) - 1) * 100
		CAGR_Dividends_rounded = str(round(CAGR_Dividends, 2)) + "%"
		#CAGR CAPEX
		CAGR_Capex = (((last_capex/first_capex) ** (1/year_count)) - 1) * 100
		CAGR_Capex_rounded = str(round(CAGR_Capex, 2)) + "%"

		return(CAGR_Dividends_rounded, CAGR_Capex_rounded)

		#Short-Term Debt Ratio
        #Grab short term debt and total assets for the latest year


		#Current Ratio

		#Capital Acquisition Ratio

		#Quality of Income Ratio

		#Create a JSON file with all the relevant data



if __name__ == '__main__':
	print(investment("AAPL"))
