---
title: Privacy en persoonsgegevens beschermen in algoritmes - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/onderwerpen/privacy-en-gegevensbescherming/
scraped_at: 2025-06-12T10:33:46.544578
---

# Privacy en persoonsgegevens beschermen in algoritmes - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/onderwerpen/privacy-en-gegevensbescherming/

---

[ ![Home Algoritmekader](../../assets/logo.svg) ](../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../soorten-algoritmes-en-ai/)
  * Onderwerpen  Onderwerpen
    * [ Onderwerpen  ](../)

Onderwerpen
      * [ Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes  ](../bias-en-non-discriminatie/)
      * [ Verantwoord datagebruik  ](../data/)
      * [ Duurzaam werken met algoritmes  ](../duurzaamheid/)
      * [ Grondrechten beschermen in algoritmes  ](../fundamentele-rechten/)
      * [ Governance van algoritmes binnen je organisatie  ](../governance/)
      * [ Menselijke controle over algoritmes  ](../menselijke-controle/)
      * Privacy en persoonsgegevens beschermen in algoritmes  [ Privacy en persoonsgegevens beschermen in algoritmes  ](./) Inhoudsopgave
        * Wat is het beschermen van privacy en persoonsgegevens in algoritmes?
        * Rechtmatig persoonsgegevens gebruiken
        * Belang van privacy en persoonsgegevens beschermen
        * Vereisten
        * Aanbevolen maatregelen
        * Aanbevolen hulpmiddelen
        * Help ons deze pagina te verbeteren
      * [ Inkoop van verantwoorde algoritmes  ](../publieke-inkoop/)
      * [ Technische robuustheid en veiligheid  ](../technische-robuustheid-en-veiligheid/)
      * [ Transparant zijn over algoritmes  ](../transparantie/)
  * [ Levenscyclus  ](../../levenscyclus/)
  * [ Rollen  ](../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../voldoen-aan-wetten-en-regels/)

Inhoudsopgave

  * Wat is het beschermen van privacy en persoonsgegevens in algoritmes?
  * Rechtmatig persoonsgegevens gebruiken
  * Belang van privacy en persoonsgegevens beschermen
  * Vereisten
  * Aanbevolen maatregelen
  * Aanbevolen hulpmiddelen
  * Help ons deze pagina te verbeteren

  1. [ Onderwerpen  ](../)
  2. [ Onderwerpen  ](../)

# Privacy en persoonsgegevens beschermen in algoritmes

Overheden die algoritmes gebruiken, moeten de persoonsgegevens van burgers beschermen. Hiervan gebruik je niet meer dan nodig is. En je beveiligt deze gegevens goed.

## Wat is het beschermen van privacy en persoonsgegevens in algoritmes?

Overheidsalgoritmes mogen persoonsgegevens gebruiken als hier een grondslag voor is, bijvoorbeeld omdat de verwerking wordt voorgeschreven in specifieke wetgeving of wanneer de verwerking noodzakelijk is voor een specifieke wettelijke taak. En wanneer je netjes omgaat met hun persoonsgegevens. Dit betekent:

  * [Verantwoord gebruik van data](../data/), zoals [rechtmatig persoonsgegevens](../../voldoen-aan-wetten-en-regels/vereisten/avg-01-persoonsgegevens-worden-rechtmatig-verwerkt/) gebruiken
  * [Beveiligen](../technische-robuustheid-en-veiligheid/) van persoonsgegevens
  * [Transparant](../transparantie/) zijn over het gebruik van persoonsgegevens

Als overheid moet je hier goed op letten. Doe dit zo vroeg mogelijk in de [levenscyclus](../../levenscyclus/) van het algoritme.

## Rechtmatig persoonsgegevens gebruiken

Als je persoonsgegevens gebruikt voor algoritmes, moet je rekening houden met wetgeving, zoals de Algemene Verordening Gegevensbescherming (AVG) en de Auteurswet. De belangrijkste regels zijn:

  * Gebruik alleen persoonsgegevens die je mag gebruiken voor het doel van je algoritme: je hebt toestemming van de eigenaar, of het mag volgens de wet.
  * Gebruik zo min mogelijk persoonsgegevens om dit doel bereiken.

