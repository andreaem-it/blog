# TechJournal.it Automation Script

Questo script automatizza la navigazione su www.techjournal.it ogni 15-30 minuti e clicca sui banner pubblicitari con comportamento umano casuale.

## Caratteristiche

- **Intervalli casuali**: Naviga ogni 15-30 minuti in modo casuale
- **Comportamento umano**: Scroll casuale, ritardi naturali, decisioni probabilistiche
- **Rilevamento banner**: Cerca automaticamente banner pubblicitari usando diversi selettori
- **Logging completo**: Registra tutte le attività in file di log
- **Gestione errori**: Gestisce errori e riavvia automaticamente

## Prerequisiti

1. **Python 3.7+**
2. **Google Chrome** installato
3. **ChromeDriver** (verrà scaricato automaticamente)

## Installazione

1. **Installa le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verifica l'installazione**:
   ```bash
   python techjournal_automation.py --help
   ```

## Utilizzo

### Avvio semplice
```bash
python techjournal_automation.py
```

### Avvio in background (Linux/Mac)
```bash
nohup python techjournal_automation.py > automation_output.log 2>&1 &
```

### Avvio con cron (Linux)
Aggiungi questa riga al crontab per avviare automaticamente:
```bash
@reboot cd /path/to/script && python techjournal_automation.py
```

## Configurazione

### Modificare gli intervalli
Nel file `techjournal_automation.py`, modifica la riga:
```python
next_interval = random.randint(15, 30) * 60  # 15-30 minuti
```

### Modificare il comportamento
- **Probabilità di click**: Modifica `if random.random() < 0.7:` nella funzione `find_and_click_banners`
- **Numero massimo di click**: Modifica `if banners_clicked >= 3:` 
- **Ritardi**: Modifica i valori in `human_like_delay()`

## Monitoraggio

### Log file
Lo script crea un file `techjournal_automation.log` con tutti i dettagli:
- Sessioni di navigazione
- Banner cliccati
- Errori e warning
- Intervalli tra le sessioni

### Controllo dello stato
```bash
# Verifica se lo script è in esecuzione
ps aux | grep techjournal_automation.py

# Visualizza i log in tempo reale
tail -f techjournal_automation.log
```

## Interruzione

### Interruzione manuale
Premi `Ctrl+C` per fermare lo script in modo sicuro.

### Interruzione forzata
```bash
pkill -f techjournal_automation.py
```

## Sicurezza e Note

⚠️ **Avvertenze importanti**:

1. **Uso responsabile**: Questo script è per scopi educativi. Rispetta i termini di servizio del sito web.
2. **Rate limiting**: Lo script include ritardi casuali per evitare di sovraccaricare il server.
3. **User Agent rotazione**: Usa user agent casuali per sembrare più umano.
4. **Gestione errori**: Include gestione robusta degli errori per evitare crash.

## Risoluzione problemi

### ChromeDriver non trovato
```bash
pip install webdriver-manager
```

### Errori di connessione
- Verifica la connessione internet
- Controlla se il sito è accessibile manualmente

### Errori di click
- I banner potrebbero essere in iframe o avere protezioni anti-bot
- Lo script gestisce automaticamente questi casi

## Personalizzazione avanzata

### Aggiungere nuovi selettori banner
Modifica l'array `banner_selectors` nel metodo `find_and_click_banners()`.

### Modificare il comportamento di scroll
Personalizza la funzione `scroll_randomly()` per diversi pattern di navigazione.

### Aggiungere proxy
```python
chrome_options.add_argument('--proxy-server=ip:port')
```

## Supporto

Per problemi o domande, controlla:
1. I log file per errori specifici
2. La documentazione di Selenium
3. I termini di servizio di www.techjournal.it