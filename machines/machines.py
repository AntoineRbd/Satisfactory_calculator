class Machine:
    def __init__(self, name: str, input_resource: str, output_resource: str) -> None :
        self.name = name
        self.input_resource = input_resource
        self.output_resource = output_resource

    def display_info(self):
        print(f"{self.name} product {self.output_resource} from {self.input_resource}")