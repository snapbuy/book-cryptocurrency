import pybithumb

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)
balance = bithumb.get_balance("BTC")
print(balance)
