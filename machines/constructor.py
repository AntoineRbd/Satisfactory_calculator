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
        "copper sheet": {"input": "copper ingot", "output": "copper sheet", "input_rate": 20 , "output_rate": 10},
        "copper powder": {"input": "copper ingot", "output": "copper powder", "input_rate": 300, "output_rate": 50},
        "empty fuid tank": {"input": "aluminium ingot", "output": "empty fuild tank", "input_rate": 60, "output_rate": 60},
        "alternate iron pipe": {"input": "iron ingot", "output": "steel pipe", "input_rate": 100, "output_rate": 25},
        "alternate aluminium beam": {"input": "aluminium ingot", "output": "steel beam", "input_rate": 22.5, "output_rate": 22.5},
        "alternate aluminium rod": {"input": "aluminium ingot", "output": "iron rod", "input_rate": 7.5, "output_rate": 52.5},
        "alternate caterium wire": {"input": "caterium ingot", "output": "wire", "input_rate": 15, "output_rate": 120},
        "alternate iron wire": {"input": "iron ingot", "output": "wire", "input_rate": 12.5, "output_rate": 22.5},
        "alternate steel screw": {"input": "steel beam", "output": "srew", "input_rate": 5, "output_rate": 260},
        "alternate cast screw": {"input": "iron ingot", "output": "screw", "input_rate": 12.5, "output_rate": 50},
        "quickwire": {"input": "caterium ingot", "output": "quickwire", "input_rate": 12, "output_rate": 60},
        "solid biofuel": {"input": "biomass", "output": "solid biofuel", "input_rate": 120, "output_rate": 60},
        "hog protein": {"input": "hog remains", "output": "alien protein", "input_rate": 20, "output_rate": 20},
        "spitter protein": {"input": "spitter remains", "output": "alien protein", "input_rate": 20, "output_rate": 20},
        "biomass (mycelia)": {"input": "mycelia", "output": "biomass", "input_rate": 15, "output_rate": 150},
        "power shard (1)": {"input": "blue power slug", "output": "power shard", "input_rate": 1, "output_rate": 1},
        "stinger protein": {"input": "stinger remains", "output": "alien protein", "input_rate": 20, "output_rate": 20},
        "hatcher protein": {"input": "hatcher remains", "output": "alien protein", "input_rate": 20, "output_rate": 20},
        "alien DNA capsule": {"input": "alien protein", "output": "alien DNA capsule", "input_rate": 10, "output_rate": 10},
        "biomass (alien protein)": {"input": "alien protein", "output": "biomass", "input_rate": 15, "output_rate": 1500},
        "iron rebar": {"input": "iron rod", "output": "iron rebar", "input_rate": 15, "output_rate": 15},
        "power shard": {"input": "purple power slug", "output": "power shard", "input_rate": 2.5, "output_rate": 12.5},
        "power shard": {"input": "yellow power slug", "output": "power shard", "input_rate": 5, "output_rate": 10},
        "biomass (leaves)": {"input": "leaves", "output": "biomass", "input_rate": 120, "output_rate": 60},
        "biomass (wood)": {"input": "wood", "output": "biomass", "input_rate": 60, "output_rate": 300},
        "concrete": {"input": "limestone", "output": "concrete", "input_rate": 45, "output_rate": 15},
        "screw": {"input": "iron rod", "output": "screw", "input_rate": 10, "output_rate": 40},
        "cable": {"input": "wire", "output": "cable", "input_rate": 60, "output_rate": 30},
        "wire": {"input": "copper ingot", "output": "wire", "input_rate": 15, "output_rate": 30}
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

        self.consumption = 
        
    def production_per_minute(self):
        print(f"Create {self.output_rate} {self.output} per minute consuming {self.input_rate} {self.input} per minutes.")