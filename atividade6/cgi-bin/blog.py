#!/usr/bin/env python3
import os
from urllib.parse import parse_qs
from datetime import datetime

qs = os.environ.get("QUERY_STRING", "")
dados = parse_qs(qs, encoding="latin-1")

if "autor" in dados and "mensagem" in dados:
    autor = dados["autor"][0]
    msg = dados["mensagem"][0]

    data = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    f = open("posts.txt", "a", encoding="latin-1")
    f.write(autor + "|" + msg + "|" + data + "\n")
    f.close()

print("Content-type: text/html;charset=utf-8")
print()

print("<html><head><title>Blog CGI</title></head><body>")

if os.path.exists("posts.txt"):
    f = open("posts.txt", "r", encoding="latin-1")
    linhas = f.readlines()
    f.close()
    
    for linha in reversed(linhas):
        partes = linha.strip().split("|")
        if len(partes) == 3:
            print("<p>Autor: " + partes[0] + " |Mensagem: " + partes[1] + " | Timestamp " + partes[2] + "</p>")

print("</body></html>")