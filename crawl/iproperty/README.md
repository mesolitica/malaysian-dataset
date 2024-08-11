# Iproperty

## download

1. sales all-residential, https://huggingface.co/datasets/malaysia-ai/iproperty/resolve/main/sales-residential.zip
2. rents all-residential, https://huggingface.co/datasets/malaysia-ai/iproperty/resolve/main/rents-residential.zip
3. sales all-commercial, https://huggingface.co/datasets/malaysia-ai/iproperty/resolve/main/sales-commercial.zip
4. rents all-commercial, https://huggingface.co/datasets/malaysia-ai/iproperty/resolve/main/rents-commercial.zip

## how-to-read

```python
# !unzip sales-residential.zip

import json
from glob import glob

files = glob('sales-residential/*.json')

with open(files[0]) as fopen:
    data = json.load(fopen)

print(data['listings']['items'][0])
```

```text
{'prices': [{'type': 'sale', 'currency': 'MYR', 'min': 899000, 'max': 899000}],
 'medias': [{'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/306bd1cdd0454c8ab73221d3a4b9fb23.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/306bd1cdd0454c8ab73221d3a4b9fb23.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/306bd1cdd0454c8ab73221d3a4b9fb23.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/67b989ed26ff4ec5ba3f9a8aeb842ea7.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/67b989ed26ff4ec5ba3f9a8aeb842ea7.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/67b989ed26ff4ec5ba3f9a8aeb842ea7.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/535d87ad364242c6b271611d6e4728fe.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/535d87ad364242c6b271611d6e4728fe.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/535d87ad364242c6b271611d6e4728fe.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/673b01c87e6449138b3211c250a383c0.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/673b01c87e6449138b3211c250a383c0.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/673b01c87e6449138b3211c250a383c0.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/f78c5d30d7f2484284d5acafe0b59614.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/f78c5d30d7f2484284d5acafe0b59614.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/f78c5d30d7f2484284d5acafe0b59614.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/4631b581e7e74e5599768e9fbdfd30e5.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/4631b581e7e74e5599768e9fbdfd30e5.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/4631b581e7e74e5599768e9fbdfd30e5.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/7e67f39e27e744a9970d7aeeba9829d8.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/7e67f39e27e744a9970d7aeeba9829d8.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/7e67f39e27e744a9970d7aeeba9829d8.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/cc1f2111c87e496bad8dec1a63393145.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/cc1f2111c87e496bad8dec1a63393145.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/cc1f2111c87e496bad8dec1a63393145.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/da909b4aa1644d958fa394ac3b97bce9.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/da909b4aa1644d958fa394ac3b97bce9.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/da909b4aa1644d958fa394ac3b97bce9.jpg',
   'mimeType': 'image/jpeg'},
  {'type': 'image',
   'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/3fd1843625e9459fbdb78a7c2d1318a9.jpg',
   'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/3fd1843625e9459fbdb78a7c2d1318a9.jpg',
   'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/3fd1843625e9459fbdb78a7c2d1318a9.jpg',
   'mimeType': 'image/jpeg'}],
 'cover': {'type': 'image',
  'url': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/306bd1cdd0454c8ab73221d3a4b9fb23.jpg',
  'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/640/10460/306bd1cdd0454c8ab73221d3a4b9fb23.jpg',
  'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/640/10460/306bd1cdd0454c8ab73221d3a4b9fb23.jpg',
  'mimeType': 'image/jpeg'},
 'logo': {},
 'address': {'formattedAddress': 'Jalan Sultan Ismail, KLCC, 50250, Kuala Lumpur',
  'lat': 3.154365,
  'lng': 101.707512,
  'hasLatLng': True,
  'hideMarker': False},
 'multilanguagePlace': {'en-GB': {'level1': 'Kuala Lumpur',
   'level2': 'KLCC',
   'level3': 'Vortex'},
  'ms-MY': {'level1': 'Kuala Lumpur', 'level2': 'KLCC', 'level3': 'Vortex'}},
 'attributes': {'builtUp': '826',
  'furnishing': 'Partly Furnished',
  'landTitleType': 'Unknown',
  'tenure': 'Freehold',
  'facingDirection': 'Unknown',
  'occupancy': 'Vacant',
  'titleType': 'Strata',
  'sizeUnit': 'SQUARE_FEET',
  'sizeUnitLandArea': 'SQUARE_FEET',
  'downloadUrl': 'http://generator.iproperty.com.my/property/generate_pdf.aspx?pid=JI-weovckV81',
  'buildingId': 3879},
 'organisations': [{'id': '1669',
   'type': 'agency',
   'name': 'Vivahomes Realty - Subang Jaya',
   'logo': {'type': 'image',
    'url': 'https://images-my.ippstatic.com/images/searchresult/agencybrandlogo/c73a67c8ab304a07b6475c23159bae33.png',
    'thumbnailUrl': 'https://images-my.ippstatic.com/images/searchresult/agencybrandlogo/c73a67c8ab304a07b6475c23159bae33.png',
    'mimeType': 'image/jpeg'},
   'color': '#80bc00',
   'contact': {'phones': [{'number': '+60380811688', 'label': 'phone'},
     {'number': ' 60380243288', 'label': 'fax'}]}}],
 'listers': [{'id': '10460',
   'type': 'agent',
   'name': 'Victor',
   'license': 'REN 11115',
   'website': 'https://www.iproperty.com.my/property-agent/victor-10460',
   'image': {'type': 'image',
    'url': 'https://pictures-my.ippstatic.com/realtors/images/agent/e34da466ea47467080016b98675ce96f.jpg',
    'urlTemplate': 'https://img.rea-asia.com/my-subsale/premium/${width}x${height}-${scale}/realtors/images/agent/e34da466ea47467080016b98675ce96f.jpg',
    'thumbnailUrl': 'https://pictures-my.ippstatic.com/realtors/images/agent/e34da466ea47467080016b98675ce96f.jpg',
    'mimeType': 'image/jpeg'},
   'contact': {'phones': [{'number': '+60132872856', 'label': 'mobile'},
     {'number': '+60132872856', 'label': 'whatsapp'}],
    'emails': ['vistaera@gmail.com']}}],
 'active': True,
 'isPrimary': False,
 'channels': ['sale'],
 'id': 'sale-7995132',
 'kind': 'property',
 'shareLink': 'https://www.iproperty.com.my/property/klcc/vortex/sale-7995132/',
 'title': 'Vortex, KLCC',
 'description': "VORTEX KLCC \r\nSize : 826 sq ft \r\n2 bedrooms 2 batrooms + 1 study room \r\nmiddle floor \r\nrenovated and full furnished \r\n\r\n\r\n** good deal, below market value\r\n\r\nVortex KLCC is a newly completed residences by Monoland which lies in the heart of Golden Triangle of KL. It is also a new iconic curvy round-shaped highrise building which totally bring a new breath to the skyline. Vortex is surrounded by corporate office buildings, luxury hotels and famous shopping malls. \r\n- Shangri-La hotel is right opposite Vortex KLCC \r\n- KLCC shopping mall and Pavilion mall is walking distance from Vortex KLCC \r\n- KL Tower is 3 minutes drive away from Vortex KLCC \r\n- Bukit Nanas Monorail Station is walking distance away from Vortex KLCC \r\n\r\nVortex is a freehold serviced apartment located at Jalan Sultan Ismail, at the heart of KL City. This serviced apartment is 58-storeys in height with 248 units in total. The serviced apartment's unit size starts from 744 sq.ft. \r\n\r\nThe facilities available at Vortex are clubhouse, gymnasium, lap pool, Alfresco lounge, water features, timber deck, sun lounge, steam room, sauna, chillout music pool bar and health spa. \r\n\r\nConsidered one of the best located serviced apartments nearby KLCC, Vortex is just minutes drive to Suria KLCC Shopping Centre and Pavilion Mall, all within 10-15 minutes. \r\n\r\n# contact agent Victor 013-2872856",
 'tier': 3,
 'isPremiumPlus': False,
 'propertyType': 'Serviced Residence',
 'updatedAt': '2020-06-03T05:22:00Z',
 'postedAt': '2020-06-03T05:22:00Z',
 'referenceCode': 'UP7995132',
 'channel': 'sale',
 'isSA': False}
```