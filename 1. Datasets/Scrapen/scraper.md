# Web Scraper voor Markdown Links

Deze Python script leest URLs uit een markdown bestand en download de content van elke URL, converteert het naar markdown formaat, en slaat het op als individuele markdown bestanden.

## Installatie

1. Installeer Python 3.8 of hoger

2. Installeer de benodigde packages:
```bash
pip install -r requirements.txt
```

## Gebruik

### Basis gebruik:
```bash
python web_scraper.py input_links.md
```

### Met opties:
```bash
# Specificeer output directory
python web_scraper.py input_links.md -o mijn_output_folder

# Pas de vertraging tussen requests aan (in seconden)
python web_scraper.py input_links.md -d 2.0
```

## Features

- **Automatische URL extractie**: Haalt alle URLs uit het markdown bestand, inclusief:
  - Platte URLs (`https://example.com`)
  - Markdown links (`[tekst](https://example.com)`)
  - URLs met beschrijvingen (`https://example.com (beschrijving)`)

- **Slimme bestandsnamen**: Genereert betekenisvolle bestandsnamen op basis van:
  - Domein naam
  - URL pad
  - Eventuele beschrijving

- **Content conversie**: 
  - Converteert HTML naar clean markdown
  - Behoudt links en afbeeldingen
  - Verwijdert scripts en styling

- **Foutafhandeling**:
  - Slaat mislukte URLs op in aparte folder
  - Houdt statistieken bij
  - Skip al gedownloade content

- **Rate limiting**: Respecteert servers met instelbare vertraging tussen requests

## Output structuur

```
scraped_content/
├── index.md           # Overzicht van alle URLs en status
├── content/          # Succesvol gescrapete pagina's
│   ├── digitaleoverheid_nl_nieuws_europese-samenwerking.md
│   ├── vng_nl_projecten_common-ground.md
│   └── ...
└── failed/           # URLs die niet gedownload konden worden
    └── ...
```

## Index bestand

Het script genereert automatisch een `index.md` met:
- Statistieken (totaal, succes, mislukt, overgeslagen)
- Lijst van alle URLs met status indicators (✓ of ✗)
- Timestamp van de scraping run

## Tips

1. **Test eerst klein**: Test met een klein markdown bestand voordat je alle links scraped
2. **Respecteer rate limits**: Gebruik een redelijke vertraging (1-2 seconden)
3. **Check robots.txt**: Sommige sites verbieden scraping
4. **PDF bestanden**: PDFs worden gedetecteerd maar niet geconverteerd

## Troubleshooting

### "Connection refused" errors
- Verhoog de vertraging met `-d 3.0`
- Sommige sites blokkeren geautomatiseerde requests

### Lege of onvolledige content
- De site gebruikt mogelijk JavaScript rendering
- Probeer de originele pagina te bezoeken

### Encoding problemen
- Het script gebruikt UTF-8 encoding
- Sommige oudere sites kunnen problemen geven

## Licentie

Dit script is bedoeld voor educatieve doeleinden. Respecteer altijd de gebruiksvoorwaarden en robots.txt van de websites die je scraped.