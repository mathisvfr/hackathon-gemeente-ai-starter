---
title: Bepaal welke feedbackloops van invloed zijn op het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-08-feedbackloops/index.html
scraped_at: 2025-06-12T10:34:36.872742
---

# Bepaal welke feedbackloops van invloed zijn op het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-08-feedbackloops/index.html

---

[ ![Home Algoritmekader](../../../assets/logo.svg) ](../../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../../soorten-algoritmes-en-ai/)
  * [ Onderwerpen  ](../../../onderwerpen/)
  * [ Levenscyclus  ](../../../levenscyclus/)
  * [ Rollen  ](../../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../)

Inhoudsopgave

  * Maatregel
  * Toelichting
    * Adversarial feedbackloops
    * Monitoring en ophalen informatie
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Bepaal welke feedbackloops van invloed zijn op het algoritme

[]( "Vereiste ID")owk-08[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)

## Maatregel

Stel vast op welke manier de uitkomst of de inzet van het algoritme van invloed kan zijn op het proces en de werking in een latere fase. Probeer deze ‘feedbackloops’ in kaart te brengen zodat ze mogelijk voorkomen kunnen worden of gemonitored kunnen worden op mogelijke negatieve effecten.

## Toelichting

Een feedbackloop kan zich voordoen wanneer de uitkomst van een algoritme wordt gebruikt als nieuwe input voor het algoritme. Deze feedbackloops kunnen een vertekend beeld van de werkelijkheid geven en de robuustheid van het algoritme over tijd in gevaar brengen. Dit is met name van belang wanneer algoritmes bijleren (continue of periodiek).

Opmerking

Merk op dat feedbackloops ook een positief effect kunnen hebben, wanneer bijvoorbeeld gebruikerservaring wordt meegenomen in de doorontwikkeling van het algoritme.

