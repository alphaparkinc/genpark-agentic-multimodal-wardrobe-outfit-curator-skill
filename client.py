"""
AI Multimodal Wardrobe & Capsule Outfit Curator (Zero External Dependencies)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
import json
import math
from typing import Dict, Any, List

class AgenticMultimodalWardrobeOutfitCurator:
    NEUTRAL_COLORS = {"black", "white", "grey", "gray", "navy", "beige", "denim", "khaki"}
    WARM_COLORS = {"red", "orange", "yellow", "burgundy", "coral", "camel"}
    COOL_COLORS = {"blue", "green", "purple", "teal", "olive", "lavender"}

    def __init__(self, brand_name: str = "GenPark Style Copilot"):
        self.brand_name = brand_name

    def evaluate_weather_suitability(self, temp_c: float, precip_prob: float, garment_layer: str) -> float:
        score = 1.0
        if temp_c < 10.0 and garment_layer in ["t-shirt", "shorts", "sandals"]:
            score -= 0.6
        elif temp_c < 15.0 and garment_layer in ["heavy_coat", "thermal_sweater", "boots"]:
            score += 0.2
        elif temp_c > 25.0 and garment_layer in ["heavy_coat", "wool_blazer", "thermal_sweater"]:
            score -= 0.7
        if precip_prob > 0.4 and garment_layer in ["suede_shoes", "silk_shirt"]:
            score -= 0.5
        return max(0.1, min(1.0, score))

    def evaluate_color_harmony(self, colors: List[str]) -> Dict[str, Any]:
        normalized = [c.lower().strip() for c in colors]
        neutral_count = sum(1 for c in normalized if c in self.NEUTRAL_COLORS)
        warm_count = sum(1 for c in normalized if c in self.WARM_COLORS)
        cool_count = sum(1 for c in normalized if c in self.COOL_COLORS)
        total = max(1, len(normalized))
        
        if neutral_count >= 1 and (warm_count == 0 or cool_count == 0):
            style = "Harmonious Monochromatic / Balanced Neutral"
            harmony_score = 0.95
        elif neutral_count >= 2:
            style = "Minimalist Classic Neutral"
            harmony_score = 0.90
        elif warm_count > 0 and cool_count > 0:
            style = "Bold High-Contrast Complementary"
            harmony_score = 0.75
        else:
            style = "Cohesive Tonal"
            harmony_score = 0.85
            
        return {
            "style_palette": style,
            "harmony_score": harmony_score,
            "neutral_ratio": round(neutral_count / total, 2)
        }

    def curate_outfit(self, wardrobe: List[Dict[str, Any]], context: Dict[str, Any]) -> Dict[str, Any]:
        temp_c = float(context.get("temp_c", 20.0))
        precip_prob = float(context.get("precip_prob", 0.1))
        occasion = context.get("occasion", "smart_casual").lower()
        
        selected_items = []
        categories_needed = ["top", "bottom", "footwear", "outerwear" if temp_c < 18.0 else None]
        categories_needed = [c for c in categories_needed if c]
        
        for cat in categories_needed:
            candidates = [item for item in wardrobe if item.get("category") == cat]
            if candidates:
                best_item = max(
                    candidates,
                    key=lambda x: self.evaluate_weather_suitability(temp_c, precip_prob, x.get("type", ""))
                )
                selected_items.append(best_item)
                
        colors = [item.get("color", "black") for item in selected_items]
        harmony = self.evaluate_color_harmony(colors)
        
        missing_complements = []
        if len(selected_items) < len(categories_needed):
            present_cats = {item.get("category") for item in selected_items}
            for cat in categories_needed:
                if cat not in present_cats:
                    missing_complements.append({
                        "category": cat,
                        "suggested_type": "waterproof_trench" if precip_prob > 0.3 else "minimalist_blazer",
                        "suggested_color": "Navy" if harmony["neutral_ratio"] < 0.5 else "Camel",
                        "curator_note": "Recommended add-on to elevate occasion elegance."
                    })
                    
        return {
            "curator_engine": self.brand_name,
            "occasion": occasion,
            "ambient_temp_c": temp_c,
            "outfit_items": selected_items,
            "color_harmony": harmony,
            "missing_complements": missing_complements,
            "readiness_verdict": "APPROVED_STYLE_FIT" if not missing_complements else "COMPLEMENTARY_UPSELL_RECOMMENDED",
            "curation_summary": f"Curated {len(selected_items)} pieces tailored for {occasion} under {temp_c}°C."
        }
