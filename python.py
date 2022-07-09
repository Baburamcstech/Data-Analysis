import pandas as pd
Google_stock=pd.read_csv('/content/robusta_data_cleaned.csv')
print('Google_stock is of type:',type(Google_stock))
print("Google_stock has shape:",Google_stock.shape)
Google_stock.columns
Google_stock.head()
Google_stock.isnull().sum()
Google_stock.rename(columns={"Country.of.Origin":"Country.of.Founder"},inplace=True)
Google_stock['Farm.Name'].isnull
#Google_stock.Country.of.Founder.nunique()
Google_stock.head(1)