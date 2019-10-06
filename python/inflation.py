"""
Name: Kennard Fung
File: inflation.py
Date: 10/05/2019
Description: Gets CPI data Federal Reserve Economic Data to
visualize how the value of money changes over time.
"""

import ast
import json

def inflation(money = 100):
	#If the input isn't an integer, return an error message.
	try:
		test = money + 1
	except TypeError:
		return("Invalid Value")

	#If all good, grab the CPI data
	inflation_data = list(open("CPI_data.json", "r"))
	inflation_data = ast.literal_eval(inflation_data[0])

	inflation_number_to_push = {}
	


	#return


print(inflation("fwwefew"))
