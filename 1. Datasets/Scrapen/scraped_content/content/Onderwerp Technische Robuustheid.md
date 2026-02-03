---
title: Technische robuustheid en veiligheid - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/onderwerpen/technische-robuustheid-en-veiligheid/
scraped_at: 2025-06-12T10:33:48.940358
---

# Technische robuustheid en veiligheid - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/onderwerpen/technische-robuustheid-en-veiligheid/

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
      * [ Privacy en persoonsgegevens beschermen in algoritmes  ](../privacy-en-gegevensbescherming/)
      * [ Inkoop van verantwoorde algoritmes  ](../publieke-inkoop/)
      * Technische robuustheid en veiligheid  [ Technische robuustheid en veiligheid  ](./) Inhoudsopgave
        * Wat is technisch robuust en veilig?
        * Belang van robuuste, veilige algoritmes
        * Gebruik algoritmes op de juiste manier
        * Controleer regelmatig
          * Voorbeeld
          * Controles voorbereiden
          * Controles uitvoeren
        * Bescherm algoritmes tegen aanvallen en bedreigingen
        * Verklein de kans op schade
        * Vereisten
        * Aanbevolen maatregelen
        * Hulpmiddelen
        * Bronnen
        * Help ons deze pagina te verbeteren
      * [ Transparant zijn over algoritmes  ](../transparantie/)
  * [ Levenscyclus  ](../../levenscyclus/)
  * [ Rollen  ](../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../voldoen-aan-wetten-en-regels/)

Inhoudsopgave

  * Wat is technisch robuust en veilig?
  * Belang van robuuste, veilige algoritmes
  * Gebruik algoritmes op de juiste manier
  * Controleer regelmatig
    * Voorbeeld
    * Controles voorbereiden
    * Controles uitvoeren
  * Bescherm algoritmes tegen aanvallen en bedreigingen
  * Verklein de kans op schade
  * Vereisten
  * Aanbevolen maatregelen
  * Hulpmiddelen
  * Bronnen
  * Help ons deze pagina te verbeteren

  1. [ Onderwerpen  ](../)
  2. [ Onderwerpen  ](../)

# Technische robuustheid en veiligheid

Algoritmes van de overheid moeten robuust en veilig zijn. Dit betekent dat je algoritmes in elke situatie goed presteren, ook als er iets onverwachts gebeurt. Gaat er toch iets mis, dan is er een noodplan.

## Wat is technisch robuust en veilig?

Een technisch robuust en veilig algoritme presteert onder elke omstandigheid zoals het bedoeld is.

Een robuust algoritme is:

  * Nauwkeurig: Het algoritme geeft de juiste uitkomst voor het gewenste doel, of meldt dat de uitkomst onzeker is.
  * Betrouwbaar: Ook in nieuwe of onverwachte situaties geeft het algoritme de juiste uitkomst.
  * Reproduceerbaar: In dezelfde situaties vertoont het algoritme hetzelfde gedrag.

Een algoritme is veilig onder deze omstandigheden:

  * Geautoriseerde toegang: Alleen personen en systemen met toestemming kunnen het algoritme gebruiken of beheren.
  * Confidentieel: Het algoritme kan geen vertrouwelijke of gevoelige informatie lekken door aanvallen.
  * Integer: Kwaadwillenden kunnen nergens in de levenscyclus van het algoritme onbedoeld de controle van het model overnemen.
  * Beschikbaar: Je kunt op elk moment het algoritme gebruiken waarvoor het bedoeld is. Gaat dit toch fout, dan ontstaat er geen grote schade.

## Belang van robuuste, veilige algoritmes

Algoritmes kunnen grote schade veroorzaken aan de maatschappij. Met een technisch robuust en goed beveiligd algoritme voorkom je:

  * onverwachte schadelijke uitkomsten, zoals verkeerde beslissingen of discriminatie door onvoldoende nauwkeurigheid
  * uitval van het systeem
  * lekken van informatie, zoals persoonsgegevens
  * gebruik van het algoritme voor verkeerde doelen
  * schade door misbruik of aanvallen van buitenaf

