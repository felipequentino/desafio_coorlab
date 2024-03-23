# Resultado - Desáfio CoorLab

Olá.

Primeiro, vamos as dependências que eu instalei:

- Primevue: para o calendário, ícones e botões da página;
- Flask: para a API do backend, como este projeto é relativamente pequeno, decidir usar o Flask ao invés de Django (que é indicado para projetos maiores e mais escalonáveis);

Explicação do backend/app.py:

- O propósito do código backend/app.py é criar uma aplicação Flask que fornece uma API para recuperar dados do data.json, e disponibilizar esses dados no endpoint api/items, isso por meio de um servidor web local (porta 3000), suportando requisições CORS.

Explicação do frontend/src/components:

- Quis "desmembrar" cada parte do site mostrado no doc/prototype.mp4 em componentes, tendo no total 4 componentes: um para uma simples SideBar (Sidebar.vue), um que recebe os items do endpoint api/items (ItemManagement.vue), um que template de Card (ItemCard.vue) e por último, um component que faz a procura dos dados por meio dos filtros dos Destinos das viagens, contendo também um simples calendário e o botão de limpar para apagar o filtro (CityFilter.vue);
- No App.vue, basicamente eu só estou juntando os components e ajeitando o CSS da página;
- Como os componentes são relativamente simples, decidi estilizar o CSS de cada um deles no próprio arquivo;
- Implementei uma media-querie para visualização para celulares com largura de até 600px.
- Instalei a biblioteca Primevue para importar botões mais bonitos, alguns ícones e um calendário.
