mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }
for i in range (len(mobile_data['data'])):
         name1 = ((mobile_data['data'][i])['name'])
         price1 = ((mobile_data['data'][i])['price'])
         manufacture = ((mobile_data['data'][i])['made'])
         price_BDT = ((float(((mobile_data['data'][i])['price']).split(' ')[0]))*(mobile_data['exchnage_rate']))

         print(f'{name1}  is made in {manufacture}. The price is {price1} which is almost equal to {price_BDT: .2f} BDT')

