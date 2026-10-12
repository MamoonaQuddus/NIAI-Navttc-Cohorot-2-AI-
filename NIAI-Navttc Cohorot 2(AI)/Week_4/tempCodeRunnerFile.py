# E 
# raw = pd.read_csv('Daily_sales_Csv')

# # T
# clean = raw.dropna().assign(
#     revenue = raw['price'] * raw['qty']
# ) 

# # L 
# clean.to_csv('processed_sales_csv', index= False)