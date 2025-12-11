import ollama

# Modelle definieren
#model_a = "ministral-3:14b"
#model_b = "ministral-3:14b"
#model_c ="ministral-3:14b"
model_a = "ministral-3:3b"
model_b = "ministral-3:3b"
model_c = "ministral-3:3b"

def ask_model(model_name, prompt):
    print(f"⏳ {model_name} denkt nach...") # Kleines Feedback beim Warten
    try:
        response = ollama.chat(model=model_name, messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except Exception as e:
        return f"Fehler bei {model_name}: {e}"

print("\n--- Start der Dreier-Konferenz ---\n")

# SCHRITT 1: Lehrer (A) generiert eine Quizfrage
topic = "Quantenphysik"
prompt_1 = f"Stelle eine kurze, aber knifflige Quizfrage zum Thema {topic}."
frage = ask_model(model_a, prompt_1)
print(f"\n👨‍🏫 [{model_a} LEHRER]:\n{frage}\n")

# SCHRITT 2: Schüler (B) versucht zu antworten
prompt_2 = f"Die Frage ist: '{frage}'. Beantworte sie kurz und prägnant."
antwort_b = ask_model(model_b, prompt_2)
print(f"\n🧑‍🎓 [{model_b} SCHÜLER]:\n{antwort_b}\n")

# SCHRITT 3: Faktenchecker (C) prüft die Antwort
# Wir geben C die Frage UND die Antwort von B
prompt_3 = f"Frage: '{frage}'. Antwort eines Schülers: '{antwort_b}'. Hat der Schüler recht? Ergänze ein wichtiges Detail, das fehlt."
kommentar_c = ask_model(model_c, prompt_3)
print(f"\n🤓 [{model_c} CHECKER]:\n{kommentar_c}\n")

# SCHRITT 4: Lehrer (A) gibt die Endnote
# A sieht nun alles: Seine Frage, die Antwort von B und die Kritik von C
prompt_4 = (f"Hier ist der Verlauf:\n"
            f"1. Deine Frage: {frage}\n"
            f"2. Antwort Schüler: {antwort_b}\n"
            f"3. Anmerkung Checker: {kommentar_c}\n\n"
            f"Fasse zusammen: War die Antwort korrekt? Gib dem Schüler eine Note (1-6) und ein kurzes Abschlussfazit.")
bewertung = ask_model(model_a, prompt_4)
print(f"\n👨‍🏫 [{model_a} ZEUGNIS]:\n{bewertung}\n")
