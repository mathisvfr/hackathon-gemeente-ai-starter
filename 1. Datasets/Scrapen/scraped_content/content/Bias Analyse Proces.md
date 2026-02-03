---
title: Toets het algoritme op bias en voer een rechtvaardigingstoets uit - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/index.html
scraped_at: 2025-06-12T10:34:45.257097
---

# Toets het algoritme op bias en voer een rechtvaardigingstoets uit - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/index.html

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
    * Stap 1: Analyseer of er sprake is van bias
    * Stap 2: Voer een rechtvaardigingstoets uit
    * Stap 3: Voer een ethische wenselijkheidstoets uit
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Toets het algoritme op bias en voer een rechtvaardigingstoets uit

[]( "Vereiste ID")ver-03[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../levenscyclus/ "Levencyclus")[Verificatie en validatie](../../../levenscyclus/verificatie-en-validatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Jurist](../../../rollen/jurist/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)

## Maatregel

Analyseer regelmatig of het gebruik van het algoritme of het proces daaromheen leidt tot onwenselijke of onrechtmatige verschillen in de behandeling van individuen en/of groepen.

## Toelichting

Het uitvoeren van een analyse over onwenselijke of onrechtmatige verschillen bestaat grofweg uit 3 stappen:

  * Stap 1: analyseer of er sprake is van bias: _systematisch verschil in behandeling van bepaalde objecten, mensen of groepen in vergelijking met anderen._
  * Stap 2: voer een rechtvaardigingstoets uit om te bepalen of het geconstateerde verschil uit stap 1 te rechtvaardigen is.
  * Stap 3: voer een ethische wenselijkheidstoets uit om te bepalen of het geconstateerde verschil uit stap 1 ethisch wenselijk is.

Voor alle stappen geldt dat het belangrijk is om de gemaakte keuzes en afwegingen zorgvuldig te onderbouwen en te documenteren. De 3 stappen worden hieronder verder toegelicht.

Opmerking

Deze maatregel is in ieder geval van toepassing op natuurlijke personen. Voor andere rechtspersonen zoals bedrijven kan dit ook van toepassing zijn. Denk bijvoorbeeld aan een gelijke behandeling tussen eenmanszaken en grotere bedrijven.

### Stap 1: Analyseer of er sprake is van bias

