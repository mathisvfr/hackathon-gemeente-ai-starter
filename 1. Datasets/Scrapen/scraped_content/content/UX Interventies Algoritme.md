---
title: Neem technische interventies op in de gebruikersinterface om verkeerd gebruik te voorkomen - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-09-interventies-ux/index.html
scraped_at: 2025-06-12T10:34:59.776197
---

# Neem technische interventies op in de gebruikersinterface om verkeerd gebruik te voorkomen - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-09-interventies-ux/index.html

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
    * Evaluatie
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Neem technische interventies op in de gebruikersinterface om verkeerd gebruik te voorkomen

[]( "Vereiste ID")imp-09[](../../../levenscyclus/ "Levencyclus")[Implementatie](../../../levenscyclus/implementatie/)[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Menselijke controle](../../../onderwerpen/menselijke-controle/)

## Maatregel

Neem technische interventies op in de gebruikersinterface om verkeerd gebruik te voorkomen.

## Toelichting

Een algoritme wat volledig correcte uitkomsten geeft maar vervolgens verkeerd wordt gebruikt kan leiden tot problemen. Neem bijvoorbeeld een algoritme wat een tekstdocument controleert en voorstelt aan de gebruiker of het compleet is, of nog onderdelen mist. Wanneer je dan een ‘goedgekeurd’ knop rood maakt, en een ‘afgekeurd’ knop groen, is er een kans dat de gebruiker uit gewoonte op de verkeerde klikt en daarmee alsnog een onjuiste beslissing neemt. Als deze keuze vervolgens als feedback ook weer wordt doorgevoerd in het systeem kan het algoritme ook nog verkeerd gedrag aanleren.

Werk bijvoorbeeld aan de hand van [User Centered Design principes](https://www.interaction-design.org/literature/topics/user-centered-design) om de gebruiker centraal te stellen.

### Evaluatie

Breng risico’s in kaart door het goed testen van het systeem in een praktijksetting. Evalueer hier het gedrag van de gebruiker in het grotere systeem.

Onderdelen hiervan zijn:

#### Aandacht van de gebruiker

Oog en muisbewegingen kunnen inzicht geven waar de aandacht van de gebruiker naartoe gaat. Als er bijvoorbeeld een controle gedaan moet worden over de uitkomst van het algoritme voor het maken van een definitieve beslissing wil je inzicht krijgen of de gebruiker naar de juiste elementen kijkt om die beslissing te maken.

#### Interactiegedrag van de gebruiker

Clicks, scrollen, of het gebruik van het algoritme op zich (in plaats van zelf tot een beslissing komen) horen bij het gedrag van de gebruiker. Dit kan inzicht geven of het systeem correct wordt gebruikt, maar ook waar gebruikers mogelijk juist blijven hangen.

#### Feedback mechanismes

  * Zijn er manieren waarop de gebruiker feedback kan geven over de uitkomsten wanneer deze naar vermoeden niet kloppen?
  * Zijn er manieren waarop de gebruiker om hulp kan vragen en wat voor vragen zijn dit?
  * Op wat voor manier worden errors in het systeem doorgegeven aan de gebruiker?

#### Transparantie en uitlegbaarheid

Een correct gebruik begint bij een [duidelijke instructie en inzicht hoe een algoritme werkt](../6-imp-01-werkinstructies-gebruikers/) en hoe daar mee om te gaan. Evalueer of de gebruikte methodes hiervoor hun doel bereiken.

#### Toegankelijkheid

Het is belangrijk om te controleren of het algoritme toegankelijk in gebruik is voor iedereen, inclusief personen met een beperking.

#### Beveiliging en controle

Het onjuist gebruik waarvoor specifiek gedrag opgemerkt kan worden bij bovenstaande evaluaties moet worden gemonitored. Vervolgens kunnen er beveiligingen (denk aan een melding ‘weet je het zeker?’) ingebouwd worden als zulk gedrag wordt geregistreerd. Kijk vervolgens of deze interventies effectief zijn om fouten te voorkomen.

## Risico

Een gebruikersinterface die verkeerd gebruik door gebruikers mogelijk maakt, kan ervoor zorgen dat gebruikers verkeerde invoerwaarden geven, zich niet aan de beoogde werkwijze houden of per ongeluk toegang geven aan kwaadwillenden.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)

## Bronnen

  * [Valid Useful User Experience Measurement ](https://www.academia.edu/28475349/Valid_Useful_User_Experience_Measurement)
  * [7 fundamental user experience (UX) design principles all designers should know (2024) - UX Design Institute](https://www.uxdesigninstitute.com/blog/ux-design-principles/)
  * [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
  * [User Centered Design (UCD)](https://www.interaction-design.org/literature/topics/user-centered-design)

## Voorbeelden

Verschillende overheden – Octobox Anonimiseren

Verschillende overheden maken gebruik van Octobox Anonimiseren, een anonimiseringstool die (persoons)gegevens aanduidt voor maskering. Octobox zoekt deze (persoons)gegevens binnen het document, ongeacht de inhoud. Na deze aanduiding moet er door een vakinhoudelijk persoon gecontroleerd worden of deze gegevens inderdaad gemaskeerd moeten worden of niet. Deze kunnen goed- en afgekeurd worden en ook gewijzigd worden voor goedkeuring. Daarnaast is er de optie om handmatig informatie te maskeren om zo andere (of gemiste) informatie te maskeren. De tool is op deze manier op een intuïtieve manier te gebruiken door medewerkers.

Bron: [Octobox Anonimiseren](https://algoritmes.overheid.nl/nl/algoritme/octobox-anonimiseren-ministerie-van-binnenlandse-zaken-en-koninkrijksrelaties/28793885)

Gemeente Veere – AI-analyse tool

De gemeente Veere heeft een analyse tool voor het versnellen en vergemakkelijken van het verwerken van input bij participatieprocessen. Hierbij worden bijvoorbeeld samenvattingen en categorieën gemaakt om zo de gebruiker te helpen bij het analyseren. De gebruikersinterface zorgt ervoor dat de originele bron data ook standaard mee getoond worden om zo te verduidelijken waar de informatie vandaan komt. Daarnaast worden ook altijd referenties naar bron meegenomen in de samenvattingen. De interface maakt de gebruiker ook bewust van mogelijke fouten of hallucinaties die gemaakt kunnen worden door waarschuwingen te tonen.

Bron: [AI-analyse tool (AI Sensemaking) - Gemeente Veere](https://algoritmes.overheid.nl/nl/algoritme/aianalyse-tool-ai-sensemaking-gemeente-veere/62557610)

Gemeente Ede – WOZ-Taxatiemodellen

De gemeente Ede heeft een algoritme in gebruik als ondersteuning bij het bepalen (en controleren) van de WOZ-waarde van woningen. Dit wordt gedaan aan de hand van Machine Learning modellen die op basis van onder andere woning- en locatiekenmerken gecombineerd met markt- en verkoop condities de WOZ-waarde kan bepalen. Hierbij wordt bepaald welke kenmerken het meeste gewicht hebben voor deze bepaling.

Als de taxateurs de WOZ-waarde gaan bepalen, zien zij ook de algoritmisch bepaalde waarde. Hierbij is aan de hand van kleuren de zekerheid van de waarde aangegeven. Groen geeft een hoge zekerheid aan, oranje een redelijke zekerheid en rood een matige zekerheid. Op deze manier wordt voor taxateurs direct duidelijk en intuïtief wat de waarden inhouden.

Bron: [WOZ-Taxatiemodellen](https://algoritmes.overheid.nl/nl/algoritme/woztaxatiemodellen-gemeente-ede/39323486)

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
