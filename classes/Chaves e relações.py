""" Veremos conceitos mais avançados que permitiram trabalhar com várias tabelas. Para selecionarmos nossos registros
vimos que precisamos contruir expressões lógicas que indentificam ou que permitam a seleção desses registros
No caso da agenda, o campo NOME foi usada nas expressões, mas ultilzar dados como critério de seleção não é
uma boa ideia a longo termo. Dados podem mudar e se repetir em várias tabela.

Imagine a situação em que nossa agenda teria vários telefones por pessoa 

    nome   |   número  |  tipo 
 
Mateus          1234-65    celular
Mateus          2345-32    residencial

Nesse exemplo, poderiamos simplismente adicionar dois registros com o mesmo nome, mas estariamos complicando nosso trabalho
mais tarde, pois, se quiséssemos mudar o número de telefone de um dos registros, não poderiamos usar apenas nome = "Mateus"
sendo preciso uma condição composta

Esse problema poderia ser resolvido adicionando-se uma chave que indentificasse cada pessoa de forma única. Essa chave pode ser 
um simples número, desde que único, vamos chamar de indentificador ou id

id  |   nome   |   número  |  tipo 
 
1       Mateus     1234-65    celular
1      Mateus      2345-32    residencial


Embora nossos dados estejam em melhor forma, ainda estamos repetindo o campo nome várias vezes. E o campo ID não se indentifica unicamente
em cada registro

Uma melhor forma de representar esses dados é dividindo nossos dados em várias tabelas. Por exemplo, uma tabela para nome e outra para o
telefone como:


id  |  nome
1      Mateus

id_nome  |   número  |  tipo 
    1       1234-65     Casa
    1       2345-32     Celular


dessa forma, armazenamento o nome em apenas um lugar. Ainda temos outros problemas, pois agora nossos telefones não possuem um indentificador
único 

id  |  id_nome  |  número  |  tipo
1         1        1234-65     Casa 
2         1        2345-32     Celular

Assim, uma chave primária é um campo de um registro que o indentifica de forma única na tabela. Resolvemos o problema de redundancia
mas para acessar os dados precisamos usar o comando select

    select * from nomes, telefones where nomes.id = telefones.id_nomes

Esse comando difere de nossos outros exemplos por ultilizar mais de uma tabela após a cláusula from
É esse relacionamento que é especificado em nomes.id = telefones.id_nomes, ou seja, especificamos um critério que liga
as duas tabelas; 

id  |  id_nome  |  número  |    id_tipo     | 
1         1        1234-65         1 
2         1        2345-32         2

id  |  descrição
1     Celular
2     Casa

Vejamos os comandos SQL para cirar essas tabelas:

create table tipos(id integer primary key autoincrement,
                    descrição text);
create table tipos(id integer primary key autoincrement,
                    nome text);
create table tipos(id integer primary key autoincrement,
                    id_nome integer, número text,
                    id_tipo integer);

    Com o uso do primary key autoincrement, o SQLite vai ser encarregado de criar os números que vamos usar nas chaves 
"""