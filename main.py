import time
import requests

# Diese Funktion übergibt deine Eingabe an das maschinelle Lernmodell
# und gibt die Kategorie mit der höchsten Wahrscheinlichkeit zurück.
def classify(text):
    #Trage hier den API Key von deinem Projekt ein. Der API Key besteht aus Zahlen, Buchstaben und Bindestrichen.
    key = "69de2810-f6e6-11eb-b1b5-d1dde5daa6135e93d63b-230b-4a2d-89fd-373b125354ee"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
  #NutzerIn wird aufgefordert eine Eingabe zu machen
  eingabe = input("Schreibe etwas...\n")
  klassifikation = classify(eingabe)
  kategorie = klassifikation["class_name"]
  confidence = klassifikation["confidence"]

  #Passe den Code hier so an, dass die Confidence berücksichtigt wird: Wenn sich der Charakter sicher ist, dann soll er reagieren, ansonsten sage "Keine Klassifikation möglich".
  if confidence > 60:
    if kategorie == "Nett":
      print(":-)")
    else:
      print(":-(")
  else:
    print("Ich verstehe dich nicht...\n")

  time.sleep(3)
  print(":-|")

#Bei Programmstart hat der Charakter ein neutrales Gesicht
print(":-|")

#Während das Programm läuft, wird die Frage/Antwort-Funktion dauerhaft aufgerufen.
while True:
  answer_question()
