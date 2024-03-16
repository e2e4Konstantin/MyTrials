from deport import Deport
from parcel import Parcel

parcels = [
    {
        'from': 'Смольный пр-д, 1, Санкт-Петербург, 191124, Россия',
        'to': 'Московский Кремль. Манежная, 2-10, Москва, 119019, Россия',
        'height': 500,
        'width': 450,
        'length': 733,
        'mass': 200,
        'type_parcel': 1,
        'method': 1,
        'fragility': 1,
        'insured_value': 500

    },
    {
        'from': 'Кремль, Рязанская область, Рязань, 390000, Россия',
        'to': 'ул. 2-я Юго-Западная, Республика Татарстан, Казань, 420034, Россия',
        'height': 300,
        'width': 100,
        'length': 200,
        'mass': 1500,
        'type_parcel': 1,
        'method': 2,
        'fragility': 0,
        'insured_value': 3000
    },
]
index = 0
p1 = Parcel(parcels[index]['from'], parcels[index]['to'], parcels[index]['length'], parcels[index]['width'],
            parcels[index]['height'], parcels[index]['mass'], parcels[index]['type_parcel'], parcels[index]['method'],
            parcels[index]['fragility'], parcels[index]['insured_value'])
index = 1
p2 = Parcel(parcels[index]['from'], parcels[index]['to'], parcels[index]['length'], parcels[index]['width'],
            parcels[index]['height'], parcels[index]['mass'], parcels[index]['type_parcel'], parcels[index]['method'],
            parcels[index]['fragility'], parcels[index]['insured_value'])

print(p1)
print()
print(p2)

store_post = Deport('Почта')
store_post.take_to_depot(p1)
store_post.take_to_depot(p2)
store_post.get_from_depot(p2)
print()
store_post.deport_out()
