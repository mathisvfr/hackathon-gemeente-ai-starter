---
title: Maak een noodplan voor het stoppen van het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-02-stopzetten-gebruik/index.html
scraped_at: 2025-06-12T10:34:29.699902
---

# Maak een noodplan voor het stoppen van het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-02-stopzetten-gebruik/index.html

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
    * Leg vast wanneer het algoritme niet meer werkt zoals beoogd
    * Zorg dat beslissingen kunnen worden herzien
    * Leg vast wat de vervolgacties zijn
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Maak een noodplan voor het stoppen van het algoritme

[]( "Vereiste ID")owk-02[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../levenscyclus/ "Levencyclus")[Implementatie](../../../levenscyclus/implementatie/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Governance](../../../onderwerpen/governance/)[](../../../onderwerpen/ "Onderwerp")[Menselijke controle](../../../onderwerpen/menselijke-controle/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Stel een duidelijk proces in voor situaties waarin het algoritme niet meer werkt zoals beoogd. Dit moet bevatten welke personen welke acties moeten doen en hoe er gewerkt wordt zonder het algoritme.

## Toelichting

Er moet gezorgd worden dat er een alternatief plan is voor als het algoritme niet meer werkt zoals beoogd. Dit kan betekenen dat het hele systeem (tijdelijk) wordt stopgezet, dat delen van het systeem (tijdelijk) worden uitgeschakeld of dat er een alternatief systeem gebruikt wordt.

Dit proces bevat in ieder geval de volgende stappen:

### Leg vast wanneer het algoritme niet meer werkt zoals beoogd

  * Leg vast wat de [beoogde werking van het algoritme](../1-pba-02-formuleren-doelstelling/) is.
  * Bepaal of [de geïmplementeerde werking overeenkomt met de vastgelegde beoogde werking](../5-ver-01-functioneren-in-lijn-met-doeleinden/) en wanneer het algoritme gestopt moet worden. Dit gebeurt tijdens een [evaluatie](../7-mon-04-evaluatieplan/) of door de [continue monitoring](../7-mon-07-plan-continue-monitoring/).

### Zorg dat beslissingen kunnen worden herzien

  * Leg vast hoe het mogelijk is na te gaan op welk moment het algoritme stopte met werken zoals beoogd. Wanneer de melding vanuit continue monitoring komt is het vaak duidelijk wanneer deze waarde wordt overschreden. Bij vaste evaluatiemomenten moet dit worden herleid. Zorg dat door middel van het [loggen](../4-owk-04-logging/) van de juiste informatie het mogelijk is te herleiden wanneer het algoritme stopte met werken zoals beoogd.
  * Zorg dat beslissingen die zijn genomen vanaf het moment dat het algoritme stopte met werken zoals beoogd kunnen worden herzien. Indien het algoritme niet direct is gestopt zodra het niet meer werkte zoals beoogd, moet er opnieuw gekeken worden naar de beslissingen die daarna zijn genomen. Leg vast op welke manier deze beslissingen herzien worden.

### Leg vast wat de vervolgacties zijn

  * Leg in een proces vast hoe het gebruik van het algoritme moet worden stopgezet.
  * Leg vast hoe er gewerkt worden zonder het algoritme en wat de impact daarvan is op het werkproces.
  * Leg vast wie er binnen en buiten de organisatie geïnformeerd moeten worden.
  * Het is van belang dat bij het ontwerp van algoritmes er rekening wordt gehouden met dat het werkproces ook zonder het algoritme kan worden uitgevoerd.
  * In het geval van risicoselectie kan er bijvoorbeeld worden teruggevallen op het enkel uitvoeren van een [aselecte steekproef](../6-imp-02-aselecte-steekproeven/) als selectieinstrument.
  * Als blijkt dat het algoritme ongewenst functioneert moeten (technische) maatregelen zijn getroffen waarmee het gebruik daadwerkelijk kan worden stopgezet. Denk hierbij aan een stopknop en [werkinstructies](../6-imp-01-werkinstructies-gebruikers/) hoe het gebruik kan worden beëindigd.
  * Maak aantoonbaar dat deze maatregelen zijn getroffen.
  * De proceseigenaar of een menselijk toezichthouder moet in staat zijn om het algoritme op elk moment te kunnen beëindigen.
  * Het stopzetten van het gebruik van een algoritme mag niet tot gevolg hebben dat betrokkenen niet meer kunnen achterhalen hoe besluiten tot stand zijn gekomen of dat gevolgen niet meer kunnen worden gecorrigeerd als dat noodzakelijk is.

Indien er sprake is van discriminerende effecten van een algoritme, kan je gebruik maken van het [discriminatieprotocol](../0-org-15-discriminatieprotocol/).

## Risico

Als er geen duidelijke acties zijn gedefinieerd, kan dat bijvoorbeeld leiden tot de volgende risico’s: het werkproces komt stil te liggen door een niet-werkend algoritme, er worden verkeerde beslissingen genomen doordat het algoritme nog wordt gebruikt terwijl het niet goed meer werkt of kwaadwillenden hebben langer toegang tot het algoritme en/of organisatiedata.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-18 - Als een hoog-risico-AI-systeem niet voldoet aan de AI-verordening, grijpt de aanbieder in](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-18-corrigerende-maatregelen-voor-non-conforme-ai/)
[awb-01 - Organisaties die algoritmes gebruiken voor publieke taken nemen besluiten zorgvuldig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-01-zorgvuldigheidsbeginsel/)
[aia-11 - Hoog-risico-AI-systemen zijn voorzien van een kwaliteitsbeheersysteem](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-11-systeem-voor-kwaliteitsbeheer/)
[grw-01 - Algoritmes schenden geen grondrechten of mensenrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-01-fundamentele-rechten/)
[aia-27 - Hoog-risico-AI-systemen voor publieke taken worden beoordeeld op gevolgen voor grondrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-27-beoordelen-gevolgen-grondrechten/)
[grw-02 - Algoritmes discrimineren niet](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/)
[aia-19 - Hoog-risico-AI-systemen voldoen aan de toegankelijkheidseisen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-19-toegankelijkheidseisen/)
[aia-09 - Hoog-risico-AI-systemen staan onder menselijk toezicht](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-09-menselijk-toezicht/)
[avg-04 - Persoonsgegevens en andere data verwerken gebeurt proportioneel en subsidiair](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-04-proportionaliteit-en-subsidiariteit/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)

## Bronnen

  * [Onderzoekskader Algoritmes Auditdienst Rijk, SV.18](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 1.03](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Impact Assessment Mensenrechten en Algoritmes, 1.5](../../hulpmiddelen/IAMA/)

## Voorbeelden

Ministerie van Economische Zaken - Uitwijkplan

Het Ministerie van Economische zaken heeft een template voor een Disaster Recovery Plan (DRP) opgesteld. Aan de hand van dit document kunnen duidelijke handelingen en verantwoordelijkheden opgeschreven worden wanneer een algoritme stop gezet moet worden. Dit DRP is vrij algemeen en heeft geen specificaties voor algoritmes in het template staan. Dit zal dus verder uitgewerkt moeten worden, maar dit DRP zou als inspiratie kunnen dienen.

Bron: [Uitwijk- en herstelplan](https://www.digitaltrustcenter.nl/informatie-advies/uitwijk-en-herstelplan)

Heb je een voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl).

19 februari 2025 14 augustus 2024

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
