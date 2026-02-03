---
title: Maak waardevolle data vindbaar, toegankelijk, interoperabel en herbruikbaar (FAIR) binnen en buiten de eigen organisatie - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-12-fair-data/index.html
scraped_at: 2025-06-12T10:34:27.315475
---

# Maak waardevolle data vindbaar, toegankelijk, interoperabel en herbruikbaar (FAIR) binnen en buiten de eigen organisatie - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-12-fair-data/index.html

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
    * 15 principes voor FAIR data
  * Risico
  * Vereisten
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Maak waardevolle data vindbaar, toegankelijk, interoperabel en herbruikbaar (FAIR) binnen en buiten de eigen organisatie

[]( "Vereiste ID")dat-12[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)

## Maatregel

Maak waardevolle data vindbaar, toegankelijk, interoperabel en herbruikbaar (FAIR) binnen en buiten de eigen organisatie.

## Toelichting

De internationale [FAIR-principes](https://www.gofair.foundation/) zijn richtlijnen voor de manier van beschrijven, opslag en publicatie van data.

  * **Findable** (vindbaar): metadata moet gemakkelijk te vinden zijn voor zowel mensen als computers.
  * **Accessible** (toegankelijk): gebruikers moeten weten hoe toegang tot de data verkregen kan worden (autorisatie en authenticatie).
  * **Interoperable** (uitwisselbaar): data moet meestal geïntegreerd worden met andere data en bijbehorende applicaties, opslag en processen.
  * **Reusable** (herbruikbaar): het uiteindelijke doel van FAIR is om hergebruik van data te optimaliseren.

Wanneer je voldoet aan de 15 principes is je data 'machine actionable'. Dit maakt het mogelijk dat de data effectief gebruikt kan worden voor verschillende algoritmes.

FAIR data betekent niet per definitie dat data open data is. Juist ook voor (privacy) gevoelige data (gesloten data) kan het heel zinvol zijn om te voldoen aan de principes voor FAIR data, om juist daarmee specifieke geautoriseerde toegang tot gevoelige data mogelijk te kunnen maken.

### 15 principes voor FAIR data

Er zijn 15 principes voor FAIR data geformuleerd:

#### Findable (vindbaar)

  * [F1: Aan (meta)data wordt een wereldwijd unieke en permanente identifier toegevoegd](https://www.gofair.foundation/f1)

Voorbeeld

Met behulp van [Persistent Identifiers (PID)](https://www.surf.nl/diensten/persistent-identifiers) zorg je ervoor dat jouw data (bijvoorbeeld onderzoeksdata) altijd vindbaar blijft. PID's kun je vergelijken met het ISBN-nummer bij boeken. Het idee is dat ook als de locatie of de onderliggende infrastructuur verandert, de verwijzing intact blijft.

  * [F2: Data wordt beschreven met rijke metadata](https://www.gofair.foundation/f2)

Voorbeeld

Het team van [data.overheid.nl](https://data.overheid.nl/) heeft de metadata standaard [DCAT-AP-DONL](https://docs.datacommunities.nl/data-overheid-nl-documentatie/dcat/dcat-ap-donl) ontwikkeld die speciaal voor de uitwisseling van dataset informatie voor de Nederlandse situatie is ingericht. Dit is gebaseerd op de [Data Catalog Vocabulary (DCAT) versie](https://www.w3.org/TR/vocab-dcat/) die de Europese Unie heeft opgesteld. Je kan hierover meer lezen op de site van [data.overheid.nl](https://data.overheid.nl/ondersteuning/open-data/dcat).

  * [F3: Metadata bevat duidelijk en expliciet de identificatie van de data die ze beschrijven](https://www.gofair.foundation/f3)

  * [F4: (Meta)data worden geregistreerd of geïndexeerd in een doorzoekbare bron](https://www.gofair.foundation/f4)

#### Accessible (toegankelijk)

  * [A1: (Meta)data zijn opvraagbaar op basis van hun identificatiecode met behulp van een gestandaardiseerd communicatieprotocol](https://www.gofair.foundation/a1)
  * [A1.1: Het protocol is open, vrij en universeel implementeerbaar](https://www.gofair.foundation/a1-1)
  * [A1.2: Het protocol maakt waar nodig een authenticatie- en autorisatieprocedure mogelijk](https://www.gofair.foundation/a1-2)
  * [A2: Metadata zijn toegankelijk, ook als de data niet meer beschikbaar zijn](https://www.gofair.foundation/a2)

#### Interoperable (uitwisselbaar)

  * [I1: (Meta)data gebruikt een formele, toegankelijke, gedeelde en breed toepasbare taal voor kennisrepresentatie](https://www.gofair.foundation/i1)
  * [I2: (Meta)data gebruikt gegevenswoordenboeken of vocabulaires die FAIR-principes volgen](https://www.gofair.foundation/i2)

Voorbeeld woordenboek

In het [woordenboek Hitte](https://woordenboek.klimaatadaptatienederland.nl/hitte/nl/) staan ongeveer 230 definities van termen rond het thema hitte die gebruikt worden in het klimaatadaptatieveld. Dit woordenboek is ontwikkeld in opdracht van het ministerie van Infrastructuur en Waterstaat door overheidsstichting Geonovum.

  * [I3: (Meta)data bevat gekwalificeerde verwijzingen naar andere (meta)data](https://www.gofair.foundation/i3)

#### Reusable (herbruikbaar)

  * [R1: (Meta)data wordt rijkelijk beschreven met een veelheid aan nauwkeurige en relevante attributen](https://www.gofair.foundation/r1)
  * [R1.1: (Meta)data wordt vrijgegeven met een duidelijke en toegankelijke licentie voor datagebruik](https://www.gofair.foundation/r1-1)
  * [R1.2: (Meta)data wordt geassocieerd met gedetailleerde herkomst](https://www.gofair.foundation/r1-1)

Voorbeeld

[PROV-DM](https://www.w3.org/TR/prov-dm/) is een conceptueel datamodel dat gebruikt kan worden voor de herkomstinformatie (provenance) van data.

  * [R1.3: (Meta)data voldoet aan domein-relevante normen](https://www.gofair.foundation/r1-3)

## Risico

Data is niet gebruiksvriendelijk en het is onduidelijk hoe de data hergebruikt kan worden wat kan leiden tot inefficiënt datagebruik.

## Vereisten

Bekijk alle vereisten

Geen vereisten beschikbaar voor deze maatregel.

Opmerking

[Artikel 5b van de Wet hergebruik van overheidsinformatie](https://wetten.overheid.nl/jci1.3:c:BWBR0036795&hoofdstuk=III&paragraaf=3.1&artikel=5b&z=2024-06-19&g=2024-06-19) stelt dat onderzoeksgegevens in overeenstemming met de FAIR-beginselen actief beschikbaar moeten worden gesteld voor hergebruik door een publiek gefinancierde onderzoeksorganisatie. Dit geldt voor zover:

  1. Die documenten zijn geproduceerd in het kader van geheel of gedeeltelijk met overheidsmiddelen gefinancierde wetenschappelijke onderzoeksactiviteiten;
  2. Die documenten openbaar zijn gemaakt via een institutionele of thematische databank als bedoeld in artikel 10, tweede lid, van de richtlijn; en
  3. Rechtmatige handelsbelangen, activiteiten inzake kennisoverdracht en reeds bestaande intellectuele eigendomsrechten zich hiertegen niet verzetten.

## Bronnen

  * [GO FAIR Foundation](https://www.gofair.foundation/interpretation)
  * [3-point FAIRification framework 3PFF](https://www.go-fair.org/how-to-go-fair/)
  * [Toolbox verantwoord datagebruik, 2b](https://realisatieibds.nl/page/view/ff607c02-9f09-440a-a0e7-9bbb6c7ceb09/3-data-verzamelen)
  * [NORA online](https://www.noraonline.nl)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

20 februari 2025 4 oktober 2024

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
