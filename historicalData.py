import pandas
quandl.ApiConfig.api_key = 'VP3AoTe9zax2xk-o_Eq-'
auth_tok = "VP3AoTe9zax2xk-o_Eq-"

tickerName = "aapl"
startDate = input("What start date? Enter as YEAR-MONTH-DAY: ")
endDate = input("What end date? Enter as YEAR-MONTH-DAY: ")

getHistorical(tickerName.upper(), startDate, endDate)
 