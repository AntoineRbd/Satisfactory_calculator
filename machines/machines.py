from typing import List, Union

class Machine:
    def __init__(self, name: str, input_resources: Union[str, List[str]], output_resource: str) -> None:
        self.name = name

        if isinstance(input_resources, str):
            self.input_resources = [input_resources]
        else:
            self.input_resources = input_resources

        self.output_resource = output_resource

    def display_info(self):
        inputs = ", ".join(self.input_resources)
        print(f"{self.name} produces {self.output_resource} from {inputs}")