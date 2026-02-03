---
title: Richt de juiste menselijke controle in van het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-03-menselijke-tussenkomst/index.html
scraped_at: 2025-06-12T10:34:52.622299
---

# Richt de juiste menselijke controle in van het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-03-menselijke-tussenkomst/index.html

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
    * Inrichten van menselijke controle
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Richt de juiste menselijke controle in van het algoritme

[]( "Vereiste ID")imp-03[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../levenscyclus/ "Levencyclus")[Implementatie](../../../levenscyclus/implementatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../onderwerpen/ "Onderwerp")[Menselijke controle](../../../onderwerpen/menselijke-controle/)[](../../../onderwerpen/ "Onderwerp")[Governance](../../../onderwerpen/governance/)

## Maatregel

Richt (technische) controlemechanismen in voor menselijke tussenkomst (of: menselijke controle) waarmee de output van een algoritme kan worden gecontroleerd.

## Toelichting

Algoritmes ondersteunen vaak beslissingen en besluitvorming van overheidsorganisaties. Deze beslissingen of besluiten kunnen betrokkenen in [aanmerkelijke mate raken of zelfs rechtsgevolgen](../../vereisten/avg-10-recht-op-niet-geautomatiseerde-besluitvorming/) hebben. Omdat algoritmes niet foutloos zijn, is het belangrijk dat een mens controleert wat een algoritme doet en, waar nodig, corrigeert. Dit proces heet 'menselijke tussenkomst' en moet betekenisvol zijn, niet slechts symbolisch.

Het inrichten, monitoren en evalueren van menselijke controle is cruciaal om te voorkomen dat algoritmes negatieve effecten veroorzaken of de menselijke autonomie ondermijnen.

Betekenisvolle menselijke controle houdt in dat:

  * Het toezicht wordt uitgevoerd door iemand die bevoegd en bekwaam is om een beslissing of besluit te wijzigen.
  * Automatische aanbevelingen niet klakkeloos worden overgenomen. Bijvoorbeeld: een systeem dat standaard een suggestie accepteert door een enkele klik voldoet hier niet aan.
  * De vormen van menselijke tussenkomst al in een vroeg stadium, bijvoorbeeld in de ontwerpfase, worden vastgesteld op basis van risicoanalyses.
  * Gebruikers voldoende kennis, tijd en verantwoordelijkheid hebben om weloverwogen beslissingen te nemen over het functioneren van algoritmes. Dit betekent ook dat externe factoren, zoals tijdsdruk of onvoldoende informatie, de beoordeling van de output niet mogen beïnvloeden. (zie ook het [Onderzoekskader algoritmes, Auditdienst Rijk, SV.6](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/hulpmiddelen/onderzoekskader-adr))

Soms is menselijke tussenkomst minder relevant, zoals bij ‘gebonden bevoegdheden’. Hierbij is weinig tot geen ruimte om een beslissing of besluit aan te passen. Voorbeelden zijn:

  * Het opleggen van verkeersboetes onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (Wahv).
  * Het automatisch aanpassen van studiefinanciering op basis van inkomenswijzigingen.

Om menselijke tussenkomst goed te organiseren, zijn technische en organisatorische maatregelen nodig. Dit geldt ook wanneer een externe aanbieder de algoritmes levert. In dat geval moet de verantwoordelijke organisatie (gebruiksverantwoordelijke) samen met de aanbieder bepalen hoe menselijke tussenkomst zinvol kan worden ingericht.

### Inrichten van menselijke controle

Er zijn verschillende manieren om menselijke tussenkomst in te richten, afhankelijk van de specifieke toepassing van een algoritme. Hieronder worden vier mogelijkheden beschreven die kunnen worden ingezet, los of in combinatie:

#### 1\. Human in the loop

Bij dit model speelt de mens een actieve rol in elke fase van het algoritme. Deze variant geeft de meeste controle en invloed, maar kan leiden tot vertraagde of minder efficiënte besluitvorming, vooral bij real-time of zeer complexe taken waarbij snelheid cruciaal is. Een voorbeeld van toepassen van human-in-the-loop is het nakijken en beoordelen van de output van een algoritme door een mens, telkens voordat een beslissing wordt genomen. Het verwerken van data gebeurt alleen in opdracht van de mens en verder neemt het algoritme of AI model geen autonome beslissingen.

#### 2\. Human on the loop

Hier behoudt de mens toezicht en kan ingrijpen wanneer dat nodig is om te garanderen dat een model veilig en ethisch opereert. Dit model biedt daardoor een balans tussen autonome besluitvorming en menselijke controle. Het is vooral nuttig in situaties waarin afwijkende keuzes of acties van het algoritme grote gevolgen kunnen hebben. De menselijke operator houdt de werking van het algoritme in de gaten en staat klaar om in te grijpen of beslissingen terug te draaien wanneer nodig.

#### 3\. Human above the loop

In dit model houdt de mens toezicht op een hoger niveau, met een focus op strategische en ethische keuzes, in plaats van dat de menselijke operator zich bezighoudt met directe operationele beslissingen. Dit stelt de mens in staat in te grijpen wanneer kritieke morele, juridische of sociale zorgen ontstaan om het model op de langere termijn bij te sturen. De menselijke tussenkomst is gericht op het bepalen van beleid en de richtlijnen voor algoritmes. Het gaat daarbij niet alleen over het definiëren van operationele procedures maar ook het maken van bepaalde ethische overwegingen, het zorgen voor naleving van regelgeving en het overwegen van de implicaties van de inzet van algoritmes op de lange termijn.

#### 4\. Human before the loop

Hier maakt de mens vooraf ethische en morele afwegingen die in het algoritme zelf worden ingebouwd. Hoewel het model in productie autonoom opereert, zal de menselijke input gedurende de ontwikkeling ervoor zorgen dat het model ook in complexe situaties volgens de juiste (ethische) afwegingen keuzes en acties onderneemt.

