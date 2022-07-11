# Я изучил работу (https://github.com/kpaveliev/skypro-c05-hw21-classes)


# Я обнаружил следующие запахи:


# 1) storage.py
#   Большой класс.
#   Он гораздо круче чем требуется в домашке.
#   Можно просто сократить до минимального рабочего функционала.

# class Storage(ABC):
#     @abstractmethod
#     def __init__(self, items, capasity):  # товары и емкость
#         self._items = items  # словарь название:количество
#         self._capasity = capasity
#
#     @abstractmethod
#     def add(self, title, count):  # увеличивает запас items
#         pass
#
#     @abstractmethod
#     def remove(self, title, count):  # уменьшает запас items
#         pass
#
#     @property
#     @abstractmethod
#     def get_free_space(self):  # вернуть количество свободных мест
#         pass
#
#     @property
#     @abstractmethod
#     def items(self):  # возвращает сожержание склада в словаре {товар: количество}
#         pass
#
#     @property
#     @abstractmethod
#     def get_unique_items_count(self):  # возвращает количество уникальных товаров.
#         pass


# 2) storage.py ---> store.py, shop.py
#   Завистливые функции.
#   Возможно, хоть логика работы и одинаковая и здорово,
#   что она в абстрактном классе, но для конкретизации каждого класса, наверное стоит
#   ее делать независимой в каждом классе
#
# class Store(Storage):
#     def __init__(self):
#         self._items = {}
#         self._capacity = 100
#
#     def add(self, title, count):
#         if title in self._items:
#             self._items[title] += count
#         else:
#             self._items[title] = count
#         self._capacity -= count
#
#     def remove(self, title, count):
#         res = self._items[title] - count
#         if res > 0:
#             self._capacity += count
#             self._items[title] = res
#         else:
#             del self._items[title]
#         self._capacity += count
#
#     @property
#     def get_free_space(self):
#         return self._capacity
#
#     @property
#     def items(self):
#         return self._items
#
#     @items.setter
#     def items(self, new_items):
#         self._items = new_items
#         self._capacity -= sum(self._items.values())
#
#     @property
#     def get_unique_items_count(self):
#         return len(self._items.keys())


# 3) utils.py
#   Посредник.
#   Домашка на проверке очень хорошая, но очень слоеная и структурная. Слишком.
#   Думаю, функции create_instances, display_items, send_request для простоты понимания
#   основной логики программы стоит просто перенести в main.py


# 4) main.py ---> utils.py ---> request.py
#   Цепочка вызовов.
#   Скорее это не антипаттерн, а специфика этого программиста - все разделить на куски,
#   а потом их соединять. Не стоит так усложнять получение нужных полей из формы
#   request. Внедрить класс Request сразу в main.py

# class Request:
#     def __init__(self, info):
#         self.info = self._split_info(info)
#         self.from_ = self.info[4]
#         self.to = self.info[6]
#         self.amount = int(self.info[1])
#         self.product = self.info[2]
#
#     @staticmethod
#     def _split_info(info):
#         return info.split(" ")