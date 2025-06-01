import json
import os

def estimate_2025_population(totpop2000, g_rate):
    """
    Estimate 2025 population using compound growth:
    P = P0 * (g_rate) ^ years
    where g_rate is an annual multiplier like 1.015
    """
    years = 25
    try:
        totpop2000 = float(totpop2000)
        g_rate = float(g_rate)
    except (ValueError, TypeError):
        return None

    projected = totpop2000 * (g_rate ** years)
    return round(projected)

def process_geojson(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for feature in data.get("features", []):
        props = feature.get("properties", {})

        # Ensure GEOCODE is correct
        correct_geocode = f"{int(props['PROV_KEY']):02}{int(props['DIST_NO']):02}{int(props['LLG_NO']):02}{int(props['WARD_NO']):02}{int(props['CU_NO']):03}"
        if props.get("GEOCODE") != correct_geocode:
            props["GEOCODE"] = correct_geocode
        
        # Prepare POP data
        pop = {}

        # 2000 Census
        pop["2000"] = {
            "TOTPOP": props.get("TOTPOP2000"),
            "MALEPOP": props.get("MALE2000"),
            "FEMALEPOP": props.get("FEMALE2000"),
            "SRC": "PNG 2000 National Census",
            "G_RATE": props.get("G_RATE")
        }

        # 2008 Projection
        pop["2008"] = {
            "TOTPOP": props.get("POP2008"),
            "SRC": f"Projection ({props.get('G_RATE')} growth rate)"
        }

        # 2025 Projection
        projected_totpop = estimate_2025_population(props.get("TOTPOP2000"), props.get("G_RATE"))
        if projected_totpop:
            male_share = float(props.get("MALE2000", 0)) / float(props.get("TOTPOP2000", 1))
            female_share = float(props.get("FEMALE2000", 0)) / float(props.get("TOTPOP2000", 1))
            pop["2025"] = {
                "TOTPOP": projected_totpop,
                "MALEPOP": round(projected_totpop * male_share),
                "FEMALEPOP": round(projected_totpop * female_share),
                "SRC": "Estimate based on PNG 2000 Census and annual compound growth using recorded G_RATE"
            }

        # Set POP property
        props["POP"] = pop

        # Clean up old population keys
        for key in ["TOTPOP2000", "MALE2000", "FEMALE2000", "POP2008", "G_RATE"]:
            if key in props:
                del props[key]

    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

