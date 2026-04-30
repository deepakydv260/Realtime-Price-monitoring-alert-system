import requests
import json
 
data= requests.get("https://fakestoreapi.com/products")
product_data = json.loads(data.content)
print(product_data)

col_name1 = product_data[0].keys()
col_name =list(col_name1)[0:5]

for i in product_data:
    for j,k in i.items():
        print(j,k)

