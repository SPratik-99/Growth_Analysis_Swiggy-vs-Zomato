from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=330)
keywords = ["Zomato", "Swiggy" ]

pytrends.build_payload(
    kw_list=keywords,
    cat=0,
    timeframe="today 5-y",
    geo="IN",
    gprop=""
)

trends_df = pytrends.interest_over_time()
print(trends_df.head())
print(trends_df.info())
