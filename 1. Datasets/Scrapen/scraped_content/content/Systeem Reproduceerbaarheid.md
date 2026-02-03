---
title: Zorg voor reproduceerbaarheid van de uitkomsten - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-07-reproduceerbaarheid/index.html
scraped_at: 2025-06-12T10:34:35.668930
---

# Zorg voor reproduceerbaarheid van de uitkomsten - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-07-reproduceerbaarheid/index.html

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
    * Bepaal welke mate van reproduceerbaarheid nodig is
    * Implementeer verschillende stappen die bijdragen aan reproduceerbaarheid
    * Test of het algoritme het gewenste niveau van reproduceerbaarheid heeft
    * Generatieve AI
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Zorg voor reproduceerbaarheid van de uitkomsten

[]( "Vereiste ID")owk-07[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Transparantie](../../../onderwerpen/transparantie/)

## Maatregel

Zorg ervoor dat uitkomsten van het algoritme herhaald of herleid kunnen worden.

## Toelichting

De reproduceerbaarheid omschrijft of de resultaten van een algoritme herhaald of herleid kunnen worden. Het betekent dat dezelfde input leidt tot dezelfde output in alle situaties. In ieder geval moet het algoritme dezelfde werking vertonen.

Reproduceerbaarheid is sterk gelinkt aan herleidbaarheid en traceerbaarheid. Uitkomsten moeten altijd herleid kunnen worden aan de hand van het model en de data.

Om te zorgen voor reproduceerbaarheid van de uitkomsten, kan je de volgende stappen nemen:

  1. Bepaal welke mate van reproduceerbaarheid nodig is
  2. Implementeer verschillende stappen die bijdragen aan reproduceerbaarheid
  3. Test of het algoritme het gewenste niveau van reproduceerbaarheid heeft

### Bepaal welke mate van reproduceerbaarheid nodig is

Afhankelijk van de toepassing moeten de resultaten van het algoritme precies te reproduceren zijn. Wanneer er gebruik wordt gemaakt van generatieve AI hoeft de output niet altijd exact hetzelfde te zijn.

### Implementeer verschillende stappen die bijdragen aan reproduceerbaarheid

Om te zorgen dat uitkomsten reproduceerbaar zijn, implementeer je het volgende in je processen en systemen:

  * Zorg voor versiebeheer op de code en de bijbehorende systemen. Dit geldt zowel tijdens ontwikkeling als tijdens operatie. Tools als [GitHub](https://github.com/) of [GitLab](https://about.gitlab.com/) kunnen ondersteunen bij versiebeheer van code.
  * Zorg dat de data (trainings- en testdata) kan worden gereproduceerd. Maak gebruik van versiebeheer op de data, maak backups van de data, sla snapshots van de data op en maak gebruik van timestamps.
  * Documenteer wijzigingen aan het algoritme of de systemen daaromheen.
  * Beheer afhankelijkheden van software bibliotheken en de beschikbare versies. Verschillende versies van veelgebruikte open-source software bibliotheken kunnen leiden tot verschillende resultaten. Gebruik bijvoorbeeld tools als [Docker](https://www.docker.com/) om deze versies te beheren.
  * Logging van tussenresultaten, eindresultaten, parameters en andere benodigde informatie.
  * Houd de documentatie compleet en compact.

### Test of het algoritme het gewenste niveau van reproduceerbaarheid heeft

Het is belangrijk om het algoritme te testen op de mate van reproduceerbaarheid. Dit kan je doen door:

  * Experimenten meerdere keren te herhalen.
  * Te testen of kan worden achterhaald hoe een bepaald resultaat tot stand is gekomen. Is het duidelijk welke data is gebruikt, en welke versie van het algoritme is gebruikt? Test of het resultaat op basis van deze informatie opnieuw kan worden gegenereerd.
  * Rekening te houden met willekeur in het systeem. Dit is bijvoorbeeld relevant wanneer er gebruikt wordt gemaakt van _seeds_ en/ of _random number generators_. Experimenteer wat de invloed is van verschillende seeds op de uitkomsten, en analyseer of het systeem dezelfde resultaten geeft voor een vaste seed. Indien van belang, documenteer de seed die gebruikt wordt.
  * Test of een versie van het algoritme opnieuw gereconstrueerd kan worden op basis van de gedocumenteerde informatie:

    * trainingsdata
    * parameters
    * versies van gebruikte software (softwarebibliotheken)
    * etc.

### Generatieve AI

Bij generatieve AI is het vaak lastiger om de reproduceerbaarheid te testen. Je kunt het volgende doen om dit risico te beperken:

  * Maak gebruik van open applicaties of modellen, waar mogelijk open source-applicaties en -modellen. Deze bieden meer inzicht op het gebied van transparantie. Let wel op dat deze transparantie niet ten koste mag gaan van de veiligheid.
  * Test wat de uitkomsten zijn voor dezelfde of heel vergelijkbare prompts, en controleer of deze exact of nagenoeg hetzelfde zijn.

## Risico

Wanneer uitkomsten niet herhaald kunnen worden, kan er niet worden gegarandeerd dat vergelijkbare casussen tot vergelijkbare uitkomsten komen. Dit maakt de uitkomsten van het algoritme mogelijk oneerlijk. Wanneer een herhaald experiment niet tot dezelfde uitkomsten leidt, kan het experiment niet vertrouwd worden. Als uitkomsten niet herleid kunnen worden, kan er geen uitleg worden gegeven waarom een bepaalde beslissing tot stand is gekomen. Hierdoor kan geen verantwoording worden geboden.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)

## Bronnen

  * [Onderzoekskader Auditdienst Rijk, DM.14](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [MLOps Principles: Reproducability](https://ml-ops.org/content/mlops-principles#reproducibility)
  * [Ministerie van Infrastructuur en Waterstaat, AI Impact Assessment](https://www.rijksoverheid.nl/documenten/rapporten/2022/11/30/ai-impact-assessment-ministerie-van-infrastructuur-en-waterstaat)
  * [Harald Semmelrock, et al., Reproducibility in Machine Learning-Driven Research](https://arxiv.org/abs/2307.10320)
  * [Odd Erik Gundersen, et al., Do machine learning platforms provide out-of-the-box reproducibility?](https://www.sciencedirect.com/science/article/pii/S0167739X21002090)
  * [Odd Erik Gundersen, et al., State of the Art: Reproducibility in Artificial Intelligence ](https://ojs.aaai.org/index.php/AAAI/article/view/11503)

## Voorbeelden

Dienst Toeslagen: Populatiebepaling Kindregeling

De Dienst Toeslagen maakt gebruik van een algoritme als ondersteuning om in kaart te brengen welke (pleeg)kinderen in aanmerking komen voor een tegemoetkoming van de kindregeling. Op deze manier kan efficiënter, nauwkeuriger en consistenter herkend worden wie hier voor in aanmerking komen. Om er voor te zorgen dat deze bepaling reproduceerbaar is wordt gebruik gemaakt van versie-beheer. Hierbij worden wijzigingen in de populatie doorgevoerd en bijgehouden. Hiernaast wordt ook aanvullende informatie die tijdens de kritieke periode bekend was in een aparte kolom gezet om zo reproduceerbaarheid te kunnen garanderen.

Bron: [Populatiebepaling kindregeling - Dienst Toeslagen](https://algoritmes.overheid.nl/nl/algoritme/populatiebepaling-kindregeling-dienst-toeslagen/34319693)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

22 april 2025 19 december 2024

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
