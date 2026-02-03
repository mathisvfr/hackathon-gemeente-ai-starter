---
title: Zorg dat (gevoelige) informatie niet kan lekken op basis van de output van het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-10-voorkom-lekken-op-basis-van-output/index.html
scraped_at: 2025-06-12T10:34:39.289800
---

# Zorg dat (gevoelige) informatie niet kan lekken op basis van de output van het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-10-voorkom-lekken-op-basis-van-output/index.html

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
    * Technieken voor voorkomen van lekken
    * Statistical Disclosure Control
    * k-anonimity
    * Differential privacy
    * Rate limiting
  * Transparantie vs veiligheidsrisico
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Zorg dat (gevoelige) informatie niet kan lekken op basis van de output van het algoritme

[]( "Vereiste ID")owk-10[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../levenscyclus/ "Levencyclus")[Implementatie](../../../levenscyclus/implementatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Zorg dat (gevoelige) informatie niet kan lekken op basis van de output van het algoritme.

## Toelichting

Een aanvaller kan aan de hand van de uitkomsten van een model proberen om bepaalde eigenschappen over het model of de dataset te achterhalen. In de [brochure van de AIVD](https://www.aivd.nl/documenten/publicaties/2023/02/15/ai-systemen-ontwikkel-ze-veilig) wordt specifiek gewaarschuwd voor “ _model engineering_ ”, “ _model inversion_ ” en “ _inference_ ” aanvallen.

  * **Model engineering** refereert naar aanvallen die als bedoeling hebben om te achterhalen hoe het model werkt. Dit kan bijvoorbeeld als doel hebben om intellectueel eigendom te stelen of om effectiever zwakheden in het model te kunnen onderzoeken.

  * **Model inversion** beschrijft aanvallen waarbij het doel is om de trainingsdata te reconstrueren. Dit kan wederom interessant zijn voor het stelen van intellectueel eigendom, maar ook het achterhalen van privé gegevens als het bijvoorbeeld om een medische dataset gaat.

  * **Inference** aanvallen zijn ook gericht op het achterhalen van informatie over de trainingsdata. In tegenstelling tot model inversion is het doel niet om de gehele trainingsdata terug te krijgen, maar specifieke informatie. Zo kan het doel bijvoorbeeld zijn om te achterhalen of een bepaald persoon onderdeel was van de trainingsdata of kan met een deel van de informatie over een persoon geprobeerd worden om missende informatie te achterhalen. Dit type aanvallen is vaak makkelijker uit te voeren van een volledige model inversion.

### Technieken voor voorkomen van lekken

### Statistical Disclosure Control

Statistical Disclosure Control (SDC) is een veelgebruikte techniek om ervoor te zorgen dat er geen gevoelige informatie lekt uit de uitkomst van een datagedreven onderzoek. Alhoewel SDC vooral gericht is op traditionele data-analyses kan het ook gebruikt worden in de context van algoritmes. Er zijn verschillende voorbeelden hoe SDC kan worden toegevoegd aan een AI-systeem, zoals [The SACRO-ML package](https://arxiv.org/abs/2212.01233).

### k-anonimity

Daarnaast bestaan er ook nieuwere technieken die kunnen helpen bij het onherkenbaar maken van mogelijk gevoelige informatie in de outputs van algoritmes. Zo zijn er technieken gebaseerd op het generaliseren van data om individuen onherkenbaar te maken, zoals [k-anonimity](https://dl.acm.org/doi/10.1142/s0218488502001648).

### Differential privacy

Ook bestaan er technieken die ruis toevoegen aan de uitkomst, met wiskundige garanties van de veiligheid. De meest populaire techniek voor het toevoegen van ruis is [differential privacy](https://dl.acm.org/doi/10.1007/11787006_1).

### Rate limiting

De hierboven benoemde oplossingen focussen op het beveiligen van één output van het algoritme. Veel aanvallen berusten echter ook op het veelvuldig aanroepen van een algoritme. Een andere oplossing die dit tegen kan gaan is het limiteren van het aantal interacties dat een gebruiker mag hebben met een algoritme, ook wel bekend als _rate limiting_.

## Transparantie vs veiligheidsrisico

Tot slot moet er ook afgewogen worden op welke manier [transparantie](../../../onderwerpen/transparantie/) van het algoritme leidt tot extra veiligheidsrisico’s. Intuïtief kan een aanvaller makkelijker dingen te weten komen over een algoritme als er informatie gepresenteerd wordt over waarom bijvoorbeeld een AI-systeem een bepaalde keuze maakt. Zo is een veelgebruikte techniek voor inference aanvallen om te kijken hoe 'zeker' een model is voor een bepaalde input. Een beslissing met hoge zekerheid duidt er in veel gevallen op dat de input inderdaad in de trainingsdata zat. Ook het gebruik van explainable AI kan leiden tot extra veiligheidsrisico’s. Zo kan een uitleg gebaseerd op een tegenvoorbeeld makkelijk informatie over een persoon lekken als deze het tegenvoorbeeld is. In 2024 is er [een overzicht van bekende gevaren van specifieke uitlegbaarheidstechnieken](https://arxiv.org/abs/2404.00673).

## Risico

Als een gebruiker teveel informatie te zien krijgt kan dit bijvoorbeeld leiden tot het lekken van trainingsdata of eigenschappen van het algoritme.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)
[aia-32 - AI-modellen voor algemene doeleinden met systeemrisico’s zijn voldoende beveiligd tegen cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-32-ai-modellen-algemene-doeleinden-systeemrisico-cyberbeveiliging/)
[bio-01 - Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/)
[avg-12 - Data zoals persoonsgegevens zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/)

## Bronnen

  * [Smith, et al., Safe machine learning model release from Trusted Research Environments: The SACRO-ML package](https://arxiv.org/abs/2212.01233)
  * [Sweeney, et al., k-anonymity: a model for protecting privacy](https://dl.acm.org/doi/10.1142/s0218488502001648)
  * [Dwork, et al., Differential privacy](https://dl.acm.org/doi/10.1007/11787006_1)
  * [Nguyen, et al., A Survey of Privacy-Preserving Model Explanations: Privacy Risks, Attacks, and Countermeasures](https://arxiv.org/abs/2404.00673)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

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
