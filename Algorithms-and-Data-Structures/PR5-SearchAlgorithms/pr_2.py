import random


class RAM:

    def __init__(self, manufacturer: str, model: str, size: int, mem_type: str, frequency: int, timing: int):
        self.manufacturer = manufacturer
        self.model = model
        self.size = size
        self.mem_type = mem_type
        self.frequency = frequency
        self.timing = timing

    def __repr__(self):
        return f"RAM ({self.manufacturer}, {self.model}, {self.size}, {self.mem_type}, {self.frequency}, {self.timing})"

    def processing(self) -> list:
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

    def processing2(self, date: str, ishighfreq: bool, nomodel=False) -> str:

        if nomodel:
            return (f"""Дополнительная информация о памяти ({self.manufacturer}, {self.model}) 
с характеристиками ({self.size}GB {self.mem_type} {self.frequency} Ghz {self.timing} tacts) отсутствует""")

        if ishighfreq:
            return (f"""Оперативная память ({self.manufacturer}, {self.model}) типа ({self.mem_type}) выпускается 
с {date} года с повышенной частотой и следующими характеристиками: {self.size}, {self.frequency} {self.timing} tacts""")

        else:
            return (f"""Оперативная память ({self.manufacturer}, {self.model}) типа {self.mem_type} выпускается 
с {date} года с такими характеристиками: {self.size}, {self.frequency} {self.timing} tacts""")

    def __lt__(self, other):
        return (self.manufacturer, self.model, self.size, self.mem_type, self.frequency, self.timing) < \
               (other.manufacturer, other.model, other.size, other.mem_type, other.frequency, other.timing)

    def __le__(self, other):
        return (self.manufacturer, self.model, self.size, self.mem_type, self.frequency, self.timing) <= \
               (other.manufacturer, other.model, other.size, other.mem_type, other.frequency, other.timing)

    def __gt__(self, other):
        return (self.manufacturer, self.model, self.size, self.mem_type, self.frequency, self.timing) > \
               (other.manufacturer, other.model, other.size, other.mem_type, other.frequency, other.timing)

    def __eq__(self, other):
        return self.manufacturer == other.manufacturer and \
               self.model == other.model and \
               self.size == other.size and \
               self.mem_type == other.mem_type and \
               self.frequency == other.frequency and \
               self.timing == other.timing

class Generator:
    manufacturer = ["Kingston", "Samsung", "Hyper-X", "TTM", "SLV_UKR"]
    model = ["P332-4", "F1A", "QES2100", "X-1000", "Ls3P", "QQR", "EW135"]
    size = [*range(2, 33, 2)]
    mem_type = ["DDR2", "DDR3", "DDR4"]
    frequency = [*range(1000, 4001, 200)]
    timing = [*range(1, 21)]

    def generate_single(self) -> RAM:
        man = random.choice(self.manufacturer)
        mod = random.choice(self.model)
        size = int(random.choice(self.size))
        mtype = random.choice(self.mem_type)
        freq = random.choice(self.frequency)
        time = random.choice(self.timing)

        return RAM(man, mod, size, mtype, freq, time)

    def generate_1000(self) -> list:
        big_list = []
        n = 1000

        while n != 0:
            man = random.choice(self.manufacturer)
            mod = random.choice(self.model)
            size = int(random.choice(self.size))
            mtype = random.choice(self.mem_type)
            freq = random.choice(self.frequency)
            time = random.choice(self.timing)

            big_list.append(RAM(man, mod, size, mtype, freq, time))
            n -= 1

        return big_list

    def generate_10000(self) -> list:
        very_big_list = []
        n = 10000

        while n != 0:
            man = random.choice(self.manufacturer)
            mod = random.choice(self.model)
            size = int(random.choice(self.size))
            mtype = random.choice(self.mem_type)
            freq = random.choice(self.frequency)
            time = random.choice(self.timing)

            very_big_list.append(RAM(man, mod, size, mtype, freq, time))
            n -= 1

        return very_big_list


if __name__ == "__main__":
    component = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
    print(component.processing2(*component.processing()))

    g = Generator()
    print(g.generate_10000())