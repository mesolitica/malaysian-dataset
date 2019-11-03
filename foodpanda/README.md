## How-to

1. [foodpanda-city.json](foodpanda-city.json),

Available cities and page links.

```python
{'Kuala Lumpur': '/city/kuala-lumpur',
 'Penang': '/city/bayan-baru',
 'Petaling Jaya': '/city/petaling-jaya',
 'Subang': '/city/puchong',
 'Shah Alam': '/city/shah-alam',
 'Cyberjaya': '/city/cyberjaya',
```

2. [foodpanda-restaurant.json](foodpanda-restaurant.json),

Available restaurants for each cities.

```python
{'Kuala Lumpur': {'La Risata Bar Pizzeria Ristorante': {'star': '4.5',
   'delivery': 'Free',
   'characters': ['Meat', 'Pasta', 'Salad', 'Pizza', 'Italian'],
   'link': '/chain/ce3iw/la-risata-bar-pizzeria-ristorante'},
  'Viapre Italian Restaurant KL': {'star': '4.3',
   'delivery': 'Free',
   'characters': ['Pizza'],
   'link': '/chain/ck3sy/viapre-italian-restaurant-kl'},
```

3. [foodpanda-foods.json](https://huseinhouse-data.s3-ap-southeast-1.amazonaws.com/foodpanda-foods.json),

Available foods for each restaurants.

```python
{'La Risata Bar Pizzeria Ristorante': {'star': '4.5',
  'delivery': 'Free',
  'characters': ['Meat', 'Pasta', 'Salad', 'Pizza', 'Italian'],
  'link': '/chain/ce3iw/la-risata-bar-pizzeria-ristorante',
  'data': []},
 'Viapre Italian Restaurant KL': {'star': '4.3',
  'delivery': 'Free',
  'characters': ['Pizza'],
  'link': '/chain/ck3sy/viapre-italian-restaurant-kl',
  'data': [['Starters',
    {'is_half_type_available': False,
     'id': 639959,
     'name': 'Bresaola',
     'code': 'm4yz-pr-dpsn',
     'description': 'Air dry beef loin slices on fresh mozzarella, mushroom pikles, evo oil and fine balsamic',
     'file_path': '',
     'logo_path': '',
     'half_type': None,
     'is_alcoholic_item': False,
     'product_variations': [{'id':
```
