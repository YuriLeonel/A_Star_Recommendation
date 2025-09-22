# A* Product Recommendation (Python)

Lightweight prototype that uses an A* search variant to recommend a path between products where the heuristic is product conversion probability (higher conversion → lower heuristic cost). Intended as a demonstration of using search algorithms for recommendation/ranking experiments.

## Features
- Simple `Product` model with `name`, `category`, `conversion_prob`.
- `AStarRecommendation` implements A*-style search across a fully-connected product graph.
- Heuristic = negative conversion probability (higher conversion approximates lower cost).
- Minimal dependencies (std lib only — `heapq`).

## File
- `produtos_eletronicos.py` — implementation and example usage (script guarded with `if __name__ == "__main__":`).

## Quick start

```bash
# run the example
python produtos_eletronicos.py
```
## Expected CLI output (example):

```
Products created:
- AirPods Pro 2nd Generation (Audio) - Conversion: 85%
- ASUS ROG Strix G15 Gaming Laptop (Computers) - Conversion: 45%
- Creality Ender-3 S1 Pro 3D Printer (3D Printing) - Conversion: 15%

Recommended path from AirPods Pro 2nd Generation to Creality Ender-3 S1 Pro 3D Printer:
AirPods Pro 2nd Generation → ASUS ROG Strix G15 Gaming Laptop → Creality Ender-3 S1 Pro 3D Printer
```

## Design Notes & Limitations

- The graph is fully connected with uniform transition cost (`1`). This is only a placeholder; real systems should derive costs from domain-specific signals such as co-purchases, similarity, or embeddings.
- The heuristic is defined as the negative conversion probability, which prioritizes high-conversion products. However, this heuristic is not guaranteed to be admissible, so the algorithm may not always return an optimal path.
- `Product` objects are compared by identity. For production use, unique identifiers and proper equality/hash methods are recommended.
- This is a prototype for demonstration and learning purposes, not a production-ready recommendation engine.

## Complexity

- In a fully connected graph of `N` products, there are \~`N²` edges.
- The A\* search processes nodes using a priority queue (`heapq`), giving a worst-case time complexity of **O(N² log N)**.
- Space complexity is also **O(N²)** due to the adjacency representation.

⚠️ This means that for a small online store, the system would be extremely fast, but for a store with millions of products, performance would drop drastically.
