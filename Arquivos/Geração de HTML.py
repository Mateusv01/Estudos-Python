""" Como páginas web são arquivos de texto, podemos criá-las facilmente em Python"""
with open("index.html", "w", encoding="utf-8") as pagina:
    pagina.write("<DOCKTYPE html>\n")
    pagina.write("<html lang=\"pt-BR\">\n")
    pagina.write("<head>\n")
    pagina.write("<meta charset=\"utf-8\">\n")
    pagina.write("<title> Minha página com Python</title>")
    pagina.write("</head>\n")
    pagina.write("<body>\n")
    pagina.write("Olá!")
    for l in range(1):
        pagina.write(f"<p>{l}</p>\n")
    pagina.write("</body>\n")
    pagina.write("</html>\n")


""" Podemos usar as aspas triplas para melhorar nosso programa fazendo ele mais claro"""


with open("index.html", "w", encoding="utf-8") as página:
    página.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usando Python</title>
</head>
<body>
    Olá, Tudo bom? """)
    for l in range(10):
        página.write(f"<p>{l}</p>\n")
    página.write("""
</body>
</html>""")







