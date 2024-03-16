import itertools


class Dimensions:
    """
    Класс Dimensions представляет физические размеры, вес объекта и операции над ними.
    Размеры в миллиметрах, вес в граммах
    """

    def __init__(self, length, width, height, mass, **kwargs) -> None:
        """
        параметры длинна, ширина, высота и масса типа integer и подчиняются условиям:
        0 <= height < 1000  0 <= width < 1000  0 <= length < 1000 0 <= mass < 100000
        """
        self.__length, self.__height, self.__width, self.__mass = 0, 0, 0, 0
        self.set_dimensions(length, width, height, mass)
        super().__init__(**kwargs)

    def set_dimensions(self, length, width, height, mass) -> None:
        if type(length) == int and 0 <= length < 1000:
            self.__length = length
        else:
            raise TypeError("длинна должна быть в диапазоне 0 - 1000 мм")
        if type(height) == int and 0 <= height < 1000:
            self.__height = height
        else:
            raise TypeError("высота должна быть в диапазоне 0 - 1000 мм")
        if type(width) == int and 0 <= width < 1000:
            self.__width = width
        else:
            raise TypeError("ширина должна быть в диапазоне 0 - 1000 мм")
        if type(mass) == int and 0 <= mass < 100000:
            self.__mass = mass
        else:
            raise TypeError("вес должен быть в диапазоне 0 - 10000 мм")

    def __str__(self) -> str:
        return f'размер: {self.__length} x {self.__width} x {self.__height} мм, вес: {round(self.__mass / 1000, 2)} кг'

    def get_volume(self) -> float:
        return self.__length * self.__width * self.__height \
            if self.__length != 0 and self.__width != 0 and self.__height != 0 else 0

    def get_storage_area(self) -> float:
        """ Площадь занимаемая грузом на полке для хранения """
        side_1 = self.__length * self.__width
        side_2 = self.__length * self.__height
        side_3 = self.__height * self.__width
        return max(side_1, side_2, side_3)

    def get_stowage_factor(self) -> float:
        """ Удельный вес груза - плотность груза. Вес в кг одного кубического сантиметра груза """
        return (self.__mass / 1000) / self.get_volume() / 1000

    def get_rotation_list(self) -> list:
        """ Все возможные повороты груза """
        tmp_key = [self.__length, self.__width, self.__height]
        return [x for x in itertools.permutations(tmp_key)]

    def get_mass(self):
        return self.__mass


    # def mass_center(self):  ------ пустышка?
    #     pass
