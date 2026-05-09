import json
import requests
import os

CATALOG_URL = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

KEY_MAP = {
    "Ability & Aptitude": "A",
    "Knowledge & Skills": "K",
    "Personality & Behavior": "P",
    "Simulations": "S",
    "Competencies": "C",
    "Biodata & Situational Judgment": "B",
    "Development & 360": "D"
}

class CatalogManager:
    def __init__(self):
        self.catalog = []
        self.name_to_item = {}
        self.load_catalog()

    def load_catalog(self):
        try:
            response = requests.get(CATALOG_URL)
            response.raise_for_status()
            # Use strict=False to handle potential invalid control characters in the JSON
            raw_data = json.loads(response.text, strict=False)
            self.catalog = self._process_catalog(raw_data)
            # Build index for fast lookup
            for item in self.catalog:
                self.name_to_item[item["name"].lower()] = item
        except Exception as e:
            print(f"Error loading catalog: {e}")
            # Fallback to local file if possible
            if os.path.exists("catalog.json"):
                with open("catalog.json", "r") as f:
                    self.catalog = self._process_catalog(json.load(f))
                    for item in self.catalog:
                        self.name_to_item[item["name"].lower()] = item

    def _process_catalog(self, data):
        processed = []
        for item in data:
            # Get the primary test type (first key mapped)
            test_type = "K"  # Default to Knowledge
            if item.get("keys"):
                for key in item.get("keys", []):
                    if key in KEY_MAP:
                        test_type = KEY_MAP[key]
                        break  # Use only the first/primary test type
            
            processed.append({
                "name": item.get("name", ""),
                "url": item.get("link", ""),
                "test_type": test_type,
                "description": item.get("description", ""),
                "keys_raw": ", ".join(item.get("keys", [])),
                "duration": item.get("duration", "—"),
                "languages": ", ".join(item.get("languages", []))
            })
        return processed

    def get_catalog_str(self):
        """Returns a compact string representation for the LLM context."""
        lines = []
        for i, item in enumerate(self.catalog):
            # Format: Name | Type: X | Keys: ... | Duration: ... | Languages: ... | URL: ... | Description: ...
            line = (
                f"{i+1}. {item['name']} | "
                f"Type: {item['test_type']} | "
                f"Keys: {item['keys_raw']} | "
                f"Duration: {item['duration']} | "
                f"Languages: {item['languages']} | "
                f"URL: {item['url']} | "
                f"Description: {item['description']}"
            )
            lines.append(line)
        return "\n".join(lines)

    def find_by_name(self, name):
        """Case-insensitive lookup of assessment by name."""
        return self.name_to_item.get(name.lower())

    def get_by_type(self, test_type: str):
        """Get all assessments of a specific type."""
        return [item for item in self.catalog if item["test_type"] == test_type]

if __name__ == "__main__":
    cm = CatalogManager()
    print(f"Loaded {len(cm.catalog)} items.")
    # Test lookups
    print("\n--- Sample Lookups ---")
    print(f"OPQ32r: {cm.find_by_name('Occupational Personality Questionnaire OPQ32r')}")
    print(f"Items of type 'P': {len(cm.get_by_type('P'))}")

