import ollama

model_a = ""
model_b = ""

def ask_model(model_name, prompt):
    response = ollama.chat(model=model_name, messages=[
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

print("--- Start der Unterhaltung ---\n")

# (Modell A) generiert eine Quizfrage
topic = "Quantenphysik"
prompt_1 = f"Stelle eine kurze, einfache Quizfrage zum Thema {topic}."
frage = ask_model(model_a, prompt_1)
print(f"[{model_a} als Lehrer]: {frage}\n")

# (Modell B) beantwortet die Frage
prompt_2 = f"Beantworte diese Frage kurz: {frage}"
antwort = ask_model(model_b, prompt_2)
print(f"[{model_b} als Schüler]: {antwort}\n")

# (Modell A) bewertet die Antwort
prompt_3 = f"Die Frage war: '{frage}'. Die Antwort war: '{antwort}'. Ist diese Antwort korrekt? Gib kurzes Feedback."
bewertung = ask_model(model_a, prompt_3)
print(f"[{model_a} Feedback]: {bewertung}\n")
