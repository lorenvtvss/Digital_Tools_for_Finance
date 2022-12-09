# downstream.py
import pandas as pd


def get_macro_data(path, macro_factor, start_dt="2007-01-01", end_dt="2021-01-01"):
  """Get all macro factors data from the DB."""
  
  filename = path+"/macro_data.xlsx"

  macro_data = pd.read_excel(filename, sheet_name=macro_factor).set_index('Date ')
  macro_data = macro_data.loc[start_dt:end_dt,:]

  return macro_data




def get_SP500_mcap_data(path):
  """Get S&P500 mcap data from the DB."""

  filename = path+"/S&P500_mcap_data.xlsx"

  data_mcap = pd.read_excel(filename, sheet_name='Market_Cap') 
  data_mcap = data_mcap.transpose()

  return data_mcap  



  