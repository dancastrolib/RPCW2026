# TPC1 — Geração de Ontologia a partir de um dataset JSON

**Data:** 2026-02-03

## Objetivo
- Especificar um modelo ontológico para representar listas de compras em JSON (classes, atributos e relações).
- (Opcional) Representar o modelo em OWL/RDF (Turtle) e/ou gerar instâncias a partir do dataset.

## Descrição do trabalho
O dataset é constituído por uma lista de listas de compras. Cada lista tem uma designação, uma data e um conjunto de produtos, onde cada produto inclui designação, categoria e quantidade (valor + unidade).

## Modelo ontológico (resumo)
- **Classes:** ListaDeCompras, ItemDeCompra, Produto, Categoria, Quantidade, Unidade
- **Relações:** temItem, refereProduto, temCategoria, temQuantidade, temUnidade
- **Atributos:** designacaoLista, data, designacaoProduto, designacaoCategoria, valor

## Ficheiros
- `README.md` — manifesto do TPC
- `ontologia.ttl` — ontologia em OWL/Turtle (se aplicável)
- `dataset.json` — dataset de entrada (se aplicável)
- `script.py` — geração de instâncias/transformação (se aplicável)

## Como executar (se aplicável)
```bash
# exemplo
python script.py
