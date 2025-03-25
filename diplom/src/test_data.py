import os

from faker import Faker
from random import randint
from datetime import datetime


class _TestData:
    def __init__(self):
        self.fake_ru = Faker("ru_RU")
        self.fake_en = Faker("en_US")
        self._category_data = None
        self._product_data = None
        self._user_data = None
        self._address_data = None
        self._voucher_data = None   # Кэшированные данные

    @property
    def get_filepath(self):
        if os.getcwd() == r"C:\Users\m.zhigunov\PycharmProjects\Diplom\diplom":
            return os.path.join(os.getcwd(), "src", "1.jpg")
        else:
            return r"C:\Users\m.zhigunov\PycharmProjects\Diplom\diplom\src\1.jpg"

    @property
    def category_data(self):
        if self._category_data is None:  # Если данные еще не сгенерированы
            self._category_data = {"category_name": self.fake_ru.word(),
                                   "description": " ".join(self.fake_ru.words(5)),
                                   "meta_title": self.fake_en.word(),
                                   "meta_description": " ".join(self.fake_ru.words(5)),
                                   "meta_keywords": " ".join(self.fake_en.words(nb=3)),
                                   "seo_url": self.fake_en.word()
                                   }
        return self._category_data

    @property
    def product_data(self):
        if self._product_data is None:  # Если данные еще не сгенерированы
            self._product_data = {"text": " ".join(self.fake_en.words(nb=3)),
                                  "select": "1",
                                  "textarea": self.fake_ru.text(max_nb_chars=20),
                                  "date": datetime.now().strftime("%Y-%m-%d"),
                                  "time": datetime.now().strftime("%H:%M"),
                                  "datetime": datetime.now().strftime("%Y-%m-%d %H:%M")
                                  }
        return self._product_data

    @property
    def user_data(self):
        if self._user_data is None:
            self._user_data = {"firstname": self.fake_ru.first_name(),
                               "lastname": self.fake_ru.last_name(),
                               "email": self.fake_en.email(),
                               "password": self.fake_ru.password(),
                               "customer_group_id": "1"
                               }
        return self._user_data

    @property
    def address_data(self):
        if self._address_data is None:
            self._address_data = {"firstname": self.fake_ru.first_name(),
                                  "lastname": self.fake_ru.last_name(),
                                  "address": self.fake_ru.address(),
                                  "city": self.fake_ru.city(),
                                  "country": "176",
                                  "zone": "4335"
                                  }
        return self._address_data

    @property
    def voucher_data(self):
        if self._voucher_data is None:
            self._voucher_data = {"from_name": self.fake_en.name(),
                                  "from_email": self.fake_en.email(),
                                  "to_name": self.fake_en.name(),
                                  "to_email": self.fake_en.email(),
                                  "voucher_theme_id": "6",
                                  "amount": str(randint(1, 1000)),
                                  "message": " ".join(self.fake_en.words(nb=3))
                                  }
        return self._voucher_data