Je organisatie moet aantoonbaar de verwerking beperken tot de persoonsgegevens die noodzakelijk zijn voor een duidelijk bepaald doel. Dit kan lastig zijn. Want welke gegevens zijn bijvoorbeeld nodig als je vooraf niet weet welke verbanden het algoritme legt?

De persoonsgegevens die overblijven, gebruik je zo minimaal mogelijk. Hoe minimaal dat is, bepaalt je organisatie zelf. Technieken om privacy zoveel mogelijk te beschermen zijn:

  * Anonimiseren: data zoveel mogelijk anoniem maken
  * [Pseudonimiseren](https://www.autoriteitpersoonsgegevens.nl/themas/beveiliging/beveiliging-van-persoonsgegevens/gegevens-pseudonimiseren): data moeilijker herleidbaar maken naar personen
  * Aggregeren: data zoveel mogelijk combineren of samenvoegen tot 1 waarde, zoals een totaal of gemiddelde

Tip

Leg de keuzes die je maakt duidelijk uit. Zo voorkom je fouten op de werkvloer. Persoonsgegevens die zijn verzameld voor doel A mogen bijvoorbeeld alleen onder specifieke voorwaarden voor doel B gebruiken.

## Belang van privacy en persoonsgegevens beschermen

Algoritmes die persoonsgegevens verwerken, kunnen snel de privacy schenden van grote groepen mensen. Vooral [impactvolle algoritmes](../../soorten-algoritmes-en-ai/impact-van-algoritmes/) kunnen veel schade veroorzaken in de maatschappij.

Wanneer je de privacy en persoonsgegevens van mensen goed beschermt, verlaag je de kans op:

  * Gebruik van persoonsgegevens voor het verkeerde doel, zoals het per ongeluk publiceren van iemands paspoortfoto op de website van een gemeente.
  * Discriminatie, bijvoorbeeld door onnodig gebruik van leeftijd in een algoritme.
  * Lekken van persoonsgegevens.

Persoonsgegevens helemaal niet gebruiken, is onmogelijk. Voor sommige taken kunnen overheden niet meer zonder algoritmes, bijvoorbeeld voor het beoordelen van grote aantallen aanvragen voor subsidies of vergunningen. Hiervoor zijn persoonsgegevens nodig zoals iemands naam, adres of bepaalde kenmerken.

## Vereisten

id| Vereisten
---|---
[aia-33](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-33-verwerking-in-testomgeving/index.html)| [AI-testomgevingen die persoonsgegevens verwerken, voldoen aan strenge voorwaarden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-33-verwerking-in-testomgeving/index.html)
[avg-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-01-persoonsgegevens-worden-rechtmatig-verwerkt/index.html)| [Persoonsgegevens worden op een rechtmatige manier verwerkt](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-01-persoonsgegevens-worden-rechtmatig-verwerkt/index.html)
[avg-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-02-beperkte-bewaartermijn-van-persoonsgegevens/index.html)| [Persoonsgegevens worden zo kort mogelijk bewaard](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-02-beperkte-bewaartermijn-van-persoonsgegevens/index.html)
[avg-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-03-minimale-verwerking-van-persoonsgegevens/index.html)| [Persoonsgegevens worden zo min mogelijk verwerkt](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-03-minimale-verwerking-van-persoonsgegevens/index.html)
[avg-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-04-proportionaliteit-en-subsidiariteit/index.html)| [Persoonsgegevens en andere data verwerken gebeurt proportioneel en subsidiair](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-04-proportionaliteit-en-subsidiariteit/index.html)
[avg-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-05-juistheid-en-actualiteit-van-persoonsgegevens/index.html)| [Persoonsgegevens zijn juist en actueel](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-05-juistheid-en-actualiteit-van-persoonsgegevens/index.html)
[avg-06](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-06-verantwoordingsplicht-rechtmatigheid/index.html)| [Organisaties kunnen bewijzen dat zij persoonsgegevens op de juiste manier verwerken](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-06-verantwoordingsplicht-rechtmatigheid/index.html)
[avg-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-07-transparantie-bij-verwerken-persoonsgegevens/index.html)| [Organisaties zijn transparant over het verwerken van persoonsgegevens](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-07-transparantie-bij-verwerken-persoonsgegevens/index.html)
[avg-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-08-wettelijke-verwerking-van-gevoelige-gegevens/index.html)| [Gevoelige persoonsgegevens worden alleen gebruikt als hiervoor een wettelijke uitzondering geldt](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-08-wettelijke-verwerking-van-gevoelige-gegevens/index.html)
[avg-09](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-09-inroepen-privacyrecht-bij-verwerking-persoonsgegevens/index.html)| [Betrokkenen kunnen een beroep doen op hun privacyrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-09-inroepen-privacyrecht-bij-verwerking-persoonsgegevens/index.html)
[avg-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-10-recht-op-niet-geautomatiseerde-besluitvorming/index.html)| [Besluiten die levens kunnen beïnvloeden, zijn niet volledig geautomatiseerd](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-10-recht-op-niet-geautomatiseerde-besluitvorming/index.html)
[avg-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-11-privacy-bij-ontwerp-bij-verwerking-van-persoonsgegevens/index.html)| [Ontwerp en standaardinstellingen (defaults) zijn zo gunstig mogelijk voor de privacy van betrokkenen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-11-privacy-bij-ontwerp-bij-verwerking-van-persoonsgegevens/index.html)
[avg-12](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/index.html)| [Data zoals persoonsgegevens zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/index.html)
[avg-13](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-13-dpia-verplicht/index.html)| [Een gegevensbeschermingseffectbeoordeling (DPIA) is verplicht, indien een verwerking van persoonsgegevens waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van natuurlijke personen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-13-dpia-verplicht/index.html)

## Aanbevolen maatregelen

id| Maatregelen
---|---
[owp-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-03-doel-verwerken-persoonsgegevens/index.html)| [Beschrijf voor welk doel het algoritme persoonsgegevens gebruikt en waarom dit mag](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-03-doel-verwerken-persoonsgegevens/index.html)
[owp-14](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-14-verwerkersovereenkomst-onderdeel-aanbesteding/index.html)| [Maak het opstellen van een verwerkersovereenkomst onderdeel van de aanbesteding als persoonsgegevens worden verwerkt](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-14-verwerkersovereenkomst-onderdeel-aanbesteding/index.html)
[dat-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-03-bewaartermijnen-persoonsgegevens/index.html)| [Geef data zoals persoonsgegevens een bewaartermijn met een vernietigingsprocedure](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-03-bewaartermijnen-persoonsgegevens/index.html)
[dat-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-04-pseudonimiseren-anonimiseren/index.html)| [Bescherm persoonsgegevens door data te anonimiseren, pseudonimiseren of te aggregeren](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-04-pseudonimiseren-anonimiseren/index.html)
[owk-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-03-privacyrisico/index.html)| [Analyseer de privacy-risico’s en neem maatregelen om deze risico’s laag te houden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-03-privacyrisico/index.html)
[imp-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-05-vermelding-in-privacyverklaring/index.html)| [Vermeld het gebruik van persoonsgegevens in een privacyverklaring](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-05-vermelding-in-privacyverklaring/index.html)
[imp-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-07-vermelding-in-verwerkingsregister/index.html)| [Vermeld het gebruik van persoonsgegevens in het verwerkingsregister](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-07-vermelding-in-verwerkingsregister/index.html)
[imp-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-10-proces-privacyrechten/index.html)| [Spreek af hoe de organisatie omgaat met privacy-verzoeken](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-10-proces-privacyrechten/index.html)
[uit-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/8-uit-01-archiveren/index.html)| [Bij uitfaseren en doorontwikkeling wordt correct omgegaan met data en modelinformatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/8-uit-01-archiveren/index.html)

## Aanbevolen hulpmiddelen
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
