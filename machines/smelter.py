from machines import Machine

class Smelter(Machine):
    RECIPES = {
        "iron ingot": {"input": "iron ore", "output": "iron ingot", "input_rate": 30, "output_rate": 30, "type": "iron"},
        "aluminium ingot": {"input": "aluminium scrap", "output": "aluminium ingot", "input_rate": 60, "output_rate": 30, "type": "aluminium"},
        "caterium ingot": {"input": "caterium ore", "output": "caterium ingot", "input_rate": 45, "output_rate": 15, "type": "caterium"},
        "copper ingot": {"input": "copper ore", "output": "copper ingot", "input_rate": 30, "output_rate": 30, "type": "copper"}
    }

    def __init__(self, recipe: str) -> None:
        self.name = "smelter"

        if recipe not in Smelter.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for smelter.")

        data = Smelter.RECIPES[recipe]

        super().__init__(self.name, data["input"], data["output"])
        self.type = data["type"]
        self.input_rate = data["input_rate"]
        self.output_rate = data["output_rate"]

    def production_per_minute(self):
        print(f"Create {self.output_rate} ingots of {self.type} per minute consuming {self.input_rate} {self.type} ores.")