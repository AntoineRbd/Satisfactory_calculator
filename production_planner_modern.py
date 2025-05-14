
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox,
    QPushButton, QScrollArea, QGroupBox, QHBoxLayout
)
from PyQt5.QtCore import Qt
import sys
from machines.machines import MACHINE_CLASSES

class ProductionPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satisfactory Planner (Thème Sombre)")
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-size: 14px;
            }
            QComboBox, QSpinBox, QPushButton {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #5c5c5c;
                padding: 4px;
            }
            QPushButton {
                background-color: #0066cc;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3399ff;
            }
            QGroupBox {
                border: 1px solid #444;
                margin-top: 10px;
                padding: 8px;
                border-radius: 4px;
            }
            QLabel {
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()

        # Sélection du produit
        header = QLabel("🎯 Ressource à produire")
        self.combo = QComboBox()
        self.recipes_map = self.load_all_recipes()
        self.combo.addItems(sorted(self.recipes_map.keys()))

        # Nombre de machines finales
        spin_layout = QHBoxLayout()
        self.spin_label = QLabel("🏭 Machines finales :")
        self.spin = QSpinBox()
        self.spin.setMinimum(1)
        self.spin.setValue(1)
        spin_layout.addWidget(self.spin_label)
        spin_layout.addWidget(self.spin)

        # Bouton de calcul
        self.button = QPushButton("🔁 Calculer la chaîne")
        self.button.clicked.connect(self.calculate_chain)

        # Zone de scroll des résultats
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.result_container = QWidget()
        self.result_layout = QVBoxLayout()
        self.result_container.setLayout(self.result_layout)
        self.scroll_area.setWidget(self.result_container)

        layout.addWidget(header)
        layout.addWidget(self.combo)
        layout.addLayout(spin_layout)
        layout.addWidget(self.button)
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)

    def load_all_recipes(self):
        recipes = {}
        for machine_class in MACHINE_CLASSES:
            for recipe in machine_class.RECIPES:
                recipes[recipe] = machine_class
        return recipes

    def calculate_chain(self):
        for i in reversed(range(self.result_layout.count())):
            widget = self.result_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        resource = self.combo.currentText()
        count = self.spin.value()
        machine_class = self.recipes_map[resource]
        instance = machine_class(resource)
        self.recursive_trace(instance, count, level=0)

    def recursive_trace(self, machine, multiplier, level):
        group = QGroupBox(f"{'  '*level}🔧 {multiplier} x {machine.name} : {machine.recipe_name}")
        layout = QVBoxLayout()

        for item, qty in machine.inputs:
            layout.addWidget(QLabel(f"📥 Besoin : {qty * multiplier:.1f} / min de {item}"))
            if item in self.recipes_map:
                sub_class = self.recipes_map[item]
                sub_machine = sub_class(item)
                needed = (qty * multiplier) / sub_machine.outputs[0][1]
                self.recursive_trace(sub_machine, round(needed), level + 1)

        for item, qty in machine.outputs:
            layout.addWidget(QLabel(f"📤 Produit : {qty * multiplier:.1f} / min de {item}"))

        group.setLayout(layout)
        self.result_layout.addWidget(group)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductionPlanner()
    window.show()
    sys.exit(app.exec_())