## Gebruik algoritmes op de juiste manier

Gebruik een algoritme alleen voor het juiste doel en op de juiste manier. Dit is de manier die is getest en gecontroleerd. Wanneer je het algoritme gebruikt voor een ander doel of in een verkeerde context, zijn de resultaten niet meer betrouwbaar.

Voorkom dat medewerkers op de verkeerde manier werken met het algoritme. Zij moeten weten wat het algoritme wel en niet kan. En wat ze moeten doen als het algoritme fouten maakt of niet goed werkt. Denk aan technische en organisatorische ondersteuning:

  * Leid medewerkers op.
  * Maak duidelijke afspraken over werkprocessen ([governance](../governance/)).
  * Stuur gebruikers in het juiste gebruik via interactie en technische verbeteringen in het ontwerp.

## Controleer regelmatig

Begin zo vroeg mogelijk met regelmatige controles van de uitkomst en werking van het algoritme. In de praktijk verandert de omgeving en de situatie waarin het algoritme wordt gebruikt. Controleer daarom regelmatig of het algoritme nog werkt zoals het is bedoeld.

### Voorbeeld

Een algoritme leest kentekens tijdens parkeercontroles. Het herkent de juiste letters en cijfers op elk kenteken. Ook als het bord een andere kleur heeft, op een andere plek zit of vies is. Het algoritme is nauwkeurig en dus robuust.

Een algoritme berekent het risico op fraude door mensen. Maar bij personen uit dezelfde groep geeft het algoritme de ene keer als uitkomst ‘hoog risico’ en de andere keer ‘geen risico’. De uitkomst is niet reproduceerbaar. Hierdoor is het algoritme niet robuust.

### Controles voorbereiden

Bereid de controles voor tijdens de levenscyclusfases [probleemanalyse](../../levenscyclus/probleemanalyse/), [ontwerp](../../levenscyclus/ontwerp/) en [dataverkenning en datapreparatie](../../levenscyclus/dataverkenning-en-datapreparatie/). Onderzoek de situatie waarin je organisatie het algoritme gaat gebruiken: Wat zijn de risico’s? Welke onderdelen van het algoritme moet je evalueren? Analyseer de kwaliteit en variatie van de data. Bedenk maatregelen waarmee je de risico’s zoveel mogelijk voorkomt. En bedenk met welke methode je de controles gaat evalueren.

Ontwikkel je het algoritme zelf, controleer dan tijdens de ontwikkeling al wat er gebeurt in de verschillende situaties die je verwacht. Experimenteer met nieuwe combinaties van de inputdata en gebruik verschillende representatieve test-sets.

### Controles uitvoeren

Voer de controles uit tijdens de [ontwikkelfase](../../levenscyclus/ontwikkelen/) en de [verificatie- en validatiefase](../../levenscyclus/verificatie-en-validatie/). Test het algoritme goed. Evalueer hoe robuust en veilig het algoritme is. Verbeter het algoritme waar nodig. En monitor goed welke data het algoritme gebruikt, zodat je veranderingen in die data snel signaleert. Maak een noodplan voor als blijkt dat het algoritme niet meer werkt zoals het bedoeld was.

Blijf regelmatig controleren tijdens de fases [implementatie](../../levenscyclus/implementatie/) en [monitoring en beheer](../../levenscyclus/monitoring-en-beheer/). Dit zijn de fases waarin je het algoritme gebruikt. Presteert het algoritme niet goed, los het probleem dan op of [stop het gebruik](../../levenscyclus/uitfaseren/).

Tip

Houd rekening met concept drift. Dit betekent dat de eigenschappen van je data in de loop van de tijd kunnen veranderen. Hierdoor trekt je algoritme mogelijk verkeerde conclusies. Zo was er vóór 2020 een verband tussen thuiswerken en ziek zijn. Maar sinds de coronacrisis in 2020 is dit verband minder sterk, omdat gezonde mensen vaker thuiswerken.

## Bescherm algoritmes tegen aanvallen en bedreigingen

