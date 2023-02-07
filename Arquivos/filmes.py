""" Gerando uma página a partir de um dicionário"""


filmes = {
    "Drama": ["Superação: O milagre de fé", "Até o último homem"],
    "Comédia": ["Cidade perdida", "Minions 2: a origem", "Free guy: assumindo o controle"],
    "Animação": ["Lightyear", "Gato de Botas 2: O Último Pedido", "Homem-Aranha no Aranhaverso"],
    "Ação": ["Trem-Bala", "Adão Negro", "Uncharted: Fora do Mapa"]
}

pagina = open("filmes.html", "w", encoding="utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
    pagina.write(f"<h1>{c.capitalize()}</h1>")
    pagina.write("<ul>")
    for e in v:
        pagina.write(f"<li>{e}</li>")
    pagina.write("</ul>")
pagina.write("""
</body>
</html>
""")
pagina.close()

