# Teste-Est-gio
Teste para estágio GPM

IMPORTANTE: antes de executar o código, é necessário inserir as informações de user e password para logar no mysql, caso contrário não será possível criar o banco de dados nem a tabela.

Optei em usar o Python para criar o programa To-do List como foi solicitado, bem como utilizar a integração com o banco de dados (utilizei MySQL) para maior facilidade e praticidade na manipulação dos dados.

Criei a aplicação utilizando Orientação a Objeto, onde o principal do código fica no arquivo principal.py, no arquivo menu.py ocorre a instanciação do objeto, que será utilizado para passar informações obtidas por meio dos inputs para os métodos da classe List no arquivo principal.py.

Usei if/elif/else para executar ações de acordo com o que o usuário digitar, bem para impedi-lo de inserir tarefas com os campos vazios.

Tentei gerar um alert no windows que disparasse de acordo com o dia e horário da tarefa, mas não encontrei bibliotecas que aceitassem a data(ex:17/12) e o horário (14:11) e que soltassem o alerta apenas uma vez. Tentei por meio do método datetime do python estabelecendo comparação entre a data atual e a data inserida, mas o alerta não apareceu, então optei por deixar sem.


