---
title: Toets en analyseer of de inputvariabelen of risicoindicatoren geschikt zijn voor het beoogde algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-02-toetsen-geschiktheid-variabelen/index.html
scraped_at: 2025-06-12T10:34:15.297732
---

# Toets en analyseer of de inputvariabelen of risicoindicatoren geschikt zijn voor het beoogde algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-02-toetsen-geschiktheid-variabelen/index.html

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
  * Bijbehorende vereiste(n)
  * Risico
  * Bronnen
  * Voorbeeld

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Toets en analyseer of de inputvariabelen of risicoindicatoren geschikt zijn voor het beoogde algoritme

[]( "Vereiste ID")dat-02[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../levenscyclus/ "Levencyclus")[Verificatie en validatie](../../../levenscyclus/verificatie-en-validatie/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../rollen/ "Rollen")[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)

## Maatregel

Toets en analyseer of de inputvariabelen of risicoindicatoren geschikt zijn voor de beoogde toepassing.

## Toelichting

Analyseer welke variabelen en risicoindicatoren geschikt en wenselijk zijn om te gebruiken als inputdata voor het beoogde algoritme.

Opmerking

Deze maatregel is specifiek relevant voor de situatie van risicoprofilering. Maar ook voor andere toepassingen zijn deze stappen aanbevolen.

Doorloop voor iedere potentiële indicator de volgende stappen:

  1. Ga na of het wettelijk gezien is toegestaan om de variabele te gebruiken voor de beoogde toepassing:

    * De [Algemene Wet Gelijke Behandeling](https://wetten.overheid.nl/BWBR0006502/2020-01-01) verbiedt het directe onderscheid op basis van verschillende kenmerken die bijvoorbeeld relatie hebben met ras of nationaliteit.
    * De [Algemene Verordening Gegevensbescherming](https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/avg-algemeen/de-avg-in-het-kort) verbiedt het onrechtmatig verwerking van persoonsgegevens.
  2. Ga na of de variabele of indicator een proxy is voor [kwetsbare groepen](../2-owp-08-kwetsbare-groepen/). Controleer bijvoorbeeld of er een correlatie bestaat tussen de variabele en nationaliteit of ras, of maak gebruik van bestaande (wetenschappelijke) inzichten uit bijvoorbeeld openbare data. Wanneer je data wilt verwerken om deze proxy's te onderzoeken, houdt dan rekening met geldende wet- en regelgeving. Het verzamelen en verwerken van data over kwetsbare groepen kan in strijd zijn met privacy vereisten uit bijvoorbeeld de Algemene Verordening Gegevensbescherming. Het is daarom van belang om duidelijk afwegingen te maken tussen privacy en het analyseren van proxy's die rekening houdt met de juridische en ethische vereisten.

  3. Bepaal of de [datakwaliteit](../3-dat-01-datakwaliteit/) van de variabele of indicator voldoende is. Bepaal of de beschikbare data voldoende representatief is voor het fenomeen dat bedoeld wordt.

  4. Ga na of de variabele of indicator een _statistisch_ verband heeft met het [beoogde doel](../1-pba-02-formuleren-doelstelling/). Maak hiervoor gebruik van een [aselecte steekproef](../6-imp-02-aselecte-steekproeven/) uit de relevante populatie om de hypothese dat de variabele verband heeft met het beoogde doel statistisch te toetsen. Toets of dit verband significant is.

  5. Ga na of de variabele of indicator een _inhoudelijk_ verband heeft met het [beoogde doel](../1-pba-02-formuleren-doelstelling/). Naast een statistisch verband kan ook een inhoudelijk verband bijdragen om het gebruik van de indicator te rechtvaardigen.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[grw-02 - Algoritmes discrimineren niet](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/)
[avg-01 - Persoonsgegevens worden op een rechtmatige manier verwerkt](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-01-persoonsgegevens-worden-rechtmatig-verwerkt/)
[avg-04 - Persoonsgegevens en andere data verwerken gebeurt proportioneel en subsidiair](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-04-proportionaliteit-en-subsidiariteit/)
[avg-10 - Besluiten die levens kunnen beïnvloeden, zijn niet volledig geautomatiseerd](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-10-recht-op-niet-geautomatiseerde-besluitvorming/)

## Risico

Indien de variabelen niet voldoende worden getoetst op geschikheid bestaat het risico dat deze variabelen onrechtmatig worden gebruikt, of dat het gebruik van deze variabelen leidt tot nadelige effecten. Dit kan leiden tot discriminerende effecten van het algoritme.

## Bronnen

  * [Toetsingskader risicoprofilering – Normen tegen discriminatie op grond van ras en nationaliteit, College voor de Rechten van de Mens](../../hulpmiddelen/toetsingskader-risicoprofilering/)
  * [Advies geautomatiseerde besluitvorming, Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/documenten/advies-geautomatiseerde-besluitvorming)

## Voorbeeld

Heb je een voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

20 februari 2025 20 februari 2025

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
