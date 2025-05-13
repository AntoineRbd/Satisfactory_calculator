from machines import Machine

class Constructor(Machine):
    RECIPES = {
        "Alternate: Compacted Coal": {"input_1": "Coal", "input_2": "Sulfur", "output": "Compacted coal", "input_1_rate": 25, "input_2_rate": 25,"output_rate": 25},
        "Circuit Board": {"input_1": "Copper Sheet", "input_2": "Plastic", "output": "Circuit board", "input_1_rate": 15, "input_2_rate": 30,"output_rate": 7.5},
        "versatile Famework": {"input_1": "Modular Frame", "input_2": "Steel Beam", "output": "Versatile Framework", "input_1_rate": 2.5, "input_2_rate": 30,"output_rate": 5},
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
        "": {"input_1": "", "input_2": "", "output": "", "input_1_rate": , "input_2_rate": ,"output_rate": },
    }

    def __init__(self, recipe: str) -> None:
        self.name = "assembler"

        if recipe not in Constructor.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for assembler.")

        data = Constructor.RECIPES[recipe]

        super().__init__(self.name, [data["input_1"], data["input_2"]], data["output"])
        self.input_1_rate = data["input_1_rate"]
        self.input_2_rate = data["input_2_rate"]
        self.output_rate = data["output_rate"]
        self.input_1 = data["input_1"]
        self.input_2 = data["input_2"]
        self.output = data["output"]
        
    def production_per_minute(self):
        print(f"Create {self.output_rate} {self.output} per minute consuming {self.input_rate} {self.input} per minutes.")