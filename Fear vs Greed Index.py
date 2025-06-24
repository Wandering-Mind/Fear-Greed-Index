# Fear_vs_Greed Index
vix = yf.download(('VIX', period ='1y')['Adj Close']
fear_greed = np.where(vix > vix.rolling(50).mean(), "FEAR", "GREED")
