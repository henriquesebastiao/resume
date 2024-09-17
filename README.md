# Resume 📃

Um CLI simples para gerar resumos de apostilas PDF com a API do OpenAI.

## Executando

Clone o repositório:

```bash
git clone https://github.com/henriquesebastiao/resume
cd resume
```

Crie um arquivo `.env` com a sua chave de API do OpenAI como o exemplo em [.env.example](.env.example)

Crie um ambiente virtual e instale as dependências com [Poetry](https://python-poetry.org/):

```bash
python -m venv venv
poetry install && poetry shell
```

Execute o CLI com para obter a mensagem de ajuda com:

```bash
poetry run resume
```
