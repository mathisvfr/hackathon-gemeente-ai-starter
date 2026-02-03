---
title: Hoog-risico-AI-systemen loggen automatisch bepaalde gegevens - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-07-automatische-logregistratie/index.html
scraped_at: 2025-06-11T13:47:20.839880
---

# Hoog-risico-AI-systemen loggen automatisch bepaalde gegevens - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-07-automatische-logregistratie/index.html

---

[ ![Home Algoritmekader](../../../assets/logo.svg) ](../../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../../soorten-algoritmes-en-ai/)
  * [ Onderwerpen  ](../../../onderwerpen/)
  * [ Levenscyclus  ](../../../levenscyclus/)
  * [ Rollen  ](../../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../)

Inhoudsopgave

  * Vereiste
  * Toelichting
  * Bronnen
  * Van toepassing op
  * Risico
  * Maatregelen

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Vereisten  ](../)

# Hoog-risico-AI-systemen loggen automatisch bepaalde gegevens

[]( "Vereiste ID")aia-07[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Vereiste

Hoog-risico-AI-systemen loggen automatisch bepaalde gegevens.

## Toelichting

AI-systemen met een hoog risico zijn ontworpen met functionaliteiten die gebeurtenissen gedurende hun levenscyclus automatisch registreren. Dit wordt vaak aangeduid als "logs".

Deze logs bieden een traceerbaarheidsmechanisme waarmee gebruiksverantwoordelijken en autoriteiten incidenten en fouten kunnen analyseren, naleving kunnen controleren en mogelijke risico's kunnen identificeren en aanpakken.

Het doel van deze registratie is om de transparantie en verantwoordingsplicht van AI-systemen te vergroten, waardoor het beheer van risico's en incidenten verbetert. Voor AI-systemen met een hoog-risico voorziet de loggingcapaciteit ten minste in:

  1. de registratie van de duur van elk gebruik van het systeem;
  2. de referentiedatabank aan de hand waarvan de inputdata zijn gecontroleerd door het systeem;
  3. de inputdata ten aanzien waarvan de zoekopdracht een match heeft opgeleverd;
  4. de identificatie van natuurlijke personen die betrokken zijn bij de verificatie van de resultaten. Specifiek voor gebruiksverantwoordelijken

Voor AI-systemen die door bestuursorganen worden gebruikt of AI-systmen die persoonsgegevens verwerken leveren de BIO en AVG vergelijkbare verplichingen op die ook van toepassing zijn op AI-systemen die niet gezien worden als een AI-systeem met hoog risico. Daarbij komen nog verplichtingen om de logs doorlopend of periodiek te monitoren op incidenten.

## Bronnen

  * [Artikel 12 Verordening Artificiële Intelligentie](https://eur-lex.europa.eu/legal-content/NL/TXT/HTML/?uri=OJ:L_202401689#d1e3495-1-1)
  * [Artikel 26(6) Verordening Artificiële Intelligentie](https://eur-lex.europa.eu/legal-content/NL/TXT/HTML/?uri=OJ:L_202401689#d1e3495-1-1), zie ook [deze vereiste over logging door gebruiksverantwoordelijke](../aia-23-gebruiksverantwoordelijken-bewaren-logs/).
  * [Hoofdstuk 12.4 Baseline Informatiebeveiliging Overheid ](https://www.bio-overheid.nl/media/13kduqsi/bio-versie-104zv_def.pdf)
  * [Artikel 5 en 32 Algemene Verordening Gegevensbescherming](https://eur-lex.europa.eu/legal-content/NL/TXT/HTML/?uri=CELEX:32016R0679)

## Van toepassing op

Deze vereiste is van toepassing voor onderstaande (combinatie van) labels. Gebruik de [beslishulp](https://ai-act-decisiontree.apps.digilab.network) voor hulp bij wat er in jouw situatie van toepassing is.

[](../../../soorten-algoritmes-en-ai/wat-is-een-algoritme/ "Soort toepassing")[AI-systeem](../../ai-verordening/#ai-systeem)[](../../../soorten-algoritmes-en-ai/wat-is-een-algoritme/ "Soort toepassing")[AI-systeem voor algemene doeleinden](../../ai-verordening/#ai-model-voor-algemene-doeleinden)[](../../ai-verordening/#risicogroepen "Risicogroep")[Hoog risico AI-systeem](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#hoog-risico-ai-systeem)[](../../ai-verordening/#rollen-uit-de-ai-verordening "Rol AI-verordening")[Aanbieder](../../ai-verordening/#aanbieder)[](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding "Transparantieverplichting AI-verordening")[Geen transparantieverplichting](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding)[](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding "Transparantieverplichting AI-verordening")[Transparantieverplichting](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding)

## Risico

Ontbreken van automatische logregistratie kan leiden tot een gebrek aan transparantie en traceerbaarheid van het AI-systeem, wat het vermogen om verantwoordelijkheid te nemen en eventuele problemen aan te pakken belemmert.

## Maatregelen

id| Maatregelen
---|---
[owp-15](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-15-bespreek-vereisten-met-aanbieders/index.html)| [Bespreek de vereisten die gelden voor een verantwoorde inzet van algoritmes met aanbieders](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-15-bespreek-vereisten-met-aanbieders/index.html)
[owp-16](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-16-vereisten-onderdeel-algemene-inkoopvoorwaarden-en-contractovereenkomst/index.html)| [Maak vereisten voor algoritmes onderdeel van algemene inkoopvoorwaarden en de contractovereenkomst](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-16-vereisten-onderdeel-algemene-inkoopvoorwaarden-en-contractovereenkomst/index.html)
[owp-21](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-21-ruimte-voor-samenwerking-met-aanbieder/index.html)| [Creëer ruimte om met een aanbieder samen te gaan werken om specifieke vereisten te realiseren](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-21-ruimte-voor-samenwerking-met-aanbieder/index.html)
[owp-23](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-23-uitvoeren-audit-voor-naleving-vereisten/index.html)| [Neem het kunnen uitvoeren van een audit over de vereiste op in contractvoorwaarden en de contractovereenkomst](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-23-uitvoeren-audit-voor-naleving-vereisten/index.html)
[owp-27](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-27-maak-vereisten-onderdeel-van-programma-van-eisen/index.html)| [Maak vereisten onderdeel van het programma van eisen bij een aanbesteding](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-27-maak-vereisten-onderdeel-van-programma-van-eisen/index.html)
[owp-28](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-28-maak-vereisten-onderdeel-van-service-level-agreement/index.html)| [Maak vereisten voor algoritmes onderdeel van de Service Level Agreement](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-28-maak-vereisten-onderdeel-van-service-level-agreement/index.html)
[owk-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-01-security-by-design/index.html)| [Ontwerp en ontwikkel het algoritme volgens de principes van ‘security by design’](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-01-security-by-design/index.html)
[owk-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-04-logging/index.html)| [Maak logbestanden waarin staat wie wanneer toegang had tot de data en de code](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-04-logging/index.html)
19 februari 2025 23 mei 2024
  *AI-modellen voor algemene doeleinden: Een AI-model, ook wanneer het is getraind met een grote hoeveelheid data met behulp van self-supervision op grote schaal, dat een aanzienlijk algemeen karakter vertoont en in staat is op competente wijze een breed scala aan verschillende taken uit te voeren, ongeacht de wijze waarop het model in de handel wordt gebracht, en dat kan worden geïntegreerd in een verscheidenheid aan systemen verder in de AI-waardeketen of toepassingen verder in de AI-waardeketen, met uitzondering van AI-modellen die worden gebruikt voor onderzoek, ontwikkeling of prototypingactiviteiten alvorens zij in de handel worden gebracht.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *AI-model voor algemene doeleinden: Een AI-model, ook wanneer het is getraind met een grote hoeveelheid data met behulp van self-supervision op grote schaal, dat een aanzienlijk algemeen karakter vertoont en in staat is op competente wijze een breed scala aan verschillende taken uit te voeren, ongeacht de wijze waarop het model in de handel wordt gebracht, en dat kan worden geïntegreerd in een verscheidenheid aan systemen verder in de AI-waardeketen of toepassingen verder in de AI-waardeketen, met uitzondering van AI-modellen die worden gebruikt voor onderzoek, ontwikkeling of prototypingactiviteiten alvorens zij in de handel worden gebracht.
  *biometrische gegevens: persoonsgegevens die het resultaat zijn van een specifieke technische verwerking met betrekking tot de fysieke, fysiologische of gedragsgerelateerde kenmerken van een natuurlijk persoon, zoals gezichtsafbeeldingen of vingerafdrukgegevens
  *AI-systeem voor algemene doeleinden: Een AI-systeem dat is gebaseerd op een AI- model voor algemene doeleinden en dat verschillende doeleinden kan dienen, zowel voor direct gebruik als voor integratie in andere AI-systemen
  *systeemrisico: een risico dat specifiek is voor de capaciteiten met een grote impact van AI-modellen voor algemene doeleinden, die aanzienlijke gevolgen hebben voor de markt van de Unie vanwege hun bereik, of vanwege feitelijke of redelijkerwijs te voorziene negatieve gevolgen voor de gezondheid, de veiligheid, de openbare veiligheid, de grondrechten of de samenleving als geheel, en dat op grote schaal in de hele waardeketen kan worden verspreid
  *AI-bureau: De taak van de Commissie waarbij zij bijdraagt aan de uitvoering van, de monitoring van en het toezicht op AI-systemen en AI-modellen voor algemene doeleinden, en AI-governance, als bepaald in het besluit van de Commissie van 24 januari 2024; verwijzingen in deze verordening naar het AI-bureau worden begrepen als verwijzingen naar de Commissie
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *kritieke infrastructuur: kritieke infrastructuur zoals gedefinieerd in artikel 2, punt 4, van Richtlijn (EU) 2022/2557
  *redelijkerwijs te voorzien misbruik: Het gebruik van een AI-systeem op een wijze die niet in overeenstemming is met het beoogde doel, maar die kan voortvloeien uit redelijkerwijs te voorzien menselijk gedrag of redelijkerwijs te voorziene interactie met andere systemen, waaronder andere AI-systemen
  *gebruiksinstructies: de door de aanbieder verstrekte informatie om de gebruiksverantwoordelijke te informeren over met name het beoogde doel en juiste gebruik van een AI-systeem
  *testdata: data die worden gebruikt voor het verrichten van een onafhankelijke evaluatie van het AI-systeem om de verwachte prestaties van dat systeem te bevestigen voordat het in de handel wordt gebracht of in gebruik wordt gesteld
  *in de handel brengen: Het voor het eerst in de Unie op de markt aanbieden van een AI-systeem of een AI-model voor algemene doeleinden
  *inputdata: data die in een AI-systeem worden ingevoerd of direct door een AI-systeem worden verworven en op basis waarvan het systeem een output genereert
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
