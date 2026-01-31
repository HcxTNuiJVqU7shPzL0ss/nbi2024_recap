# pylint: skip-file
# noqa


class Country:
    # noqa
    def __init__(self, name, pop, area=None):
        # noqa
        self.__name = name
        self.__population = pop
        # 1c
        self.__area = area
        self.language = []

    # 1b
    def print_info(self):
        # noqa
        # 1d
        if self.__area is not None:
            print_area = f", the area of the country is {self.__area} km2"
        else:
            print_area = ""

        print(f"\nIn {self.__name} there are {self.__population} "
              f"million inhabitants{print_area}.")

        print_lang = "They speak the following language"
        if len(self.language) > 0:
            first_index = self.language[0]
            last_index = self.language[-1]
            if len(self.language) == 1:
                print_lang += f": {self.language[0]}."
            else:
                print_lang += "s: "
                for lang in self.language:
                    if lang == first_index:
                        print_lang += f"{lang}"
                    elif lang != last_index and lang != first_index:
                        print_lang += f", {lang}"
                    else:
                        print_lang += f" and {lang}."
            print(print_lang)


    # 1e
    def add_language(self, lang):
        # noqa
        self.language.append(lang)


country_list = []


se = Country("Sweden", 10.5, "450,295")
country_list.append(se)

no = Country("Norway", 5.5)
country_list.append(no)

# 1a
ic = Country("Iceland", 0.4) # Not allowed to use "is" (official short)
country_list.append(ic)

dk = Country("Denmark", 6.0)
country_list.append(dk)

# 1f
fi = Country("Finland", 5.6)
country_list.append(fi)

ch = Country("Switzerland", 8.9)
country_list.append(ch)

se.add_language("Swedish")

fi.add_language("Swedish")
fi.add_language("Finnish")

ch.add_language("German")
ch.add_language("French")
ch.add_language("Italian")
ch.add_language("Romanch")


for country in country_list:
    country.print_info()
