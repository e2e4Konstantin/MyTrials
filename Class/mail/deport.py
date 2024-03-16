from datetime import datetime
from parcel import Parcel


class Deport:
    __items_counter = 0
    __profit = 0

    def __init__(self, title: str):
        self.title = title
        self.lists = {}

    def take_to_depot(self, post_item: Parcel):
        t = datetime.now()
        self.lists.update({post_item.id: (t, post_item)})
        self.__items_counter += 1
        self.__profit -= post_item.get_price() * 0.1
        print(f'На склад {self.title} получено почтовое отправление: {post_item.id} '
              f'Дата: {str(t.day)} {str(t.month)} {str(t.year)}')

    def get_from_depot(self, post_item: Parcel):
        if self.lists.pop(post_item.id, None) is None:
            print(f'отправления с идентификатором {post_item.id} на складе нет')
        else:
            self.__profit += post_item.get_price() * 0.5
            self.__items_counter -= 1
            t = datetime.now()
            print(f'Со склада: {self.title} удалено почтовое отправление: '
                  f'{post_item.id} Дата: {str(t.day)} {str(t.month)} {str(t.year)}')

    def deport_out(self):
        print(f'Склад: {self.title}. Посылок на складе: {self.__items_counter}. '
              f'Склад заработал: {self.__profit} \n{self.lists}')
