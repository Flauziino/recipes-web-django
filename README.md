# Projeto web simples utilizando Django

Um projeto simples em Django Web Framework 4.2.11 com o intuito de demonstrar o nível de habilidade, com foco na organização das pastas, cobertura de testes (100%), uso de classes based views e realização do deploy.

## Conteúdo geral do projeto

O projeto conta com APPs para autores, receitas e tags. O app de tag em si foi criado apenas para ser atrelado às receitas, então seus testes estão dentro do mesmo.

Dentro do app de autores, o único model utilizado foi o de perfil, contendo o Nome do autor (OneToOneField para o model User do próprio Django) e uma bio.

Dentro do app de receitas, tem-se dois modelos: o de categoria, que contém apenas o nome da mesma, e o modelo de receita, que contém título, descrição, slug, tempo de preparação, unidade de tempo de preparação, porções, unidade de porção (pedaços, pessoas, etc.), passo-a-passo da preparação da receita, data de criação, data de atualização, se está publicado ou não, capa (imagem para fazer referência à receita), categoria (sendo uma chave estrangeira para o modelo de categoria), autor (chave estrangeira para o modelo User do Django) e tags (uma ManyToMany) para o modelo de tag.

Por fim, temos o modelo das tags, dentro do app de tag, que contém apenas um nome e uma slug.

+ ### Dentro do app de autores

Dentro do app de autores, é possível a realização de cadastro, login, logout e a criação do perfil. Além disso, tem-se acesso à dashboard (acessível apenas se estiver logado), onde é possível visualizar as suas receitas criadas, criar novas receitas, editar as receitas ou, finalmente, apagá-las.

+ ### Dentro do app de receitas

Dentro do app de receitas, é possível visualizar a lista total de receitas (por página), visualizar apenas uma receita selecionada por ID, visualizar a categoria e, finalmente, realizar pesquisas que filtram por conteúdo do título ou da descrição da receita.

## Considerações finais

O sistema fornece uma interface simples e eficiente para as atividades de criação de usuário, login, logout, dashboard onde é possível visualizar, editar, criar e apagar receitas com facilidade.

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas ao abrir uma issue.

Autor: Flauziino - Desenvolvedor
