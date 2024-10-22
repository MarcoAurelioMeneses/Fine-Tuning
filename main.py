from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Carregando um documento para o fine-tuning
client.files.create(
    file=open("teste_tuning.jsonl", "rb"),
    purpose="readme",
)

# Criando um fine-tuning
client.fine_tuning.jobs.create(
    # Arquivo carregado
    training_file="file-YVQXH6F0n9FVtW6zNz5Eg",
    model="gpt-4o-mini"
)

#Usando o modelo treinado
completion = client.chat.completions.create(
    model="nome-do-modelo-treinado",
    messages=[{"role": "system", "content": "Asssitent X"}, 
              {"role": "user", "content": "qual o nome da empresa"}]
)

print(completion.choices[0].message.content)