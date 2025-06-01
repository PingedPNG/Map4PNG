import os
import json

# Directory containing all the nested folders with individual geojsons
root_dir = "../data/villages_by_prov_dist_llg_ward"
output_file = "../build/all_villages.geojson"
os.makedirs("../build", exist_ok=True)
merged = {
    "type": "FeatureCollection",
    "features": []
}

# Walk through all subdirectories
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".geojson"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("type") == "FeatureCollection":
                    merged["features"].extend(data.get("features", []))

# Write merged output
with open(output_file, "w", encoding="utf-8") as out:
    json.dump(merged, out, ensure_ascii=False, indent=2)

print(f"Merged GeoJSON saved to: {output_file}")