Dit model is essentieel in situaties waar menselijk ingrijpen tijdens de uitvoering niet mogelijk is (wanneer er bijvoorbeeld weinig of helemaal geen tijd is om als mens te interveniëren), maar waar ethische keuzes cruciaal blijven. Denk aan bestrijding van zeemijnen of situaties met zelfrijdende auto’s in onvoorspelbare verkeerssituaties (bron: [Towards Digital Life: Een toekomstvisie op AI anno 2032, TNO](https://www.tno.nl/nl/visie-ai-2032/)). Deze variant kan ook worden ingezet voor situaties waarin wel nog menselijk ingrijpen mogelijk is.

## Risico

Het niet inrichten van passende menselijke controle leidt tot onverantwoorde inzet van algoritmen en het niet voldoen aan wettelijke vereisten.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[avg-10 - Besluiten die levens kunnen beïnvloeden, zijn niet volledig geautomatiseerd](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-10-recht-op-niet-geautomatiseerde-besluitvorming/)
[grw-01 - Algoritmes schenden geen grondrechten of mensenrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-01-fundamentele-rechten/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)
[awb-01 - Organisaties die algoritmes gebruiken voor publieke taken nemen besluiten zorgvuldig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-01-zorgvuldigheidsbeginsel/)
[aia-09 - Hoog-risico-AI-systemen staan onder menselijk toezicht](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-09-menselijk-toezicht/)
[aia-21 - Menselijk toezicht van hoog-risico-AI-systemen wordt uitgevoerd door mensen met voldoende kennis en mogelijkheden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-21-gebruiksverantwoordelijken-menselijk-toezicht/)

## Bronnen

  * [Toetsingskader Algoritmes Algemene Rekenkamer, 3.11](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Menselijke tussenkomst | Algoritmes | Algemene Rekenkamer](https://www.rekenkamer.nl/onderwerpen/algoritmes/toetsingskader/ethiek/menselijke-tussenkomst)
  * [Onderzoekskader Algoritmes Auditdienst Rijk, SV.5, SV.6](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Advies landsadvocaat over geautomatiseerde selectietechnieken, p.9](https://www.rijksoverheid.nl/documenten/rapporten/2024/03/13/bijlage-2-advies-landsadvocaat-over-geautomatiseerde-selectietechniek)
  * [Recht op een menselijke blik bij besluiten | Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/privacyrechten-avg/recht-op-een-menselijke-blik-bij-besluiten#:~:text=Reactie%20op%20verzoek-,Geautomatiseerd%20besluit,noemen%20dit%20een%20geautomatiseerd%20besluit.)
  * Kamerstukken IT 2017-2018, 34 851, nr. (MvT UAVG), p. 120-121
  * [Ethics guidelines for trustworthy AI | Shaping Europe’s digital future](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai), deel (64)
  * [Towards Digital Life: Een toekomstvisie op AI anno 2032, TNO](https://www.tno.nl/nl/visie-ai-2032/)
  * [Algoritmes afwegen | Rathenau Instituut](https://www.rathenau.nl/nl/digitalisering/algoritmes-afwegen)
  * [Managing supplier delivery reliability risk under limited information: Foundations for a human-in-the-loop DSS - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167923612002886)
  * [Human control of AI systems: from supervision to teaming | AI and Ethics (springer.com)](https://link.springer.com/article/10.1007/s43681-024-00489-4)
  * [Zijn er beperkingen op het gebruik van geautomatiseerde besluitvorming? - Europese Commissie](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/dealing-citizens/are-there-restrictions-use-automated-decision-making_nl#:~:text=Example-,Antwoord,is%20of%20hen%20aanzienlijk%20be%C3%AFnvloedt.)

## Voorbeelden

Hof van Justitie van de Europese Unie: Prejudiciële verwijzing

In 2021 heeft een burger SCHUFA (een Duits bedrijf wat kredietwaardigheid informatie deelt met derden) aangeklaagd naar aanleiding van een niet ingewilligd verzoek tot inzage en wissing van diens persoonsgegevens. De reden hiervoor kwam door een afwijzing van ondersteuning op basis van geautomatiseerde individuele besluitvorming. Zij maakten geen gebruik van betekenisvolle menselijke controle en dus is SCHUFA verantwoordelijk gehouden.

Bron: [HvJEU december 2023, ECLI:EU:C:2023:957 (SCHUFA Scoring)](https://eur-lex.europa.eu/legal-content/nl/TXT/?uri=CELEX:62021CJ0634)

Rijksdienst voor Ondernemend Nederland: Risicocontrole Subsidieaanvragen

De Rijksdienst voor Ondernemend Nederland (RVO) maakt gebruik van een algoritme bij het behandelen van subsidieaanvragen. Hierbij wordt bij iedere aanvraag een risico-indicatie gemaakt op basis van een aantal regels. Als er volgens het algoritme geen risico’s zijn wordt de aanvraag automatisch aangemaakt, zo niet wordt de aanvraag nog beoordeeld door een adviseur.

Daarnaast worden aanvragen met ingewikkelde technieken of boven een bepaald bedrag altijd door een adviseur beoordeeld. Op deze manier is er sprake van betekenisvolle [menselijke controle](../../../onderwerpen/menselijke-controle/).

Bron: [Rijksdienst voor Ondernemend Nederland: Risicocontrole Subsidieaanvragen](https://algoritmes.overheid.nl/nl/algoritme/risicocontrole-sde-subsidieaanvragen-rijksdienst-voor-ondernemend-nederland/51892728#verantwoordGebruik)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

10 april 2025 14 augustus 2024

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
