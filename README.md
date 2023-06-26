<h2>Para rodar o projetos</h2>

Numa máquina que possuo Docker:

- No terminal digite o comando:
  - ```commandline
    docker-compose up -d
    ```

O frontend estará rodando no link: http://localhost:5173/

O backend estará rodando no link: http://localhost:8000/

- É possível acessar o admin do Django pelo link http://localhost:8000/admin
- As credenciais de acesso são admin e admin, como login e senha.

O CLI do RabbitMQ estará rodando no link: http://localhost:15672/

- Você poderá logar utilizando as credenciais admin e mypass, como login e senha respectivamente.

O Flower - Sistema de monitoração de fila estará rodando no link: http://localhost:5555

<h4>Rotas disponívels</h4>
URL: http://localhost:8000/api/v1/proposals/<br>
Método: GET<br>
Descrição: Retorna lista das propostas feitas.<br>
Exemplo de retorno:<br>

```json
[
  {
    "value": 12.0,
    "accepted": false,
    "user": {
      "name": "Willian Ribeiro dos Santos",
      "cpf": "teste",
      "address": "QE 44 CONJUNTO I CASA 10"
    }
  },
  {
    "value": 17.0,
    "accepted": true,
    "user": {
      "name": "Willian Ribeiro dos Santos",
      "cpf": "teste",
      "address": "QE 44 CONJUNTO I CASA 10"
    }
  }
]
```

URL: http://localhost:8000/api/v1/proposals/<br>
Método: POST<br>
Descrição: Envia nova proposta sem uso do sistema de filas <br>
Body:

```json
{
  "value": 4,
  "user": {
    "name": "4",
    "cpf": "4",
    "address": "4"
  }
}
```

URL: http://localhost:8000/api/v1/proposals/celery<br>
Método: POST<br>
Descrição: Envia nova proposta utilizando sistema de filas <br>
Body:

```json
{
  "value": 4,
  "user": {
    "name": "4",
    "cpf": "4",
    "address": "4"
  }
}
```

Exemplo de retorno:

```json
{
  "proposal": "18c60fca-b073-49d1-a755-5ad852accb85"
}
```