Beveilig het ICT-systeem waarin het algoritme wordt gebruikt. Dit zijn bijvoorbeeld maatregelen uit de [Baseline Informatiebeveiliging Overheid (BIO)](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/) die je standaard neemt voor beveiliging van ICT-systemen tegen cyberaanvallen.

Beveilig de algoritmes zelf tegen cybercriminelen. Belangrijke bedreigingen voor algoritmes zijn:

  * Trainingsdata van een AI-model aanpassen, waardoor het later fouten gaat maken tijdens het gebruik.
  * Input van een algoritme aanpassen om het normale gedrag te omzeilen, of om het algoritme specifieke, ongewenste output te laten geven.
  * Een ‘achterdeurtje’ inbouwen met toegang tot het algoritme, waardoor aanvallers het algoritme kunnen misbruiken.
  * Intellectueel eigendom of kwetsbaarheden afleiden uit de details van een AI-model.
  * Gevoelige informatie afleiden uit de eigenschappen van trainingsdata.

Lees meer in het [TNO-rapport Verkenning van het raakvlak cybersecurity en AI](https://www.rijksoverheid.nl/documenten/rapporten/2024/10/28/tk-bijlage-4-tno-2024-r10768-verkenning-van-het-raakvlak-van-cybersecurity-en-ai).

Aandachtspunten voor het beschermen van algoritmes tegen specifieke dreigingen:

  * Controleer of de trainingsdata geschikt, correct en betrouwbaar is.
  * Controleer of de inputdata geschikt, correct en betrouwbaar is.
  * Houd bij complexe algoritmes rekening met verborgen en onwenselijke functionaliteiten.
  * Train je algoritme om bestand te zijn tegen aanvallen.
  * Stimuleer veilig gebruik van het algoritme door gebruikers.
  * Maak afspraken met leveranciers en controleer de geleverde algoritmes voor gebruik.
  * Test periodiek of het algoritme weerbaar is tegen bekende aanvallen.

Hiermee voorkom je:

  * misleiding, doordat het algoritme niet werkt op de bedoelde manier
  * verkeerde implementatie en daardoor een verkeerde werking

Begin zo vroeg mogelijk met beveiligen. Beveilig in elk geval in de fases [ontwikkelen](../../levenscyclus/ontwikkelen/), [verificatie en validatie](../../levenscyclus/verificatie-en-validatie/), [implementatie](../../levenscyclus/implementatie/), [monitoring en beheer](../../levenscyclus/monitoring-en-beheer/) en [uitfaseren](../../levenscyclus/uitfaseren/).

## Verklein de kans op schade

Veroorzaak zo min mogelijk schade als het toch fout gaat. En maak een noodplan voor incidenten. Het doel van dit plan is ervoor zorgen dat de fout zo min mogelijk gevolgen heeft voor de organisatie en de maatschappij. In het plan staat bijvoorbeeld wie wat moet doen als het systeem uitvalt.

## Vereisten

id| Vereisten
---|---
[aia-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-07-automatische-logregistratie/index.html)| [Hoog-risico-AI-systemen loggen automatisch bepaalde gegevens](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-07-automatische-logregistratie/index.html)
[aia-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/index.html)| [Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/index.html)
[aia-12](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-12-bewaartermijn-voor-documentatie/index.html)| [Documentatie over hoog-risico-AI-systemen wordt 10 jaar bewaard door de aanbieder](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-12-bewaartermijn-voor-documentatie/index.html)
[aia-13](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-13-bewaartermijn-voor-gegenereerde-logs/index.html)| [Logs van hoog-risico-AI-systemen worden zes maanden bewaard door de aanbieder](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-13-bewaartermijn-voor-gegenereerde-logs/index.html)
[aia-18](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-18-corrigerende-maatregelen-voor-non-conforme-ai/index.html)| [Als een hoog-risico-AI-systeem niet voldoet aan de AI-verordening, grijpt de aanbieder in](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-18-corrigerende-maatregelen-voor-non-conforme-ai/index.html)
[aia-19](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-19-toegankelijkheidseisen/index.html)| [Hoog-risico-AI-systemen voldoen aan de toegankelijkheidseisen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-19-toegankelijkheidseisen/index.html)
[aia-23](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-23-gebruiksverantwoordelijken-bewaren-logs/index.html)| [Logs voor hoog-risico-AI-systemen worden bewaard door de gebruiksverantwoordelijke](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-23-gebruiksverantwoordelijken-bewaren-logs/index.html)
[aia-30](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-30-ai-modellen-algemene-doeleinden-systeemrisico/index.html)| [Aanbieders van AI-modellen voor algemene doeleinden met een systeemrisico treffen extra maatregelen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-30-ai-modellen-algemene-doeleinden-systeemrisico/index.html)
[aia-32](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-32-ai-modellen-algemene-doeleinden-systeemrisico-cyberbeveiliging/index.html)| [AI-modellen voor algemene doeleinden met systeemrisico’s zijn voldoende beveiligd tegen cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-32-ai-modellen-algemene-doeleinden-systeemrisico-cyberbeveiliging/index.html)
[aia-34](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-34-monitoring-na-het-in-de-handel-brengen/index.html)| [Hoog-risico-AI-systemen zijn voorzien van een monitoringsysteem](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-34-monitoring-na-het-in-de-handel-brengen/index.html)
[aia-38](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-38-testen/index.html)| [Hoog-risico-AI-systemen zijn getest](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-38-testen/index.html)
[avg-12](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/index.html)| [Data zoals persoonsgegevens zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/index.html)
[bio-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/index.html)| [Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/index.html)

## Aanbevolen maatregelen

id| Maatregelen
---|---
[org-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-11-gebruikersbeheer/index.html)| [Maak afspraken over het beheer van gebruikers](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-11-gebruikersbeheer/index.html)
[org-13](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-13-wachtwoordbeheer/index.html)| [Maak afspraken over het beheer van wachtwoorden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-13-wachtwoordbeheer/index.html)
[org-14](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-14-wijzigingenproces/index.html)| [Maak afspraken over het wijzigen van de code](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-14-wijzigingenproces/index.html)
[owp-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-04-gebruikte-techniek/index.html)| [Beschrijf welke techniek gebruikt wordt voor de beoogde toepassing](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-04-gebruikte-techniek/index.html)
[owp-06](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-06-impactanalyse/index.html)| [Leg vast wat de impact van het algoritme is als het niet werkt zoals beoogd](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-06-impactanalyse/index.html)
[owp-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-10-projectstartarchitectuur/index.html)| [Maak een Project Startarchitectuur (PSA) voor de ontwikkeling of inkoop van algoritmes](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-10-projectstartarchitectuur/index.html)
[owp-26](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-26-risico-analyse-informatiebeveiliging-leverancier/index.html)| [Voer een risico-analyse met de aanbieder uit op het gebied van informatiebeveiliging bij een uitbestedingstraject](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-26-risico-analyse-informatiebeveiliging-leverancier/index.html)
[owp-33](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-33-technische-interventies-robuustheid/index.html)| [Identificeer en implementeer technische interventies die robuustheid vergroten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-33-technische-interventies-robuustheid/index.html)
[owp-34](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-34-voorkom-kwetsbaarheden-supplychain/index.html)| [Voorkom kwetsbaarheden die geïntroduceerd worden in de supply-chain van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-34-voorkom-kwetsbaarheden-supplychain/index.html)
[dat-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-03-bewaartermijnen-persoonsgegevens/index.html)| [Geef data zoals persoonsgegevens een bewaartermijn met een vernietigingsprocedure](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-03-bewaartermijnen-persoonsgegevens/index.html)
[dat-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html)| [Gebruik bij machine learning technieken gescheiden train-, test- en validatiedata en houd rekening met underfitting en overfitting](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html)
[dat-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-10-datamanipulatie/index.html)| [Controleer de data op manipulatie en ongewenste afhankelijkheden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-10-datamanipulatie/index.html)
[dat-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-11-controleren-inputdata/index.html)| [Controleer de input van gebruikers op misleiding](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-11-controleren-inputdata/index.html)
[owk-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-01-security-by-design/index.html)| [Ontwerp en ontwikkel het algoritme volgens de principes van ‘security by design’](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-01-security-by-design/index.html)
[owk-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-02-stopzetten-gebruik/index.html)| [Maak een noodplan voor het stoppen van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-02-stopzetten-gebruik/index.html)
[owk-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-04-logging/index.html)| [Maak logbestanden waarin staat wie wanneer toegang had tot de data en de code](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-04-logging/index.html)
[owk-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-07-reproduceerbaarheid/index.html)| [Zorg voor reproduceerbaarheid van de uitkomsten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-07-reproduceerbaarheid/index.html)
[owk-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-08-feedbackloops/index.html)| [Bepaal welke feedbackloops van invloed zijn op het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-08-feedbackloops/index.html)
[owk-09](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-09-adversarial-aanvallen/index.html)| [Ontwerp en train het algoritme om bestand te zijn tegen (cyber)aanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-09-adversarial-aanvallen/index.html)
[owk-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-10-voorkom-lekken-op-basis-van-output/index.html)| [Zorg dat (gevoelige) informatie niet kan lekken op basis van de output van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-10-voorkom-lekken-op-basis-van-output/index.html)
[owk-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-11-documenteer-parameters/index.html)| [Documenteer en beargumenteer de keuze voor gebruikte modellen en parameters](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-11-documenteer-parameters/index.html)
[ver-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-01-functioneren-in-lijn-met-doeleinden/index.html)| [Controleer regelmatig of het algoritme werkt zoals het bedoeld is](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-01-functioneren-in-lijn-met-doeleinden/index.html)
[ver-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-02-evalueer-nauwkeurigheid/index.html)| [Evalueer de nauwkeurigheid van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-02-evalueer-nauwkeurigheid/index.html)
[ver-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-04-representatieve-testomgeving/index.html)| [Zorg voor een representatieve testomgeving](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-04-representatieve-testomgeving/index.html)
[ver-06](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-06-evalueer-betrouwbaarheid/index.html)| [Evalueer de betrouwbaarheid van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-06-evalueer-betrouwbaarheid/index.html)
[imp-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/index.html)| [Doe aselecte steekproeven om algoritmes met 'risicogestuurde selectie’ te controleren](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/index.html)
[imp-09](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-09-interventies-ux/index.html)| [Neem technische interventies op in de gebruikersinterface om verkeerd gebruik te voorkomen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-09-interventies-ux/index.html)
[mon-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-01-backups-maken/index.html)| [Maak back-ups van algoritmes](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-01-backups-maken/index.html)
[mon-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-02-beveiliging-algoritme/index.html)| [Beveilig de software](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-02-beveiliging-algoritme/index.html)
[mon-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-03-informatiebeveiligingsincidenten/index.html)| [Maak een noodplan voor beveiligingsincidenten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-03-informatiebeveiligingsincidenten/index.html)
[mon-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-04-evaluatieplan/index.html)| [Maak een evaluatieplan voor tijdens het gebruik van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-04-evaluatieplan/index.html)
[mon-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-05-evalueer-bij-veranderingen-in-data/index.html)| [Monitor regelmatig op veranderingen in de data. Bij veranderingen evalueer je de prestaties en output van het algoritme.](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-05-evalueer-bij-veranderingen-in-data/index.html)
[mon-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-07-plan-continue-monitoring/index.html)| [Stel een plan op voor continue monitoring](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-07-plan-continue-monitoring/index.html)
[mon-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-08-test-weerbaarheid-tegen-aanvallen/index.html)| [Controleer regelmatig of een algoritme voldoende weerbaar is tegen bekende aanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-08-test-weerbaarheid-tegen-aanvallen/index.html)
[uit-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/8-uit-01-archiveren/index.html)| [Bij uitfaseren en doorontwikkeling wordt correct omgegaan met data en modelinformatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/8-uit-01-archiveren/index.html)

## Hulpmiddelen
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
