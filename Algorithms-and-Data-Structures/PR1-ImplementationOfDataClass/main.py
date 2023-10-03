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


if __name__ == "__main__":
    component = RAM("Corsair", "LM-600", 2, "DDR2", 1200, 8)
    print(component.get_general_information())

    component = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
    print(component.get_general_information())

    component = RAM("Razor", "LN131", 32, "DDR4", 1666, 6)
    print(component.get_general_information())

    component = RAM("HyperX", "NM-200", 2, "DDR43", 1300, 2)
    print(component.get_general_information())
