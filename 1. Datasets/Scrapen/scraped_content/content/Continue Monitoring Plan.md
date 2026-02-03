---
title: Stel een plan op voor continue monitoring - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-07-plan-continue-monitoring/index.html
scraped_at: 2025-06-12T10:35:09.411944
---

# Stel een plan op voor continue monitoring - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-07-plan-continue-monitoring/index.html

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
    * Bepaal waar je continu op wilt monitoren
    * Bepaal hoe je het gaat meten en welke informatie je hiervoor nodig hebt
    * Bepaal de grenswaarden: bij welke overschrijding moet er actie worden genomen?
    * Bepaal welke acties genomen moeten worden bij een overschrijding
    * Leg vast hoe en aan wie er een waarschuwing wordt gegeven wanneer een waarde wordt overschreden
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Stel een plan op voor continue monitoring

[]( "Vereiste ID")mon-07[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Maak een plan voor wat er continu gemonitored moet worden tijdens het gebruik van het algoritme. Dit plan bevat niet alleen wat en hoe er gemonitored wordt, maar ook bij welke overschrijdingen actie moet worden ondernomen.

## Toelichting

Het plan voor monitoring moet aangeven wat er continu moet worden gemonitored en op welke manier dit moet gebeuren. Daarnaast bevat het plan in welke situaties er actie moet worden ondernomen, en wie daarbij betrokken moet zijn.

Voor het opstellen van het plan voor monitoring zijn de volgende stappen nodig:

### Bepaal waar je continu op wilt monitoren

Denk hierbij aan:

  * [Bias en discriminerende effecten](../5-ver-03-biasanalyse/).
  * Toegankelijkheid van het model (uitvallen of haperingen).
  * Foutmeldingen.
  * Prestaties: [werkt het model nog zoals beoogd](../5-ver-01-functioneren-in-lijn-met-doeleinden/).
  * [Datakwaliteit](../3-dat-01-datakwaliteit/) en data drift (de data die in het systeem wordt ingevoerd kan veranderen over tijd).
  * Invoerwaarden (probeert een gebruiker het systeem te manipuleren).

### Bepaal hoe je het gaat meten en welke informatie je hiervoor nodig hebt

Welke metrieken worden er gebruikt om de vastgelegde aspecten te meten? Welke informatie moet er opgeslagen worden om deze metrieken te kunnen meten? Analyseer ook of er aspecten zijn die niet met metrieken gemeten kunnen worden en hoe je die aspecten kan monitoren.

### Bepaal de grenswaarden: bij welke overschrijding moet er actie worden genomen?

Voor een effectieve monitoring is het van belang dat duidelijk is wanneer er actie moet worden ondernomen op de resultaten. Leg vast voor elk van de aspecten die gemonitored worden bij welke waarden er actie moet worden genomen. Hiervoor is het noodzakelijk om een duidelijke omschrijving te hebben wat de beoogde werking van het systeem is. Het is ook mogelijk om meerdere waarden per monitor te bepalen, waarbij bij een eerste overschrijding alleen een waarschuwing wordt gegeven en bij een tweede bij het algoritme bijvoorbeeld wordt overgegaan tot het [noodplan](../4-owk-02-stopzetten-gebruik/).

### Bepaal welke acties genomen moeten worden bij een overschrijding

Je legt hier in eerste instantie vast of het algoritme moet worden stopgezet, beperkt moet worden in de inzet of in gebruik kan blijven. Ten tweede bepaal je wat voor andere acties er moeten worden genomen, bijvoorbeeld of er een nieuwe uitgebreide evaluatie moet plaatsvinden, moet het algoritme worden bijgewerkt, moet er nieuwe data verzameld worden, moet de beveiliging verbeterd worden of moet er worden overgestapt op plan B.

### Leg vast hoe en aan wie er een waarschuwing wordt gegeven wanneer een waarde wordt overschreden

Om effectief te kunnen ingrijpen is het van belang dat wordt vastgelegd in het monitoringsplan op welke manier er een waarschuwing wordt gegeven, aan wie deze waarschuwing wordt gegeven en welke informatie deze persoon nodig heeft. Bepaal bijvoorbeeld ook of een systeem automatisch wordt uitgeschakeld of dat een mens die keuze moet maken.

Betrek bij het opstellen van dit plan een [diverse groep van belanghebbenden](../1-pba-04-betrek-belanghebbenden/) met onder andere ontwikkelaars, gebruikers en ethisch adviseurs. Zorg dat het evaluatieplan periodiek wordt herzien of deze nog voldoet.

## Risico

Tijdens dagelijks gebruik wil je continu monitoren of het systeem nog werkt zoals beoogd. Wanneer dit niet gebeurt worden mogelijke fouten en veiligheidsrisico’s niet opgemerkt.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-03 - Hoog-risico-AI-systemen zijn voorzien van een risicobeheersysteem](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-03-risicobeheersysteem/)
[aia-18 - Als een hoog-risico-AI-systeem niet voldoet aan de AI-verordening, grijpt de aanbieder in](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-18-corrigerende-maatregelen-voor-non-conforme-ai/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)
[aia-34 - Hoog-risico-AI-systemen zijn voorzien van een monitoringsysteem](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-34-monitoring-na-het-in-de-handel-brengen/)

## Bronnen

  * [Toetsingskader Algemene Rekenkamer, 2.14](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Toetsingskader risicoprofilering – Normen tegen discriminatie op grond van ras en nationaliteit, College voor de Rechten van de Mens](https://publicaties.mensenrechten.nl/publicatie/4093c026-ae41-4c1d-aa78-4ce0e205b5de)

## Voorbeelden

Gemeente Montferland - Montferland AI

De gemeente Montferland heeft een chatbot (MAI) ontwikkeld voor het beantwoorden van algemene vragen. Op deze manier is algemene informatie binnen de gemeente 24/7 bereikbaar voor haar inwoners en worden de medewerkers ontlast van de live chat. Om privacy te waarborgen wordt MAI continu via een automatisch systeem op locatie gemonitored via het controleren van de logbestanden per chat. Als in dit logbestand privacygevoelige informatie gesignaleerd wordt, wordt er direct melding van gemaakt. In dat geval wordt een mail verstuurd naar de servicedesk, systeembeheer en naar de hoofdontwikkelaar van MAI. Daarnaast wordt er een incident aangemaakt door de servicedesk en wordt het incident getoond op het grote scherm bij de systeembeheerders.

Bron: [Mai (Montferland AI) - Gemeente Montferland](https://algoritmes.overheid.nl/nl/algoritme/mai-montferland-ai-gemeente-montferland/96671359)

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
  *direct onderscheid: Indien een persoon op een andere wijze wordt behandeld dan een ander in een vergelijkbare situatie wordt, is of zou worden behandeld, op grond van godsdienst, levensovertuiging, politieke gezindheid, ras, geslacht, nationaliteit, hetero- of homoseksuele gerichtheid of burgerlijke staat;
  *bijzondere categorieën persoonsgegevens: de categorieën persoonsgegevens als bedoeld in artikel 9, lid 1, van Verordening (EU) 2016/679, artikel 10 van Richtlijn (EU) 2016/680 en artikel 10, lid 1, van Verordening (EU) 2018/1725
  *operator: een aanbieder, productfabrikant, gebruiksverantwoordelijke, gemachtigde, importeur of distributeur
