class Machine:
    def __init__(self, name: str, input_resource: str, output_resource: str) -> None :
        self.name = name
        self.input_resource = input_resource
        self.output_resource = output_resource

    def display_info(self):
        print(f"{self.name} product {self.output_resource} from {self.input_resource}")

class Fonderie(Machine):
    def __init__(self, recipe: str) -> None:
        self.name == "smelter"

        if recipe == "iron ingot":
            super().__init__(self.name, "iron ore", "iron ingot")
            self.type = "iron"
            self.input_rate = 30
            self.output_rate = 30

        if recipe == "aluminium ingot":
            super().__init__(self.name, "aluminium scrap", "aluminium ingot")
            self.type = "aluminium"
            self.input_rate = 60
            self.output_rate = 30

        if recipe == "caterium ingot":
            super().__init__(self.name, "caterium ore", "caterium ingot")
            self.type = "caterium"
            self.input_rate = 45
            self.output_rate = 15

        if recipe == "copper ingot":
            super().__init__(self.name, "copper ore", "copper ingot")
            self.type = "copper"
            self.input_rate = 30
            self.output_rate = 30

    def production_per_minute(self):
        print(f"Create {self.output_rate} ingots of {self.type} per minute consuming {self.input_rate} {self.type} ores.")