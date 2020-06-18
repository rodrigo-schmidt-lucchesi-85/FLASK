# Leve Capital

​																		   Processo de Recrutamento

---

Instalação: Com o seu ambiente de desenvolvimento favorito (PipEnv,Conda,...), utilize o instalador pip para salvar os requisitos no arquivo requirements.txt:

```bash
pip install requirements.txt
```

O diretório raiz da aplicação está dividido nos seguintes arquivos:

    ├── api.py  # Arquivo com as Rotas para a API REST
    ├── db.sqlite  # Banco de dados SQL (Sqlite3)
    ├── __pycache__
    │   └── api.cpython-38.pyc
    ├── README.md   # Arquivo com a explicação do software
    └── requirements.txt  # Arquivo texto com as bibliotecas requeridas para o funcionamento da API

---

## Rotas

|                      | GET                                                          | POST         | PUT                                                     | DELETE                   |
| -------------------- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------- | ------------------------ |
| /users               | mostra todos os usuários                                     | ---          | ---                                                     | ---                      |
| /users/<cpf>         | mostra um usuário por CPF                                    | ---          | ---                                                     | ---                      |
| /users/create        | ---                                                          | cria usuário |                                                         |                          |
| /users/delete/<cpf>  | ---                                                          | ---          | ---                                                     | Deleta o usuário por cpf |
| /users/update/<cpf>  | ---                                                          | ---          | faz o update dos dados de um usuário, buscando pelo cpf | ---                      |
| /salaries            | Pega todos os salários existentes no db                      |              |                                                         |                          |
| /salaries/<cpf>      | Busca o histórico dos salários de um usuário, por cpf        | ---          | ---                                                     | ---                      |
| /salaries/mean_value | Calcula os valores médios (salário e desconto) de todos os usuários | ---          | ---                                                     | ---                      |
| /salaries/max_value  | Calcula o valor máximo de todos os usuários existentes       | ---          | ---                                                     | ---                      |
| --- new routes ?     | ---                                                          | ---          | ---                                                     | ---                      |
|                      | ---                                                          | ---          | ---                                                     | ---                      |
|                      |                                                              |              |                                                         |                          |
|                      |                                                              |              |                                                         |                          |
|                      |                                                              |              |                                                         |                          |

## Bancos de Dados

Usuário:

- username: Nome do usuário

- cpf: cpf do usuário

- birthday_year: ano de nascimento do usuário



Salário:

- date: data de registro

- cpf: cpf do usuário

- salary: salario registrado do CPF

- discount : disconto atribuido ao salario do CPF

