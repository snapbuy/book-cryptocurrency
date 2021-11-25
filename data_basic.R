url.aapl = "https://www.quandl.com/api/v3/datasets/WIKI/AAPL/data.csv?api_key=xw3NU3xLUZ7vZgrz5QnG"
data.aapl = read.csv(url.aapl)

head(data.aapl)

library(quantmod)
getSymbols('AAPL')
chart_Series(Ad(AAPL))
data = getSymbols('AAPL',
                  from = '2000-01-01', to = '2018-12-31',
                  auto.assign = FALSE)
head(data)


ticker = c('FB', 'NVDA') 
getSymbols(ticker)


getSymbols('005930.KS',
           from = '2000-01-01', to = '2018-12-31')


tail(Ad(`005930.KS`))
tail(Cl(`005930.KS`))


getSymbols("068760.KQ",
           from = '2000-01-01', to = '2018-12-31')
tail(Cl(`068760.KQ`))


getSymbols('DGS10', src='FRED')
getSymbols('DEXKOUS', src='FRED')
