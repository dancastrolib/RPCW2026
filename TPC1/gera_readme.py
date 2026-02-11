#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from rdflib import Graph, Namespace
from rdflib.namespace import RDF

NS = Namespace("http://www.di.uminho.pt/rpcw2026/manifesto#")

def get_literal(g, s, p):
    vals = list(g.objects(s, p))
    return str(vals[0]) if vals else ""

def main():
    if len(sys.argv) != 4:
        print("Uso: python3 gera_readme.py <instancia.ttl> <ontologia.ttl> <output.md>")
        sys.exit(1)

    inst_path = sys.argv[1]
    onto_path = sys.argv[2]
    out_path  = sys.argv[3]

    g = Graph()
    g.parse(onto_path, format="turtle")
    g.parse(inst_path, format="turtle")

    manifesto = next(g.subjects(RDF.type, NS.Manifesto))
    trabalho  = next(g.objects(manifesto, NS.manifestoDe))

    titulo = get_literal(g, manifesto, NS.titulo)
    data = get_literal(g, manifesto, NS.data)
    resumo = get_literal(g, manifesto, NS.resumo)

    numero = get_literal(g, trabalho, NS.numero)
    descricao = get_literal(g, trabalho, NS.descricao)

    recursos = []
    for r in g.objects(trabalho, NS.temRecurso):
        nome = get_literal(g, r, NS.nome)
        caminho = get_literal(g, r, NS.caminho)
        recursos.append((nome, caminho))

    comandos = []
    for c in g.objects(trabalho, NS.temComando):
        texto = get_literal(g, c, NS.texto)
        comandos.append(texto)

    md = []
    md.append(f"# {titulo}")
    md.append(f"\n**TPC:** {numero}")
    md.append(f"\n**Data:** {data}")

    if resumo:
        md.append("\n\n## Resumo")
        md.append(resumo)

    md.append("\n\n## Descrição")
    md.append(descricao)

    md.append("\n\n## Ficheiros")
    for nome, caminho in recursos:
        md.append(f"- **{nome}** — `{caminho}`")

    if comandos:
        md.append("\n\n## Como executar")
        md.append("```bash")
        for cmd in comandos:
            md.append(cmd)
        md.append("```")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print("README gerado com sucesso.")

if __name__ == "__main__":
    main()