Er zijn verschillende vormen van feedbackloops:

  * _Sampling feedbackloop_ : wanneer de beslissing die volgt uit het algoritme effect heeft op de kans dat bepaalde groepen in een volgende selectie terechtkomen.

  * _Individual feedbackloop_ : wanneer de mening of visie van een beoordelaar verandert door [het gebruiken van het algoritme](../../../onderwerpen/bias-en-non-discriminatie/#bias-in-menselijk-denken)(het overnemen van de ‘vooroordelen van een systeem’).

  * _Feature feedbackloop_ : bijvoorbeeld wanneer de uitkomst dat een subsidie niet verstrekt wordt, ook als kenmerk ‘eerdere weigering van subsidie’ wordt gebruikt door het algoritme.

  * _Outcome feedbackloop_ : wanneer burgers of bedrijven op basis van de uitkomst ander gedrag gaan vertonen. In het voorbeeld van de subsidie betekent dit bijvoorbeeld dat burgers hun uitgavepatroon veranderen.

  * _Machine-learning model feedbackloop_ : wanneer nieuwe data die beschikbaar komt is beïnvloed door de beslissing van het algoritme zelf en deze data wordt gebruikt om een machine-learning model mee te (her)trainen. Een ander voorbeeld is wanneer alleen data wordt gebruikt van de personen die daadwerkelijk subsidie ontvangen om het algoritme op te (her)trainen. De groep die geen subsidie ontvangt ontbreekt dan in de dataset.

### Adversarial feedbackloops

Soms kunnen feedbackloops opzettelijk ingezet worden als ‘aanval’ op het systeem. Dit hoeft niet per se vijandig te zijn, maar het kan gaan om het opzettelijk reageren op of aanpassen van de beslissingen die uit een algoritme volgen. Bijvoorbeeld wanneer mensen liegen bij het invullen van een vragenlijst van de GGD wanneer ze een soa-test willen doen, omdat ze weten dat ze dan gekwalificeerd worden voor een gratis test 1. Wanneer de belanghebbende het gedrag aanpast zonder dat zijn of haar kenmerken daadwerkelijk veranderen, omdat het heeft geleerd hoe het algoritme oordeelt, is dat voorbeeld van een adversarial feature feedbackloop. Deze feedbackloops wil je het liefste voorzien en mitigeren.

### Monitoring en ophalen informatie

Feedbackloops kunnen ook een positieve werking hebben op het algoritme. Het is verstandig om feedback op te halen om in te zien wat de reactie is van mensen op (beslissingen van) een algoritme. Dit kan bijvoorbeeld door gebruikers of belanghebbende burgers vragenlijsten te laten invullen met vragen over hun gedrag en de ontwikkelingen hierin te monitoren. Daarnaast kan het ophalen van ervaringen met het algoritme worden gebruikt voor doorontwikkeling en verbetering van het algoritme waarbij de gewenste en ongewenste effecten meegenomen worden.

Ten slotte verdient [bias](../../../onderwerpen/bias-en-non-discriminatie/) specifieke aandacht. Houd goed in de gaten hoe het algoritme gebruikmaakt van de kenmerken van gevoelige groepen en wat de effecten van de uitkomsten zijn op hun gedrag en de datadistributie.

## Risico

Feedbackloops kunnen invloed hebben op verschillende onderdelen van het systeem waarin een algoritme zit. Als dit onopgemerkt gebeurt kan dit een negatief effect hebben op de accuraatheid en betrouwbaarheid van het algoritme, of ongewenste bias ontwikkelen.

## Bijbehorende vereiste(n)

Bekijk alle vereisten

Geen vereisten beschikbaar voor deze maatregel.

## Bronnen

  * [Lucía Vicente, et al., Humans inherit artificial intelligence biases](https://www.nature.com/articles/s41598-023-42384-8)
  * [Nicolò Pagan, et al., A Classification of Feedback Loops and Their Relation to Biases in Automated Decision-Making Systems](https://arxiv.org/abs/2305.06055)
  * [Jonathan Stray, The AI Learns to Lie to Please You: Preventing Biased Feedback Loops in Machine-Assisted Intelligence Analysis](https://www.mdpi.com/2813-2203/2/2/20)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

* * *

  1. Zie https://nos.nl/op3/artikel/2143511-soa-sjoemelaars-liegen-voor-gratis-test ↩

19 februari 2025 19 december 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *geharmoniseerde norm: Een Europese norm die op verzoek van de Commissie is vastgesteld met het oog op de toepassing van harmonisatiewetgeving van de Unie
  *conformiteitsbeoordeling: Het proces waarbij de naleving wordt aangetoond van de voorschriften van hoofdstuk III, afdeling 2 van de AI-Verordening in verband met een AI-systeem met een hoog risico
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
  *AI-bureau: De taak van de Commissie waarbij zij bijdraagt aan de uitvoering van, de monitoring van en het toezicht op AI-systemen en AI-modellen voor algemene doeleinden, en AI-governance, als bepaald in het besluit van de Commissie van 24 januari 2024; verwijzingen in deze verordening naar het AI-bureau worden begrepen als verwijzingen naar de Commissie
  *proceseigenaar: De proceseigenaar is verantwoordelijk voor de kwaliteit van het proces en de vastlegging daarvan in een processchema
  *testdata: data die worden gebruikt voor het verrichten van een onafhankelijke evaluatie van het AI-systeem om de verwachte prestaties van dat systeem te bevestigen voordat het in de handel wordt gebracht of in gebruik wordt gesteld
  *verwerker: Een .. rechtspersoon, een overheidsinstantie, een dienst of een ander orgaan die/dat ten behoeve van de verwerkingsverantwoordelijke persoonsgegevens verwerkt.
  *trainingsdata: data die worden gebruikt voor het trainen van een AI-systeem door de leerbare parameters hiervan aan te passen
  *AI-model voor algemene doeleinden: Een AI-model, ook wanneer het is getraind met een grote hoeveelheid data met behulp van self-supervision op grote schaal, dat een aanzienlijk algemeen karakter vertoont en in staat is op competente wijze een breed scala aan verschillende taken uit te voeren, ongeacht de wijze waarop het model in de handel wordt gebracht, en dat kan worden geïntegreerd in een verscheidenheid aan systemen verder in de AI-waardeketen of toepassingen verder in de AI-waardeketen, met uitzondering van AI-modellen die worden gebruikt voor onderzoek, ontwikkeling of prototypingactiviteiten alvorens zij in de handel worden gebracht.
  *AI-systeem voor algemene doeleinden: Een AI-systeem dat is gebaseerd op een AI- model voor algemene doeleinden en dat verschillende doeleinden kan dienen, zowel voor direct gebruik als voor integratie in andere AI-systemen
  *importeur: Een natuurlijke of rechtspersoon die zich bevindt of gevestigd is in de Unie die een AI-systeem in de handel brengt dat de naam of merknaam van een in een derde land gevestigde natuurlijke of rechtspersoon draagt
  *distributeur: Een andere natuurlijke persoon of rechtspersoon in de toeleveringsketen dan de aanbieder of de importeur, die een AI-systeem in de Unie op de markt aanbiedt
  *gemachtigde: een natuurlijke of rechtspersoon die zich bevindt of gevestigd is in de Unie die een schriftelijke machtiging heeft gekregen en aanvaard van een aanbieder van een AI-systeem of een AI-model voor algemene doeleinden om namens die aanbieder de verplichtingen en procedures van deze verordening respectievelijk na te komen en uit te voeren;
  *discriminatiegrond: Beschermde persoonskenmerken op basis waarvan het maken van onderscheid tussen personen verboden is. Bijvoorbeeld: ras, nationaliteit, religie, geslacht, seksuele gerichtheid, handicap of chronische ziekte.
  *indirect onderscheid: Indien een ogenschijnlijk neutrale bepaling, maatstaf of handelwijze personen met een bepaalde godsdienst, levensovertuiging, politieke gezindheid, ras, geslacht, nationaliteit, hetero- of homoseksuele gerichtheid of burgerlijke staat in vergelijking met andere personen bijzonder treft.
  *objectieve rechtvaardiging: Van een objectieve rechtvaardiging voor onderscheid is sprake wanneer onderscheid een legitiem doel nastreeft en er een redelijke relatie van evenredigheid bestaat tussen het gemaakte onderscheid en het nagestreefde doel.
  *inputdata: data die in een AI-systeem worden ingevoerd of direct door een AI-systeem worden verworven en op basis waarvan het systeem een output genereert
  *gebruiksinstructies: de door de aanbieder verstrekte informatie om de gebruiksverantwoordelijke te informeren over met name het beoogde doel en juiste gebruik van een AI-systeem
  *validatiedata: data die worden gebruikt voor het verrichten van een evaluatie van het getrainde AI-systeem en voor het afstemmen van onder andere de niet-leerbare parameters en het leerproces ervan, om underfitting of overfitting te voorkomen
  *open-source: Open source is een manier van werken waarbij de makers de broncode, documentatie en ontwerp openbaar beschikbaar stellen onder een opensourcelicentie. Hierdoor kan iedereen de software bekijken, kopiëren, aanpassen of delen. Mensen kunnen voorstellen doen voor verbeteringen of toevoegingen.
