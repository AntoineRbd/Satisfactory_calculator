
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox,
    QSpinBox, QPushButton, QTextEdit, QHBoxLayout
)
import sys
from machines.machines import MACHINE_CLASSES 

class ProductionPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satisfactory Production Planner")
        self.setMinimumWidth(600)

        layout = QVBoxLayout()

        # Sélection de la ressource finale
        self.label = QLabel("Choisir une ressource à produire :")
        self.combo = QComboBox()
        self.recipes_map = self.load_all_recipes()
        self.combo.addItems(sorted(self.recipes_map.keys()))

        # Sélection du nombre de machines
        spin_layout = QHBoxLayout()
        self.machine_label = QLabel("Nombre de machines finales :")
        self.spin = QSpinBox()
        self.spin.setMinimum(1)
        self.spin.setValue(1)
        spin_layout.addWidget(self.machine_label)
        spin_layout.addWidget(self.spin)

        # Bouton de calcul
        self.button = QPushButton("Calculer la chaîne de production")
        self.button.clicked.connect(self.calculate_chain)

        # Zone de sortie
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        # Layout principal
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addLayout(spin_layout)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def load_all_recipes(self):
        recipes = {}
        for machine_class in MACHINE_CLASSES:
            for recipe in machine_class.RECIPES:
                recipes[recipe] = machine_class
        return recipes

    def calculate_chain(self):
        resource = self.combo.currentText()
        count = self.spin.value()
        machine_class = self.recipes_map[resource]
        instance = machine_class(resource)
        lines = []
        self.recursive_trace(instance, count, lines, level=0)
        self.output.setPlainText("\n".join(lines))

    def recursive_trace(self, machine, multiplier, lines, level):
        indent = "  " * level
        lines.append(f"{indent}- {multiplier} x {machine.name} ({machine.recipe_name})")
        for item, qty in machine.inputs:
            lines.append(f"{indent}  besoin: {qty * multiplier:.1f} / min de {item}")
            if item in self.recipes_map:
                sub_machine_class = self.recipes_map[item]
                sub_instance = sub_machine_class(item)
                units_needed = (qty * multiplier) / sub_instance.outputs[0][1]
                self.recursive_trace(sub_instance, round(units_needed), lines, level + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductionPlanner()
    window.show()
    sys.exit(app.exec_())
