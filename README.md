# ✅ API de Gerenciamento de Tarefas com Flask

Este projeto é uma **API RESTful** simples desenvolvida em **Python usando Flask**. Ela permite **criar, visualizar, editar e deletar tarefas** utilizando os métodos HTTP `GET`, `POST`, `PUT` e `DELETE`.

---

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/nicolasandreos/REST-API
cd API-REST
````

2. Instale as dependências (se necessário):

```bash
pip install flask
```

3. Execute a aplicação:

```bash
python app.py
```

A API estará disponível em:
📍 `http://localhost:5000/tarefas`

---

## 📌 Rotas da API

### 🔍 `GET /tarefas`

Retorna todas as tarefas armazenadas.

**Resposta:**

```json
[
  {
    "id": 1,
    "titulo": "Estudar Flask",
    "concluida": false
  }
]
```

---

### ➕ `POST /tarefas`

Adiciona uma ou mais tarefas.

**Corpo da Requisição:**

```json
[
  {
    "id": 1,
    "titulo": "Estudar Flask",
    "concluida": false
  }
]
```

**Resposta:**

```json
{ "mensagem": "Nova tarefa adicionada com sucesso!" }
```

---

### 🔍 `GET /tarefas/<id>`

Retorna os dados de uma tarefa específica.

**Exemplo:**
`GET /tarefas/1`

---

### ✏️ `PUT /tarefas/<id>`

Edita uma tarefa com o ID especificado.

**Corpo da Requisição:**

```json
{
  "titulo": "Estudar Flask e FastAPI",
  "concluida": true
}
```

**Resposta:**

```json
{ "mensagem": "Tarefa atualizada com sucesso!" }
```

---

### 🗑️ `DELETE /tarefas/<id>`

Remove uma tarefa com o ID especificado.

**Resposta:**

```json
{ "mensagem": "Tarefa deletada com sucesso!" }
```

---

## 💡 Tecnologias Utilizadas

* Python 3
* Flask (micro framework para APIs)
* JSON (para troca de dados)

---

## 📚 Requisitos

* Python 3.7 ou superior
* Biblioteca Flask:

```bash
pip install flask
```

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.

```

Se quiser, posso gerar esse `README.md` como arquivo para download. Deseja isso?
```
