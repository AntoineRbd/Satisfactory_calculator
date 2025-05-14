from typing import List, Tuple

from machines.recipe import recipe_constructor, recipe_assembler, recipe_foundry, recipe_manufacturer, recipe_packager, recipe_refinery, recipe_blender, recipe_particle_accelerator, recipe_quantum_encoder, recipe_converter, recipe_smelter 

class Machine:
    def __init__(self, name: str, recipe_name: str, inputs: List[Tuple[str, float]], outputs: List[Tuple[str, float]]) -> None:
        self.name = name
        self.recipe_name = recipe_name
        self.inputs = inputs
        self.outputs = outputs

    def display_info(self) -> None:
        print(f"{self.name} - Recipe : {self.recipe_name}")
        print("  Inputs :")
        for item, rate in self.inputs:
            print(f"    - {rate} / min of {item}")
        print("  Outputs :")
        for item, rate in self.outputs:
            print(f"    - {rate} / min of {item}")

class Constructor(Machine):
    RECIPES = recipe_constructor.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Constructor"

        if recipe not in Constructor.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for constructor.")

        data = Constructor.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Assembler(Machine):
    RECIPES = recipe_assembler.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Assembler"

        if recipe not in Assembler.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for assembler.")

        data = Assembler.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Foundry(Machine):
    RECIPES = recipe_foundry.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Foundry"

        if recipe not in Foundry.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for foundry.")

        data = Foundry.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Manufacturer(Machine):
    RECIPES = recipe_manufacturer.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Manufacturer"

        if recipe not in Manufacturer.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for manufacturer.")

        data = Manufacturer.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Packager(Machine):
    RECIPES = recipe_packager.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Packager"

        if recipe not in Packager.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for packager.")

        data = Packager.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Refinery(Machine):
    RECIPES = recipe_refinery.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Refinery"

        if recipe not in Refinery.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for refinery.")

        data = Refinery.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Blender(Machine):
    RECIPES = recipe_blender.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Blender"

        if recipe not in Blender.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for blender.")

        data = Blender.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Particle_accelerator(Machine):
    RECIPES = recipe_particle_accelerator.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Particle_accelerator"

        if recipe not in Particle_accelerator.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for particle accelerator.")

        data = Particle_accelerator.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Quantum_encoder(Machine):
    RECIPES =  recipe_quantum_encoder.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = " Quantum_encoder"

        if recipe not in  Quantum_encoder.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for quantum encoder.")

        data =  Quantum_encoder.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Converter(Machine):
    RECIPES = recipe_converter.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Converter"

        if recipe not in Converter.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for converter.")

        data = Converter.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])

class Smelter(Machine):
    RECIPES = recipe_smelter.RECIPES

    def __init__(self, recipe: str) -> None:
        self.name = "Smelter"

        if recipe not in Smelter.RECIPES:
            raise ValueError(f"Recipe '{recipe}' not recognized for smelter.")

        data = Smelter.RECIPES[recipe]

        super().__init__(self.name, recipe_name=recipe, inputs=data["inputs"], outputs=data["outputs"])


MACHINE_CLASSES = [
    Constructor,
    Assembler,
    Manufacturer,
    Foundry,
    Refinery,
    Packager,
    Blender,
    Particle_accelerator,
    Quantum_encoder,
    Converter,
    Smelter
]