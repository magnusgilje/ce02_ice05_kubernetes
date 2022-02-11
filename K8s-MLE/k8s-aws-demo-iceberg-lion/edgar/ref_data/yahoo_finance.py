#pylint: disable=c0305,c0301,c0116,c0103,c0303,w0511,r0914,w0613,w0612,r1705,w0703,c0114,c0325,c0410,c0413,e0401,c0411,w0611,e0102,r1721,c0121,w0621,w0622,w0107,w0702,e0012
'''
Author : Albert Tran
Created: 2020-08-08

Module to download data from yahoo finance and calculate short-term returns.

Example usage:
df_returns = get_yahoo_data('2000-01-01', '2020-08-01', tickers, 'daily')
df_returns.to_csv(r'D:\\stock_returns_daily.csv', index=False)

'''
# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import pandas as pd
from yahoofinancials import YahooFinancials


# %%
# ------------------------------------------------------------------------------
# Yahoo Finance Data
# ------------------------------------------------------------------------------
def get_yahoo_data(start_date, end_date, tickers, period='daily'):
    '''
    Returns prices and returns for a list of given tickers.
    '''
    yf      = YahooFinancials(tickers)
    yf_data = yf.get_historical_price_data(start_date, end_date, period)

    list_df = []
    for ticker in yf_data.keys():
        try:
            # Get the data for the relevant ticker
            df_tmp = pd.DataFrame(yf_data[ticker]['prices'])[['formatted_date', 'high', 'low', 'adjclose', 'volume']]
            df_tmp.rename(columns={'formatted_date':'date', 'adjclose':'price'}, inplace=True)
            for i in [1,2,3,5,10]:
                df_tmp[f'{i}{period}_return'] = df_tmp['price'].pct_change(i).shift(-i)
            df_tmp['Symbol'] = ticker

            list_df.append(df_tmp)
        except:
            print(f'Data extraction failed for ticker: {ticker}.')

    df = pd.concat(list_df)
    return df

