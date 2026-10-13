#!/usr/bin/env python3
import json
import sys
from client import AgenticMultimodalWardrobeOutfitCurator

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        curator = AgenticMultimodalWardrobeOutfitCurator()
        sample_wardrobe = [
            {"id": "w1", "name": "Merino Wool Turtleneck", "category": "top", "type": "thermal_sweater", "color": "Navy"},
            {"id": "w2", "name": "Chino Trousers", "category": "bottom", "type": "chinos", "color": "Beige"},
            {"id": "w3", "name": "Chelsea Leather Boots", "category": "footwear", "type": "boots", "color": "Black"},
            {"id": "w4", "name": "Technical Trench Coat", "category": "outerwear", "type": "heavy_coat", "color": "Khaki"}
        ]
        ctx = {"temp_c": 12.0, "precip_prob": 0.45, "occasion": "business_casual"}
        res = curator.curate_outfit(sample_wardrobe, ctx)
        assert res["readiness_verdict"] in ["APPROVED_STYLE_FIT", "COMPLEMENTARY_UPSELL_RECOMMENDED"]
        assert len(res["outfit_items"]) >= 3
        print(f"[TEST PASS] Wardrobe Outfit Curated: {res['color_harmony']['style_palette']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-wardrobe-outfit-curator", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "curate_outfit", "description": "Curate capsule wardrobe outfit for weather & occasion"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                curator = AgenticMultimodalWardrobeOutfitCurator()
                out = curator.curate_outfit(args.get("wardrobe", []), args.get("context", {}))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
