# I will be using panda_datereader as well as Morningstar for my API

import pandas_datareader.data as web
from datetime import datetime

start = datetime(2018, 2, 9)
end = datetime(2018 , 2, 20)

f = web.DataReader('F', 'morningstar', start, end)
print(f)