class Address:
    def __init__(self, to_address: str = '', from_address: str = '', **kwargs) -> None:
        self.__to_address = to_address
        self.__from_address = from_address
        self.__to_dict = dict
        self.__from_dict = dict
        self.unpack_address()
        super().__init__(**kwargs)

    def unpack_address(self):
        sep_address = self.__to_address.split(' ')
        self.__to_dict = {"country": sep_address[-1].strip(','), "zip_code": sep_address[-2].strip(','),
                          "place_name": sep_address[-3].strip(','), 'addr': ' '.join(sep_address[:-3])}
        sep_address = self.__from_address.split(' ')
        self.__from_dict = {"country": sep_address[-1].strip(','), "zip_code": sep_address[-2].strip(','),
                            "place_name": sep_address[-3].strip(','), 'addr': ' '.join(sep_address[:-3])}

    def address_out(self):
        print(f'Откуда: {self.__from_dict}\n Куда: {self.__to_dict}')

    def get_city_from(self):
        return f"{self.__from_dict['place_name']}, {self.__from_dict['country']}"

    def get_city_to(self):
        return f"{self.__to_dict['place_name']}, {self.__to_dict['country']}"

    def __str__(self) -> str:
        return f'куда:\t{self.__to_address}\nоткуда:\t{self.__from_address}'
