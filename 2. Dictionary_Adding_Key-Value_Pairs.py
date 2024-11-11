a = {'place': 'Dhaka', 'postal_code': 1219, 'country': 'Bangladesh'}      

place = a['place']                                         
postal_code = a.get('postal_code')
country = a['country']


print('place:', place)                                          
print('postal code:', postal_code)
print('country:', country)