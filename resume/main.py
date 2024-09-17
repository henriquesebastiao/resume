import os
from pathlib import Path

import tiktoken
import typer
from load_dotenv import load_dotenv
from openai import OpenAI
from pymupdf4llm import to_markdown
from rich import print
from rich.progress import track

MODEL = 'gpt-4o'


def order(text: str):
    return f"""Você é um assistente de resumo de textos. Receberá um documento em formato Markdown contendo a apostila de uma faculdade. Sua tarefa é resumir o conteúdo do documento de maneira organizada de forma bem completa e com qualidade.
A ideia do resumo é com a sua leitura obter o mesmo grau de conhecimento da apostila, fornecendo uma leitura e aprendizado profundos dentro do conteúdo que a apostila apresenta.

O resumo deve:
1. Fornecer um resumo completo e detalhado para cada capítulo e tópico, seguindo a mesma ordem apresentada na apostila.
2. Garantir que o texto resumido também esteja formatado em Markdown, com os títulos e subtítulos com mesmos nomes do documento original.

Aqui está o conteúdo da apostila em Markdown:

{text}

Por favor, forneça resumos correspondentes a cada seção do documento original."""


def split_text(text, max_tokens):
    encoder = tiktoken.encoding_for_model(MODEL)
    tokens = encoder.encode(text)
    parts = []
    while tokens:
        part_tokens = tokens[:max_tokens]
        tokens = tokens[max_tokens:]
        part_text = encoder.decode(part_tokens)
        parts.append(part_text)
    return parts


load_dotenv()

app = typer.Typer(
    help='Um CLI que usa a API da OpenAI para gerar resumos de apostilas :books:',
    rich_markup_mode='rich',
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def main(): ...


@app.command(help='Gera o resumo de um arquivo Markdown')
def md():
    origin_file = typer.prompt('Caminho do arquivo para resumir')

    text = to_markdown(origin_file)
    client = OpenAI(api_key=os.getenv('OPENAPI_KEY'))

    max_tokens = 3000
    parts = split_text(text, max_tokens)

    summaries = []
    for part in track(parts, description='Gerando resumo...'):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{'role': 'user', 'content': order(part)}],
            temperature=0.5,
        )
        summary = response.choices[0].message.content.strip()
        summaries.append(summary)

    full_summary = '\n\n'.join(summaries)

    summary_md_path = 'resume.md'
    Path(summary_md_path).write_bytes(full_summary.encode())
    print(
        f'[bold]Resumo salvo em: {summary_md_path}[/bold] :white_heavy_check_mark:'
    )
