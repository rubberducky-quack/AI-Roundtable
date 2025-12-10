# Setup-Anleitung für AI-Roundtable

## Ordnerstruktur erstellen

```bash
# Hauptverzeichnis wechseln
cd AI-Roundtable

# Optional: Zusätzliche Ordner erstellen (nach Bedarf)
mkdir -p data
mkdir -p models
mkdir -p logs
```

## Virtuelles Environment (venv) einrichten

### Virtuelle Umgebung erstellen
```bash
python3 -m venv venv
```

### Virtuelle Umgebung aktivieren

**Auf Linux/Mac:**
```bash
source venv/bin/activate
```

**Auf Windows:**
```bash
venv\Scripts\activate
```

### Abhängigkeiten installieren
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Anwendung ausführen

```bash
python main.py
```

## Virtuelle Umgebung deaktivieren

```bash
deactivate
```

## Hinweise

- Die `.gitignore` Datei ist bereits konfiguriert für Python-Projekte und Mac-spezifische Dateien (.DS_Store)
- Das virtuelle Environment (`venv/`) wird automatisch von Git ignoriert
- Die `requirements.txt` enthält die ollama Bibliothek für AI-Funktionalität
