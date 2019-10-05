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
		BS_financials = balance_sheet_json.get("financials")

		#Then, collect the data for the big five criteria
		#CAGR Revenue
		#Try getting the CAGR for eight years, if not available, then five, if not, three
		IS_length = len(IS_financials)
		last_revenue = float(IS_financials[0].get("Revenue"))
		last_net_income = float(IS_financials[0].get("Net Income"))

		if IS_length >= 5:
			first_revenue = float(IS_financials[4].get("Revenue"))
			first_net_income = float(IS_financials[4].get("Net Income"))
			year_count = 4
		else:
			first_revenue = float(IS_financials[CF_length - 1].get("Revenue"))
			first_net_income = float(IS_financials[CF_length - 1].get("Net Income"))
			year_count = CF_length

		CAGR_Revenue = (((last_revenue/first_revenue) ** (1/year_count)))
		CAGR_Revenue_rounded = str(round(CAGR_Revenue, 2))

		if CAGR_Revenue >= 1:
			CAGR_Revenue_question = "True"
		else:
			CAGR_Revenue_question = "False"



		#CAGR CAPEX
		CF_length = len(CF_financials)
		last_capex = float(CF_financials[0].get("Capital Expenditure"))
		last_dividends = float(CF_financials[0].get("Dividend payments"))
		last_ops_CF = float(CF_financials[0].get("Operating Cash Flow"))

		if CF_length >= 5:
			first_capex = float(CF_financials[4].get("Capital Expenditure"))
			first_dividends = float(CF_financials[4].get("Dividend payments"))
			year_count = 4
		else:
			first_capex = float(CF_financials[CF_length - 1].get("Capital Expenditure"))
			first_dividends = float(CF_financials[CF_length - 1].get("Dividend payments"))
			year_count = CF_length

		#CAGR Dividends
		try:
			CAGR_Dividends = (((last_dividends/first_dividends) ** (1/year_count)))
			CAGR_Dividends_rounded = str(round(CAGR_Dividends, 2))

			if CAGR_Dividends >= 0:
				CAGR_Dividends_question = "True"
			else:
				CAGR_Dividends_question = "False"
		except:
			CAGR_Dividends_rounded = "None"
			CAGR_Dividends_question = "None"



		#CAGR CAPEX
		CAGR_Capex = (((last_capex/first_capex) ** (1/year_count)))
		CAGR_Capex_rounded = str(round(CAGR_Capex, 2))

		if CAGR_Capex >= 1:
			CAGR_Capex_question = "True"
		else:
			CAGR_Capex_question = "False"

		#Short-Term Debt Ratio
		#Grab short term debt and total assets for the latest year

		st_debt = float(BS_financials[0].get("Short-term debt"))
		total_assets = float(BS_financials[0].get("Total assets"))

		st_debt_ratio = (st_debt/total_assets)
		st_debt_ratio_rounded = str(round(st_debt_ratio, 2))

		if st_debt_ratio <= 1:
			st_debt_question = "True"
		else:
			st_debt_question = "False"

		#Current Ratio
		current_assets = float(BS_financials[0].get("Total current assets"))
		current_liabilities = float(BS_financials[0].get("Total current liabilities"))

		current_ratio = (current_assets/current_liabilities)
		current_ratio_rounded = str(round(current_ratio, 2))

		if current_ratio >= 1:
			current_ratio_question = "True"
		else:
			current_ratio_question = "False"

		#Capital Acquisition Ratio
		#divide cash flow from ops by CAPEX
		cap_acq = (last_ops_CF/abs(last_capex))
		cap_acq_rounded = str(round(cap_acq, 2))

		if cap_acq >= 1:
			cap_acq_question = "True"
		else:
			cap_acq_question = "False"

		#Quality of Income Ratio
		#divide operating cash flow by net income
		income_quality = (last_ops_CF/last_net_income)
		income_quality_rounded = str(round(income_quality, 2))

		if income_quality >= 1:
			income_quality_question = "True"
		else:
			income_quality_question = "False"

		#Create a JSON file with all the relevant data
		investment_json = {}

		investment_json["CAGR Revenue"] = CAGR_Revenue_rounded
		investment_json["CAGR Revenue Question"] = CAGR_Revenue_question

		investment_json["CAGR Dividends"] = CAGR_Dividends_rounded
		investment_json["CAGR Dividends Question"] = CAGR_Dividends_question

		investment_json["CAGR Capex"] = CAGR_Capex_rounded
		investment_json["CAGR Capex Question"] = CAGR_Capex_question

		investment_json["Short-Term Debt Ratio"] = st_debt_ratio_rounded
		investment_json["Short-Term Debt Question"] = st_debt_question

		investment_json["Current Ratio"] = current_ratio_rounded
		investment_json["Current Ratio Question"] = current_ratio_question

		investment_json["Capital Acquisition Ratio"] = cap_acq_rounded
		investment_json["Capital Acquisition Question"] = cap_acq_question

		investment_json["Income Quality Ratio"] = income_quality_rounded
		investment_json["Income Quality Question"] = income_quality_question

		return(investment_json)

if __name__ == '__main__':
	print(investment("EL"))
	print(investment("PG"))
	print(investment("PVH"))
	print(investment("GPS"))
