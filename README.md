# 🛫 Mentor-ATM: Assistente para aprender sobre ATM, sistemas críticos e Java embarcado

Este projeto é um assistente técnico interativo, criado para ajudar profissionais a aprenderem, em 1 mês, os conceitos fundamentais de:
- **ATM (Gerenciamento de Tráfego Aéreo)**
- **Sistemas Críticos**
- **Sistemas Legados**
- **Java Embarcado**

O assistente foi desenvolvido para a conclusão do **curso de IA Generalista da Generation Brasil**. O agente escolhido tem o objetivo de tirar dúvidas e auxiliar no aprendizado sobre sistemas ATM.

O assistente atua como um FAQ inteligente, respondendo perguntas de forma didática, técnica e objetiva, com exemplos e sugestões de estudos.

---

## Funcionalidades

✅ Responde perguntas sobre ATM, sistemas críticos, sistemas legados e Java embarcado  
✅ Dá exemplos práticos em Java quando aplicável  
✅ Sugere exercícios e projetos para consolidar o aprendizado  
✅ Orienta com boas práticas para manutenção e desenvolvimento em sistemas críticos

---

## 🔧 Requisitos

- Python 3.9 ou superior  
- Uma chave da API da OpenAI (você pode obter em [https://platform.openai.com/](https://platform.openai.com/))

---

## 🛠️ Instalação

1️⃣ Clone este repositório:  

```git clone https://github.com/biancasuarz/mentor-atm.git```
```cd mentor-atm ```

2️⃣ Instale as dependências:

```pip install openai ```

3️⃣ Configure sua chave da API da OpenAI:

Edite o arquivo assistente_atm.py e substitua:

```api_key="SUA_API_KEY_AQUI"```
pela sua chave real.

## 💬 Como usar
Execute no terminal:
```python assistente_atm.py ```

E faça perguntas como:

- O que são sistemas ATM?
- Como funciona a tolerância a falhas em sistemas críticos?
- Como modernizar sistemas legados?
- Como usar Java em sistemas embarcados?

Para sair, digite: sair

## 📄 Exemplo de uso

Você: O que são sistemas ATM?
GPT: ATM significa Gerenciamento de Tráfego Aéreo e envolve...
