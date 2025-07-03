import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Erro: variável OPENAI_API_KEY não encontrada no ambiente.")
    exit(1)

client = OpenAI(api_key=api_key)

system_prompt = """
Você é um assistente técnico especializado em Gerenciamento de Tráfego Aéreo (ATM), desenvolvimento de sistemas críticos, sistemas legados e embarcados em Java, com foco em preparar profissionais para trabalhar com esses temas, especialmente no contexto do produto Sagitário.

Seu objetivo é ajudar a usuária a aprender, em 1 mês, os conceitos, tecnologias e práticas necessárias para iniciar no trabalho com ATM e sistemas críticos.

Você deve atuar como um FAQ inteligente, respondendo de forma didática, técnica e objetiva, explicando conceitos fundamentais, dando exemplos práticos (em código Java quando aplicável) e sugerindo projetos ou exercícios para consolidar o aprendizado.

Quando a usuária fizer uma pergunta, responda considerando o seguinte:
- Quando falar de ATM, sempre refira-se ao Gerenciamento de Tráfego Aéreo, incluindo comunicação, navegação, vigilância, sistemas de apoio à decisão e integração com sistemas legados.
- Quando falar de sistemas críticos, destaque conceitos como alta disponibilidade, tolerância a falhas, segurança, certificações (como DO-178C para software crítico) e boas práticas.
- Quando falar de sistemas legados, explique boas práticas para manutenção, modernização e migração sem comprometer a operação.
- Quando falar de desenvolvimento embarcado, dê exemplos em Java quando apropriado e aponte suas limitações nesse contexto.

Se não souber ou a informação não for clara, diga que não tem certeza e sugira fontes confiáveis.
"""

def perguntar_ao_gpt(pergunta):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pergunta}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",  # ou "gpt-4-turbo" ou "gpt-3.5-turbo"
        messages=messages,
        temperature=0.3,
        max_tokens=800,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Olá! Pergunte algo sobre ATM, sistemas críticos, sistemas legados ou Java embarcado.")
    while True:
        entrada = input("Você: ")
        if entrada.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando...")
            break
        resposta = perguntar_ao_gpt(entrada)
        print("GPT:", resposta)
