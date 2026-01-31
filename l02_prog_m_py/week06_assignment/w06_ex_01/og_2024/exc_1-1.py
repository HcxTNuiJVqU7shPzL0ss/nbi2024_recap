# pylint: skip-file
# noqa


class SafeStorage:
    # noqa
    __data = None

    def get(self):
        # noqa
        return self.__data

    def put(self, data):
        # noqa
        self.__data = data


safe = SafeStorage()

safe.put("Anakonda")
x = safe.get()

safe.put("Boaorm")
y = safe.get()

print(x, y)
