
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsTextItem, QGraphicsRectItem, QGraphicsLineItem
)
from PyQt5.QtGui import QPen, QColor, QFont, QPainter
from PyQt5.QtCore import Qt
from typing import Dict, Tuple, List
import sys

# Ratios de production par usine (en unités/minute)
PRODUCTION_RATIOS: Dict[str, Dict[str, Tuple[int, int, str, str]]] = {
    "Fer": {
        "Fonderie": (30, 30, "minerais de fer", "lingots de fer"),
        "Constructeur (Plaques)": (30, 15, "lingots de fer", "plaques de fer"),
        "Constructeur (Tiges)": (15, 15, "lingots de fer", "tiges de fer"),
        "Constructeur (Vis)": (10, 40, "tiges de fer", "vis")
    },
    "Cuivre": {
        "Fonderie": (30, 30, "minerais de cuivre", "lingots de cuivre"),
        "Constructeur (Câbles)": (15, 30, "lingots de cuivre", "câbles"),
        "Constructeur (Fil)": (30, 60, "lingots de cuivre", "fil de cuivre")
    },
    "Calcaire": {
        "Constructeur (Béton)": (45, 15, "calcaire", "béton")
    },
    "Pétrole": {
        "Raffinerie (Plastique)": (30, 20, "barils de pétrole", "plastique"),
        "Raffinerie (Caoutchouc)": (30, 20, "barils de pétrole", "caoutchouc")
    }
}

class ProductionVisualizer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.nodes = {}
    
    def add_factory_node(self, x, y, name, input_res, output_res, input_qty, output_qty):
        rect = QGraphicsRectItem(x, y, 150, 100)
        rect.setPen(QPen(QColor("#3498db"), 2))
        self.scene.addItem(rect)

        title = QGraphicsTextItem(name)
        title.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        title.setPos(x + 10, y + 5)
        self.scene.addItem(title)

        inputs = QGraphicsTextItem(f"{input_qty} {input_res}")
        inputs.setPos(x + 10, y + 30)
        self.scene.addItem(inputs)

        outputs = QGraphicsTextItem(f"{output_qty} {output_res}")
        outputs.setPos(x + 10, y + 55)
        self.scene.addItem(outputs)

        self.nodes[output_res] = (x + 150, y + 50)
    
    def connect_nodes(self, input_res, output_res):
        if input_res in self.nodes and output_res in self.nodes:
            x1, y1 = self.nodes[input_res]
            x2, y2 = self.nodes[output_res]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(QPen(QColor("#2ecc71"), 2))
            self.scene.addItem(line)

class SatisfactoryCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satisfactory Production Visualizer")
        self.setGeometry(100, 100, 1200, 800)

        self.layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.resource_label = QLabel("Sélectionnez la ressource:")
        self.resource_combo = QComboBox()
        self.resource_combo.addItems(PRODUCTION_RATIOS.keys())

        self.input_label = QLabel("Débit d'entrée (unités/min):")
        self.input_line = QLineEdit()
        
        self.calculate_button = QPushButton("Calculer")
        
        self.visualizer = ProductionVisualizer()

        self.layout.addWidget(self.resource_label)
        self.layout.addWidget(self.resource_combo)
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_line)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.visualizer)

        self.calculate_button.clicked.connect(self.calculate)

        self.setCentralWidget(self.container)

    def calculate(self):
        resource = self.resource_combo.currentText()
        try:
            input_rate = int(self.input_line.text())
            x, y = 50, 50
            previous_output = None
            for factory, (input_per_min, output_per_min, input_name, output_name) in PRODUCTION_RATIOS[resource].items():
                count = -(-input_rate // input_per_min)
                total_input = count * input_per_min
                total_output = count * output_per_min
                self.visualizer.add_factory_node(x, y, factory, input_name, output_name, total_input, total_output)
                if previous_output:
                    self.visualizer.connect_nodes(previous_output, output_name)
                previous_output = output_name
                x += 200
        except ValueError:
            print("Entrée invalide, veuillez saisir un nombre.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SatisfactoryCalculator()
    window.show()
    sys.exit(app.exec_())
