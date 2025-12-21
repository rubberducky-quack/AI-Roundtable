import ollama

# Konfiguration

#m1 = "ministral-3:14b"
#m2 = "ministral-3:14b"
#m3 = "ministral-3:14b"
m1 = "ministral-3:3b"
m2 = "ministral-3:3b"
m3 = "ministral-3:3b"
m4 = "functiongemma:latest"

def query(model, text):
    try:
        res = ollama.chat(model=model, messages=[{'role': 'user', 'content': text}])
        return res['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Hauptablauf
task = input("Aufgabe/Input: ")
print("\nBearbeite Anfrage...\n")

# Variante 1
p1 = f"Aufgabe: {task}\n\nBitte bearbeiten."
res1 = query(m1, p1)
#print(f"--- Output {m1} (A) ---\n{res1}\n")

# Variante 2
p2 = f"Aufgabe: {task}\n\nBitte bearbeiten."
res2 = query(m2, p2)
#print(f"--- Output {m2} (B) ---\n{res2}\n")

# Vergleich
p3 = (f"Originalaufgabe: {task}\n\n"
      f"Lösung A:\n{res1}\n\n"
      f"Lösung B:\n{res2}\n\n"
      f"Vergleiche A und B und nenne die bessere Lösung mit Begründung.")

verdict = query(m3, p3)
print(f"--- Fazit ({m3}) ---\n{verdict}\n")