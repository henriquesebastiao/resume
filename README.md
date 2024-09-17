# Resume 📃

Um CLI simples para gerar resumos em Markdown de apostilas PDF com a API do OpenAI.

O processo de geração do resumo leva um certo tempo, conforme a quantidade de páginas no ducmento PDF. Umas apostila com 84 páginas leva cerca de 6 minutos para ser resumida:

![2024-09-16_20-07](https://github.com/user-attachments/assets/31b3fe92-44c2-4ce5-a273-deeb8d1c7d33)

> É importante ressaltar que a geração do resumo por IA pode ser pobre de confiabilidade com relação ao conteúdo original, devendo ser feita uma análise da qualidade do conteúdo gerado. O resumo gerado em Markdown também pode conter inconsistências de formatação quanto a própria síxtaxe do Markdown fazendo-se necessária uma formatação para melhor uso com aplicativos de leitura de Markdown.


## Executando

Clone o repositório:

```bash
git clone https://github.com/henriquesebastiao/resume && cd resume
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
