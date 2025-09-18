# A* Product Recommendation (Python)

Lightweight prototype that uses an A* search variant to recommend a path between products where the heuristic is product conversion probability (higher conversion → lower heuristic cost). Intended as a demonstration of using search algorithms for recommendation/ranking experiments.

## Features
- Simple `Produto` model with `nome`, `categoria`, `prob_Conversao`.
- `RecomendacaoAEstrela` implements A*-style search across a fully-connected product graph.
- Heuristic = negative conversion probability (higher conversion approximates lower cost).
- Minimal dependencies (std lib only — `heapq`).

## File
- `recomendacao.py` — implementation and example usage (script guarded with `if __name__ == "__main__":`).

## Quick start

```bash
# run the example
python recomendacao.py
```
## Expected CLI output (example):

```
Produtos criados:
- AirPods Pro 2ª Geração (Áudio) - Conversão: 85%
- Laptop Gamer ASUS ROG Strix G15 (Computadores) - Conversão: 45%
- Impressora 3D Creality Ender-3 S1 Pro (Impressão 3D) - Conversão: 15%

Caminho recomendado do AirPods Pro 2ª Geração para Impressora 3D Creality Ender-3 S1 Pro:
AirPods Pro 2ª Geração → Impressora 3D Creality Ender-3 S1 Pro
```

## Design Notes & Limitations

- The graph is fully connected with uniform transition cost (`1`). This is only a placeholder; real systems should derive costs from domain-specific signals such as co-purchases, similarity, or embeddings.
- The heuristic is defined as the negative conversion probability, which prioritizes high-conversion products. However, this heuristic is not guaranteed to be admissible, so the algorithm may not always return an optimal path.
- `Produto` objects are compared by identity. For production use, unique identifiers and proper equality/hash methods are recommended.
- This is a prototype for demonstration and learning purposes, not a production-ready recommendation engine.

## Complexity

- In a fully connected graph of `N` products, there are \~`N²` edges.
- The A\* search processes nodes using a priority queue (`heapq`), giving a worst-case time complexity of **O(N² log N)**.
- Space complexity is also **O(N²)** due to the adjacency representation.

⚠️ This means that for a small online store, the system would be extremely fast, but for a store with millions of products, performance would drop drastically.

