def detect_mine(data: dict) -> str:
    metal_detected = data.get("metal", 0) > 300
    magnetic_variation = data.get("magnetic_field", 0) > 100
    gas_detected = data.get("gas", 0) > 400
    distance = data.get("distance", 100)

    if metal_detected and magnetic_variation:
        if distance < 20:
            return "Mine détectée"
    return "Aucune mine"                                                                                                                            