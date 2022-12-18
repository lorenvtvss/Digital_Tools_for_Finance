### TODO before running this code:
# - run in console:
#   "conda install fredapi" or "pip install fredapi"
# - save environmental variable FRED_API_KEY with your own FRED api key


from fredapi import Fred
import pandas as pd


# activate fred api key
fred = Fred(api_key=FRED_API_KEY)


# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('macro_factors_api.xlsx', engine='xlsxwriter')


# Write each dataframe to a different worksheet
# get U.S. real gdp
gdp = fred.get_series('GDPC1', observation_start='2007-01-01', observation_end='2021-01-01')
gdp.to_excel(writer, sheet_name='Real_GDP')

# get U.S. unemployment rate
unrate = fred.get_series('UNRATE', observation_start='2007-01-01', observation_end='2021-01-01')
unrate.to_excel(writer, sheet_name='Unemployment_rate')

# get crude oil price
crude = fred.get_series('POILWTIUSDM', observation_start='2007-01-01', observation_end='2021-01-01')
crude.to_excel(writer, sheet_name='Crude_price')

# get U.S. federal debt
feddebt = fred.get_series('GFDEBTN', observation_start='2007-01-01', observation_end='2021-01-01')
feddebt.to_excel(writer, sheet_name='Federal_debt')

# get U.S. federal rate
fedrate = fred.get_series('FEDFUNDS', observation_start='2007-01-01', observation_end='2021-01-01')
fedrate.to_excel(writer, sheet_name='Federal_rate')


# Close the Pandas Excel writer and output the Excel file.
writer.close()