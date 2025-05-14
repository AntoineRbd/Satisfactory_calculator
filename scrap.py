from pathlib import Path
import requests
from bs4 import BeautifulSoup, Tag
import re
import json
from typing import Dict, List, Tuple

machines: Dict[str, str] = {
    "constructor": "https://satisfactory.wiki.gg/wiki/Constructor",
    "assembler": "https://satisfactory.wiki.gg/wiki/Assembler",
    "foundry": "https://satisfactory.wiki.gg/wiki/Foundry",
    "manufacturer": "https://satisfactory.wiki.gg/wiki/Manufacturer",
    "packager": "https://satisfactory.wiki.gg/wiki/Packager",
    "refinery": "https://satisfactory.wiki.gg/wiki/Refinery",
    "blender": "https://satisfactory.wiki.gg/wiki/Blender",
    "particle_accelerator": "https://satisfactory.wiki.gg/wiki/Particle_Accelerator",
    "quantum_encoder": "https://satisfactory.wiki.gg/wiki/Quantum_Encoder",
    "converter": "https://satisfactory.wiki.gg/wiki/Converter"
}

def parse_ingredients(cell: Tag) -> List[Tuple[str, float]]:
    items: List[Tuple[str, float]] = []
    lines = list(cell.stripped_strings)
    i = 0
    print(f"====\nLine parse : {lines}")
    while i < len(lines):
        line = lines[i]
        print(f"Currently watched: {line}")
        match_qty = re.match(r"^([\d\.,]+)\s*/\s*min$", line, re.IGNORECASE)
        print(f"Check du if: match_qty = {match_qty}")
        if match_qty:
            qty_str = match_qty.group(1)
            item_name = lines[i - 1]
            try:
                qty = float(qty_str.replace(',', ''))
                print(f"Item name found: {item_name}")
                print(f"Quantity found: {qty}")
                items.append((item_name.title(), qty))
            except ValueError:
                pass
            i += 2
        else:
            i += 1
    return items

def scrape_machine_recipes(machine_name: str, url: str) -> Dict[str, Dict[str, List[Tuple[str, float]]]]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", class_="wikitable")

    recipes: Dict[str, Dict[str, List[Tuple[str, float]]]] = {}

    for table in tables:
        headers = [th.get_text(strip=True).lower() for th in table.find_all("th")]
        if not ("recipe" in headers and "ingredients" in headers and "products" in headers):
            continue

        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) < 3:
                continue

            recipe_name: str = cols[0].get_text(strip=True).title()
            inputs: List[Tuple[str, float]] = parse_ingredients(cols[1])
            outputs: List[Tuple[str, float]] = parse_ingredients(cols[3])
            recipes[recipe_name] = {
                "inputs": inputs,
                "outputs": outputs
            }

    return recipes

def main() -> None:
    base_path: Path = Path("machines/recipe")
    base_path.mkdir(parents=True, exist_ok=True)

    for machine, url in machines.items():
        try:
            data = scrape_machine_recipes(machine, url)
            output_file: Path = base_path / f"recipe_{machine}.py"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("RECIPES = ")
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"[OK] {machine.capitalize()} - {len(data)} recettes enregistrées dans {output_file}")
        except Exception as e:
            print(f"[ERREUR] pour {machine}: {e}")

if __name__ == "__main__":
    main()
