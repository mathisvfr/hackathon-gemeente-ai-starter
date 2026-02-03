---
title: Ontwerp en train het algoritme om bestand te zijn tegen (cyber)aanvallen - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-09-adversarial-aanvallen/index.html
scraped_at: 2025-06-12T10:34:38.064138
---

# Ontwerp en train het algoritme om bestand te zijn tegen (cyber)aanvallen - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-09-adversarial-aanvallen/index.html

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
    * Poisoning aanval
    * Input- of evasion aanval
    * Backdoor
    * Model stealing
    * Inversion of inference aanval
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Ontwerp en train het algoritme om bestand te zijn tegen (cyber)aanvallen

[]( "Vereiste ID")owk-09[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Ontwerp en train het algoritme om bestand te zijn tegen adversarial aanvallen.

## Toelichting

De impact van een adversarial AI-aanval hangt af van de [mate van autonomie](../../ai-verordening/#ai-systeem) waarmee een algoritme wordt ingezet. Een algemene impact-beperkende maatregel is daarom om menselijke gebruikers duidelijke instructies mee te geven om de uitkomsten van de algoritmes te controleren.

Voor de verschillende types adversarial AI-aanvallen zijn specifieke maatregelen mogelijk:

### Poisoning aanval

Bij een poisoning aanval wordt het AI-systeem vergiftigd doordat een aanvaller aanpassingen aan de trainingsdata doet, waardoor het AI-systeem fouten gaat maken. Bijvoorbeeld een spamfilter die getraind is op gemanipuleerde data en zo bepaalde spam e-mails doorlaat. Maatregelen gericht op het [behoud van de integriteit van de trainingsdata](../3-dat-10-datamanipulatie/) kunnen hiertegen worden ingezet.

### Input- of evasion aanval

Bij een input- of evasion aanval voegt een aanvaller hele kleine bewerkingen toe aan input zodat een AI-systeem wordt misleid: het trekt een foute conclusie. Een voorbeeld hiervan is het plakken van een gele post-it op een stopbord, waardoor een auto met AI gebaseerde omgevingsherkenning het bord niet meer goed kan herkennen en zijn snelheid aanpast. Op evasion aanvallen kan geanticipeerd worden bij het testen van de [robuustheid](../2-owp-33-technische-interventies-robuustheid/) van algoritmes. Bijvoorbeeld door als onderdeel van een [representatieve testomgeving](../5-ver-04-representatieve-testomgeving/) ook rekening te houden met moedwillig, subtiel aangepaste input.

### Backdoor

Een backdoor in een algoritme geeft een aanvaller toegang en/ of de mogelijkheid om deze te manipuleren. Een voorbeeld hiervan is een nummerbord herkenningsalgoritme dat tijdens de ontwikkelfase van een backdoor voorzien is van een aanvaller, waardoor via een speciale toevoeging aan een nummerbord deze niet meer herkend wordt. Maatregelen gericht op controle van verwerking van trainingsdata, gebruik van ontwikkeltools en halffabricaten en het trainingsproces beperken de mogelijkheid om aanvallers backdoors te laten injecteren.

### Model stealing

Bij _model stealing_ of _model reverse engineering_ brengt een aanvaller in kaart hoe een algoritme in elkaar zit. Hierdoor kan een aanvaller het algoritme voor andere doeleinden misbruiken, zoals het vinden van kwetsbaarheden of van _evasion tactieken_ voor het algoritme.

### Inversion of inference aanval

Met _inversion of inference_ aanvallen kan een aanvaller achterhalen wat voor (mogelijk vertrouwelijke) trainingsdata is gebruikt. Zo kunnen gevoelige informatie worden blootgelegd, waaronder privacygevoelige gegevens en intellectueel eigendom.

## Risico

Adversarial AI-aanvallen kunnen leiden tot ongewenste misleiding, manipulatie of uitschakeling van de werking van een algoritme of tot verlies van gevoelige gegevens.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)
[aia-32 - AI-modellen voor algemene doeleinden met systeemrisico’s zijn voldoende beveiligd tegen cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-32-ai-modellen-algemene-doeleinden-systeemrisico-cyberbeveiliging/)
[bio-01 - Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/)
[avg-12 - Data zoals persoonsgegevens zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/)

## Bronnen

  * [Adversarial AI in het cyberdomein, TNO](https://www.tno.nl/nl/newsroom/2023/02/technieken-cyberaanvallen-ai/)
  * [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## Voorbeelden

Sandia: Defending against Adversarial Examples

Adversarial aanvallen zijn er zoals hierboven uitgelegd op verschillende manieren wat er voor zorgt dat per aanval een andere aanpak nodig is. Sandia, een Amerikaanse nationale veiligheidsorganisatie, heeft onderzoek gedaan naar een aantal van deze aanvallen en is met maatregelen gekomen. De meerderheid van deze maatregelen zijn redelijk technisch en kunnen het beste in context geplaatst worden aan de hand van het artikel. Een maatregel daarentegen kan redelijk gemakkelijk uitgevoerd worden en dat is het analyseren van mogelijke risico’s. Sandia geeft drie categoriën aan: _defensible_ , _semi-defensible_ , en _indefensible_ ; respectievelijk verdedigbaar, semi-verdedigbaar en onverdedigbaar. Verdedigbare modellen zijn in de juiste omstandigheden goed te vertrouwen. Semi-verdedigbare modellen hebben minstens één hoog-risico grens waar op een manier omheen gewerkt kan worden. Onverdedigbare modellen geven toegang tot input en output data, vaak zijn dit real-time algoritmes of algoritmes waar de trainingsdata openbaar (toegankelijk) is. In alle drie de gevallen moet voorzichtig worden omgegaan met het ontwerp, maar in het geval van semi-verdedigbaar en onverdedigbaar moet er extra [goed gemonitored worden](../7-mon-07-plan-continue-monitoring/).

Bron: [Defending against Adversarial Examples](https://doi.org/10.2172/1569514)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

10 april 2025 19 december 2024

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
