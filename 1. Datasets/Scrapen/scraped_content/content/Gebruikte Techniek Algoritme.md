---
title: Beschrijf welke techniek gebruikt wordt voor de beoogde toepassing - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-04-gebruikte-techniek/index.html
scraped_at: 2025-06-12T10:33:19.983821
---

# Beschrijf welke techniek gebruikt wordt voor de beoogde toepassing - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-04-gebruikte-techniek/index.html

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
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Beschrijf welke techniek gebruikt wordt voor de beoogde toepassing

[]( "Vereiste ID")owp-04[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Beschrijf welke techniek gebruikt wordt voor de beoogde toepassing.

## Toelichting

  * Beschrijf wat voor soort algoritme er gebruikt gaat worden voor de beoogde toepassing.
  * Bepaal of je gebruik wilt maken van een:

    * [zelflerend algoritme](../../../soorten-algoritmes-en-ai/wat-is-een-algoritme/#zelflerende-algoritmes)
    * niet-zelflerend algoritme zoals een algoritme gebaseerd op [rekenregels](../../../soorten-algoritmes-en-ai/wat-is-een-algoritme/#rekenregels)
  * Beschrijf vervolgens ook:

    * waarom er voor dit type algoritme wordt gekozen
    * wat de alternatieven zijn en waarom die minder passend zijn
    * waarom dit algoritme het meest geschikt is om het [beoogde doel](../1-pba-02-formuleren-doelstelling/) van het algoritme te bereiken.
  * De precieze details kunnen in dit stadium van de levenscyclus waarschijnlijk nog niet ingevuld worden. Maak een goede eerste inschatting van de gebruikte techniek. Eventueel kan je er ook voor kiezen om verschillende technieken verder te onderzoeken. Dat betekent dat er meerdere algoritmes ontwikkeld worden (op basis van verschillende technieken), en je later een definitieve keuze maakt.

  * Het is belangrijk om uiteindelijk een passend uitlegbaar algoritme te selecteren voor de context waarin het wordt toegepast. Daarin moet de afweging gemaakt worden of de technische [uitlegbaarheid](../2-owp-32-toepassen-uitlegbaarheidstechnieken/) voldoende is in de context die de inzet van het algoritme vereist. Hierbij kan ook de conclusie worden getrokken dat een simpeler, inzichtelijker algoritme de voorkeur krijgt.

  * Maak hierbij een bewuste afweging tussen [uitlegbaarheid](../2-owp-32-toepassen-uitlegbaarheidstechnieken/) en [prestaties](../5-ver-02-evalueer-nauwkeurigheid/) van het algoritme. Over het algemeen geldt dat complexere maar minder uitlegbare algoritmes nauwkeuriger zijn.

  * Veel (statistische) modellen zijn gebaseerd op (statistische) aannames over bijvoorbeeld eigenschappen van de data. Ga na of er aan deze aannames wordt voldaan.

## Risico

Wanneer je geen zorgvuldige afweging maakt over de techniek die je gebruikt om het doel te bereiken, dan is het niet duidelijk of de meest geschikte techniek wordt gebruikt. Mogelijk zijn er passendere oplossingen om het doel te bereiken.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[awb-01 - Organisaties die algoritmes gebruiken voor publieke taken nemen besluiten zorgvuldig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-01-zorgvuldigheidsbeginsel/)
[aia-06 - Hoog-risico-AI-systemen zijn voorzien van voldoende technische documentatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-06-technische-documentatie/)
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)

## Bronnen

  * [Impact Assessment Mensenrechten en Algoritmes, 2A.1, 2B.1](../../hulpmiddelen/IAMA/)
  * [Onderzoekskader Auditdienst Rijk, DM.2](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algemene Rekenkamer, 2.04, 2.17](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)

## Voorbeelden

Douane: Risico detectie aangiften

De douane maakt gebruik van een algoritme om te selecteren welke goederen een (extra) controle krijgen. Dit wordt gedaan op basis van aangiftegegevens van bedrijven waarmee mogelijk verhoogde risico’s worden aangegeven. In het algoritmeregister geven zij aan dat dit algoritme gebruik maakt van beslisregels gebaseerd op “if-then-else” combinaties. Zij geven aan dat gedaan wordt om zo aangiften efficiënter te kunnen behandelen en dus mogelijk sneller vrijgegeven kunnen worden.

Bron: Detecteren risico’s in douaneaangiften voor naleving opiumwetontheffing - Douane

Provincie Zuid-Holland: Webapplicatie Impactmonitor Brugopening

De Provincie Zuid-Holland (PZH) maakt gebruik van een webapplicatie om brugbedieners te ondersteunen bij het optimale moment kiezen voor het openen van de brug. De applicatie voorspelt tot 21 minuten in de toekomst en houd rekening met verkeersdoorstroom en uitstoot. In het algoritmeregister hebben zij in detail uitgelegd welke technieken gebruikt worden. Zij maken gebruik van _Recurring Neural Networks_ (RNNs), een specifieke vorm van Artificiële Neurale Netwerken. Deze worden getraind op tijdserie data wat in dit geval belangrijk is vanwege de afhankelijkheid van drukte op en rondom de brug.

Bron: [Webapplicatie Impactmonitor Brugopening - Provincie Zuid-Holland](https://algoritmes.overheid.nl/nl/algoritme/webapplicatie-impactmonitor-brugopening-provincie-zuidholland/96895333)

Heb je een ander voorbeeld of best practice, laat het weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl).

18 april 2025 31 oktober 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *geharmoniseerde norm: Een Europese norm die op verzoek van de Commissie is vastgesteld met het oog op de toepassing van harmonisatiewetgeving van de Unie
  *conformiteitsbeoordeling: Het proces waarbij de naleving wordt aangetoond van de voorschriften van hoofdstuk III, afdeling 2 van de AI-Verordening in verband met een AI-systeem met een hoog risico
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
  *AI-bureau: De taak van de Commissie waarbij zij bijdraagt aan de uitvoering van, de monitoring van en het toezicht op AI-systemen en AI-modellen voor algemene doeleinden, en AI-governance, als bepaald in het besluit van de Commissie van 24 januari 2024; verwijzingen in deze verordening naar het AI-bureau worden begrepen als verwijzingen naar de Commissie
  *proceseigenaar: De proceseigenaar is verantwoordelijk voor de kwaliteit van het proces en de vastlegging daarvan in een processchema
