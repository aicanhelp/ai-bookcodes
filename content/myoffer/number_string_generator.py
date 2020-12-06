class StringNumberGenerator:
    def __init__(self, parent=None, auto_tick=False):
        self.__parent = parent
        self.__current = 0
        self.__auto_tick = auto_tick

    def set_auto_tick(self):
        self.__auto_tick = True

    def next(self, tick=False):
        parent_tick = False
        if tick or self.__auto_tick:
            self.__current = self.__current + 1

        parent_number = ''

        if self.__current == 10:
            if not self.__parent: return None
            parent_tick = True
            self.__current = 0

        if self.__parent:
            parent_number = self.__parent.next(parent_tick)
            if not parent_number: return None

        return parent_number + str(self.__current)


def generate_string_numbers(bit_length=3):
    generator = StringNumberGenerator(None)
    for i in range(0, bit_length - 1):
        generator = StringNumberGenerator(generator)

    generator.set_auto_tick()

    while True:
        number_string = generator.next()
        if not number_string: return
        print(number_string)
