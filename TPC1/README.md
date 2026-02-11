# TPC1 — Geração de Ontologia a partir de um dataset JSON

**TPC:** 1

**Data:** 2026-02-03


## Resumo
Modelo ontológico + instância do manifesto + geração automática do README a partir de RDF.


## Descrição
Especificação de uma ontologia para listas de compras e geração automática do manifesto.


## Ficheiros
- **Ontologia do manifesto** — `TPC1/manifesto.ttl`
- **Script Python gerador do README** — `TPC1/gera_readme.py`


## Como executar
```bash
python3 gera_readme.py manifesto.ttl manifesto_tpc1.ttl README.md 
```