In deze stap is het doel om te bepalen in welke mate er sprake is van een systematisch verschil in behandeling van bepaalde objecten, mensen of groepen in vergelijking met anderen. Dit verschil kan zowel op een [directe als een indirecte manier](../../../onderwerpen/bias-en-non-discriminatie/#herken-bias) ontstaan.

#### Toetsen op direct onderscheid

Toetsen op direct onderscheid is in vergelijking tot toetsen op indirect onderscheid relatief eenvoudig.

Bepaal of de inputvariabelen die gebruikt worden leiden tot een direct onderscheid op basis van godsdienst, levensovertuiging, politieke gezindheid, ras, geslacht, nationaliteit, hetero- of homoseksuele gerichtheid1 of burgelijke staat.

Het is niet mogelijk om een uitputtend overzicht te geven van alle selectiecriteria die mogelijk tot direct onderscheid op één van deze gronden leiden. Wel is duidelijk dat verschillende criteria verband houden met bijvoorbeeld nationaliteit of ras. Gebruik van deze factoren wordt dan gezien als direct onderscheid en is verboden. De volgende criteria duiden in ieder geval (niet limitatief) op een onderscheid op ras2: huidskleur, eventueel andere geracialiseerde uiterlijke kenmerken zoals gezicht of haar, etniciteit, etnische achtergrond, allochtoon/autochtoon, migratieachtergrond, buitenlandse afkomst of nationale oorsprong, specifiek benoemde afkomst (bijv. Marokkaans, Antilliaans etc.), ‘niet-Westers’ klinkende naam, ‘Roma’ of ‘woonwagenbewoners’.

Wel zijn in de jurisprudentie verschillende voorbeelden en aanknopingspunten te vinden. Zo staat vast dat selectie op basis van fysieke etnische kenmerken, zoals huidskleur, direct onderscheid op grond van ras oplevert2. Een ander voorbeeld is dat onderscheid op grond van een niet-westers klinkende naam direct onderscheid op grond van afkomst (en dus ras) oplevert2.

#### Toetsen op indirect onderscheid

Ook selectiecriteria die op het eerste gezicht geen enkele link lijken te hebben met een discriminatiegrond kunnen leiden tot indirect onderscheid op grond van een discriminatiegrond. Enkele voorbeelden van zulke 'ogenschijnlijk neutrale' selectiecriteria die verband hebben met ras of nationaliteit zijn: postcode, hoogte van het inkomen, kenteken, familielid in het buitenland, laaggeletterdheid. Indirect onderscheid is in vergelijking met direct onderscheid lastiger te signaleren en te voorkomen. Daarom is het belangrijk jouw algoritmische toepassing [regelmatig te analyseren](../7-mon-07-plan-continue-monitoring/) op eventueel indirect onderscheid. Het toetsen op indirect onderscheid bestaat uit 5 stappen:

  1. **Bepaal wat de[kwetsbare groepen](../2-owp-07-afwegen-grondrechten/) zijn.** Eventueel kan dit aangevuld worden op basis van de discriminatiegronden uit non-discriminatie wetgeving. Of andere groepen waarvoor verschillen in behandeling ethisch onwenselijk zijn.

  2. **Bepaal wat "verschillen in behandeling" betekent in de context van het algoritme.** In deze stap is het belangrijk om voorafgaand aan de daadwerkelijke analyse met een [brede groep stakeholders](../1-pba-04-betrek-belanghebbenden/) te bepalen wat 'eerlijk' en 'rechtvaardig' wordt bevonden in de context van het betreffende algoritme. Er zijn veel verschillende manieren waarop je kan kijken naar onderscheid bij het gebruik van algoritmes. Voorbeelden van manieren waarop je naar onderscheid kan kijken zijn:

    * **Onderscheid op basis van gelijke uitkomsten (representatie)**. De belangrijkste vraag die hier mee beantwoord wordt is: hebben personen uit verschillende groepen gelijke kans om geselecteerd te worden door het algoritme? Of is er sprake van een over- of ondervertegenwoording van bepaalde groepen in de selectie ten opzichte van de betreffende populatie?
    * **Onderscheid op basis van gelijke prestaties (fouten)**. De belangrijkste vraag die hier mee beantwoord wordt is: presteert het algoritme gelijk voor personen uit verschillende groepen? Met andere woorden: maakt het algoritme vaker fouten bij bepaalde groepen? Dat kan er eventueel toe leiden dat bepaalde groepen vaker onterecht wel of niet geselecteerd worden door het algoritme.

Om te toetsen of er sprake is van onderscheid op basis van gelijke prestaties, is het noodzakelijk om [de prestaties van het algoritme goed te analyseren](../5-ver-01-functioneren-in-lijn-met-doeleinden/). In het geval van classificatie is het daarvoor nodig om een zogeheten _confusion matrix_ op te stellen. Een confusion matrix is een tabel waarin de voorspellingen van het algoritme worden vergeleken met de werkelijke waarden (de _ground truth_ ).

De verschillende maten/metrieken waarop gekeken kan worden naar onderscheid, worden in de (wetenschappelijke) literatuur ook wel _fairness metrieken_ genoemd. Veel van deze metrieken kunnen op basis van de confusion matrix berekend worden. Een hulpmiddel om de meest passende metrieken te kiezen in jouw situatie is de [Fairness tree](https://openresearch.amsterdam/nl/page/87589/the-fairness-handbook).

Door te denken vanuit verschillende perspectieven, zullen er in de praktijk meerdere metrieken van belang zijn. Het kan echter voorkomen dat deze metrieken elkaar tegenspreken. Maak een duidelijke prioritering van de verschillende metrieken om afwegingen te maken tussen de verschillende opvattingen van eerlijkheid.

  3. **Verzamel de benodigde data die nodig is om bovenstaande groepen te bepalen.** Bepaal welke data nodig is om te analyseren of er verschillen zijn tussen bepaalde groepen. In veel gevallen zal data nodig zijn die demografische en beschermde kenmerken van groepen omschrijft. Het verzamelen en verwerken van deze data kan in strijd zijn met privacy vereisten uit bijvoorbeeld de [Algemene Verordening Gegevensbescherming](../../vereisten/avg-01-persoonsgegevens-worden-rechtmatig-verwerkt/). Het is daarom van belang om duidelijk afwegingen te maken tussen privacy en het analyseren van bias die rekening houdt met de juridische en ethische vereisten.

Uitzondering voor hoog risico AI-systemen

De AI-verordening biedt een uitzondering voor het verwerken van bijzondere categorieën persoonsgegevens voor het monitoren, opsporen en corrigeren van bias bij AI-systemen met een hoog risico. Zie [artikel 10.5, AI-verordening](https://eur-lex.europa.eu/legal-content/NL/TXT/HTML/?uri=OJ:L_202401689#d1e3348-1-1).

Om de data op een veilige en rechtmatige manier te gebruiken voor een biasanalyse dient de data van voldoende kwaliteit te zijn. Denk hier goed na of de data eventuele bias bevat die kan duiden op een bepaalde vooringenomenheid in de biasanalyse zelf (historische bias of representatie bias). De data dient bijvoorbeeld voldoende actueel en volledig te zijn.

Voor sommige groepen zal het onmogelijk zijn om te beschikken over data van voldoende kwaliteit om zorgvuldig te toetsen op bias. De laaggeletterdheid van burgers of personen is bijvoorbeeld lastig meetbaar en in veel gevallen niet beschikbaar. Bepaal in zo'n situatie [of er andere mogelijkheden zijn deze groepen te helpen](../2-owp-07-afwegen-grondrechten/), of er andere mogelijkheden zijn om eventuele ongelijke behandeling bij deze groepen te constateren. Bijvoorbeeld door hierop te monitoren in de klacht- en bezwarenprocedure.

  4. **Bereken de verschillen in behandeling en/of uitkomsten van het algoritme**. Bepaal of er sprake is van een onderscheid en of dit significant is. Er zijn verschillende open source softwarepakketten die je hierbij kunnen ondersteunen, zoals [fairlearn](https://fairlearn.org/), [Aequitas](https://github.com/dssg/aequitas), [fairml](https://cran.r-project.org/web/packages/fairml/index.html), [fairness](https://cran.r-project.org/web/packages/fairness/index.html) of [AI Fairness 360](https://github.com/Trusted-AI/AIF360).

  5. **Probeer te verklaren hoe het geconstateerde onderscheid is ontstaan**. Als er in de vorige stap een significant onderscheid is geconstateerd, is het belangrijk om na te gaan hoe en waar in het proces dit onderscheid is ontstaan. Dit kan bijvoorbeeld ontstaan door:

    * Een vorm van bias in de onderliggende inputdata. Je kan hierbij denken aan:
      * Historische bias: in hoeverre beschrijft de data de huidige situatie?
      * Representatie bias: is de data waarop getraind wordt representatief voor de bijbehorende populatie? Zijn trends uit de gebruikte data generaliseerbaar naar de totale populatie?
      * Meetbias: beschrijven de inputvariabelen wel wat ze moeten beschrijven? In hoeverre zijn dit benaderingen waarbij eventuele factoren worden weggelaten?
    * Een vorm van bias in het proces na afloop van het algoritme:
      * Is er sprake van automatiseringsbias of bevestigingsbias in de (handmatige) beoordeling?

Wanneer duidelijker is hoe de geconstateerde bias is ontstaan, is het goed om te verkennen of er mogelijkheden zijn om dit (in de toekomst) te voorkomen.

Het is belangrijk hier [een brede groep aan belanghebbenden bij te betrekken](../1-pba-04-betrek-belanghebbenden/). De oorzaken van bias komen in veel gevallen uit de 'echte wereld', waarbij patronen in datasets historische, demografische en sociale verschillen weerspiegielen. Het verklaren en voorkomen van bias vraagt daarmee niet alleen om technische oplossingen, maar het is belangrijk de hele socio-technische omgeving waarin het algoritme wordt ingezet mee te nemen.

### Stap 2: Voer een rechtvaardigingstoets uit

Wanneer er in Stap 1 is geconstateerd dat er sprake is van een onderscheid, dient de volgende vraag beantwoord te worden:

> Valt dit onderscheid te rechtvaardigen?

Een geconstateerd systematisch onderscheid is niet altijd fout en is niet altijd verboden, maar het vraagt wel altijd om aandacht en zorgvuldigheid. Het geconstateerde onderscheid kan in bepaalde situaties en onder bepaalde strikte voorwaarden gerechtvaardigd zijn:

  * Voor **direct onderscheid** kan er bijvoorbeeld sprake zijn van een wettelijke uitzondering die het gemaakte onderscheid toelaat.
  * Voor **indirect onderscheid** geldt dat behalve een wettelijke uitzondering er ook een **objectieve rechtvaardiging** kan bestaan, waarmee het geconstateerde onderscheid in bepaalde gevallen toelaatbaar kan zijn.

Vier subvragen die hierbij beantwoord moeten worden zijn:

  * Streeft het in te zetten algoritme een legitiem doel na?
  * Is het in te zetten algoritme geschikt om het doel te bereiken?
  * Is het algoritme noodzakelijk? Zijn er geen redelijke, minder bezwaarlijke alternatieven?
  * Is het algoritme alles afwegend proportioneel?

Wanneer er geen rechtvaardiging is voor het gemaakte onderscheid, spreken we van een verboden direct of indirect onderscheid, ofwel discriminatie. Het algoritme mag in dat geval niet gebruikt worden.

Voor meer toelichting over het uitvoeren van een rechtvaardigingstoets, verwijzen we naar het [Toetsingskader Risicoprofilering](https://publicaties.mensenrechten.nl/publicatie/4093c026-ae41-4c1d-aa78-4ce0e205b5de) van het College voor de Rechten van de Mens.

### Stap 3: Voer een ethische wenselijkheidstoets uit

Bepaal of het geconstateerde onderscheid uit Stap 1 ethisch wenselijk is. Dit hangt samen met de algemene wenselijkheid van de inzet van het algoritme.

In sommige gevallen kan het zo zijn dat ondanks dat er een objectieve rechtvaardiging bestaat voor het gemaakte onderscheid, dit vanuit ethisch perspectief toch onwenselijk is. Bepaal [met een grote groep belanghebbenden](../1-pba-04-betrek-belanghebbenden/) wat eventuele (nadelige) effecten van het gemaakte onderscheid kunnen zijn, of jullie dit eerlijk vinden en of er eventuele alternatieven zijn.

Opmerking

De bepaling over wat eerlijk is en wat ethisch wenselijk is kan in sommige gevallen ook politiek bevonden worden. Houd hier rekening met de politiek-bestuurlijke verantwoordelijkheden en zorg indien nodig dat de [politiek-bestuurlijke verantwoordelijkhden](../0-org-04-politiek-bestuurlijke-verantwoordelijkheid/) duidelijk zijn.

## Risico

Wanneer er geen zorgvuldige analyse naar (onwenselijke) bias is uitgevoerd bestaat het risico dat het gebruik van het algoritme discriminerende effecten met zich meebrengt. Dit kan leiden tot een ongelijke behandeling van burgers met eventuele schade voor betrokkenen.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[grw-02 - Algoritmes discrimineren niet](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/)
[aia-27 - Hoog-risico-AI-systemen voor publieke taken worden beoordeeld op gevolgen voor grondrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-27-beoordelen-gevolgen-grondrechten/)
[grw-01 - Algoritmes schenden geen grondrechten of mensenrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-01-fundamentele-rechten/)
[avg-10 - Besluiten die levens kunnen beïnvloeden, zijn niet volledig geautomatiseerd](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-10-recht-op-niet-geautomatiseerde-besluitvorming/)
[aia-05 - Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/)
[aia-06 - Hoog-risico-AI-systemen zijn voorzien van voldoende technische documentatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-06-technische-documentatie/)

## Bronnen

  * [Toetsingskader Algoritmes Algemene Rekenkamer, 2.18, 2.19, 3.08, 3.09](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Onderzoekskader Algoritmes Auditdienst Rijk, DM.16, DM.17, DM.18, DM.20, DM.21, DM.22](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader risicoprofilering – Normen tegen discriminatie op grond van ras en nationaliteit, College voor de Rechten van de Mens](https://publicaties.mensenrechten.nl/publicatie/4093c026-ae41-4c1d-aa78-4ce0e205b5de)
  * [Handreiking non-discriminatie by design](https://www.rijksoverheid.nl/documenten/rapporten/2021/06/10/handreiking-non-discriminatie-by-design)

## Voorbeelden

Algorithm Audit – Addendum Vooringenomenheid voorkomen

Algorithm Audit heeft de risicoprofilering in het Controle Uitwonendenbeurs-proces (CUB-proces) onderzocht op verzoek van Dienst Uitvoering Onderwijs (DUO). DUO heeft tussen 2010 en 2023 gebruik gemaakt van een risicoprofiel voor het tegengaan van onrechtmatig gebruik van de uitwonendenbeurs. Dit is in 2023 in opspraak geraakt en DUO heeft verzocht om hier verder onderzoek naar te doen.

Hieruit bleek dat er inderdaad onvoldoende statistisch verband was tussen een aantal selectiecriteria. Dit is gebleken uit een kwantitatieve analyse aan de hand van verschillende onderzoeksvragen. Zij hebben hun analyses ook publiekelijk online gezet op [GitHub](https://github.com/NGO-Algorithm-Audit/DUO-CUB), zodat andere organisaties een soortgelijke analyse kunnen uitvoeren.

Bron: [Addendum Vooringenomenheid voorkomen, Algorithm Audit](https://algorithmaudit.eu/nl/algoprudence/cases/aa202402_preventing-prejudice_addendum/)

Voorbeeld: PricewaterhouseCoopers – Onderzoek misbruik uitwonendenbeurs

PricewaterhouseCoopers (PwC) heeft onderzoek gedaan op verzoek van het Ministerie van Onderwijs, Cultuur en Wetenschap (OCW) naar de controle op het misbruik en oneigenlijk gebruik van uitwonendenbeurs (controleproces MUB). Het gaat om de uitwonendenbeurs die de Dienst Uitvoering Onderwijs (DUO) destijds onder deze naam verstrekte (tegenwoordig Controle Uitwonendenbeurs-proces (CUB-proces)). PwC heeft een kwalitatief onderzoek gedaan naar de procedures rond de opzet, validatie en evaluatie van het MUB-proces.

Dit kwalitatieve onderzoek is uitgevoerd aan de hand van een eerder opgesteld analysekader voor onderzoek naar selectiesystemen bij andere Nederlandse overheden. Het analysekader bestaat uit drie delen: procedures rond opzet, de gevolgen van de inrichting en omgang met risicosignalen. In het rapport van PwC staat dit in sectie 1.3.1 in meer detail uitgelegd.

Bron: [Onderzoek misbruik uitwonendenbeurs, PricewaterhouseCoopers](https://www.rijksoverheid.nl/documenten/rapporten/2024/03/01/eindrapport-pwc-rapportage-onderzoek-misbruik-uitwonendenbeurs)

Rijks ICT Gilde – Bias toetsing 'Kort Verblijf Visa' aanvragen

Het Rijks ICT Gilde (RIG) heeft op verzoek van het Ministerie van Buitenlandse Zaken (BZ) een bias-toetsing uitgevoerd rondom beslissingen van bepaalde visumaanvragen. Hierbij heeft het RIG onderzoek gedaan naar welke typen bias zich voordoen en hoe deze bias verminderd kan worden.

Zij hebben een kwantitatief onderzoek gedaan en hieruit bleek dat er aanzienlijk verschil (dus bias) was op basis van nationaliteit. Daarom heeft het RIG geadviseerd om het gebruik van profielscore en risicogroepen te beëindigen.

Bron: [Bias toetsing 'Kort Verblijf Visa' aanvragen, Rijks ICT Gilde](https://www.rijksoverheid.nl/documenten/publicaties/2023/04/01/bias-toetsing-kort-verblijf-visa-aanvragen)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

* * *

  1. Er is een wetsvoorstel om de term 'hetero- of homoseksuele gerichtheid' in de Algmemene wet gelijke behandeling (Awgb) te wijzigingen in 'seksuele gerichtheid'. Met deze wijziging sluit de Awgb aan bij een eerdere wijziging van artikel 1 van de Grondwet. ↩

  2. Zie voor meer informatie het [Toetsingskader Risicoprofilering](https://publicaties.mensenrechten.nl/publicatie/4093c026-ae41-4c1d-aa78-4ce0e205b5de) van het College voor de Rechten van de Mens. ↩↩↩

10 april 2025 25 september 2024

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
