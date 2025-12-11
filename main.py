import ollama

# Modelle definieren
#model_a = "ministral-3:14b"
#model_b = "ministral-3:14b"
#model_c ="ministral-3:14b"
model_a = "ministral-3:3b"
model_b = "ministral-3:3b"
model_c = "ministral-3:3b"
#model_a = input("Bitte gib das Modell für den Lehrer ein (z.B. ministral-3:3b): ")
#model_b = input("Bitte gib das Modell für den Schüler ein (z.B. deepseek-r1:8b): ")
#model_c = input("Bitte gib das Modell für den Checker ein (z.B. qwen3-vl:2b): ")

topic = input("Zu welchem Thema soll eine Quizfrage gestellt werden?: ")

def ask_model(model_name, prompt):
    print(f"⏳ {model_name} denkt nach...")
    try:
        response = ollama.chat(model=model_name, messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except Exception as e:
        return f"Fehler bei {model_name}: {e}"

print("\n--- Start der Dreier-Konferenz ---\n")

prompt_1 = f"Stelle eine kurze, aber knifflige Quizfrage zum Thema {topic}."
frage = ask_model(model_a, prompt_1)
print(f"\n👨‍🏫 [{model_a} LEHRER]:\n{frage}\n")

prompt_2 = f"Die Frage ist: '{frage}'. Beantworte sie kurz und prägnant."
antwort_b = ask_model(model_b, prompt_2)
print(f"\n🧑‍🎓 [{model_b} SCHÜLER]:\n{antwort_b}\n")

prompt_3 = f"Frage: '{frage}'. Antwort eines Schülers: '{antwort_b}'. Hat der Schüler recht? Ergänze ein wichtiges Detail, das fehlt."
kommentar_c = ask_model(model_c, prompt_3)
print(f"\n🤓 [{model_c} CHECKER]:\n{kommentar_c}\n")

prompt_4 = (f"Hier ist der Verlauf:\n"
            f"1. Deine Frage: {frage}\n"
            f"2. Antwort Schüler: {antwort_b}\n"
            f"3. Anmerkung Checker: {kommentar_c}\n\n"
            f"Fasse zusammen: War die Antwort korrekt? Gib dem Schüler eine Note (1-6) und ein kurzes Abschlussfazit.")
bewertung = ask_model(model_a, prompt_4)
print(f"\n👨‍🏫 [{model_a} ZEUGNIS]:\n{bewertung}\n")
