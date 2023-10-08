import random
from typing import Optional


class RAM:
    def __init__(self, manufacturer, model, size, memory_type, frequency, timing):
        self.manufacturer = manufacturer
        self.model = model
        self.size = size
        self.memory_type = memory_type
        self.frequency = frequency
        self.timing = timing

    def get_creation_date_and_frequency_type(self) -> tuple:
        has_high_frequency = False
        model_not_defined = False
        year: Optional[str] = None

        if self.memory_type == "DDR2":
            year = "2004"

        elif self.memory_type == "DDR3":
            year = "2010"

            if int(self.frequency) > 1600:
                has_high_frequency = True

        elif self.memory_type == "DDR4":
            year = "2014"

            if int(self.frequency) > 2666:
                has_high_frequency = True

        else:
            model_not_defined = True

        return year, has_high_frequency, model_not_defined

    def get_general_information(self) -> str:
        year, has_high_frequency, model_not_defined = self.get_creation_date_and_frequency_type()

        if model_not_defined:
            return (f"Additional information about memory ({self.manufacturer}, {self.model})\n"
                    f"with specifications ({self.size}GB {self.memory_type} {self.frequency}GHz, {self.timing} tacts) "
                    f"is missing")

        if has_high_frequency:
            return (f"RAM ({self.manufacturer}, {self.model}) of type ({self.memory_type}) has been produced\n"
                    f"with increased frequency since {year} and has the following characteristics: "
                    f"{self.size}, {self.frequency}GHz, {self.timing} tacts")

        else:
            return (f"RAM ({self.manufacturer}, {self.model}) of type {self.memory_type} has been produced\n"
                    f"since {year} with the following characteristics: {self.size}, {self.frequency}GHz, "
                    f"{self.timing} tacts")

class Generator:
    manufacturer = ["Kingston", "Samsung", "Hyper-X", "TTM", "SLV_UKR"]
    model = ["P332-4", "F1A", "QES2100", "X-1000", "Ls3P", "QQR", "EW135"]
    mem_type = ["DDR2", "DDR3", "DDR4", "DDR5"]
    size = [*range(2, 128, 2)]
    frequency = [*range(1000, 5800, 200)]
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
    ram = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
    print(ram.get_general_information())

    g = Generator()
    print(g.generate_10000())