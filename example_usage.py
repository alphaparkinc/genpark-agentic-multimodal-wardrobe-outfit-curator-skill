from client import AgenticMultimodalWardrobeOutfitCurator

def main():
    curator = AgenticMultimodalWardrobeOutfitCurator()
    sample_wardrobe = [
        {"id": "w1", "name": "Oversized Linen Shirt", "category": "top", "type": "t-shirt", "color": "White"},
        {"id": "w2", "name": "Pleated Dress Trousers", "category": "bottom", "type": "trousers", "color": "Charcoal"},
        {"id": "w3", "name": "Derby Shoes", "category": "footwear", "type": "derbies", "color": "Black"}
    ]
    ctx = {"temp_c": 16.0, "precip_prob": 0.10, "occasion": "gallery_opening"}
    result = curator.curate_outfit(sample_wardrobe, ctx)
    print("--- GenPark Curated Outfit Output ---")
    print(f"Occasion: {result['occasion']} | Ambient Temp: {result['ambient_temp_c']}C")
    print(f"Harmony: {result['color_harmony']['style_palette']} (Score: {result['color_harmony']['harmony_score']})")
    print(f"Verdict: {result['readiness_verdict']}")
    for item in result['outfit_items']:
        print(f"  - [{item['category'].upper()}] {item['name']} ({item['color']})")

if __name__ == "__main__":
    main()
