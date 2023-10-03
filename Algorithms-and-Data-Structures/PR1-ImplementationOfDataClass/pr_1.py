class RAM:
    def __init__(self, manufacturer, model, size, mem_type, frequency, timing):
        self.manufacturer = manufacturer
        self.model = model
        self.size = size
        self.mem_type = mem_type
        self.frequency = frequency
        self.timing = timing

    def processing(self):
        ishighfreq = False

        if self.mem_type == "DDR2":
            date = "2004"
            return [date, ishighfreq]

        elif self.mem_type == "DDR3":
            date = "2010"

            if int(self.frequency) > 1600:
                ishighfreq = True

            return [date, ishighfreq]

        elif self.mem_type == "DDR4":
            date = "2014"

            if int(self.frequency) > 2666:
                ishighfreq = True

            return [date, ishighfreq]

        else:
            return [None, None, True]

    def processing2(self, date: str, ishighfreq: bool, nomodel=False):

        if nomodel:
            return (f"""Дополнительная информация о памяти ({self.manufacturer}, {self.model}) 
с характеристиками ({self.size}GB {self.mem_type} {self.frequency}Ghz {self.timing}tacts) отсутствует""")

        if ishighfreq:
            return (f"""Оперативная память ({self.manufacturer}, {self.model}) типа ({self.mem_type}) выпускается 
с {date} года с повышенной частотой и следующими характеристиками: {self.size}, {self.frequency} {self.timing} tacts""")

        else:
            return (f"""Оперативная память ({self.manufacturer}, {self.model}) типа {self.mem_type} выпускается 
с {date} года с такими характеристиками: {self.size}, {self.frequency} {self.timing} tacts""")


if __name__ == "__main__":
    component = RAM("Corsair", "LM-600", 2, "DDR2", 1200, 8)
    print(component.processing2(*component.processing()))

    component = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
    print(component.processing2(*component.processing()))

    component = RAM("Razor", "LN131", 32, "DDR4", 1666, 6)
    print(component.processing2(*component.processing()))

    component = RAM("HyperX", "NM-200", 2, "DDR43", 1300, 2)
    print(component.processing2(*component.processing()))
