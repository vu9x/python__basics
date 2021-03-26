def accepted(el):
   return el.lower().startswith('i')


products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
products_sample = filter(accepted, products)
print(type(products_sample))  # <class 'filter'>
print(*products_sample)  # iPad iPhone iRiver
print(*products_sample)  # iPad iPhone iRiver
