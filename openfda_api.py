import requests

def extract_fda_info(drug_name, limit=1):
    url = "https://api.fda.gov/drug/label.json"
    params = {
        "search": f"openfda.brand_name:{drug_name}",
        "limit": limit
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    results = response.json().get("results", [])
    if not results:
        return None

    entry = results[0]
    return {
        "warnings": entry.get("warnings", ["Not found"])[0],
        "reactions": entry.get("adverse_reactions", ["Not found"])[0],
        "usage": entry.get("indications_and_usage", ["Not found"])[0],
    }
