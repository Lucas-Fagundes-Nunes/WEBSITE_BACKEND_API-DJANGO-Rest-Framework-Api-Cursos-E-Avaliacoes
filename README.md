# API Django Framework Cursos e Avaliações


> Sistema desenvolvido para aprendizado, com django rest framework, utilizando os métodos GET, POST, PUT e DELETE, para os modelos cursos e avaliações dos cursos.

### URLS
Foram desenvolvidas no curso, 2 versões, para aprender a lidar com versões, fazem as mesmas requisições, porem na versão 1 foi utilizado o generics e na versão 2, foi utilizado o viewsets. 


* /api/v2/cursos/ - GET, POST utilizado para buscar todos os cursos e cadastrar cursos;
* /api/v2/cursos/1/ - GET, PUT, DELETE utilizado para buscar apenas 1 curso, e atualizar e deletar o curso; 
* /api/v2/avaliacoes/ - GET, POST utilizado para buscar todas as avaliações e cadastrar avaliações;
* /api/v2/avaliacoes/1/ - GET, PUT, DELETE utilizado para buscar apenas 1 avaliação, e atualizar e deletar a avaliação;  
* /api/v2/cursos/1/avaliacoes/ - GET utilizado para buscar todas as avaliações relacionadas ao curso;
* /api/v2/cursos/1/avaliacoes/2/ - GET, PUT, DELETE utilizado para buscar apenas 1 avaliação relacionada ao curso selecionado da URL, atualizar e deletar as avaliações;


### Models

##### Avaliações
* Curso - nome do curso;
* Nome - Nome da pessoa que avaliou o curso;
* Email - de quem avaliou o curso;
* Avaliação - Avaliação de 1 á 5;
* Criação - Dia em que foi enviado a avaliação;
* Atualização - Dia em que foi atualizado a avaliação;
* Ativo - Caso não queira que apareça a avaliação;

##### Cursos
* Título - Título do curso;
* URL - URL onde está o curso;
* Criação - Dia em que foi adicionado o curso;
* Atualização - Dia em que foi atualizado o curso;


### Autenticação
Como autenticação foi utilizado o formato Token ao invés de Session, para trazer mais para como será usado no dia a dia pelas aplicações.

##### > Restrição Cursos: 
* GET: Apenas usuários com token;
* POST: Apenas usuário que tenham permissão pelo Django ( DjangoModelPermissions );
* PUT: Apenas usuário que tenham permissão pelo Django ( DjangoModelPermissions );
* DELETE: Apenas Super usuário;

##### > Restrição Avaliação: 
* GET: Todos os usuários;
* POST: Apenas usuários com token;
* PUT: Apenas usuários com token;
* DELETE: Apenas usuários com token;

### Linguagem, Bibliotecas, Frameworks
* Python;
* Django;
* Django Rest Framework;
* Django_filters;
* Avg;