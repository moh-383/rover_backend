# app/services/detection.py

def detect_mine(data: dict) -> str:
    """
    Détecte une mine si certaines conditions sont remplies.
    """
    metal_detected = data.get("metal") > 300  # seuil fictif, à ajuster
    magnetic_variation = data.get("magnetic_field") > 100  # seuil fictif
    gas_detected = data.get("gas") > 400  # seuil fictif
    distance = data.get("distance")

    if metal_detected and magnetic_variation:
        if distance < 20:  # proche du sol
            return "Mine détectée"
    return "Aucune mine"
