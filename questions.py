import requests
import pandas as pd
import winsound
import time

TOKEN = "Bearer APP_USR-1980722105262368-102312-bd9ccc8737153e15ccce89e7b7cae8ed-194549496"


def all_questions(offset):
  url = f"https://api.mercadolibre.com/my/received_questions/search?offset={offset}&limit=50"

  payload = {}
  headers = {
    'Authorization': TOKEN
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  data = response.json()

  data_response = []

  questions = data["questions"]
  print(f"offset {offset}")
  for data in questions:

    data_response.append({"item_id":data["item_id"], "text": data["text"], "answer": data["answer"]})
  
  return data_response



def questions_by_item_id(item_id):
  url = f"https://api.mercadolibre.com/questions/search?item_id={item_id}"


  headers = {
    'Authorization': TOKEN
  }

  response = requests.request("GET", url, headers=headers)
  questions = response.json()["questions"]

  data_response = []

  for question in questions:
    data_response.append({"item_id":question["item_id"], "question": question["text"], "answer": question["answer"]["text"] if question["answer"] else "" })

  return data_response



if __name__ == '__main__':
    
  questions_by_item = []

  for offset in range(1, 2):
    questions = all_questions(offset)
    for question in questions:
      item_id = question["item_id"]
      questions_for_item = questions_by_item_id(item_id)
      questions_by_item.extend(questions_for_item)  # Añade las preguntas a la lista principal

  # Crear un DataFrame con las nuevas preguntas
  new_data = pd.DataFrame(questions_by_item, columns=["item_id", "question", "answer"])

  # Leer el archivo CSV existente
  try:
    existing_data = pd.read_csv('questions_by_item.csv')
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
  except FileNotFoundError:
    combined_data = new_data

  # Guardar el DataFrame actualizado en el archivo CSV
  combined_data.to_csv('questions_by_item.csv', encoding='utf-8-sig', sep=";", index=False)

  frequency = 2500  # Set Frequency in Hertz, e.g., 2500 Hertz
  duration = 1000  # Set Duration in milliseconds, e.g., 1000 ms == 1 second
  winsound.Beep(frequency, duration)
