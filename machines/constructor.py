from machines import Machine

class Constructor(Machine):
    RECIPES = {
        "iron plate": {"input": "iron ingot", "output": "iron plate", "input_rate": 30, "output_rate": 20},
        "iron rod": {"input": "iron ingot", "output": "iron rod", "input_rate": 15, "output_rate": 15},
        "ficsite trigon": {"input": "ficsite ingot", "output": "ficsite trigon", "input_rate": 10, "output_rate": 30},
        "reanimated SAM": {"input": "SAM", "output": "reanimated SAM", "input_rate": 120, "output_rate": 30},
        "alternate charcoal": {"input": "wood", "output": "coal", "input_rate": 15, "output_rate": 150},
        "alternate biocoal": {"input": "biomass", "output": "coal", "input_rate": 37.5, "output_rate": 45},
        "alternate steel rod": {"input": "steel ingot", "output": "iron rod", "input_rate": 12, "output_rate": 48},
        "steel beam": {"input": "steel ingot", "output": "steel beam", "input_rate": 60, "output_rate": 15},
        "steel pipe": {"input": "steel ingot", "output": "steel pipe", "input_rate": 30, "output_rate": 20},
        "alternate steel canister": {"input": "steel ingot", "output": "empty canister", "input_rate": 40, "output_rate": 40},
        "empty canister": {"input": "plastic", "output": "empty canister", "input_rate": 30, "output_rate": 60},
        "quartz cristal": {"input": "raw quartz", "output": "quartz cristal", "input_rate": 37.5, "output_rate": 22.5},
        "alimunium casing": {"input": "aluminium ingot", "output": "alumunium casing", "input_rate": 90, "output_rate": 60},
        "silica": {"input": "raw quartz", "output": "silica", "input_rate": 22.5, "output_rate": 37.5},
        "copper sheet": {"input": "", "output": "", "input_rate": , "output_rate": },
        "": {"input": "", "output": "", "input_rate": , "output_rate": },
        "": {"input": "", "output": "", "input_rate": , "output_rate": },
        "": {"input": "", "output": "", "input_rate": , "output_rate": },

    }

    def __init__(self, recipe: str) -> None:
        self.name = "constructor"

        if recipe not in Constructor.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for constructor.")

        data = Constructor.RECIPES[recipe]

        super().__init__(self.name, data["input"], data["output"])
        self.input_rate = data["input_rate"]
        self.output_rate = data["output_rate"]
        self.input = data["input"]
        self.output = data["output"]
        
    def production_per_minute(self):
        print(f"Create {self.output_rate} {self.output} per minute consuming {self.input_rate} {self.input} per minutes.")