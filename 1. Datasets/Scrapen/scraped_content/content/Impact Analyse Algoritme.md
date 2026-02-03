---
title: Leg vast wat de impact van het algoritme is als het niet werkt zoals beoogd - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-06-impactanalyse/index.html
scraped_at: 2025-06-12T10:33:22.378727
---

# Leg vast wat de impact van het algoritme is als het niet werkt zoals beoogd - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-06-impactanalyse/index.html

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

# Leg vast wat de impact van het algoritme is als het niet werkt zoals beoogd

[]( "Vereiste ID")owp-06[](../../../levenscyclus/ "Levencyclus")[Probleemanalyse](../../../levenscyclus/probleemanalyse/)[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Fundamentele rechten](../../../onderwerpen/fundamentele-rechten/)

## Maatregel

Leg vast wie er wordt geraakt, welke processen beïnvloed worden door het algoritme en wat de impact is wanneer het systeem niet werkt zoals beoogd. Neem deze informatie proactief mee in het ontwerp en de ontwikkeling van een algoritme.

## Toelichting

Er moet een analyse gemaakt worden van de impact van een algoritme dat niet werkt zoals bedoeld. Een algoritme dat niet werkt zoals bedoeld kan bijvoorbeeld betekenen dat het algoritme een foutieve beslissing maakt of dat het algoritme is uitgevallen. De analyse op wie dit een impact heeft en hoe groot die impact is, is van belang voor de ontwerpkeuzes, de risicoanalyse en de evaluatie. Wanneer een foutieve beslissing zwaarwegende gevolgen heeft, moet er in het ontwerp gezorgd worden dat de kans op deze fout verminderd wordt. In de evaluatie moet er worden bepaald of de resterende risico’s acceptabel zijn. Voer de impactanalyse uit met een multidisciplinaire groep en documenteer afwegingen en keuzes hierbij. Wanneer een algoritme niet werkt als beoogd, kan dit inbreuk maken op [grondrechten](../../../onderwerpen/fundamentele-rechten/) van eventuele betrokken burgers. Onderdeel van de impactanalyse is om te bepalen of je algoritme bepaalde [grondrechten kan raken](../2-owp-07-afwegen-grondrechten/), aantasten of mogelijk schenden. Neem in de impactanalyse de volgende stappen.

  * Leg vast welke stakeholders worden geraakt. Denk hierbij aan de directe gebruiker, degene waarover het besluit wordt genomen en derde partijen die input leveren of de resultaten ontvangen. Houd hierbij rekening met [kwetsbare groepen waarbij het nodig is om deze groep extra bescherming te bieden](../2-owp-07-afwegen-grondrechten/).

  * Leg vast welke processen worden geraakt. Denk hierbij aan werkproces(sen) waarin het algoritme wordt gebruikt, maar ook aan vervolgprocessen of parallelle processen die beïnvloed worden door de resultaten van het algoritme.

  * Leg vast wat de impact is van een niet goed werkend algoritme (per stakeholder en proces). Bepaal per stakeholder en per proces wat het gevolg is van een niet goed werkend systeem. Indien het systeem uitvalt, hoe worden de partijen daardoor geraakt en wat is het gevolg? Zijn er processen die mogelijk stilvallen of moeten worden aangepast?

Analyseer ook de gevolgen van foutieve beslissingen. Let op dat verschillende typen fouten een verschillende impact hebben. Bijvoorbeeld in het geval van een ziektedetectie algoritme als voorsortering of een patiënt een uitgebreidere test moet ondergaan is de impact groter als de patiënt ten onrechte als geen-risico wordt geclassificeerd dan als iemand ten onrechte een extra controle moet ondergaan.

  * Bepaal welke factoren van invloed zijn op de kans dat het fout gaat. Het risico is afhankelijk van de kans dat een fout voorkomt. Voor risicoanalyse en mitigatie is het van belang om de factoren die van invloed zijn op de fouten in kaart te brengen. Deze geven input aan de ontwerpfase en mitigerende maatregelen. Denk hierbij aan factoren in de [data](../3-dat-01-datakwaliteit/), [het soort algoritme](../2-owp-05-soort-algoritme/), het gebruik en externe factoren.

## Risico

Als er geen goede impactanalyse wordt gemaakt, kunnen risico’s over het hoofd worden gezien. Een niet werkend systeem kan dan een grote impact hebben op mensen of de organisatie.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[grw-01 - Algoritmes schenden geen grondrechten of mensenrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-01-fundamentele-rechten/)
[avg-11 - Ontwerp en standaardinstellingen (defaults) zijn zo gunstig mogelijk voor de privacy van betrokkenen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-11-privacy-bij-ontwerp-bij-verwerking-van-persoonsgegevens/)

## Bronnen

  * [Onderzoekskader Auditdienst Rijk, SV.4](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

11 februari 2025 19 december 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *geharmoniseerde norm: Een Europese norm die op verzoek van de Commissie is vastgesteld met het oog op de toepassing van harmonisatiewetgeving van de Unie
  *conformiteitsbeoordeling: Het proces waarbij de naleving wordt aangetoond van de voorschriften van hoofdstuk III, afdeling 2 van de AI-Verordening in verband met een AI-systeem met een hoog risico
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
  *AI-bureau: De taak van de Commissie waarbij zij bijdraagt aan de uitvoering van, de monitoring van en het toezicht op AI-systemen en AI-modellen voor algemene doeleinden, en AI-governance, als bepaald in het besluit van de Commissie van 24 januari 2024; verwijzingen in deze verordening naar het AI-bureau worden begrepen als verwijzingen naar de Commissie
  *proceseigenaar: De proceseigenaar is verantwoordelijk voor de kwaliteit van het proces en de vastlegging daarvan in een processchema
