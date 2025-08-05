# TechJournal.it Automation - Setup Guide

## 📋 Panoramica

Questo progetto automatizza la navigazione su www.techjournal.it ogni 15-30 minuti e clicca sui banner pubblicitari con comportamento umano casuale.

## 🚀 Installazione Rapida

### 1. Installazione automatica
```bash
chmod +x install.sh
./install.sh
```

### 2. Test del setup
```bash
python3 test_script.py
```

### 3. Avvio dell'automazione
```bash
python3 techjournal_automation.py
```

## 📁 Struttura del Progetto

```
├── techjournal_automation.py    # Script principale
├── config.py                    # File di configurazione
├── requirements.txt             # Dipendenze Python
├── install.sh                  # Script di installazione
├── test_script.py              # Script di test
├── README_automation.md        # Documentazione completa
└── SETUP_GUIDE.md             # Questa guida
```

## ⚙️ Configurazione

### Modificare il comportamento
Modifica `config.py` per personalizzare:

```python
# Intervalli tra le sessioni (minuti)
MIN_INTERVAL = 15
MAX_INTERVAL = 30

# Comportamento dei click
BANNER_CLICK_PROBABILITY = 0.7  # 70% di probabilità di click
MAX_BANNER_CLICKS_PER_SESSION = 3  # Massimo 3 click per sessione

# Ritardi umani
MIN_DELAY = 1.0  # Ritardo minimo tra azioni
MAX_DELAY = 3.0  # Ritardo massimo tra azioni
```

### Modalità headless
Per eseguire senza interfaccia grafica:
```python
HEADLESS_MODE = True
```

## 🎯 Utilizzo

### Avvio semplice
```bash
python3 techjournal_automation.py
```

### Avvio in background
```bash
nohup python3 techjournal_automation.py > automation_output.log 2>&1 &
```

### Monitoraggio
```bash
# Verifica se è in esecuzione
ps aux | grep techjournal_automation.py

# Visualizza log in tempo reale
tail -f techjournal_automation.log

# Visualizza output dell'automazione
tail -f automation_output.log
```

### Interruzione
```bash
# Interruzione sicura
pkill -f techjournal_automation.py

# Oppure premi Ctrl+C se in foreground
```

## 🔧 Risoluzione Problemi

### ChromeDriver non trovato
```bash
pip3 install webdriver-manager
```

### Errori di dipendenze
```bash
pip3 install -r requirements.txt
```

### Problemi di permessi
```bash
chmod +x techjournal_automation.py
chmod +x install.sh
```

### Test di connessione
```bash
python3 test_script.py
```

## 📊 Monitoraggio e Log

### File di log
- `techjournal_automation.log` - Log dettagliati dell'automazione
- `automation_output.log` - Output dello script (se eseguito in background)

### Informazioni registrate
- Sessioni di navigazione
- Banner cliccati
- Errori e warning
- Intervalli tra le sessioni
- Comportamento umano simulato

## 🛡️ Sicurezza e Best Practices

### Uso responsabile
- Rispetta i termini di servizio del sito web
- Non sovraccaricare i server
- Usa intervalli ragionevoli

### Protezioni integrate
- Ritardi casuali per evitare rilevamento
- User agent rotazione
- Comportamento umano simulato
- Gestione robusta degli errori

## 🔄 Automazione Avanzata

### Avvio automatico al boot (Linux)
```bash
# Aggiungi al crontab
crontab -e

# Aggiungi questa riga:
@reboot cd /path/to/script && python3 techjournal_automation.py
```

### Rotazione VPN (opzionale)
Modifica `config.py`:
```python
ENABLE_VPN_ROTATION = True
VPN_ROTATION_INTERVAL = 3600  # Ogni ora
```

### Proxy (opzionale)
Modifica `config.py`:
```python
ENABLE_PROXY = True
PROXY_SERVER = "ip:port"
```

## 📈 Personalizzazione Avanzata

### Aggiungere nuovi selettori banner
Modifica `BANNER_SELECTORS` in `config.py`:
```python
BANNER_SELECTORS = [
    "iframe[src*='ads']",
    "div[class*='banner']",
    # Aggiungi i tuoi selettori qui
]
```

### Modificare il comportamento di scroll
Personalizza `scroll_randomly()` in `techjournal_automation.py`

### Aggiungere nuove azioni
Estendi la classe `TechJournalAutomation` con nuovi metodi

## 🆘 Supporto

### Comandi utili
```bash
# Verifica versione Python
python3 --version

# Verifica dipendenze
pip3 list | grep selenium

# Test completo
python3 test_script.py

# Log in tempo reale
tail -f techjournal_automation.log
```

### Troubleshooting comune
1. **Script non si avvia**: Verifica Python 3.7+
2. **Errori WebDriver**: Esegui `python3 test_script.py`
3. **Nessun banner trovato**: Verifica connessione internet
4. **Errori di click**: I banner potrebbero essere protetti

## 📝 Note Importanti

⚠️ **Avvertenze**:
- Questo script è per scopi educativi
- Rispetta sempre i termini di servizio
- Non abusare delle risorse del server
- Usa responsabilmente

✅ **Caratteristiche di sicurezza**:
- Comportamento umano simulato
- Ritardi casuali
- Gestione errori robusta
- Logging completo

## 🎯 Prossimi Passi

1. **Testa il setup**: `python3 test_script.py`
2. **Configura le impostazioni**: Modifica `config.py`
3. **Avvia l'automazione**: `python3 techjournal_automation.py`
4. **Monitora i log**: `tail -f techjournal_automation.log`
5. **Personalizza**: Modifica i parametri in `config.py`

---

**Buon utilizzo!** 🚀