# genpark-agentic-multimodal-wardrobe-outfit-curator-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

AI Multimodal Wardrobe & Capsule Outfit Curator. Aligns digital wardrobe inventories with real-time weather forecasts, occasion formality constraints, and color harmony models (monochromatic, complementary, neutral anchors) to curate optimal daily looks and recommend missing complementary items for seamless one-click commerce checkout.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
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

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
