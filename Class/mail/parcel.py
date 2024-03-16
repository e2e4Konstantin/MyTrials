from address import Address
from dimensions import Dimensions
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


class Parcel(Dimensions, Address):
    """ Почтовое отправление хранит следующие характеристики:
        -адресный блок (куда/откуда)
        -физические параметры (размер, вес)
        -тип отправления (посылка, бандероль...)
        -метод отправки (обычный,ускоренный....)
        -хрупкость 1/0,
        -страховая стоимость в рублях"""

    __type_dict = {1: 'Посылка', 2: 'Бандероль', 3: 'Ценное письмо'}
    __shipping_method = {1: 'Обычный', 2: 'Ускоренный'}

    def __init__(self, adr_to, adr_from, length, width, height, mass,
                 method, parcel_type, fragility, insured_value, **kwargs) -> None:
        super().__init__(to_address=adr_to, from_address=adr_from,
                         length=length, width=width, height=height, mass=mass, **kwargs)
        self.id = id(self)
        self.__parcel_type = self.__type_dict[parcel_type]
        self.__method = self.__shipping_method[method]
        self.__fragility = fragility
        self.__insured_value = insured_value
        self.__price = self.postage_price()

    def __str__(self):
        adr_dim = f'Почтовое отправление: {self.id}\n{Address.__str__(self)}\n{Dimensions.__str__(self)}'
        param_1 = f'тип отправления: {self.__parcel_type}\nметод: {self.__method}'
        param_2 = f'хрупкое: {"да" if self.__fragility else "нет"}\nстраховая стоимость: {self.__insured_value} руб.'
        param_3 = f'цена услуги: {self.__price} руб.'
        return f'{adr_dim}\nобъем:\t{round(self.get_volume() / 1e9, 2)} m3.\n{param_1}\n{param_2}\n{param_3}'

    def postage_price(self) -> float:
        """ Определить стоимость отправления
            расстояние, вес, страховая стоимость
        """
        tarif = 300
        dist = get_distance(self.get_city_from(), self.get_city_to())
        return round(self.__insured_value * 0.05 + tarif * self.get_mass() / dist, 2)

    def get_price(self):
        return self.__price


def get_distance(place_1: str, place_2: str):
    def get_point_coordinates(place: str):
        nom = Nominatim(user_agent='user')
        location = nom.geocode(place)
        if location is not None:
            return float(location.raw['lat']), float(location.raw['lon'])
        return None

    point_1 = get_point_coordinates(place_1)
    point_2 = get_point_coordinates(place_2)
    if point_1 is not None and point_2 is not None:
        return geodesic(point_1, point_2).km
    return None
