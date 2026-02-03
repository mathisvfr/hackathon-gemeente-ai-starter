---
title: Vng Nl 2021 03 Bijlage 3 Architectuur Ontwerp Incl  Eisen Specificaties En Wensen Def Pdf
url: https://vng.nl/sites/default/files/2021-03/bijlage-3-architectuur-ontwerp-incl.-eisen-specificaties-en-wensen-def.pdf
converted_at: 2025-06-11T13:27:35.385347
source_type: PDF
---

# Vng Nl 2021 03 Bijlage 3 Architectuur Ontwerp Incl  Eisen Specificaties En Wensen Def Pdf

Source: https://vng.nl/sites/default/files/2021-03/bijlage-3-architectuur-ontwerp-incl.-eisen-specificaties-en-wensen-def.pdf

---

## Page 1

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020 1 -












BIJLAGE 3
ARCHITECTUUR & ONTWERP;
INCLUSIEF: PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN

## Page 2

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 1 van 102

Inhoudsopgave

1
INLEIDING ............................................................................................................................................................ 4
1.1
INHOUD .................................................................................................................................................................. 4
1.2
CENTRALE BEGRIPPEN EN SCOPE ................................................................................................................................... 4
1.3
GEVRAAGDE SITUATIE ................................................................................................................................................ 6
2
PERSONA’S EN PROCESSEN .................................................................................................................................. 7
3
PDC EN ZTC .......................................................................................................................................................... 8
3.1
OW: ACTIVITEITEN, AANVULLINGSSPOREN EN LOKALE REGELS ............................................................................................ 8
3.2
PRODUCTEN- EN DIENSTENCATALOGUS ......................................................................................................................... 9
3.3
ZAAKTYPENCATALOGUS .............................................................................................................................................. 9
4
ARCHITECTUUR EN SYSTEMEN ............................................................................................................................11
4.1
INLEIDING .............................................................................................................................................................. 11
4.2
GEMMA-ARCHITECTUUR EN FUNCTIONELE SCHETS ARCHITECTUUR .................................................................................. 11
4.3
ONTWERP ............................................................................................................................................................. 15
4.3.1
Inleiding en Overzicht .................................................................................................................................. 15
4.3.2
Informatiestromen ...................................................................................................................................... 15
4.3.3
Multi-tenant inrichting ................................................................................................................................ 16
4.4
SPECIFICATIES EN WENSEN ........................................................................................................................................ 17
4.4.1
Inkomende informatiestromen (DSO-LV en overig) ..................................................................................... 17
4.4.2
Ketenintegratie ............................................................................................................................................ 17
4.4.2.1
Ketenintegratie: Specificaties en Wensen .............................................................................................................18
4.4.3
Procesvolgsysteem (PVS) ............................................................................................................................. 19
4.4.3.1
Specificaties en Wensen: Algemeen ......................................................................................................................19
4.4.3.2
Specificaties en Wensen: Vergunningverlening / Toetsen van verzoeken .............................................................20
4.4.3.3
Specificaties en Wensen: Advies ............................................................................................................................20
4.4.3.4
Specificaties en Wensen: Toezicht en Handhaving ................................................................................................21
4.4.3.5
Specificaties en Wensen: Mobiel Toezicht .............................................................................................................21
4.4.3.6
Specificaties en Wensen: Besluiten .......................................................................................................................22
4.4.3.7
Specificaties en Wensen: Leges en heffingen ........................................................................................................22
4.4.3.8
Specificaties en Wensen: Documentgeneratie ......................................................................................................23
4.4.4
Zaaksysteem en DMS/RMA ......................................................................................................................... 23
4.4.5
Objectregistratie.......................................................................................................................................... 23
4.4.5.1
Specificaties en Wensen Objectregistratie ............................................................................................................24
4.4.6
Ruimtelijke Ordening ................................................................................................................................... 25
4.4.7
Minimale, standaard, maximale  uitvraag .................................................................................................. 26
4.4.7.1
Minimale Uitvraag .................................................................................................................................................27
4.4.7.2
Standaard Uitvraag ................................................................................................................................................28
4.4.7.3
Maximale Uitvraag .................................................................................................................................................29
4.5
STANDAARDEN ....................................................................................................................................................... 29
4.5.1
Algemeen..................................................................................................................................................... 29
4.5.1.1
Verplichte standaarden..........................................................................................................................................30
4.5.1.2
Aanbevolen standaarden .......................................................................................................................................31
4.5.2
GEMMA Principes ........................................................................................................................................ 31
4.5.3
Standaarden ‘Domeinen’ ............................................................................................................................. 31

## Page 3

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 2 van 102
4.5.4
Architectuurstandaarden: GEMMA/NORA .................................................................................................. 32
4.5.5
Standaarden – aansluiting DSO – STAM/IMAM .......................................................................................... 32
4.5.6
Technische standaarden – infra .................................................................................................................. 32
4.5.7
Gegevensstandaarden ................................................................................................................................. 33
4.6
KOPPELINGEN EN INTEGRATIE .................................................................................................................................... 33
4.6.1
Algemeen..................................................................................................................................................... 33
4.6.2
Koppelingen met interne systemen ............................................................................................................. 33
4.6.2.1
Koppeling met generiek Zaaksysteem en DMS/RMA .............................................................................................33
4.6.2.2
Koppeling ESB en/of data distributie .....................................................................................................................34
4.6.2.3
Integratie met decentrale functionaliteit voor Kantoorautomatisering ................................................................34
4.6.2.4
Integratie met decentrale functionaliteit voor tijdverantwoording en/of planning ..............................................34
4.6.2.5
Integratie met decentrale functionaliteit voor In- en Excasso ...............................................................................35
4.6.3
Koppelingen met externe systemen ............................................................................................................ 35
4.6.3.1
Integratie met landelijke Intake-voorzieningen Digitaal Stelsel Omgevingswet (DSO) ..........................................35
4.6.3.2
Integratie met Informatiehuizen/Informatieproducten ........................................................................................35
4.6.3.3
Koppeling publicaties (DROP/KOOP en LVBB)........................................................................................................35
4.6.3.4
Informatie-uitwisseling ten behoeve van Inspectieview (Milieu, IvM) ..................................................................35
4.6.3.5
Koppeling Bodeminformatiesysteem (BIS) ............................................................................................................35
4.6.3.6
Koppeling overige ..................................................................................................................................................36
4.6.4
Koppelingen met Basisregistraties .............................................................................................................. 36
4.6.4.1
Integratie met Handelsregister (NHR) ....................................................................................................................36
4.6.4.2
Integratie met Basisregistratie Adressen en Gebouwen (BAG) .............................................................................36
4.6.4.3
Integratie met Basisregistratie Grootschalige Topografie (BGT) ............................................................................36
4.6.4.4
Integratie met Basisregistratie Ondergrond (BRO) ................................................................................................36
4.6.4.5
Integratie met basisregistratie personen (BRP) .....................................................................................................36
4.7
GENERIEKE FUNCTIONALITEIT EN OVERIGE SPECIFICATIES ................................................................................................. 36
4.7.1
Integratie beleidsvelden (RO) ...................................................................................................................... 36
4.7.2
Rapportages: Datawarehouse / BI .............................................................................................................. 36
4.7.3
Cloud............................................................................................................................................................ 37
4.7.4
Backup en Recovery ..................................................................................................................................... 37
4.7.5
Authenticatie en Rollen ............................................................................................................................... 37
4.7.6
Gebruikersvriendelijkheid ............................................................................................................................ 37
4.7.7
Webbrowser en Web-standaarden ............................................................................................................. 38
4.7.8
GEO/GIS ....................................................................................................................................................... 38
4.7.9
Autonoom gebruik ....................................................................................................................................... 38
4.7.10
Mobiel gebruik ......................................................................................................................................... 38
5
DOORONTWIKKELING .........................................................................................................................................39
5.1
DOORONTWIKKELING APPLICATIES .............................................................................................................................. 39
5.2
KOPPELINGEN ZAAKGERICHT WERKEN (API’S) ............................................................................................................... 39
5.3
PUBLICATIES ........................................................................................................................................................... 39
5.4
ONDERSTEUNING BELEIDSCYCLUS ............................................................................................................................... 40
5.4.1
Monitoring................................................................................................................................................... 40
5.4.2
Integratie met Beleidsontwikkeling ............................................................................................................. 41
5.5
COMMON GROUND................................................................................................................................................. 42
5.6
ZOEKFUNCTIONALITEIT ............................................................................................................................................. 42
Annex A
Persona’s en Processen .......................................................................................................................................44
1.
Inleiding .....................................................................................................................................................................44
2.
Processen ...................................................................................................................................................................45
3.
Uitwerking Persona’s .................................................................................................................................................47
Annex B
 Eisen en wensen vanuit GEMMA requirements .................................................................................................63

## Page 4

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 3 van 102
1.
Requirements Applicatiefunctie: Ondersteunen van generieke VTH-OW functionaliteit..........................................64
2.
Requirements Applicatiefunctie: Ondersteunen van aanvragen en meldingen ........................................................71
3.
Requirements Applicatiefunctie: Ondersteunen van toezicht ...................................................................................75
4.
Requirements Applicatiefunctie: Ondersteunen van handhaving .............................................................................75
5.
Requirements Applicatiefunctie: Ondersteunen van objecten en activiteiten ..........................................................76
6.
Principes ....................................................................................................................................................................77
Annex C
  Begrippenlijst .....................................................................................................................................................81
Annex D
 Overzichten Eisen, Specificaties en Wensen ......................................................................................................82
1.
Eisen ...........................................................................................................................................................................82
2.
Specificaties ...............................................................................................................................................................85
3.
Wensen en Doorontwikkeling ....................................................................................................................................91
Annex E
  Koppelingen aan bestaande systemen ..............................................................................................................94






## Page 5

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 4 van 102
1 Inleiding
1.1
Inhoud
Deze bijlage 3 geeft weer wat de technische -en functionele specificaties zijn van de gevraagde ICT-Oplossing
t.b.v. een VTH applicatie. Inhoudelijke onderbouwing hierbij is opgesteld door de GEMMA-architectuur te
verbinden met de gewenste functionele structuur (ontwerp), en de bijbehorende GEMMA-requirements en
ontwerpspecificaties (specificaties en wensen) te plaatsen in het perspectief van de gebruikers, de
Zaaktypencatalogus (ZTC) en de Producten- en DienstenCatalogus (PDC).

In dit document worden begrippen met een hoofdletter aangeduid; deze begrippen zijn in de bijlage
‘Begrippenlijst’ opgenomen.
1.2
Centrale begrippen en scope
De situatie is geprojecteerd op ondersteuning van de VTH-processen onder de Omgevingswet1, zonder
‘backwards compatibility’ naar pre-Omgevingswet regelgeving, standaarden en aansluitingen, met migratie of
conversie van alle relevante gegevens.

Drie begrippen, met een onderlinge verbinding staan centraal in de startsituatie. Dit zijn:



In hoofdstuk 3 worden deze begrippen en hun onderlinge relaties toegelicht.

Rond deze drie begrippen is de scope van de oplossing (zie ook paragraaf 1.2 Aanbestedingsdocument)
opgesteld met behulp van de afbeelding op de volgende pagina. De scope is opgedeeld in afzonderlijke
elementen en componenten, die weergegeven zijn vanuit een functioneel en een architectuur-
/informatiemanagementperspectief.



1 Uitgangspunt is ingangsdatum 01-01-2021

## Page 6

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 5 van 102

Figuur 1
Scope

De verschillende blokken beschrijven de te leveren functionaliteit. De blokken zijn - waar mogelijk -
gegroepeerd naar de op de vorige pagina genoemde begrippen. Tevens vormen de blokken de basis voor de
verdere indeling van het inhoudelijke deel van dit document.

De meest tastbare onderdelen zijn de kernsystemen ter ondersteuning van de primaire (individuele) VTHA-
processen van de deelnemers. Dit zijn:
het Procesvolgsysteem (PVS);
het Zaaksysteem (ZS);
het DMS/RMA.

Om deze systemen in de keten goed te laten functioneren, zijn de volgende centrale/collectieve
voorzieningen in de ICT-oplossing (op termijn) randvoorwaardelijk:
Ketenintegratie;
Objectregistratie.

Hierbij zijn de volgende opmerkingen van toepassing:
In de praktijk zijn de genoemde onderdelen vaak geen losse of strikt gescheiden systemen, maar zijn het
verschillende systemen die verenigd zijn in één (software)pakket, zijnde een domein specifiek
zaaksysteem, en/of geleverd als één geheel, al dan niet door één leverancier;
Een Procesvolgsysteem wordt weliswaar veel toegepast, maar de functionaliteit kan ook door andere
(samengestelde) deeloplossingen worden geleverd;
Per deelnemer verschilt het of deze systemen onderdeel uitmaken van de gevraagde  ICT-oplossing.

Later worden deze onderdelen en begrippen verder uitgewerkt in dit Ontwerpdocument.

## Page 7

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 6 van 102
1.3
Gevraagde situatie
De situatie bij de inwerkingtreding van de Omgevingswet is aan de hand van onderstaand schema uitgewerkt:


Figuur 2
Schema uitvraag

Hoofdstuk 2 verdiept door beschrijvingen van persona’s en processen. Hierbij is uit de ervaring van
eindgebruikers geput, zowel bij het werken intern binnen de organisaties als tussen verschillende
organisaties. Hiermee kunnen we bepalen of het systeem aansluit bij de daadwerkelijke werkwijzen, alsmede
bij de verschillen in werkwijzen. Dit hoofdstuk heeft de basis gevormd voor het opstellen van de eisen,
(hierna:ook requirements), specificaties en wensen.

Hoofdstuk 3 definieert welke activiteiten (voorheen thema’s en domeinen onder WABO) en andere processen
ondersteund moeten worden, ofwel: wat is onder de OW de dienstverlening naar burgers, bedrijven en andere
overheden. Dit resulteert in zaaktypen in de zaaktypencatalogus (ZTC) en producten in de Product-
/Dienstencatalogus (PDC), ofwel de output van het systeem, de wettelijke verankering en de basis voor
archivering, waarbij de PDC ‘leading’ is en de ZTC hiermee verbonden dient te zijn.

Hoofdstuk 4 behandelt de inhoud, de architectuur waar de ICT-Oplossing aan dient te voldoen en de
systemen die dat ondersteunen. Hierbij zijn de GEMMA-architectuur en de bijbehorende GEMMA requirements
verbonden aan een eigen functioneel ontwerp dat aansluit op ketensamenwerking en informatiedeling. Aan
de verschillende onderdelen van dit ontwerp is het totaal van requirements/eisen, specificaties en wensen
verbonden.

De hoofdstukkengaan uit van de huidige kennis, de stand van zaken en ervaringen uit de praktijk..
Ontwikkelingen kunnen met name volgen op het gebied van de Omgevingswet zelf, de (door)ontwikkeling
van de DSO-LV en de verdere ontwikkeling en adoptie van het  Common Ground-initiatief. De aanbestedende
dienst eist  derhalve actieve participatie van de leverancier tijdens de uitvoering van de opdracht. De
opdrachtbeschrijving in het Aanbestedingsdocument gaat hier nader op in, aangevuld met inhoudelijke
beschrijvingen die terugkomen in Hoofdstuk 5.




## Page 8

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 7 van 102
2 Persona’s en Processen



Dit hoofdstuk beschrijft in de vorm van persona’s de verschillende gebruikers van de Oplossing . Deze
beschrijvingen zijn door en vanuit het perspectief van de gebruikers gemaakt om inzicht te krijgen op welke
manier zij het PVS nodig hebben om straks uitvoering te geven aan de Omgevingswet.

De beschrijvingen hebben voornamelijk betrekking op de ‘reguliere’ VTH-processen, die in grote mate
gestandaardiseerd en gepland worden uitgevoerd. Inbegrepen zijn zowel de inhoudelijke uitvoering als de
ondersteuning alsmede de monitoring op de uitvoering in de keten. Er is sprake van interne en externe
complicerende factoren, zoals bijvoorbeeld intern de verschillen in werkwijzen tussen de verschillende
domeinen. Extern zijn er verschillen in de wijzen van mandatering, opdrachtverstrekking en werkafspraken
tussen bevoegde gezagen en de uitvoeringsorganisaties.

Daarnaast komen ook processen aan bod die minder in het standaard VTH-kader passen, zoals processen
vanuit de rol en verantwoordelijkheid bij calamiteiten en klachten, zoals bij de consignatiedienst, met
specifieke vervolgacties en monitoring. Deze processen kenmerken zich door een ad-hoc karakter en
specifieke werkafspraken, terwijl op basis van vaak minimale informatie 24/7 een snelle interventie gevraagd
wordt met specifieke betrokkenen, zoals externe meldkamers, politie en brandweer. Dit vereist een systeem
met flexibele functionaliteit om ook deze processen zaakgericht te kunnen afhandelen.








## Page 9

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 8 van 102
3 PDC en ZTC




3.1
OW: Activiteiten, aanvullingssporen en lokale regels
Onder de Omgevingswet kennen we geen thema’s en domeinen meer, zoals voorheen bij de Wabo het geval
was, maar wordt er gesproken over ‘Activiteiten’. Voor een totaaloverzicht van de activiteiten die de
Omgevingswet kent, zie https://aandeslagmetdeomgevingswet.nl/regelgeving/regels-voor-activiteiten/.
Het activiteitenoverzicht is hieronder opgenomen. De cursief geschreven activiteiten zijn voor deze
aanbesteding niet van toepassing.

Omgevingsplan
    Omgevingsplanactiviteit
    Verschil binnenplanse en buitenplanse omgevingsplanactiviteit
Bouwen
    Technische bouwactiviteit
    Sloopactiviteit
    Mobiel breken bouw- en sloopafval
    In stand houden bestaand bouwwerk
    Bouwwerk brandveilig gebruiken
Wateractiviteiten
    Wateronttrekkingsactiviteit
    Lozingsactiviteit op oppervlaktewater of zuiveringtechnisch werk
    Activiteiten in en bij de Noordzee
    Beperkingengebiedactiviteit waterstaatswerken
Milieubelastende activiteiten
    Milieubelastende activiteiten hoofdstuk 3 Bal
    Toelichting milieubelastende activiteiten
    Rioollozingen van milieubelastende activiteiten
Erfgoed
    Rijksmonumentenactiviteit
    Werelderfgoedactiviteit
Natuur
    Flora- en fauna-activiteit
    Vellen en beheren van houtopstand
    Natura 2000-activiteit
Beperkingengebiedactiviteiten
    Weg
    Waterstaatswerk
    Luchthaven
    Mijnbouwinstallatie in waterstaatswerk
Overige activiteiten
    Ontgrondingsactiviteit
    Lozingen van schepen op binnenwateren

## Page 10

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 9 van 102
    Gelegenheid bieden tot zwemmen en baden
    Mijnbouwlocatieactiviteit

De activiteiten worden aangevuld met:
- de zogenoemde ‘Aanvullingssporen’, zijnde:
▪
Natuur
▪
Bodem
▪
Geluid
▪
Grondeigendom
- lokaal op te stellen regels en aanvullingen.
Deze worden onder meer opgenomen in het omgevingsplan. Denk hierbij aan de opvolging van huidige
regels rond Drank & Horeca, APV en andere bijzondere wetten.

Bovenstaande lijst is de stand van zaken per december 2019. Het is niet uit te sluiten dat hier nog activiteiten
of andere aanvullingen bijkomen. Deze veranderingen dienen ook door de ICT-Oplossing ondersteund te
worden, mits van toepassing op gemeenten en/of omgevingsdiensten.
3.2
Producten- en Dienstencatalogus
De Producten- en Dienstencatalogus (PDC) is een verzameling van alle relevante producten en diensten die
onderdeel uitmaken van de Omgevingswet en waarvoor de bevoegde gezagen verantwoordelijk zijn. De
bevoegde gezagen kunnen de realisatie van een product of een dienst opdragen aan uitvoeringsinstanties
zoals de omgevingsdienst. Het proces tot realisatie van een product start door middel van een zaak op basis
van een passend zaaktype. Bij de afronding van een zaak wordt het desbetreffende product opgeleverd aan
de aanvrager c.q. het bevoegde gezag. Details en achtergronden van de PDC Omgevingswet zijn te vinden op:
https://omgevingswet.wiki/bin/view/360/Lees%20dit%20eerst/#HProducten-endienstencatalogus

Eis 1
De meest recente PDC (van tijd tot tijd gewijzigd) maakt steeds onderdeel uit van de inrichting van de ICT-
Oplossing.
3.3
Zaaktypencatalogus
De Zaaktypencatalogus (ZTC) voor de Omgevingswet is een op landelijk niveau samengestelde verzameling
van zaaktypen met bijbehorende informatieobjecten, die goed toepasbaar is bij de uitvoering van de VTH-
werkprocessen onder de Omgevingswet. Voor details en achtergronden, zie:
https://omgevingswet.wiki/bin/view/360/Lees%20dit%20eerst/#HZaaktypecatalogus

In gezamenlijkheid hebben de gemeenten en de ODZOB zich recent in de landelijke basis-ZTC2 verdiept.
Hieruit volgen de volgende eisen en specificaties.

Eis 2
Ten minste de onderstaande vijftien (15) zaaktypen, overeenkomstig de landelijke ZTC, dienen standaard
onderdeel uit te maken van de ICT-Oplossing.

Dit betreft:
1. Advies verstrekken
2. Advies verstrekken (informeel)/Vooroverleg voeren
3. Last onder bestuursdwang ten uitvoer leggen


4. Controle uitvoeren
5. Handhavingsbesluit nemen
6. Handhavingsverzoek behandelen
7. Incidentmelding behandelen
8. Last onder dwangsom ten uitvoer leggen

2 https://omgevingswet.wiki/bin/view/Zaaktypecatalogi/CAT_97oa2kKoeuKy8/zaaktype/?view=zaaktype


## Page 11

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 10 van 102
9. Melding activiteit behandelen
10. Aanvraag beschikking regulier behandelen
11. Aanvraag beschikking uitgebreid behandelen
12. Zienswijze behandelen
13. Beroep behandelen
14. Voorlopige voorziening behandelen
15. <niet ingevuld in wiki>
16. Bezwaar behandelen
Eis 3
Ten minste de onderstaande zes (6) aanvullende zaaktypen dienen aan de basisconfiguratie te worden
toegevoegd en daarmee onderdeel uit te maken van de ICT-Oplossing.
De informatieobjecten die bij de inrichting van deze zaaktypen horen, worden na de gunning door de
regiogemeenten aangereikt.

17. Omgevingsvisie/Structuurvisie
18. Omgevingsplan: vooroverleg
19. Omgevingsplan/bestemmingsplan
20. Beschikking RO behandelen
21. Principeverzoek
22. Overeenkomsten m.b.t. RO

Wens 1
In de basis wordt de inrichting van de zaaktypen overgenomen zoals de landelijke ZTC deze kent. Het kan
echter zijn dat er per deelnemende organisatie andere eisen  bestaan voor lokale aanpassingen (de zgn.
Coulour Locale). De ICT-Oplossing ondersteunt dit bij de hier opgenomen elementen.
➢
Zaaktype: Servicenorm behandeling
➢
Zaaktype: Archiefclassificatiecode
➢
Zaaktype: Verantwoordelijke
➢
Zaaktype: Product of dienst
➢
Zaaktype: Formulier
➢
Zaaktype: Referentieproces
➢
Zaaktype: Verantwoordingsrelatie (kan per soort ‘bevoegd gezag’ - gemeente, provincie, … -
verschillen)
➢
Statustype: Doorlooptijd status (afgeleid van Zaaktype - Servicenorm behandeling)
➢
Statustype: Checklistitem (i.v.m. afwijkende toetsing per Deelnemer, m.n. bij APV-producten)
➢
Roltype: Soort betrokkene (i.v.m. afwijkende functiebenamingen per Deelnemer)
➢
Roltype: Mag zetten Statustype (i.v.m. afwijkende afspraken over fiattering/mandatering per
Deelnemer)
➢
Eigenschap: de gemeenschappelijke Zaaktypencatalogus bevat de gemeenschappelijke
Eigenschappen die alle Deelnemers zullen implementeren. Aan deze minimale set kunnen individuele
Deelnemers eigen Eigenschappen toevoegen, bijvoorbeeld Eigenschappen die noodzakelijk zijn voor
het genereren van werkvoorraden en managementinformatie.
➢
Resultaattype: Parameters die betrekking hebben op archivering (i.v.m. verschillen tussen
selectielijsten

Aanvullende requirements/eisen, specificaties en wensen op het gebied van metadata e.a. zijn opgenomen in
Hoofdstuk 4

In hoofdstuk 4 vindt de functionele verdieping plaats op:
Informatiestromen
Zaaksysteem, DMS/RMA
Ketenintegratie
Objectregistratie


## Page 12

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 11 van 102


4 Architectuur en Systemen
4.1
Inleiding
De architectuur en de benodigde systemen van de Oplossing worden zowel technisch  als functioneel
beschreven door de verbinding te leggen met de GEMMA-componenten. Vervolgens zijn de relaties met de
technische specificaties, functioneel of non-functioneel, de benodigde koppelingen, de integratie en de te aan
te houden standaarden uitgewerkt.

In deze aanbesteding wordt uitgegaan van de standaarden en de standaardmodellen. Afwijkingen van de
standaarden creëren immers afhankelijkheden en afwijkingen die op termijn mogelijk lastig te migreren zijn
of problemen veroorzaken in de verbinding naar derde partijen. Het is echter denkbaar dat landelijk
vastgestelde standaarden niet geheel voldoen of lokaal/regionaal ongewenste beperkingen opleggen. In die
gevallen geldt het principe ‘pas toe of leg uit’.
4.2
GEMMA-architectuur en functionele schets architectuur
De standaard architectuurplaat van GEMMA is in perspectief van deze aanbesteding geplaatst: een brug naar
de (functionele) plaat die de ICT-Oplossing in de keten positioneert, met als doel hiermee een verbinding te
leggen naar:
de landelijk vastgestelde requirements (GEMMA), hier vertaald naar eisen en wensen;
de specificaties en wensen die de aanbestedende dienst als aanvulling op de GEMMA-requirements aan de
ICT-Oplossing stelt;
in te zetten koppelingen ten behoeve van integratie toepassingen;
doorontwikkeling.

Hierbij is https://www.gemmaonline.nl/index.php/Thema_Omgevingswet als basis genomen,






## Page 13

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 12 van 102


Figuur 3
‘De architectuurschets o.b.v. de GEMMA-plaat’3

De componenten zelf en de onderlinge relaties tussen de componenten is niet aangepast, wel is een meer
logische indeling in blokken gemaakt. Blok 5 (VTH) en blokken 1 en 9 (samenwerken/loket) vormen dé
kernelementen van de gevraagde  ICT-Oplossing, inclusief de verbindingen naar de Landelijke Voorzieningen
zowel DSO-LV als GDI.
De blokken 4 en 6 tot en met 8 zijn indirect onderdeel van de ICT-Oplossing of zijn optionele componenten,
afhankelijk van de soort (minimale, standaard, maximale) uitvraag bij deze aanbesteding (zie verder 4.4.7 van
deze bijlage en paragraaf 2.1 Aanbestedingsdocument).

De blokken 2 en 3 zijn geen kernelement van de gevraagde ICT-Oplossing, maar hebben wel interactie met de
ICT-Oplossing, minimaal in de vorm van procesondersteuning in deze aanbesteding. Of er in een later
stadium nadere integratie zal volgen, is mede afhankelijk van de ontwikkelingen van het DSO ná 2021.

Eis 4
Ontwikkelingen t.a.v. blok 2 en 3 die hun weerslag hebben op procesondersteuning dienen na 2021 ingericht
en ondersteund te worden.



3 Als bijlage (PDF) beschikbaar voor meer detailniveau

## Page 14

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 13 van 102
De ICT-Oplossing in de keten is  als volgt weer te geven:


Figuur 4
Functionele schets VTH

De ICT-Oplossing bevat voorzieningen en compartimenten, die wat betreft compartimenten collectief of
individueel/optioneel ingezet en uitgevraagd worden.
Collectieve voorzieningen
o
Ketenintegratie
Deze voorziening vormt het hart van de ICT-Oplossing, door de binnenkomende en
uitgaande informatiestromen te verdelen naar de juiste schakels in de keten.
o
Objectregistratie
Is de voorziening waar output van verzoeken en andere informatiestromen centraal en
voor de gehele keten inzichtelijk samenkomt en vormt het vertrekpunt voor toezicht en
handhaving. Daarnaast geeft het samen met informatie uit het DSO-LV een sluitend beeld
van objecten in de leefomgeving, ten behoeve van de beleidscyclus en
informatieverstrekking aan initiatiefnemers en andere belanghebbenden.
Individuele en/of optionele compartimenten (VTH):
o
Procesvolgsysteem (PVS)
Systeem dat gebruiker door het proces leidt van het behandelen van een aanvraag of melding
vanaf het ontvangen van de aanvraag tot en met het sluiten van een zaak, waarna het
vervolgens in het DMS/RMA wordt gearchiveerd. Hierbij dient er aandacht te zijn voor
termijnbewaking, rappelfunctie en een goede uitwisseling met de collectieve voorzieningen,
zodat op efficiënte en effectieve wijze de procesafhandeling kan plaatsvinden.

## Page 15

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 14 van 102
o
Zaaksysteem4
Systeem ter ondersteuning van zaakgericht werken, waarbij een zaak is gedefinieerd als '…
een samenhangende hoeveelheid werk met een gedefinieerde aanleiding en een gedefinieerd
resultaat waarvan kwaliteit en doorlooptijd bewaakt moeten worden'.
o
DMS/RMA4
Systeem voor het beheer van documenten ongeacht de vorm en toegepaste techniek waarbij
metadata is vastgelegd omtrent toegankelijkheid, beschikbaarheid, vindplaats, zaaktype,
resultaat, gevoeligheid en voortgang. Het document en de documentflow staan centraal.

Procesondersteuning voor RO:
o
Beleid en Planvorming (Conform standaard STOP/TP) (buiten scope)
o
Opstellen Toepasbare regels Conform Standaard (STTR) (buiten scope)
o
Monitoring

De individuele componenten zijn compartimenten binnen de ICT-Oplossing waar de aanbestedende dienst
zijn (hun) taken uitvoeren, gegevens beheren en een zekere vrijheid van inrichting hebben.
Er is gekozen voor een uitvraag waarbij deze compartimenten  optioneel af te nemen zijn in een standaard en
maximale uitvraag. De redenen hiervoor zijn:
te lage volumes binnen het VTH-domein om een specifiek VTH-systeem te rechtvaardigen dan wel de
keuze om VTH af te handelen in het (al dan niet bestaande) generieke Zaaksysteem;
de deelnemende gemeenten hebben (veelal) reeds een breed ingezet Zaaksysteem/DMS/RMA. Aan dit
systeem dient de gevraagde ICT-Oplossing gekoppeld te worden, waarbij de uitvraag zich strekt tot de
‘stekker’ naar het generieke zaaksysteem/DMS/RMA. De leveranciers van die systemen dienen de
‘contrastekker’ te leveren.
De uitvraag kent een minimale, standaard en maximale uitvraag (zie verder 4.4.7 van deze bijlage en
paragraaf 2.1 Aanbestedingsdocument). ,

Spec 1
De ICT-Oplossing voldoet aan de GEMMA-architectuur en kan de ‘Functionele schets VTH’ zoals weergegeven
in Figuur 4 (inclusief bovenstaande toelichting) invullen.



4 Het Zaaksysteem/DMS/RMA vallen buiten de primaire scope van deze aanbesteding m.u.v. de koppelingen naar de
systemen.

## Page 16

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 15 van 102
4.3
Ontwerp
4.3.1
Inleiding en Overzicht
De basisplaat hieronder geldt als uitgangspunt voor de rest van dit document.

Figuur 5
Basisplaat Architectuur Regionale aanbesteding VTH

Paragraaf 4.4 en verder geeft een nadere toelichting op de basisplaat. Hierbij is aangegeven wat de functie is
en welke functionaliteit de ICT-Oplossing hierbij dient te leveren. Waar mogelijk is dit gekoppeld aan de
GEMMA-componenten en -requirements.
4.3.2
Informatiestromen
Essentieel voor de samenwerking tussen verschillende organisaties is een beeld van de informatiestromen.
Temeer omdat een efficiënte en beveiligde digitale informatie-uitwisseling tussen de uitvoeringsdienst en de
regiogemeenten, in welke vorm dan ook, tot op heden problematisch is. De bestaande methodieken,
waaronder e-mail, WeTransfer en Dropbox, hebben specifieke nadelen op het gebied van
informatiebeveiliging en privacy. De ICT-Oplossing, en dan met name de ketenuitwisseling, moet hiervoor een
goede en rechtmatige oplossing bieden.
De informatievoorziening tussen Bevoegde Gezagen, uitvoeringsdiensten en landelijke voorzieningen is in
onderstaande afbeelding te zien. Bevoegd Gezag en de ODZOB hebben beide een aansluiting op het DSO en
kunnen via de STAM-standaard verzoeken ontvangen. Tevens biedt de samenwerkingsruimte van het DSO-LV
vanuit gebruikersperspectief een rudimentaire mogelijkheid om informatie uit te wisselen. Dit beperkt zich
tot het delen van een ‘projectmap’ en een ‘werkmap’ met daarin de aanvragen en begeleidende documenten.
De services van de DSO-LV Samenwerkfunctie vormen een goed uitgangspunt om te voldoen aan
samenwerking in de keten.

Zowel de regiogemeenten als de uitvoeringsdiensten gebruiken veel basisregistraties, landelijke
voorzieningen en sectorale informatievoorzieningen om gegevens op te halen c.q. vast te leggen. Wat nu

## Page 17

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 16 van 102
ontbreekt is een mogelijkheid om zaken, zijnde niet-vergunningsgerelateerde documenten (adviezen,
besluiten, opdrachtverlening, (output van) e-formulieren e.d.), maar ook objectgerichte registraties, vast te
leggen. Hiervoor is functionaliteit nodig ten behoeve van Ketenintegratie en Objectregistratie. Deze
onderdelen worden respectievelijk in paragraaf 4.4.2 en 4.4.5 uitvoerig beschreven. Onderstaand plaatje
maakt duidelijk waar deze in de informatiestromen gepositioneerd zijn.


Figuur 6
Informatiestromen
4.3.3
Multi-tenant inrichting
Spec 2
De ICT-Oplossing biedt deelnemers die onderdeel uitmaken van ambtelijke samenwerkingsverbanden de
mogelijkheid  om in een multi-tenant omgeving dan wel in separate omgevingen per gemeente te werken.

Toelichting:
Met multi-tenancy bedoelen we in dit geval één omgeving waarin meerdere gemeenten kunnen werken. De
(persoons)gegevens van de gemeenten blijven altijd gescheiden dan wel herleidbaar naar de betreffende
gemeente. De applicatie, autorisaties en gegevens zijn bovendien zo in te richten per gemeentelijke
deelomgeving dat gemeenten rechtmatig conform de privacywetgeving (AVG) kunnen werken.

Er zijn meerdere argumenten voor multi-tenancy:
Veel regiogemeenten maken deel uit van een gemeentelijk samenwerkingsverband. Zij hanteren
daarin verschillende filosofieën over harmonisatie van applicatielandschappen. Deze filosofieën zijn
deels afhankelijk van de juridische vorm van samenwerking, de doelstellingen van de samenwerking
en het aantal deelnemers. Voorbeelden hiervan zijn:
o
de werkorganisatie Druten Wijchen: harmonisatie naar één multi-tenancyomgeving voor beide
gemeenten om complexiteit, kosten en kwetsbaarheid te verminderen. Medewerkers kunnen
elkaar op termijn gaan vervangen in de processen voor Druten en Wijchen. Er zijn daarnaast
minder lokale koppelingen nodig voor uitwisseling van gegevens, waardoor de
implementatie- en beheerkosten en –lasten worden gereduceerd;
o
binnen de Dienst Dommelvallei zijn de desbetreffende drie gemeenten zelf de gebruikers en
functioneel beheerders van de ICT-oplossing. Harmonisatie van de drie applicaties naar één

## Page 18

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 17 van 102
multi-tenancyoplossing voor drie gemeenten betekent een (te) complex (organisatorisch)
scenario. Deze gemeenten kiezen er voor om driemaal dezelfde applicatie naast elkaar te
gebruiken. Indien deze gemeenten in de toekomst meer met elkaar willen samenwerken,
overwegen ze een multi-tenancyoplossing.
Het contract wordt aangegaan voor maximaal tien jaar. Binnen die periode kunnen (de
uitgangspunten voor) ambtelijke samenwerkingen veranderen. De leverancier moet voorzien in deze
mogelijke veranderingen.

Het is bij de aanbestedende dienst bekend dat het al dan niet inrichten van een multi-tenancyoplossing
afhankelijk is van andere factoren, zoals de mate van gezamenlijk gebruik van de GBA, het DMS en de Active
Directory, alsmede van het gezamenlijke gebruik van een KlantContactCentrum (KCC).

4.4
Specificaties en Wensen
4.4.1
Inkomende informatiestromen (DSO-LV en overig)
Het VTH-proces start met een binnenkomend verzoek, dat veelal uit het DSO-LV afkomstig is en voldoet aan
de STAM/IMAM-standaard. De praktijk wijst uit dat er vele andere binnenkomende informatiestromen zijn,
niet alleen vanuit verzoeken (vergunningen/meldingen) maar ook vanuit toezicht en handhaving. Denk bij dat
laatste aan informatie vanuit registers en diverse sectorale voorzieningen. Kenmerkend is dat deze
informatiestromen (nog) niet-gestandaardiseerd binnenkomen en daardoor vaak op allerlei wijzen verwerkt
worden; doorgaans niet zaakgericht.
De ICT-Oplossing dient ook deze ‘derde’ stromen te kunnen ontvangen, en biedt daar een standaard
(koppelvlak) voor aan, zodat bronhouders/eigenaren van dergelijke voorzieningen daar op kunnen aansluiten.
Zie inhoudelijk ook het onderwerp ‘Ketenintegratie’.


Functie

Start van een (keten)proces door een
trigger via:
- een verzoek vanuit het DSO volgens
STAM/IMAM;
- een andere bron (non-DSO, non-STAM).
Denk aan e-formulieren, gekoppelde
registers, opdrachten vanuit Bevoegde
Gezagen naar Omgevingsdienst of
Veiligheidsregio etc.

Informatie terug naar de bron kan
voorkomen; Denk bijvoorbeeld aan een
verzoek om aanvullingen.

4.4.2
Ketenintegratie
Binnen de ICT-Oplossing is dit het knooppunt tussen DSO-LV, het Procesvolgsysteem c.q. het Zaaksysteem,
Bevoegde gezagen en de Objectregistratie. Dit knooppunt stuurt informatie vanuit deze bronnen de goede
kant op en communiceert hierbij voor wat betreft de STAM-aanvragen met de samenwerkingsruimte in het
DSO. Het portaal draagt zorg voor een rechtmatige/veilige, uitwisseling van de door de diverse partijen
benodigde informatie. Hierbij gaat het niet alleen om de informatie die door middel van de STAM wordt
uitgewisseld, maar zeker ook voor overige informatie. Te denken valt aan externe adviesrapporten,
(aanvullende) stukken die betrekking hebben op de besluitvorming en de formele archivering
(Dossieroverdracht), binnenkomende informatiestromen uit centrale registers, niet-zijnde basisregistraties et
cetera.
Naast uitwisseling kan de Ketenintegratie ook statussen van lopende zaken weergeven in de keten zodat op
casusniveau actief gemonitord kan worden zonder de noodzaak te beschikken over derde informatiestromen
of te moeten inloggen op systemen van ketenpartners.

## Page 19

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 18 van 102


Functie

Binnenkomende informatie-
stromen landen in de
Ketenintegratie. Verzoeken
(STAM) verdelen zich naar de
juiste ketenpartner(s) ter
afhandeling in het eigen PVS
en/of zaaksysteem. Relevante
zaakinformatie gaat actief of
passief via Ketenintegratie naar
de juiste ketenpartner, zowel
tussentijdse resultaten als
eindresultaten van een zaak.
Andere (non-STAM)
informatiestromen kunnen op
dezelfde wijze als hierboven
leiden tot een zaak, maar
kunnen ook rechtstreeks (en evt.
geautomatiseerd) tot een zaak
en een update in de
Objectregistratie leiden.
GEMMA: component voor het op afstand onafhankelijk van elkaar, gecoördineerd samenwerken aan een
gezamenlijk doel.


4.4.2.1
Ketenintegratie: Specificaties en Wensen
Eis 5
De ICT-Oplossing is in staat om adviezen bij een ketenpartner uit te zetten via DSO-LV door middel van de
Samenwerkingsruimte (werkmap) of direct via de Ketenintegratie als het oorspronkelijke verzoek niet via
DSO-LV is ontvangen. In het PVS en/of Zaaksysteem van de ketenpartner wordt vervolgens automatisch een
zaak gestart. De Ketenintegratie geeft hier een terugkoppeling (alert/notificatie) op. De oplevering van het
advies aan de aanvragende ketenpartner verloopt eveneens via de Ketenintegratie, waarbij er via een
notificatie wordt geattendeerd.

Spec 3
Ketenpartners kunnen digitaal (aan)vragen indienen bij een uitvoeringsorganisatie binnen de keten, inzage
krijgen in opdrachten die binnen de keten worden uitgevoerd dan wel in samenwerking met de ketenpartner.
Relevante documentatie kan met uploaden en downloaden via de Ketenintegratie uitgewisseld worden. Deze
functionaliteit is uitsluitend toegankelijk voor geauthentiseerde partijen en ontsluit alleen functionaliteit en
informatie waarvoor de desbetreffende partij is geautoriseerd.
De Ketenintegratie geeft voor ketenpartners zaakstatusinformatie weer, waaronder in elk geval de stand van
zaken in het proces, de behandelaar en de verzoeken om aanvullende informatie.

Spec 4
De Ketenintegratie kan volledige dossieroverdracht ondersteunen. Met andere woorden: naast
procesgebonden documenten (archiefbescheiden) kan ook het (volledige) zaakdossier en de erbij behorende
metadata ten behoeve van de formele archiefplicht worden uitgewisseld.

Spec 5
De Ketenintegratie heeft tezamen met het gekoppelde PVS en de Objectregistratie zowel administratieve als
geo-zoekingangen naar objecten en de daaraan gekoppelde zaken.

Spec 6
In de Ketenintegratie kan een gebruiker bij een aanvraag middels een selectie de gewenste bijlagen
toevoegen aan de (advies)zaak.

Spec 7
De Ketenintegratie en de Objectregistratie bieden de mogelijkheid om de aanvrager en (medewerkers van)
organisaties buiten de keten (externe adviseurs, laboratoria etc.) toegang te geven tot specifieke dossiers.

Spec 8
De Ketenintegratie biedt duidelijk overzicht welke partijen zijn betrokken bij een zaak, ook als deze zich niet
in de primaire keten bevinden.


## Page 20

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 19 van 102
Wens 2
Er is sprake van een directe overdracht van Vergunningverlening naar Toezicht & Handhaving tussen
organisaties, met name van Bevoegd Gezag naar uitvoeringsorganisaties.

Spec 9
De ketenintegratie kan afgeronde zaken archiefwaardig overdragen, bijvoorbeeld van uitvoeringsorganisatie
naar bevoegd gezag. Dit moet  op termijn (uiterlijk voor 2024) ook een (common ground) functionaliteit zijn
tussen de zaaksystemen/DMS-RMA’s.

Wens 3
Het is mogelijk om e-formulieren te koppelen, inclusief het opstellen van en verwerken van de output van
vragenbomen.

Wens 4
Er is sprake van een centraal binnenkomend kanaal met signalering indien niet op tijd geacteerd wordt, waar
dan ook in de keten.

4.4.3
Procesvolgsysteem (PVS)5
Een PVS  leidt de gebruiker door het volledige proces, namelijk vanaf het behandelen van een aanvraag of
melding tot en met de afhandeling. De archivering van het volledige dossier vindt plaats in het
Zaaksysteem/DMS/RMA. In het PVS is aandacht voor termijnbewaking, rappellering en de uitwisseling met de
Ketenintegratie en de Objectregistratie.


Het PVS is de primaire interface voor medewerkers VTH om de
processtappen van een zaak te doorlopen. Het biedt
toegevoegde waarde ten opzichte van een standaard
zaaksysteem door aanvullende functionaliteit te benutten,
zoals legesberekeningen, selecteren van voorschriften,
besluitenregistratie, publicaties naar DROP et cetera.
Verder biedt het ondersteuning in de communicatie met het
DSO: dynamische voorschriften, opvragen van stelselcatalogus,
integratie wet- en regelgeving.

Mobiel toezicht is een belangrijke aanvulling op het PVS om de
administratieve last van toezicht zoveel mogelijk te beperken.

4.4.3.1
Specificaties en Wensen: Algemeen
Spec 10 De ICT-Oplossing bevat een workflowmanagementcomponent waarmee de verschillende typen werkprocessen
van de opdrachtgevers kunnen worden ingericht.

Spec 11 De ICT-Oplossing beschikt over standaard werkprocessen die door de leverancier zijn geleverd en actueel
worden gehouden als gevolg van wetswijzigingen. Tot de standaard werkprocessen die de leverancier heeft
ingericht, behoren in ieder geval de (basis)processen behorend bij de regionaal afgesproken ZTC, opgenomen
in deze aanbesteding.

Spec 12 Indien een standaard werkproces door een wetswijziging verandert, moeten lopende zaken nog met het
voorgaande werkproces, dat gebaseerd is op de oude wetgeving, afgehandeld kunnen worden.

Spec 13 Documenten zijn digitaal te waarmerken, te ondertekenen en te annoteren tijdens het procesverloop. Vanuit
het PVS is deze functionaliteit te initiëren, feitelijke handeling vindt in het zaaksysteem of DMS plaats.

Spec 14 Er dient bij de overheveling van (afgehandelde) zaakdossiers naar het DMS ten behoeve van de archiefplicht,
controle- en correctieslagen in het PVS mogelijk te zijn.

Spec 15 Ten tijde van vernietiging van gegevens in het zaaksysteem, leidt dit ook tot een vernietiging van deze
gegevens in de overige componenten van de ICT-oplossing (Ketenintegratie en Objectregistratie)


5 Andere benamingen voor het PVS zijn: vakapplicatie, procesapplicatie of taak-/domeinspecifieke applicatie (TSA).

## Page 21

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 20 van 102
Spec 16 De ICT-Oplossing kan geautomatiseerd, zowel als dataveld als in documenten, persoonsgegevens
pseudonimiseren in de zin van artikel 32 lid 1 A AVG. De brongegevens c.q. –documenten blijven hierbij in
tact.

Wens 5
Op het gebied van metadata kan de ICT-Oplossing aanvullende gegevens registreren, zoals hier opgenomen:

1. Ten behoeve van het proces Handhaving is het mogelijk een datumveld op te nemen waarin de einddatum
van een hersteltermijn (= verbeurddatum) kan worden aangegeven.
2. Eveneens voor het handhavingsproces is het mogelijk de functionaliteit te leveren dat er automatisch
wordt doorgeteld naar de volgende juridische actie (van verbeurdverklaring naar invorderingsbeschikking).
3. Voor het genereren van management-/sturingsinformatie bij zienswijzen is een veld op te nemen waarin
kan worden vastgelegd of een zienswijze tot een gewijzigd besluit heeft geleid.
4. Tijdens de configuratie van het systeem is het mogelijk om bij de zaaktypen de onderdelen uit de
Checklist bij het tab Statussen ook als fasen in te richten.

4.4.3.2
Specificaties en Wensen: Vergunningverlening / Toetsen van verzoeken
Spec 17 De ICT-Oplossing ondersteunt tijdens het procesverloop het overstappen van een reguliere naar een
uitgebreide (gefaseerde) aanvraag voor een omgevingsvergunning.

Spec 18 De ICT-Oplossing bevat ten behoeve van de volledigheidstoets van een aanvraag checklists, conform de
wettelijk geldende indieningsvereisten. De leverancier onderhoudt deze lijsten en past deze bij
wetswijzigingen onverwijld (uiterlijk binnen 2 maanden) aan.
Toelichting: checklists worden gevraagd om aanvragen om een omgevingsvergunning voor bouw en
milieuactiviteiten te beoordelen.

Wens 6
Tijdens de procesafhandeling van bijvoorbeeld een bouw- of een inritvergunning kan in het PVS een stap
worden opgenomen waarbij een BAG- of een BGT-bericht (door middel van bijv. een geautomatiseerde mail)
wordt gestuurd naar de betreffende beheerder bij een regiogemeente ter actualisatie van de basisregistratie.

Spec 19 De ICT-Oplossing biedt een integrale voorschriftenbibliotheek, welke (aan)gevuld kan worden via externe
bibliotheken, met name met de content van LRSO. Eventueel vanuit derde partijen als BRIS en SesomWeb.

Wens 7
De vergunningverlener kan adviezen die extern worden afgehandeld via de ICT-Oplossing (en eventueel DSO-
LV) uitzetten, volgen en weer ontvangen.
Toelichting: denk aan adviesaanvragen vanuit Bevoegd Gezag naar een uitvoeringsorganisatie.

Wens 8
De ICT-Oplossing biedt de mogelijkheid BIBOB informatie op te vragen en te verwerken.

Spec 20 De ICT-Oplossing ondersteunt de veranderingen als gevolg van de aanstaande inwerkingtreding van de Wkb.
Toelichting: Gelijktijdig met de Omgevingswet treedt de Wet Kwaliteitsborging voor het bouwen in werking.
De rol en verantwoordelijkheden van de gemeente en van de bouwer veranderen daardoor flink, een
onafhankelijk kwaliteitsborger verschijnt ten tonele en er dienen andere stukken gegenereerd te worden.  Dit
betekent een ander proces, met andere actoren en andere documenten.

4.4.3.3
Specificaties en Wensen: Advies
Spec 21 De ICT-Oplossing kan bij advieszaken de hierna gespecificeerde gegevens c.q. overzichten tonen.
▪
Aan wie om advies is gevraagd.
▪
Wanneer dit is gevraagd.
▪
Wanneer het advies uiterlijk terug moet zijn.
▪
Wanneer het advies is terug ontvangen.
▪
Of het een akkoord/niet-akkoord of een akkoord onder voorwaarden betreft (overzicht)
▪
Of aanvullende gegevens nodig zijn.
▪
Of de aanvullende gegevens zijn opgevraagd.
▪
Wanneer deze uiterlijk binnen moeten zijn.
▪
Het advies zelf.


## Page 22

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 21 van 102
Wens 9
De ICT-Oplossing ondersteunt mogelijkheden om vervolgacties en monitoring in te plannen
Toelichting: De procesbeschrijvingen (en zaaktypes) beperkt zich veelal tot de standaard VTH-procedures. De
daarmee samenhangende opvolging van die procedures niet is vermeld. Zo is het bijvoorbeeld na doorlopen
van een vergunningprocedure nodig dat periodiek wettelijk geregelde vervolgactie wordt uitgevoerd
(bijvoorbeeld 5-jaarlijkse actualisatie risicoregister en 5-jaarlijkse evaluatie van zeer zorgwekkende stoffen).
Het is wenselijk om hier in de ontwerpfase hiermee rekening te houden, zodat de hiervoor benodigde
gegevens bij het doorlopen van een procedure kunnen worden ingevoerd en gemonitord

4.4.3.4
Specificaties en Wensen: Toezicht en Handhaving
Spec 22 Resultaten uit toezicht moeten landen in het VTH systeem en direct in een sjabloon op te nemen zijn.

Spec 23 De ICT-Oplossing is in staat de status van het uitvoeren van bestuursdwang, het voornemen tot het opleggen
van c.q. het vorderen van een dwangsom en gedogen te registreren. Geldt eveneens voor bezwaar en beroep
en zienswijzen.

Spec 24 Zaken kunnen ook starten vanuit (mobiel) toezicht, bijvoorbeeld bij een constatering of een klacht. De ICT-
Oplossing maakt het daartoe mogelijk naast zaakgericht ook locatiegericht te werken.

Spec 25 Toezichtsprogramma’s zijn te plannen en prioriteren op basis van (combinaties van) kenmerken van
inrichtingen.

Spec 26 Toezichtszaken zijn te plannen op basis van/te koppelen aan een financiële verantwoording en/of planning.

Spec 27 De ICT-oplossing is in te zetten als registratiemiddel (bundeling) bij bulkmeldingen.
Toelichting (voorbeeld): er kunnen meerdere meldingen van klachten binnenkomen over één locatie c.q.
incident. Deze meldingen dienen wel geregistreerd te worden zonder dat hiervoor per melding een zaak
wordt aangemaakt.
4.4.3.5
Specificaties en Wensen: Mobiel Toezicht
De ICT-Oplossing heeft voor Toezicht & Handhaving op locatie de mogelijkheid controles uit te voeren met
behulp van een tablet zonder dat er tijdens de inspectie nog andere middelen nodig zijn, zoals andere
digitale devices en pen en papier. Een camera voor detailfoto’s is hierop een uitzondering.

Spec 28 Met de ICT-Oplossing kan mobiel toezicht worden uitgeoefend met behulp van een portable device. Op
locatie kan een medewerker hierdoor controle uitvoeren, registreren en afhandelen.

Spec 29 Een medewerker kan op locatie zelf een controle(zaak) aanmaken, als die nog niet is aangemaakt.
Bijvoorbeeld naar aanleiding van een waarneming ‘in het veld’.

Spec 30 Bij het aanmaken van een werkvoorraad kunnen de documenten en tekeningen geselecteerd worden die
tijdens de controle op locatie beschikbaar moeten zijn. Daarnaast moeten de contactgegevens van aannemers
en constructeurs op locatie beschikbaar zijn en moet de status van (bouw)tekeningen en andere documenten
duidelijk te zien zijn.

Zie ook ‘Objectregistratie’

Spec 31 Synchronisatie van de gegevens van een werkvoorraad c.q. van uitgevoerde controles moet op minimaal 4G-
verbinding en WiFi werken. Om bandbreedte te besparen heeft de gebruiker de keuze welke gegevens (bijv.
hoeveelheid controles, wel/geen foto’s, tijdspanne) gesynchroniseerd moeten worden.

Spec 32 Een controle moet offline uitgevoerd kunnen worden en de controlebevindingen worden automatisch
gesynchroniseerd zodra er weer een internetverbinding is.

Spec 33 Met de ICT-Oplossing moeten controlebevindingen op een (bouw)tekening vastgelegd kunnen worden zodat
direct duidelijk is op welke locatie deze betrekking hebben. Het gaat hierbij om ten minste een bevinding,
een aantekening en één of meerdere foto's.


## Page 23

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 22 van 102
Spec 34 De ICT-Oplossing moet de controlelijsten van het integraal Toezicht Protocol (iTP van de vereniging Bouw-en
Woningtoezicht Nederland) ondersteunen voor wat betreft bouwen en slopen. Zodra er nieuwe versies van het
iTP beschikbaar zijn, draagt de leverancier er zorg voor dat deze beschikbaar komen in De ICT-Oplossing.

Spec 35 De ICT-Oplossing ondersteunt controlelijsten die door de Opdrachtgevers zelf ontwikkeld en beheerd kunnen
worden of van andere instanties afkomstig zijn zoals van ODnl (Omgevingsdienst NL) voor bijvoorbeeld sloop
en monumenten. Controlelijsten zijn ook tussen organisaties te delen binnen het systeem.

Spec 36 De Landelijke HandhavingsStrategie (LHS) moet ondersteund worden. Dat houdt ten minste in dat de gekozen
strategie als bedoeld in de interventiematrix, per constatering vastgelegd kan worden en er
verandering/opschaling mogelijk is, ook als dit later in het proces, bijvoorbeeld door een juridisch
medewerker, wordt vastgesteld. De (uiteindelijk) gekozen strategie (bijv B4) moet als data inzichtelijk in een
monitoring kunnen worden opgeleverd.

Spec 37 Van de controle kan een automatisch gegenereerd controlerapport met bevindingen worden verkregen. In
brieven die naar aanleiding van een controle worden opgesteld, kunnen controlegegevens zoals bezoekdatum
en controleresultaat automatisch verwerkt worden.

Wens 10 (Basis-)Gegevens over inrichtingen moeten ter plekken kunnen worden aangepast in de tablet en daarmee
automatisch geregistreerd in de Objectregistratie.

Wens 11 Controlelijsten zijn ‘slim’ en/of te filteren, bijv. op basis van de activiteiten van een bedrijf komen de juiste
vragen (als eerste) naar voren en hoeft niet een volledige lijst te worden doorlopen.

4.4.3.6
Specificaties en Wensen: Besluiten
Spec 38 De ICT-Oplossing is in staat om genomen besluiten te registreren. Van de besluiten kunnen minimaal de
hierna opgesomde gegevens worden geregistreerd.
▪
Type en soort besluit
▪
Datum besluit
▪
Status
▪
Kenmerk
▪
Datum ter-inzage-legging
▪
Publicatiedatum
▪
Verzenddatum
▪
Ingangsdatum
▪
Datum onherroepelijk besluit
▪
Documenten die bij het besluit horen

Spec 39 Voor bouw: voorwaarden die gesteld worden bij vergunningverlening dienen in de ICT-Oplossing
geregistreerd en bewaakt te worden. Toelichting: het gaat hier onder andere om constructiegegevens.

Spec 40 Na definitieve besluitvorming en het sluiten van de zaak moet de ICT-Oplossing via de koppeling de gegevens
van de betreffende zaak in het Zaaksysteem kunnen vergrendelen (freeze), zodat documenten en metadata
niet meer gewijzigd kunnen worden door de gebruikers, m.u.v. een recordsmanager.

Spec 41 Het publiceren van kennisgevingen en bekendmakingen naar DROP moet vanuit de ICT-Oplossing met behulp
van sjablonen ondersteund worden zodat een vergunningverlener dit eenvoudig zelf kan doen.

4.4.3.7
Specificaties en Wensen: Leges en heffingen
Spec 42 De ICT-Oplossing heeft een door de applicatiebeheerder aanpasbare rekenmodule voor leges.

Spec 43 De ICT-Oplossing ondersteunt meerdere legesverordeningen van meerdere gemeenten (multi-tenant).

Spec 44 De legesmodule van de ICT-Oplossing moet de hierna gespecificeerde typen legesartikelen ondersteunen.
▪
Vast bedrag per aanvraag
▪
Variabel bedrag, bijvoorbeeld een percentage van de bouwkosten
▪
Staffel, waarbij de hoogte van de bouwkosten in schijven (staffels) wordt verdeeld. Voor elke staffel wordt
een bepaald percentage van dat deel van de bouwkosten gerekend als leges.


## Page 24

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 23 van 102
Spec 45 De ICT-Oplossing kan vastleggen gedurende welke periode een legesverordening geldig is.

Spec 46 Alleen een daartoe geautoriseerde medewerker (applicatiebeheerder) kan de parameters voor
legesberekeningen aanpassen.

Spec 47 De ICT-Oplossing levert de CBS W011 export (= opgave gegevens verleende omgevingsvergunningen bouwen,
bouwkosten > € 50.000,-), volgens het format van het CBS).

4.4.3.8
Specificaties en Wensen: Documentgeneratie
Spec 48 De ICT-Oplossing heeft een eigen interne sjabloonapplicatie voor het maken van standaardbrieven.

Spec 49 Er bestaat de mogelijkheid om de ICT-Oplossing te koppelen met sjablonengeneratoren die verbonden zijn
met de Kantoorautomatisering van opdrachtgevers. Voorbeelden van gangbare documentgeneratoren zijn
iWriter, SmartDocuments en Xential.

Spec 50 De ICT-Oplossing is in staat om het zaaknummer (kenmerk), NAW-gegevens, referenties en datums uit het
gekoppelde zaaksysteem op te halen en in te voegen in de standaardbrieven.

Spec 51 De ICT-Oplossing is in staat om zelf te kiezen variabelen en velden toe te voegen aan standaardbrieven.

Spec 52 De ICT-Oplossing is in staat om tekstblokken toe te voegen aan standaardbrieven, afhankelijk van een
voorwaarde (als-dan constructie).

Spec 53 De ICT-Oplossing is in staat om de huisstijl van de betreffende opdrachtgevers toe te passen op de door het
systeem gegenereerde standaardbrieven.

Spec 54 De ICT-Oplossing is in staat om wijzigingen van de huisstijl op één plaats te beheren.

Spec 55 De ICT-Oplossing is in staat om standaard tekstblokken in meerdere sjablonen te kunnen gebruiken.

Spec 56 De ICT-Oplossing is in staat om metadata van de standaardbrieven uit te wisselen met de metadata van het
document in het gekoppelde Zaaksysteem/DMS-RMA.

4.4.4
Zaaksysteem en DMS/RMA
Voor de ODZOB is voor de maximale uitvraag als separaat onderdeel in de aanbesteding opgenomen.
4.4.5
Objectregistratie
De Objectregistratie is de centrale opslag van locatiegerelateerde gegevens, conform het ‘locatiedomein’
(nader toegelicht bij Standaarden ‘Domeinen’)



De Objectregistratie geeft per Omgevingsobject minimaal weer:
▪
Basisgegevens (waaronder GEO-informatie)
▪
Specifieke gegevens per domein/thema (activiteitstypen)

## Page 25

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 24 van 102
▪
Status en historie van het object
▪
Koppelingen/verwijzingen naar afgeronde, lopende en toekomstige zaken en de bijbehorende
documenten

De gegevens in de Objectregistratie zijn inzichtelijk voor de betreffende bevoegde gezagen en muteerbaar
voor de organisatie die uitvoerder is van de wettelijke taak.

In de startarchitectuur:
Functie:

De Objectregistratie legt
basisgegevens van de ruimtelijke
objecten vast en koppelt hieraan
de output van de VTH-processen
en wel zodanig dat informatie:
- geo-traceerbaar is;
- tijdsgebonden weergegeven
wordt, o.a. conform de
zaakafhandeling rond het
object;
- vanuit verschillende activiteiten
koppelbaar is;
- deelbaar is tussen Bevoegd
Gezag en
uitvoeringsorganisaties.

Daarnaast dient de informatie
samen met informatie uit het
DSO als input te dienen voor de
beleidscyclus, in het bijzondere
voor de monitoringsfunctie.

4.4.5.1
Specificaties en Wensen Objectregistratie
Spec 57 De Objectregistratie kent een logische gelaagdheid van registratie: object/locatie – activiteiten –
voorzieningen, of direct: object/locatie – voorzieningen. Onder de Omgevingswet kan dit een model worden
als: activiteitstype – activiteiten – kenmerken. De lijst van activiteiten is gelijk aan de activiteiten zoals die
gedefinieerd zijn in het DSO-LV.

Spec 58 De Objectregistratie levert van de objecten een integraal beeld op. Dat wil zeggen dat de Objectregistratie
activiteiten koppelt aan een object/locatie, die door verschillende ketenpartners worden afgehandeld als één
geheel. De verantwoordelijke binnen de keten heeft exclusief mutatierechten (beheer) op eigen te behandelen
activiteiten en kan deze rol overdragen aan een andere ketenpartner. Een ketenpartner heeft hiertoe
standaard alleen toegang tot de objecten/locaties waar de ketenpartner Bevoegd Gezag is of de aangewezen
uitvoeringsorganisatie is. Betreffende ketenpartner kan aan een object/locatie wel een andere ketenpartner
toegang verlenen, bijv. bij een object op de grens van twee gemeenten.

Spec 59 De Objectregistratie volgt statusgewijs de VTH-processen, ofwel: bij een object zijn hierna gespecificeerde
statussen minimaal te onderscheiden.
▪
binnengekomen verzoek, nog niet in behandeling
▪
verzoek in behandeling
▪
vigerende situatie
▪
toezicht/handhaving: geconstateerde situatie
Bij deze statussen horende documenten uit de corresponderende zaken zijn via het object in te zien door
middel van objectgericht zoeken. De diverse statussen blijven afzonderlijk van elkaar bewaard ten behoeve
van een doorlopend tijdsbeeld, zijn eenvoudig in te zien en te onderscheiden.


## Page 26

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 25 van 102
Wens 12 De Objectregistratie kent ook een status om informatie (vanuit derde systemen) te verwerken die niet via het
‘reguliere’ VTH proces binnenkomt. In het PVS kunnen dergelijk informatiestromen als een eenvoudige
toezichtszaak (geautomatiseerd) verwerkt en daarmee gearchiveerd worden.
Toelichting: Denk hierbij aan cases als ‘gegevens energiebesparende maatregelen’ (RVO), PRTR en
zwemwatergegevens.

Spec 60 NAW-gegevens zijn tussen de objecten en de zaken te synchroniseren, binnen de ICT-oplossing óf met het
generieke zaaksysteem.

Spec 61 Gegevens(velden) en statussen in de Objectregistratie zijn te vullen vanuit de processen/workflows in het
gekoppelde PVS. Dit geldt eveneens voor additionele gegevens(velden), die later op verzoek van de
opdrachtgevers zijn toegevoegd. Waarbij deze additionele gegevensvelden per opdrachtgever in het
datamodel in te passen zijn, en niet als zgn. vrije velden worden toegevoegd.

Spec 62 De Objectregistratie kan relationele verbanden leggen tussen objecten op één locatie of dicht bij elkaar
gelegen, met globaal dezelfde of vergelijkbare activiteiten, maar wel met verschillende
eigenaren/drijvers/Kamer van Koophandel-inschrijvingen. Met name voor toezicht, maar soms ook voor
vergunningverlening, moeten deze als één object te benaderen zijn.

Spec 63 De ICT-oplossing is in staat een adres te herkennen als een adres met de aanwezigheid van een
Rijksmonument of een Gemeentelijk Monument dan wel een Karakteristiek pand en legt dit vast in de
Objectregistratie.

Spec 64 Kadastrale gegevens (BRK) worden geïmporteerd in de Objectregistratiecomponent van de ICT-Oplossing via
de Landelijke Voorziening of het gemeentelijk beheersysteem.

Spec 65 Gegevens in de Objectregistratie zijn direct uit het systeem te halen voor gebruik in andere toepassingen  van
de opdrachtgevers, bijvoorbeeld via GEO (WMS/WFS) en als ruwe data. Dit staat los van de monitoring in het
kader van de beleidscyclus (Big8). Voor operationele taken moeten soms ook analyses gemaakt worden op
basis van gegevens uit objectdossiers. Voor de minder complexe vraagstukken is dit zelfstandig mogelijk.

Spec 66 De ICT-oplossing voorziet in de mogelijkheid de volgende gevoeligheden vast te leggen:
•
een bestuurlijke gevoeligheid;
•
een historische gevoeligheid (denk ook aan gevaarlijke situatie, agressie, etc.);
•
een omgevingsgevoeligheid.

Spec 67 Locatie moet aangemaakt kunnen worden zonder (directe) aanleiding in de vorm van een verzoek. De
informatie moet geborgd kunnen worden zonder ‘harde’ melding of klacht, maar bijvoorbeeld op basis van
een waarneming of mutatie in derde systemen, zoals de basisregistraties.

Wens 13 Voor wat betreft zaakgerelateerde informatie volgt de Objectregistratie het gekoppelde PVS en het
Zaaksysteem/DMS-RMA ten behoeve van documentmanagement en archieffunctionaliteit.

Wens 14 Ten behoeve van de gegevenskwaliteit kan de Objectregistratie in bulk gegevens verifiëren en hierover
rapporteren en benodigde correcties voorbereiden.
Voorbeeld: voor alle locaties van een industrieterrein in één keer de NHR- en BAG-gegevens checken,
eventueel in combinatie met een bulkcontrole (‘gevelcontroles’) via (mobiel) toezicht. Afwijkingen kunnen
vervolgens administratief, en mogelijk ook zaakgericht, verwerkt worden.

Wens 15 De Objectregistratie biedt een logische registratiewijze van objecten (inrichting – activiteiten – voorzieningen)
en sluit hierbij in de toekomst aan op de wijze van registratie onder de Omgevingswet/DSO en/of een nog te
ontwikkelen landelijke standaard.
Toelichting: Denk hierbij ook aan het op termijn verdwijnen van kenmerkende gegevens zoals SBI, A/B/C
typeringen et cetera. Mogelijk krijgt dit opvolging in de registratie van activiteiten met unieke
registratiekenmerken en/of volgt hier nog een landelijke standaard voor.
4.4.6
Ruimtelijke Ordening
Software om omgevingsplannen te maken, te publiceren en te beheren, valt buiten de scope van deze
aanbesteding. Het gaat dan om plansoftware en software voor Toepasbare Regels. Het besluitvormingsproces
rondom deze (RO-)zaken is wel onderdeel van de uitvraag. De ICT-oplossing zal de besluitvorming rondom

## Page 27

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 26 van 102
omgevingsplannen, visies, zienswijzen, bezwaren en dergelijke wel moeten kunnen ondersteunen, inclusief
de RO-attributen. De procesmatige vaststelling van deze plannen, de besluitvorming, wordt vaak wel in VTH-
software afgehandeld. Dit kan ook omdat het besluitvormingstraject rondom bestemmingsplannen kan
verlopen via het bestaande zaaktype ‘Afhandelen aanvraag uitgebreid’, aangevuld met attributen. Omdat
deze aanbesteding breed uitvraagt (zie 3.1 Activiteiten), komt deze functionaliteit al mee en kunnen de RO-
processen afgehandeld worden. Dit deel van het RO-proces maakt daarmee onderdeel uit van de
aanbesteding.
4.4.7
Minimale, standaard, maximale  uitvraag
In het Aanbestedingsdocument is aangegeven welke keuzes elke deelnemer van de uitvraag maakt.
De keuzes zijn:
1.  Minimale uitvraag; dit is het minimale instapniveau om aan de aanbesteding te kunnen deelnemen.
2.  Standaard uitvraag, al dan niet met optionele componenten met als aanvullende opmerking dat deze
gericht zijn op de kern van de uitvraag, zijnde het VTH-domein.

De uitvragen zijn hier weergegeven en nader toegelicht, mede omdat de gekozen uitvraag gevolgen heeft op
de te leveren dan wel te realiseren koppelingen en de prestatie  voor inrichting en support.




## Page 28

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 27 van 102
4.4.7.1
Minimale Uitvraag


Figuur 7: Minimale Uitvraag

Deze variant kent geen PVS of een (eerder ingekocht) PVS van een 3e  leverancier:
Zonder PVS: de inkomende informatiestroom zal direct in het zaaksysteem verwerkt worden, via hier
(zelf) te configureren zaaktypen en processen. Output van de zaakafhandeling gaat voor wat betreft
de ketenuitwisseling terug naar de Ketenintegratie, voor wat betreft de objecten en
activiteitenregistratie naar de Objectregistratie en op termijn mogelijk (ook) naar het DSO.
Deze variant is een valide optie indien de volumes bij VTH laag zijn (kleine gemeente, veel taken
uitbesteed aan ketenpartners, etc.).
PVS van 3e leverancier: in basis functioneel geen verschil met basissituatie. Wel dient de deelnemer
met de leverancier van het betreffende PVS een koppeling (contrastekker) te leveren naar de
Ketenintegratie en de Objectregistratie of te kiezen voor handmatige overdracht van gegevens.
Deze optie is valide indien de opdrachtgever een eigen PVS gebruikt en wil aanhaken bij de
collectieve compartimenten.




## Page 29

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 28 van 102
4.4.7.2
Standaard Uitvraag


Figuur 8: Standaard Uitvraag

Bij deze variant sluit de ICT-Oplossing aan op het al aanwezige Zaaksysteem en DMS/RMA, dat doorgaans al
breed in de organisatie wordt ingezet – (veel) breder dan in het VTH-domein.
Deelnemer levert met de leverancier van het betreffende Zaaksysteem en/of DMS/RMA de koppeling(en)/
stekker(s) naar het PVS en de aansluitende Ketenintegratie en Objectregistratie.

Voor de te koppelen zaaksystemen en DMS-en zie de Annex E ‘Koppelingen aan bestaande systemen’




## Page 30

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 29 van 102
4.4.7.3
Maximale Uitvraag


Figuur 9: maximale uitvraag

In deze uitvraag levert de aanbieder naast de functionaliteit van de standaard uitvraag, ook het generieke
Zaaksysteem in combinatie met het DMS/RMA, als één integraal geheel of via een 3e partij. De aanbieder is
verantwoordelijk en het eerste aanspreekpunt voor de implementatie en de support van het geheel.
4.5
Standaarden
Deze paragraaf geeft de standaarden weer waar de oplossing aan dient te voldoen,
4.5.1
Algemeen
De ICT-Oplossing wordt door de aanbestedende dienst gebruikt in een complexe omgeving en binnen een
domein waarin het belang van ketensamenwerking steeds groter wordt. De aanbestedende dienst beoogt met
het aanbesteden van dezelfde ICT-Oplossing - en de daarbij behorende afspraken over harmonisatie - zoveel
mogelijk organisatorische, functionele en technische hindernissen op te ruimen.

Toch zal het gebruik van één ICT-Oplossing ter ondersteuning van de taken binnen het VTHA-domein door de
aanbestedende dienst  geen oplossing opleveren voor alle, in de huidige praktijk bestaande, problemen en
obstakels. In de eerste plaats niet, omdat niet alle partijen die deel uitmaken van de VTHA-keten, gebruik
zullen maken van de geselecteerde ICT-Oplossing. Landelijke inspecties (bijvoorbeeld GGD, IL&T, inspectie
SZW), Politie en Openbaar Ministerie zullen de ICT-Oplossing niet gebruiken.

De ICT-Oplossing moet daarnaast worden geïntegreerd met de informatievoorziening van de Opdrachtgevers,
bijvoorbeeld voor de ‘intake’ en de daarop volgende behandeling binnen de ICT-Oplossing van
vergunningaanvragen voor een APV-product, het synchroniseren van ‘zaakgegevens’ ten behoeve van de

## Page 31

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 30 van 102
ondersteuning van klantcontacten (veelal belegd in een Klantcontactcentrum) en het dossier- en archiefbeheer
waarvoor elke Opdrachtgever verantwoordelijk is.

Het is voor de informatie-uitwisseling met ketenpartners en de eigen informatievoorziening van de
Opdrachtgever cruciaal dat de ICT-Oplossing maximaal gebruik maakt van standaarden. De ICT-Oplossing
sluit daarom waar mogelijk aan op (vastgestelde en/of de facto) courante (inter)nationale standaarden en best
practices, waarbij vastgestelde standaarden uiteraard prevaleren boven de facto standaarden. De standaarden
die zijn benoemd / vastgesteld door het Forum Standaardisatie zijn hiervoor een goed richtsnoer.
Bovenstaande geldt zowel voor de inrichting (gebaseerd op de informatiemodellen voor o.a. ‘zaakgericht
werken’), informatie-uitwisseling (gebaseerd op uitwisselingsstandaarden), registratie en presentatie (denk
aan de standaarden voor basisregistraties, presentatie van geo-informatie), als niet functionele aspecten (denk
aan schaalbaarheid, betrouwbaarheid, beveiliging, et cetera).

Eis 6
De ICT-Oplossing volgt standaarden op de voet: binnen 6 maanden nadat een nieuwe (versie van een)
standaard door een op de Nederlandse markt verkrijgbaar softwareproduct wordt ondersteund, zal deze ook
worden ondersteund door de ICT-Oplossing. Daarnaast ondersteunt de Leverancier - voor zover nodig voor de
integratie met applicaties van de Opdrachtgevers - ook ten minste de twee daaraan voorafgaande versies van
die standaarden.
Aanbestedende dienst zal zich eveneens committeren aan de toepassing van standaarden, zowel in de
technische zin als in functionele / semantische zin (het ook in de eigen applicaties implementeren van de
gemeenschappelijke zaaktypecatalogus, toepassing van gezamenlijk vastgestelde metadataprofiel(en), et
cetera).

4.5.1.1
Verplichte standaarden
Naam
Versie
Omschrijving
Verplichte standaarden
DNSSEC
RFC 4033, RFC4034,
RFC4035
Domeinnaam-beveiliging
Geo-Standaarden
Zie 'Toelichting bij Opname'
op site Forum
Standaardisatie
Geografische informatie
HTTPS en HSTS
RFC2818, RFC6797
Veilig Webverkeer
IPv6 en IPv4
4 en 6
Internetnummers
ODF
1.2
Formaat documentbewerking
OpenAPI
Specification
3.0
Beschrijven van REST APIs
OWMS
4.0
Metadata overheidsinformatie
PDF 1.7
ISO 32000-1:2008
Formaat documentpublicatie
PDF A1
NEN-ISO 19005-1:2005
Formaat documentpublicatie en archivering
PDF A2
ISO 19005-2
Formaat documentpublicatie en archivering
SAML
2.0
Authenticatie
SIKB0101
13.5
Bodeminformatie
SIKB0102
3.3.0
Archeologische informatie
SKOS
SKOS W3C Recommendation
18 August 2009
Linked data en begrippenlijsten
STARTTLS en DANE
RFC 3207 en RFC 7672
Beveiligd mailverkeer
StUF
laatste
Uitwisseling administratieve
overheidsgegevens
TLS
1.2, 1.1 en 1.0
Veilige verbinding


## Page 32

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 31 van 102
4.5.1.2
Aanbevolen standaarden
Aanbevolen standaarden
CSS
2.1
Website-opmaak
CSV
RFC4180
Tabelbestanden
Datum en Tijd
NEN-ISO 8601:2005
Datum en tijd
DCAT
Recommendation 16-01-
2014
Beschrijven van datasets
ETSI TS 119 312
v1.1.1 (2014-11)
Digitale handtekening
HTML
5.2
Opmaak van webpagina's.
IP Sec
RFC 4301 met RFC4309 +
RFC 6040 en 7619
Beveiligde IP verbindingen
ISO 3166-1
ISO 3166-1:2013 Landcodes
Codes voor landnamen
JSON
RFC 7159, Juli 2006
Uitwisselen van datastructuren
OData
4.0
Bevraging van REST API’s
OWL
OWL 2
Beschrijvingstaal semantisch web
SCIM
RFC 7642, 7643 en 7644
Uitwisseling identiteitsinformatie
SHA-2
ISO/IEC 10118- 3:2016
Authenticatie en integriteitscontrole
SMTP
RFC 5321
Versturen van e-mail
SSH-2
RFC 4251: 2006
Versleuteld inloggen
SVG
1.1
Grafische afbeeldingen
TCP/IP
December 1975 /
September 1981
Netwerkcommunicatie
WSDL
2.0
Interface van Webservices
X509
RFC5280 en update
RFC6818
Authenticatie (PKI Certificaten)
XML
1.0 (fifth edition)
Opmaaktaal voor gestructureerde gegevens
XSD
XCD 1.1
Beschrijven van XML documenten
XSL
XSL family
Transformeren XML berichten

4.5.2
GEMMA Principes
In deze paragraaf is beschreven hoe aan de geldende afgeleide (GEMMA-)principes invulling wordt gegeven in
deze aanbesteding. Door het realiseren van deze afgeleide principes, worden de strategische doelen voor
burger, bedrijf en overheid gerealiseerd die staan beschreven in de basisprincipes van NORA. Afhankelijk van
de oplossing en de omgeving moet de oplossing ook voldoen aan de dochters van NORA6. In de bijlage wordt
in dat geval beschreven wat de impact van de principes uit de betreffende architecturen is op de oplossing, of
anders gezegd: hoe wordt omgegaan met de principes.
De principes zijn als tabel opgenomen in Annex 2.
4.5.3
Standaarden ‘Domeinen’
De uitvoering van de VTH-processen leidt tot het vastleggen en opslaan van informatie, die kunnen
onderverdelen in 3 logische domeinen:

1. Het zaakdomein: zaakinformatie ter ondersteuning van het procesgestuurd behandelen van een zaak,
conform de principes van zaakgericht werken.
2. Het locatiedomein: dit is gestructureerde informatie over wat er op een bepaalde locatie
daadwerkelijk is, wat er mag en wat er waargenomen wordt.
3. Het documentdomein: authentieke, niet-gestructureerde broninformatie, die enerzijds als bewijs kan
dienen voor de uitvoering van een werkproces, anderzijds aanvullende locatie informatie bevat.

6 Zie: https://www.noraonline.nl

## Page 33

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 32 van 102

De domeinen worden aan de hand van onderstaand schema7 nader toegelicht.

Figuur 10 Relaties zaak-, document- en locatiedomein

Het zaakmodel heeft relaties met de twee andere domeinen. Het Zaakobject is nl. een gegevensobject in het
locatiedomein en Document is een gegevensobject in het documentdomein.
Daarnaast kennen zowel het Zaakdomein als het Documentdomein standaarden, RGBZ resp. TMLO. Het
Locatiedomein kent geen standaard, dit is een zwak element binnen dit model.

Spec 68 De ICT-oplossing ondersteunt gedurende de looptijd van de overeenkomst het hier geschetste model,
inclusief de onderlinge relaties, of landelijke ontwikkelingen in dit model.
4.5.4
Architectuurstandaarden: GEMMA/NORA
De ICT-oplossing voldoet aan de in GEMMA standaarden, zoals opgenomen onder: ‘Gemeentelijke
Applicatiearchitectuur Omgevingswet, Requirements Vergunning-, Toezicht- en Handhavingcomponenten’.

Zie:
https://www.gemmaonline.nl/index.php/GAO_-_Vergunning-_Toezicht-_en_Handhavingcomponenten
4.5.5
Standaarden – aansluiting DSO – STAM/IMAM
Primair betreft het hier de aansluiting voor het ontvangen van verzoeken, via de koppelstandaard STAM en
het informatiemodel IMAM.
Deze zijn (status december 2019) als 1.0 versie beschikbaar via
https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/aansluiten/standaarden/stam-imam/
Zie ook 4.6.3.1 Koppeling DSO.
4.5.6
Technische standaarden – infra
Zie hiervoor Standaarden

7 Bron: Architectuurvisie Informatievoorziening Omgevingsdiensten ODNL v10
Documentregister
Metagegevens
Documentdomein
Zaakdomein
Locatiedomein
Zaak
Betrokkene
(Fysiek)
object
Activiteit
Zaakdossier
Document
Archief
RGBZ
Besluit
Zaakobject
TMLO
Document
• identificerend
• classificerend
• situerend in
ruimte en tijd
• verantwoordend
• voorschrijvend
• waarnemend
• besluitend
• beschrijvend
Gegevens:
Handelsregister (HR)
Personen (BRP)
Basisregistraties:
Handelsregister (HR)
Adressen en gebouwen (BAG)
Percelen (BRK)
Topografie (BRT)
Grootschalige topografie (BGT)
Ondergrond (BRO)
Voertuigen (BRV)
X
Status

## Page 34

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 33 van 102
4.5.7
Gegevensstandaarden
Gegevensstandaarden volgen uit het Domeinen-model zoals eerder beschreven. Waar nodig voor de
Omgevingswet volgen aanpassingen, deze waren nog niet compleet te overzien bij het opstellen van dit
document.

Aanvullend gelden de volgende specificaties t.a.v. gegevensstandaarden en gegevensinvoer in de ICT-
oplossing:

Spec 69 Te allen tijde is traceerbaar wat versie/actualiteit van achterliggende gegevens, datalijsten en bronnen zijn.
Denk aan SBI codes, RAV codes, tabellen activiteitenbesluit, gebruikersnamen, et cetera.

Spec 70 Bij stappen in het proces waar een gegevensbron wordt geraadpleegd, ingevoerd of gewijzigd, vindt altijd
verificatie plaats en is er de mogelijkheid een nul- of dummywaarde in te voeren of te kiezen, zodat gebruiker
altijd bewust/verplicht een keuze maakt en daarmee de invoer traceerbaar en rapporteerbaar is.
4.6
Koppelingen en Integratie
4.6.1
Algemeen
Integratie met landelijke voorzieningen (Koppelfunctionaliteit) en interne systemen.
De Opdrachtgevers weten uit ervaring dat koppelingen tussen (ICT-)systemen veelal complex en daardoor
kwetsbaar zijn. Daarom sturen zij sterk op het gebruik van landelijke en internationale (vastgestelde en de
facto) standaarden (Standaarden en Principes) voor de integratie tussen systemen en zijn de opdrachtgevers
ook bereid, zolang dat niet ten koste gaat van de functionaliteit die de ICT-Oplossing biedt, concessies te
doen die de complexiteit en kwetsbaarheid reduceren.
4.6.2
Koppelingen met interne systemen
Definitie: Koppelingen naar ‘eigen’ informatiesystemen.
Betreft koppelingen naar Zaaksysteem en DMS/RMA, naar BI-omgevingen, GEO platformen en overige interne
systemen, zoals financiële systemen met tijdschrijfcomponent et cetera.

Elk van de hieronder beschreven koppelingen en integraties moet met - de betreffende ICT-systemen van - de
Opdrachtgever kunnen worden gerealiseerd. Hiervoor geldt dat de ICT-Oplossing voor elke integratie een
gestandaardiseerd (zie Standaarden en Principes) koppelvlak zal aanbieden en dat elke Opdrachtgever er zelf
verantwoordelijk voor is de ‘contra-stekker’ vanuit de eigen, te integreren, ICT-systemen te realiseren en zo
zorg te dragen voor de feitelijke integratie met de eigen informatievoorziening. Zie hiervoor ook de eigen
verantwoordelijkheid van Opdrachtgevers op dit punt, zoals eerder ook beschreven.

Opmerking: Het kan per deelnemer verschillen of de koppeling naar een externe informatievoorziening
centraal via één centrale koppeling van de Cloud voorziening gaat, of een directe koppeling van de deelnemer
naar de informatievoorziening.
Voor een overzicht van koppelingen per deelnemer zie de Annex E ‘Koppelingen aan bestaande systemen’.

4.6.2.1
Koppeling met generiek Zaaksysteem en DMS/RMA
De ICT-oplossing moet koppelen met het reeds aanwezig zaaksysteem, op basis van de GEMMA standaarden:

Eis 7
Standaard services voor het ontsluiten en koppelen van Zaaksysteem (ZS) en Document Managementsysteem
(DMS) zijn gebaseerd op StUF en CMIS.

Zaak- en documentservices is een op StUF-ZKN en CMIS gebaseerde berichtenstandaard voor de uitwisseling
van zaakgegevens en zaakgerelateerde documenten tussen zaaksystemen en
documentmanagementsystemen ten behoeve van zaakgericht werken. Ook de interactie van het zaaksysteem
en het DMS met andere applicaties in het gemeentelijk applicatielandschap wordt met behulp van deze

## Page 35

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 34 van 102
services gestandaardiseerd. In de toekomst (uiterlijk per 2024) al de koppeling via API’s gaan verlopen (zie
Hoofdstuk ‘Doorontwikkeling’ en de GEMMA requirements).

Integratie met decentrale functionaliteit voor Document- en Dossierbeheer:

Spec 71 De ICT-Oplossing zal alle ongestructureerde informatie, zijnde de documenten in een zaakdossier van de ICT-
Oplossing, aanbieden aan de functionaliteit voor het beheer van documenten en dossiers (Document
Management Systeem, Records Management Systeem) van een Opdrachtgever o.b.v. de Zaak- en
Documentservices. Vice versa is het mogelijk om ongestructureerde informatie die voor de ICT-Oplossing
relevant is, maar die niet binnen de ICT-Oplossing is gecreëerd, beschikbaar te maken binnen de ICT-
Oplossing. Voor deze koppeling is het Toepassingskader Metadatering Lokale Overheid (TMLO) het
uitgangspunt.

Spec 72 De ICT-oplossing realiseert de aansluitingen op Zaaksystemen en/of DMS-RMA op de beschreven wijze, met
dien verstande dat de leverancier de stekker ‘levert’, en de derde partij de ‘contrastekker’

De te koppelen systemen zijn in onderstaande tabel opgenomen:
Minimaal te koppelen zaaksystemen
Minimaal te koppelen DMS-systemen
Exxellence 7.2 (Exxellence)
Djuma (Circle software)
Djuma (Circle software)
Corsa (BCT)
iZaaksuite (Pink Roccade)
Sharepint Online (Microsoft)
OneGov Dynamics 365 SaaS (Microsoft)
Version (Circle)
Verseon (Circle)
eSuite (Atos)
Liber (BCT)
JOIN (Decos)
eSuite (Atos)

JOIN (Decos)


4.6.2.2
Koppeling ESB en/of data distributie
Naast directe koppelingen zoals benoemd in de vorige paragraaf kunnen dergelijke informatieleveringen ook
via een derde partij of via een centrale voorziening als een Enterprise Service Bus (ESB) plaatsvinden.

Spec 73 De ICT-oplossing dient aan te sluiten op een aantal vooraf gespecificeerde ESB- of data-
distributievoorzieningen, met dien verstande dat de leverancier de stekker ‘levert’, en de derde partij de
‘contrastekker’

Minimaal te koppelen ESB Systemen
Minimaal te koppelen Datadistributie systemen
Exxellence datadistributie (Exxellence)
Makelaar MKS (PinkRoccade)
2Secure & U 2Orchestrate (Enable-U)
CiVision MKS (Pink Roccade)
Jnet (Jnet)
Neuron Stroomlijn (Vicrea)

Key2Datadistributie (Centric)

4.6.2.3
Integratie met decentrale functionaliteit voor Kantoorautomatisering
Spec 74 De ICT-Oplossing zal integreren met de decentrale functionaliteit voor kantoorautomatisering (Microsoft
Office-applicaties) en decentrale printvoorzieningen.

Voorbeelden: grid-exports naar Excel, gegenereerde documenten in Word-compatible format, et cetera.

4.6.2.4
Integratie met decentrale functionaliteit voor tijdverantwoording en/of planning
Spec 75 De ICT-Oplossing kan voor elke procesgang (zaak) de identificerende zaak- en/of productinformatie aan het
Tijdverantwoordings- en/of Planningssysteem van een Opdrachtgever leveren, zodat tijd kan worden
verantwoord ‘per zaak’ of in te zetten resources kunnen worden geprognotiseerd.

## Page 36

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 35 van 102
4.6.2.5
Integratie met decentrale functionaliteit voor In- en Excasso
Spec 76 De ICT-Oplossing zal de financiële transacties (ten minste: te incasseren leges, optioneel: te vorderen of te
betalen dwangsommen, te vorderen kosten, te betalen producten en diensten, et cetera) voor een
Opdrachtgever moeten kunnen genereren op een wijze die door het financiële systeem van de Opdrachtgever
geautomatiseerd kan worden verwerkt, bijvoorbeeld op basis van StUF-FIN.
4.6.3
Koppelingen met externe systemen
Definitie: Koppelingen met ‘niet eigen’ informatiesystemen, zoals landelijke of sectorale voorzieningen, niet
zijnde basisregistraties.
4.6.3.1
Integratie met landelijke Intake-voorzieningen Digitaal Stelsel Omgevingswet (DSO)
Spec (reeds benoemd): De ICT-Oplossing koppelt aan het DSO voor aanvragen en meldingen via STAM en voor
het bevragen van de stelselcatalogus (begrippen en definities). De STOP/TP alsmede de STTR standaard wordt
indirect (via de daarvoor geëigende applicaties) ondersteund en valt buiten de scope.
De ICT-Oplossing integreert met alle intake-functionaliteiten van het Digitaal stelsel Omgevingswet die voor
Opdrachtgevers - als hoofdbehandelaar (Bevoegd Gezag) of ketenpartner (bijv. adviseur) - van belang zijn.
Voor de aansluiting op de huidige intake-voorzieningen geldt dat de integratie met de ICT-Oplossing alle
functionaliteit van de voorziening dient te omvatten.

Eis 8
De aansluiting op DSO-LV voldoet aan de specificaties zoals gepubliceerd op
https://www.gemmaonline.nl/index.php/GAO_-_Koppelingen
4.6.3.2
Integratie met Informatiehuizen/Informatieproducten
Wens 16 De ICT-Oplossing zal alle binnen de ICT-Oplossing bijgehouden objectgegevens waarvoor een Opdrachtgever
formeel bronhouder is, als Informatieproduct leveren aan het Digitaal stelsel Omgevingswet. De ICT-
Oplossing zal alle gegevens die relevant zijn voor de uitoefening van de (wettelijke) taken van Opdrachtgevers
als Informatieproducten betrekken uit het Digitaal Stelsel Omgevingswet.
4.6.3.3
Koppeling publicaties (DROP/KOOP en LVBB)
Spec 77 De ICT-Oplossing integreert met de huidige en toekomstige landelijke publicatievoorzieningen, zoals
Decentrale Regelgeving en Officiële Publicaties en toekomstige voorzieningen binnen het Digitaal Stelsel
Omgevingswet voor het kenbaar maken van individuele (bijv. zaakspecifieke) of collectieve informatie, zoals
plannen, verordeningen, besluiten.

Wens 17 In gevallen waarin een Opdrachtgever deze integratie met eigen functionaliteit, bijvoorbeeld met het eigen
zaaksysteem, wenst te realiseren, ondersteunt de ICT-Oplossing deze integratie maximaal. Bijvoorbeeld door
de inhoudelijke informatie die moet worden gepubliceerd, te genereren binnen de ICT-Oplossing en deze aan
de component die de feitelijke publicatie verzorgt, beschikbaar te stellen.

4.6.3.4
Informatie-uitwisseling ten behoeve van Inspectieview (Milieu, IvM)
Inspectieview Milieu (IvM) is een landelijke voorziening die het mogelijk maakt de inspectieresultaten van
toezichthoudende overheidsorganisaties te delen met andere toezichthoudende overheidsorganisaties.
Dankzij IvM ‘weet’ de inspecteur van de ‘Inspectie Leefomgeving en Transport’ wat de inspectieresultaten
waren van de toezichthouder van een omgevingsdienst die enkele weken geleden een inspectie
uitvoerde, en vice versa.  Inspectieview Milieu is een voorziening waarop omgevingsdiensten zich verplicht
dienen aan te sluiten. Omgevingsdiensten zullen de resultaten van het toezicht dat zij houden op milieu-
inrichtingen via IvM moeten delen met andere toezichthouders.

Spec 78 De ICT-Oplossing draagt er zorg voor dat alle voor IvM benodigde gegevens binnen de ICT-Oplossing kunnen
worden bijgehouden en geautomatiseerd worden geëxporteerd naar het stelsel van Inspectieviews.
4.6.3.5
Koppeling Bodeminformatiesysteem (BIS)
Spec 79 De ICT-Oplossing – specifiek het PVS – is gekoppeld aan het BIS dat bij de ODZOB en een groeiend aantal
gemeenten in gebruik is c.q. wordt genomen, dit betreft (de meest recente versie van) Squit iBis van Roxit.

## Page 37

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 36 van 102
4.6.3.6
Koppeling overige
Naast de al genoemde koppelingen naar basisregistraties en informatiehuizen, bestaan nog veel andere
‘informatiebronnen’. De denken valt aan Bbk database en e-formulieren (bijvoorbeeld zwemwater). Maar ook
Sensoren/meetnetwerken, registratiesystemen van RVO, LMA, registers van installaties, et cetera.
Wens 18 Koppelingen, al dan niet geautomatiseerd, naar overige informatiebronnen. Hetzij om gegevens in te zien,
hetzij om gegevens over te halen naar de ICT-oplossing. Voorkeur is dat de gegevens bij de bronnen blijven.
4.6.4
Koppelingen met Basisregistraties
Spec 80 De ICT-Oplossing integreert met minimaal de volgende basisregistraties: NHR, BAG, BGT, BRO en BRP

Nadere toelichting in de volgende paragrafen:
4.6.4.1
Integratie met Handelsregister (NHR)
De ICT-Oplossing betrekt gegevens van niet-natuurlijke personen uit het Handelsregister door integratie van
de ICT-Oplossing met het Handelsregister. Deze integratie is zodanig uitgevoerd dat wijzigingen in
bedrijfsgegevens (nieuwe bedrijven, wijzigingen in bestaande bedrijven en bedrijfsbeëindiging) automatisch
binnen de ICT-Oplossing beschikbaar komen.
4.6.4.2
Integratie met Basisregistratie Adressen en Gebouwen (BAG)
De ICT-Oplossing zal gegevens van Adressen en Gebouwen betrekken uit de Basisregistraties Adressen en
Gebouwen en deze te allen tijde actueel houden voor gebruik binnen de ICT-Oplossing.
4.6.4.3
Integratie met Basisregistratie Grootschalige Topografie (BGT)
De ICT-Oplossing zal de objectgegevens uit de Basisregistratie Grootschalige Topografie betrekken en deze te
allen tijde actueel houden voor gebruik binnen de ICT-Oplossing.
4.6.4.4
Integratie met Basisregistratie Ondergrond (BRO)
De ICT-Oplossing zal de gegevens over de ondergrond uit de Basisregistratie Ondergrond betrekken en deze
te allen tijde actueel houden voor gebruik binnen de ICT-Oplossing.
4.6.4.5
Integratie met basisregistratie personen (BRP)
De ICT-Oplossing zal gegevens van natuurlijke personen betrekken uit de individuele decentrale registraties
(lokale BRP) van het Bevoegd Gezag / de Bevoegde Gezagen waarvoor binnen de ICT-Oplossing taken worden
uitgevoerd.

4.7
Generieke functionaliteit en overige specificaties
4.7.1
Integratie beleidsvelden (RO)
Koppeling om samenwerking te bevorderen tussen alle beleidsterreinen die samenkomen in de
omgevingsvisie en omgevingsplannen van gemeenten/provincie en vice versa. (BP, APV,
Geurgebiedsvisie/verordening veehouderij, geluidsbeleid, afvalbeleid, beleid luchtkwaliteit, kader
volksgezondheid en veehouderij, welstand et cetera). In hoofdstuk 5 ‘Doorontwikkeling’ is dit inhoudelijk
nader uiteengezet.
De software rondom dit beleid (Plansoftware en Toepasbare Regels) valt buiten de scope van deze
aanbesteding.
Wens 19 Koppelingen tussen Plan-/Toepasbare Regels-software en de ICT-oplossing.
4.7.2
Rapportages: Datawarehouse / BI
Eindgebruikers van de ICT-oplossing kunnen zelf (eenvoudige/operationele) rapportages en overzichten
genereren, dit is elders al gespecificeerd.
De ICT-Oplossing dient ook gegevens te leveren op meer (geaggregeerd) organisatieniveau en voor
management, denk hierbij aan aantal openstaande/afgeronde verzoeken, lopende/afgeronde controles,
inhoudelijke overzichten uit de Objectregistratie, legestotalen, werkvoorraad, et cetera.

## Page 38

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 37 van 102

Eis 9
De ICT-Oplossing kan bij aanvang (bulk)data aanleveren ten behoeve van (lokale) datawarehouses/BI tools of
gegevens sets. Hierbij is niet alleen de data zelf van belang maar ook inzicht in het datamodel: De geleverde
gegevens zijn duidelijk en inzichtelijk, bijv. door duidelijk beschreven kolommen in tabellen en database-
diagrammen/-views, en door bijgeleverde documentatie. De (bulk)data is niet limitatief en bevat alle velden
en variabelen die door de organisaties ingevoerd zijn/in te voeren zijn. De data wordt minimaal dagelijks
aangeleverd, bijv. via nachtelijke batchjobs.
4.7.3
Cloud
Spec 81 De oplossing is een Cloud applicatie, door of onder beheer van de leverancier gehost en met een absoluut
minimum aan onderdelen  on-premise bij de afnemers, in ieder geval geen componenten on-premise die een
directe interface met de standaard gebruikers bieden.
4.7.4
Backup en Recovery
Spec 82 De leverancier zorgt voor een backup- en restore mogelijkheid binnen de ICT-Oplossing, die minimaal voldoet
aan de hier opgenomen uitgangspunten – vast te stellen in de na gunning op te leveren SLA.
▪
Maximale ‘leeftijd’ (hoe oud mag de data zijn): x uur (RPO);
▪
Maximale restoretijd (tijd tussen verzoek en beschikbaarheid data: x dagen (RTO);
▪
Volledige restore van de omgeving moet mogelijk zijn;
▪
Individuele bestanden moeten hersteld kunnen worden.

Spec 83 De backup/restore voorziening voldoet aan de Baseline Informatiebeveiliging Overheid (BIO) “of
gelijkwaardig”.
4.7.5
Authenticatie en Rollen
Spec 84 Authenticatie aan de applicatie(s) is geïntegreerd met de lokale authenticatievoorziening van de afnemers.
Indien deze is gebaseerd op Microsoft Active Directory, op basis van ADFS versie 3.0 of hoger of Azure Active
Directory. Voor specifieke situaties waar ADFS geen optimale situatie oplevert is een alternatieve
authenticatiemethode voorhanden.

Toelichting: Indien afnemer (nog) geen mogelijkheid heeft tot ADFS of Azure Active Directory volstaat een
lokale/ingebouwde vorm van gebruikersbeheer binnen het Cloud-platform. Bij migratie van de lokale
authenticatie naar ADFS of Azure Active Directory blijven gebruikersprofielen en persoonlijke instellingen
behouden.
Voorbeelden van specifieke situaties waar ADFS niet optimaal is en een alternatieve authenticatiemethode
(bijvoorbeeld lokale gebruikersaccounts) beter passen:
Beheeraccounts;
Gebruikers binnen de keten, maar van organisaties die zelf geen afnemer van de ICT-oplossing zijn.
Denk aan medewerkers van belastingsamenwerkingen (informatie inwinnen voor WOZ), andere
Omgevingsdiensten, Provincie, et cetera;
(Incidentele) Gebruikers van buiten de keten (bijv. adviesbureaus);

Spec 85 Er zijn rollen beschikbaar in de ICT-Oplossing die de juiste rechten verlenen aan alle gebruikers en
beheerders van het systeem.

Toelichting: Iedere betrokkene moet geautoriseerd documenten uit een dossier kunnen raadplegen, wijzigen,
aanbieden en verwijderen. Er wordt geen onderscheid gemaakt tussen interne en externe adviseurs. Allen
krijgen alleen die informatie en documenten te zien die zij nodig hebben voor de hun rol. Indien nodig
hebben zij wel toegang tot de andere documenten van de zaak. Ook registreren zij allen hun advies in het
systeem, voortgang dient zowel bij intern- als bij extern advies te monitoren te zijn.
4.7.6
Gebruikersvriendelijkheid
Spec 86 De ICT-Oplossing kan door elke medewerker op onderdelen naar eigen behoefte ingedeeld worden.
Medewerkers kunnen zelf de opbouw van schermen beïnvloeden, zoals de te tonen velden en de indeling en
breedte van kolommen. Deze instellingen worden ook opgeslagen. Medewerkers kunnen knoppen wel of niet
tonen.


## Page 39

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 38 van 102
Wens 20 De ICT-oplossing maakt de gebruikers opmerkzaam op de verplicht te registreren gegevens, bijvoorbeeld
door het hanteren van een andere kleur voor verplichte velden

Spec 87 De ICT-oplossing ondersteunt het gebruik van twee beeldschermen (functie “uitbreiden” in Windows). Hierbij
maakt de applicatie logisch gebruik van browsertabbladen, groepering van tabbladen en van een minimum
aan pop-up browserschermen.
4.7.7
Webbrowser en Web-standaarden
Er geldt een sterke afhankelijkheid van webtechnologie, webstandaarden, et cetera.

Spec 88 Ondersteuning dient er te zijn voor gangbare browsers. Ten tijde van de gunning zijn dat Mozilla Firefox,
Google Chrome en Microsoft Edge (Chromium based). Leverancier is verantwoordelijk voor continue
ondersteuning van de oplossing onder de laatste drie (3) hoofdversies van de browsers. De afnemers zijn
verantwoordelijk voor het aan de eindgebruikers ter beschikking stellen van deze versies.

Spec 89 De webapplicaties werken conform de laatste courante HTML standaarden (HTML5 of hoger) en kennen geen
afhankelijkheden van 3rd party of eigen plug-ins (Java, Adobe Flash, Silverlight, et cetera), tenzij dit
toegevoegde waarde biedt voor de integratie met lokale (kantoorautomatisering-)applicaties, bijvoorbeeld
Office plug-ins ten behoeve van Outlook-integratie. Zie ook standaarden.
4.7.8
GEO/GIS
Spec 90 Informatie met een Geo-component moet (ook) op een kaart binnen ICT-oplossing en eventueel aanvullende
mobiele toepassing (bijvoorbeeld app) getoond worden.
Denk hierbij aan het tonen van de historie, van verleende vergunningen, toezicht en handhavingszaken, op
BAG objecten (verblijfsobject, pand, stand- en ligplaats).

Spec 91 Kaartlagen binnen de ICT-oplossing zijn te ontsluiten in andere Geo/GIS-toepassingen. Omgekeerd zijn eigen
Geo/GIS-kaartlagen in de ICT-oplossing te tonen, gebruik makende van in de GEO wereld geldende
standaarden (zoals WMS/WFS standaard).
4.7.9
Autonoom gebruik
Spec 92 Het systeem dient ook autonoom te kunnen functioneren. Concreet, bij (incidentele) uitval van een koppeling
naar een Zaaksysteem en/of DMS, dient de voortgang van de verwerking niet in gevaar te komen.
4.7.10
Mobiel gebruik
De oplossing is aangepast op mobiel gebruik alleen voor specifieke toepassingen of onderdelen die
ondersteuning bieden aan activiteiten of processen die buiten/op locatie worden uitgevoerd, mobiel toezicht
is hier de enige hier opgenomen toepassing momenteel. Functioneel is deze functie al eerder gespecificeerd,
hierna volgen nog de aanvullende non-functionele specificaties:

Spec 93 De ICT-Oplossing heeft de hierna opgenomen non-functionele specificaties bij mobiel gebruik (mobiel
toezicht)
Lay-out en bediening zijn aangepast op touchscreens;
Offline gebruik: een controle waarvan de gegevens al gedownload zijn is offline (zonder WiFi/4G
verbinding) te starten/te continueren en af te ronden;
Indien als App uitgevoerd: Ondersteuning voor Apple iOS en Microsoft Windows 10 pro/enterprise.
Optioneel voor Android;
Indien geen App: voor mobiel gebruik geoptimaliseerd browserscherm (responsive design).



## Page 40

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 39 van 102
5 Doorontwikkeling
5.1
Doorontwikkeling applicaties
Na 1 januari 2021 zal de software voor VTH zich verder ontwikkelen. Aanbestedende dienst wil dat de
software voldoet aan het gedachtengoed van Common Ground en dat de gehele beleidscyclus (van visie, naar
plan, vergunning verlening, toezicht, handhaving en evaluatie) wordt ondersteund met integrale software.
Komende periode zal deze doorontwikkeling verder in beeld worden gebracht, ondermeer via de
Gemeentelijke Applicatiearchitectuur Omgevingswet op:
https://www.gemmaonline.nl/index.php/GAO_-_Vergunning-_Toezicht-_en_Handhavingcomponenten

Een aantal van deze ontwikkelingen heeft nu al specifieke aandacht en is hier nader toegelicht.
5.2
Koppelingen zaakgericht werken (API’s)
Op dit moment zijn de koppelingen met zaaksystemen op basis van berichtenverkeer. In de toekomst gaat dit
over op API’s.
De API’s voor Zaakgericht werken zijn een uitwerking van de visie rond Common Ground:
Zie : https://www.vngrealisatie.nl/producten/api-standaarden-zaakgericht-werken



Wens 21 De ICT-oplossing sorteert voor op deze toekomstige API ontwikkeling. Deze is ingericht uiterlijk in januari
2024.
5.3
Publicaties
Onder de omgevingswet dienen ook beschikkingen en bijlagen gepubliceerd te worden via ander medium dan
KOOP).

## Page 41

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 40 van 102
Wens 22 De ICT-oplossing biedt mogelijkheden om, naast bekendmakingen e.d. op mijnoverheid.nl, ook
beschikkingen en bijlagen extern digitaal te raadplegen.
5.4
Ondersteuning Beleidscyclus
5.4.1
Monitoring
Beleidsvorming voor de uitvoering van VTH taken vindt momenteel plaats volgens de beleidscyclus, die
gebaseerd is op de BIG-8 systematiek. Zie onderstaande afbeelding.

Figuur 11 Big-8 Monitoring in de Operationele Cyclus

De BIG-8 systematiek maakt onderscheid tussen een jaarlijkse (onderste cirkel) en een meerjaarlijkse cyclus
(bovenste cirkel). De meerjaarlijkse cyclus bevat de langeretermijndoelen en is meer beleidsmatig en
strategisch van aard. De jaarlijkse (operationele) cyclus is een uitvoeringscyclus van planning, uitvoering en
verslaglegging waarbinnen sneller geschakeld en aangepast kan worden. Onderdeel van deze
uitvoeringscyclus is het jaarlijkse uitvoeringsplan (jaarplan) en jaarverslag. Door over een langere termijn
jaarlijks op eenzelfde wijze te plannen en verslag te leggen is het makkelijker om ontwikkelingen te zien en
te evalueren. Daardoor kan beter worden bepaald of bepaalde ontwikkelingen moeten leiden tot aanpassing
van de lange termijn doelen en strategieën.

Een belangrijke stap in deze cyclus is daarom de monitoring. De organisatie monitort met behulp van de ICT-
oplossing resultaten en de voortgang van de uitvoering van het beleid en het uitvoeringsprogramma. De
monitoringsresultaten worden weergegeven in het jaarverslag en gebruikt voor
bijsturing van de operationele cyclus en voor input op de beleidsevaluatie.

De ICT-oplossing draagt bij aan de monitoring in het kader van de BIG-8 cyclus, in elk geval voor de
uitvoering van VTH taken. Daarbij valt te denken   aan:
•
Aantallen producten
o
Per locatie/deelgebied
o
Status producten
o
Zaaktypen ten behoeve van die producten
o
Activiteiten producten
o
Doorlooptijden procedures en daadwerkelijk gehanteerde termijnen
•
Controlebezoeken
o
Per locatie/deelgebied

## Page 42

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 41 van 102
o
Per activiteit
o
Naleefpercentages
o
LHS-categorieën
•
Opgelegde bestuurlijke sancties
•
Processen-verbaal
•
Over mogelijke overtredingen ontvangen klachten
o
Per locatie/deelgebied
o
Aard klachten
o
Vervolgacties
o
Gegrond/ongegrond
•
Actuele werkvoorraad

Deze monitoring kan op elk gewenst moment uitgevoerd worden, door zowel het bevoegd gezag als een
uitvoeringsorganisatie. Daarnaast kan deze monitoring eenvoudig vergeleken worden met resultaten uit
voorgaande perioden/jaren.

Uit de monitoring kunnen (veranderde) risico’s opgemaakt worden. Denk aan probleemlocaties rondom
klachten of sectoren met activiteiten waar vaker overtredingen geconstateerd worden. Dit soort gegevens uit
de monitoring levert daardoor een bijdrage voor de evaluatierapportages (jaarverslagen) en kan waar nodig
leiden tot bijsturing van het (uitvoerings)beleid.

Wens 23 De ICT-Oplossing ondersteunt op termijn (uiterlijk januari 2024)  de monitoringsfunctie in de Big-8
systematiek.
5.4.2
Integratie met Beleidsontwikkeling
Naast de hierboven beschreven monitoring vanuit de operationele cyclus kent de Big-8 ook een zgn.
Strategische cyclus, in onderstaand schema nader aangeduid:

Figuur 12 Big-8 Strategische Cyclus

Wens 24  Uw ICT-oplossing levert binnen een termijn van uiterlijk 24 maanden een bijdrage aan de ontwikkeling van
lokaal en regionaal omgevingsbeleid, kijkend naar de doorontwikkeling van de Omgevingswet in combinatie
met de mogelijkheden en roadmap van uw productielijn.
Het gaat dan niet louter om VHT-(uitvoerings)beleid, maar ook over de vorming van de omgevingsvisie en het
omgevingsplan. Hierbij kan gedacht worden aan bijvoorbeeld ruimtelijke ordening, gezondheid en/of andere

## Page 43

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 42 van 102
thema’s die een relatie hebben met de fysieke leefomgeving waar een bestuur beleid over wil ontwikkelen,
dan wel veranderen of bijsturen.
5.5
Common Ground
De ICT-systemen dreigen vast te lopen als gevolg van de snel wassende stroom aan digitale gegevens. De
ontsluiting van deze gegevens loopt via een complex systeem van koppelingen. Het maakt het huidige ICT-
systeem weinig flexibel, kwetsbaar en duur. En het staat daarmee een optimale dienstverlening aan burgers
en ondernemers in de weg. Dit besef zette een beweging in gang voor de stapsgewijze ontwikkeling van een
nieuwe, toekomstbestendige gemeentelijke ICT-infrastructuur. De door de Taskforce Samen Organiseren
enthousiast omarmde beweging kreeg de toepasselijke naam Common Ground.

Het grote voordeel van dit model, dat is geïnspireerd op de Estlandse X-road, is dat het niet alleen goedkoper
is, maar ook meer ruimte biedt om sneller en gemakkelijker te innoveren. Common Ground maakt tevens
gemeenten minder afhankelijk van hun vaste leveranciers en geeft burgers en ondernemers meer en beter
inzicht in de wijze waarop met hun gegevens wordt omgegaan.

Met Common Ground wordt een grote stap gezet in de richting van een open, transparante overheid
waarbinnen met inachtneming van de privacy-regels gegevens sneller en veiliger kunnen worden
uitgewisseld, intern zowel als extern.
Nieuw is ook de wijze waarop Common Ground wordt vormgegeven. Het is geen van bovenaf opgelegde
systeemwijziging, maar een beweging die samen met gemeenten werkt aan een stapsgewijze modernisering
van de ICT-infrastructuur. En elke gemeente de kans biedt om in eigen tempo en op eigen voorwaarden de
overstap te maken.

Wens 25 U garandeert binnen een termijn van uiterlijk 24 maanden toe te groeien naar het Common Ground model. U
kunt op verzoek een concreet plan overhandigen hoe u van de huidige situatie naar het Common Ground
model toewerkt, inclusief groeipad en planning.
5.6
Zoekfunctionaliteit
Integraal zoeken is een ontwikkeling die jaren geleden is ingezet en nog steeds enorme groei doormaakt.
Naarmate meer data beschikbaar komt, groeit ook de behoefte, en noodzaak, om steeds ‘breder’ te kunnen
zoeken. ‘Breder’ in deze zin wordt bedoeld: meer en meer bronnen en meer en meer zoekingangen.
Ook binnen de VTH-keten wordt deze behoefte steeds groter. Denk aan informatie gestuurde handhaving
(IGH), waarbij het zaak is om niet enkel informatie uit dossiers ter beschikking te hebben, maar juist de
informatie in relatie tot deze dossiers inzichtelijk en doorzoekbaar te hebben. De ideaalsituatie is dat de data
benaderbaar is, onafhankelijk van de vak-applicatie(s), en dat deze doorzoekbaar is d.m.v. ‘search engines’.
Dit is een toekomstscenario waar de ICT-oplossing wel stapsgewijs naar kan groeien.
De eerste stap is de zaak-gerelateerde data in de ICT-oplossing beter doorzoekbaar te maken. Zowel dossiers,
metadata, zaakdata en PDF’s. Deze data is goed doorzoekbaar door middel van de applicatie zelf, en/of een
externe search engine. Onwenselijk is dat deze data eerst geëxporteerd moet worden om vervolgens met,
bijvoorbeeld BI-Tooling te analyseren. Een volgende stap is om aanpalende data in de Objectregistratie, op
dezelfde manier doorzoekbaar is.

Wens 26 U levert onderstaande toegevoegde waarde op het vlak van geavanceerde zoekmogelijkheden en de functies
die u hierin ziet binnen de ICT-oplossing.

•
Data wordt op korte en lange termijn beter doorzoekbaar. Denkt u aan een applicatie gebonden
search engine, of ontwikkelingen meer in de vorm van (de verbinding met) een externe search engine
(bijvoorbeeld SOLR, Elastic Search);
•
Er is een standaard set met zoekvragen (incl. parameters/filters voor gebruikers) gekoppeld aan
persona’s beschikbaar;

## Page 44

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 43 van 102
•
Er is vrijheid/reikwijdte om standaard zoekvragen zelf aan te kunnen passen (zonder tussenkomst
van de leverancier)?
•
Er is mogelijkheid om ongestructureerde data (bijv. in PDF’s)  om te zetten naar gestructureerde data,
en deze bijvoorbeeld zichtbaar te maken in de Object Registratie.

## Page 45

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 44 van 102
Annex A  Persona’s en Processen

1. Inleiding
Onder de GEMMA landelijke bedrijfsarchitectuur omgevingswet is een beschrijving gemaakt van actoren en
rollen enerzijds en producten en diensten anderzijds en de verbinding naar de (bedrijfsprocessen), zie
https://www.gemmaonline.nl/index.php/Bedrijfsarchitectuur_omgevingswet.
De bijlage geeft vanuit de deelnemers een nadere verdieping en waar mogelijk verbinding met de specifieke
invulling in GEMMA.

Persona’s

Figuur 13: GEMMA standaard weergave ‘Actoren en Rollen’:

https://www.gemmaonline.nl/index.php/Omgevingswet/1.5/id-637b2d4a-4891-4be2-8388-da31ee7b284a)

Om een goed beeld te schetsen van de behoefte aan informatievoorziening voorziet Sectie 2 van deze bijlage,
in een aantal typische gebruikersprofielen (persona’s) van de deelnemende organisaties, met een focus rond
het kernproces van VTH (vergunningverlening, toezicht en handhaving) en A (advisering). Naast deze
profielen is tevens in Sectie 2 de informatieverwerking rond het kernproces weergegeven, specifiek voor de
situatie van uitwisseling in de keten.

Een aantal persona’s worden in Sectie 2 verder uitgewerkt. Het doel van deze uitwerking is:
•
Inzichtelijk maken van verschillende rollen en functies
•
Duidelijk maken dat deze rollen bij elke deelnemer op een andere manier ingevuld kunnen zijn
•
Verschillende rollen ‘overlap’ hebben en ‘in elkaar’ over kunnen lopen
•
Er naast het VTHA systeem ook geregeld andere systemen gebruikt worden, ter ondersteuning,
raadpleging of het vastleggen van (extra) informatie.



## Page 46

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 45 van 102
2. Processen
Generieke bedrijfsprocessen onder de omgevingswet zijn in de Gemma als volgt belegd:

Figuur 14: Generieke bedrijfsprocessen GEMMA

Toelichting bij deze afbeelding:
URL: https://www.gemmaonline.nl/index.php/Bedrijfsprocessen_omgevingswet ;
De onderlinge genummerde verbindingen tussen de processen geven onderlinge relaties weer, ook
op de opgenomen URL te raadplegen;
Zowel de Procesclusters als de Bedrijfsprocessen zijn aan te klikken voor nadere toelichting, waarbij
een aantal processen zeer uitvoerig is toegelicht (bijv. Behandelen vergunningsaanvraag).
Zoals eerder al beschreven kunnen deze standaard processen over de organisaties heen anders ingevuld
worden, door processtappen op verschillende wijzen aan te roepen en over verschillende personen binnen en
zeker ook over organisaties heen (ketensamenwerking) te beleggen.
Voorbeelden hierbij:
Verschillen in uitvoering tussen de diverse wettelijke domeinen (industrieel – agrarisch, etc.)
Verschillen in mandaatstelling en/of taakoverdracht van BG naar uitvoeringsorganisaties, dit kent de
volgende varianten:
o
geen mandaat, met alleen advisering;
o
wel mandaat, maar geen ondertekening
o
volledig mandaat incl. ondertekening
o
volledige taakoverdracht (alleen Veiligheidsregio)
Samensmelting van met name T&H: scheidslijn kan bijv. bij lichte overtredingen niet aanwezig zijn
Uitvoering van processen indien meerdere Bevoegde Gezagen betrokken zijn
Het uitvoeren van processen over verschillende ketenpartners heen vereist ook soepele en eenduidige
informatie-uitwisseling tussen de organisaties, eveneens in de verschillende varianten zoals hier geschetst.
Deze informatie-uitwisseling (overzicht informatiestromen) is geadresseerd in dit Ontwerpdocument.
Kanttekening bij de geschetste GEMMA processen: deze zijn geschetst vanuit een ‘koninklijke route’, d.w.z.
de hoofdprocessen bij VTH starten vanuit een melding of vergunningsaanvraag (V) of vanuit het indienen van
een incidentmelding of handhavingsverzoek. In de praktijk wijkt dit soms af:
Een zaak kan starten vanuit een object. Dit betekent dat de procesgang geen éénrichtingsverkeer is
en (deels) ook andersom lopen. Denk ook aan verschillen zaakgericht vs objectgericht werken.
Praktijk: ervaring van de toezichthouders die o.b.v. een aangetroffen en/of onbekend object een

## Page 47

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 46 van 102
controle starten. Dit kan een compleet nieuw bedrijf zijn, maar meestal een activiteit of voorziening
binnen een bedrijf dat we nog niet kenden.
Aan objecten kan informatie toegevoegd worden die niet direct aanleiding voor een zaakgerichte
afhandeling hoeft te zijn. Als deze informatie echter direct een object wordt toegevoegd (= niet
zaakgericht), is er geen historie te achterhalen en zal deze informatie doorgaans ook niet
gearchiveerd en op termijn vernietigd worden. Dit is veelal informatie vanuit externe systemen en
registers, denk aan monitoringscijfers of gegevens van installaties.
Ketensamenwerking & Processen
In veel gevallen speelt het proces zich niet af binnen één organisatie en is er sprake van ketensamenwerking,
veelal van bevoegd gezag naar uitvoeringsorganisatie en weer terug naar het bevoegd gezag. Generiek is dit
bij GEMMA als volgt weergegeven8:


Figuur 15 Proces Ketensamenwerking

Naast de juiste ondersteuning van de (interne) processen zijn de ‘kruispunten’ of ‘overdrachtsmomenten’ in
de processen van groot belang, de ervaring leert dat hier diverse aandachtspunten zijn:
Overdracht van informatie (aanvraag, documenten, adviezen, etc.)
Procesvoortgang
Diversiteit in (proces-)afspraken
Mede om deze reden is in dit Ontwerpdocument al aangegeven dat een Ketenintegratievoorziening een
prominente rol in de oplossing heeft.











8 Zie ook: https://www.gemmaonline.nl/index.php/Omgevingswet/1.5/id-be067db5-0b5c-403a-81be-531b4b5bee0c

## Page 48

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 47 van 102
3. Uitwerking Persona’s
Indeling
In deze bijlage worden persona’s benoemd en in een categorie 1 of 2 ondergebracht. Tevens worden enkele
van deze persona’s concreet uitgewerkt.

Categorieën van persona’s
Cat 1 = (in)directe gebruikers van het systeem, binnen de organisaties/keten
Cat 2 = indirect gebruikers van het systeem, buiten de organisaties/keten

Profiel
categorie
Persona omschrijving
Voorbeelden
1
Kerngebruikers systeem / direct: VTHA, procesondersteuning.
Zowel binnen één organisatie als over organisaties heen
(meervoudige aanvragen, deeladviezen).

•
Vergunningverlener
(casemanager + toetser, …)
•
Toezichthouder
•
Handhaver
•
Jurist (losse rol of integreren als
processtap)
•
(Technisch) Adviseur
•
Proceduremedewerker,
procesondersteuning, KCC
•
RO-medewerkers
1
Kerngebruikers systeem / indirect
•
Casemanager/Werkverdeler
(intern)
•
Regisseur (vanuit BG naar
uitvoeringsorganisaties)
•
Opdrachtgever
1
Management en bestuur
•
Managers
•
Bestuurders
2
Aanvragers/eigenaar/drijver
•
Burger
•
Bedrijf
•
Gemachtigde namens aanvrager
/adviesbureaus
2
Adviseurs extern
•
Adviesbureaus
•
Samenwerkingspartners, w.o.:
•

Waterschappen
•

GGD
•

VR
•

Politie
•

OM
•

RIEC
•
Monumentencommissie
(gemeentelijk en rijksniveau)
2
Belanghebbenden
•
Omwonenden
•
Belangenverenigingen
(milieuvereniging, heemkunde,
dorpsraden etc)..

n.v.t.
Functioneel/technisch beheer, informatiebeheer: apart te
benoemen onder ‘Beheer’, geen specifieke persona’s

n.v.t.






## Page 49

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 48 van 102
Persona
Vergunningverlener milieu/Medewerker vergunningen milieu
Gemma
Verantwoordelijk voor besluiten op vergunningaanvragen en het waar nodig of gewenst
inschakelen van ketenpartners voor advies (al dan niet met instemming) en samenwerking.
En behandeling van de meldingen.
Behandelaar van aanvragen omgevingsvergunningen Wabo. Behandelen met zowel een
inhoudelijke component als een zaakmanagers rol.
Persona-omschrijving

Behandelt aanvragen en meldingen van bedrijven, instellingen of (soms) burgers, die in hun
bedrijfsvoering of op hun locatie activiteiten willen gaan uitvoeren met een potentieel
milieubelastende component, of wijzigingen hebben binnen deze activiteiten. De
milieubelastende component kan de activiteit zelf zijn, maar ook benodigde installaties,
voorzieningen, te verwerken stoffen, etc. Voorbeelden zijn lozen van afvalwater, geluid- of
geurproductie of opslag en gebruik van gevaarlijke stoffen. Daarnaast toetsing van
leefkwaliteit voor toekomstige bewoners van een nieuwe ontwikkeling.
Behandelt ook verzoeken om ‘hogere waarde’ en toetst aan geluidszones en Milieu effect
rapportages
Taak van de vergunningverlener is toetsen of beoordelen of de aanvraag voldoet aan  wet-
en regelgeving. Bij het besluit worden tevens het van toepassing zijnde beleid/ verordening
in de beoordeling betrokken. Daarbij verbindt de vergunningverlener voorschriften aan het
uitvoeren van een activiteiten dan wel drijven van een inrichting om bescherming van milieu
te waarborgen.  Beoordeling vindt plaats al dan niet met aanpassingen in de aanvraag.
Wanneer de aanvraag niet voldoet wordt deze  geweigerd. Ook kan in de uitvoering de
aanvraag buiten behandeling worden gelaten of afgebroken wanneer de aanvraag wordt
ingetrokken.
Bij beoordeling van de melding wordt getoetst aan de compleetheid van de melding (het
voldoen aan indieningsvereisten) en het voldoen aan de gestandaardiseerde voorschriften
uit het geldende Besluit. (AMvB)

Proces op hoofdlijnen,
Informatieverwerking
Een aanvraag wordt altijd gericht aan het ‘bevoegd gezag’, in dit geval één van de
gemeenten of de Provincie. Afhankelijk van mandatering en/of de werkafspraken met het
betreffende bevoegd gezag komt een aanvraag 1-op-1 of gedeeltelijk bij een
uitvoeringsorganisatie (Omgevingsdienst, Veiligheidsregio, etc.) binnen ter behandeling. De
werkafspraken en de wijze van indienen bepalen ook of een aanvraag geautomatiseerd
binnenkomt in het procesvolgsysteem en/of Zaaksysteem-DMS/RMA, inclusief bijbehorende
documenten.
De aanvraag met alle documenten vormen een ‘zaak’ (zaakgericht werken), die grotendeels
procesmatig wordt afgehandeld, met een vastgesteld zaakresultaat. Processtappen zijn in
hoofdlijnen: De vergunningverlener beoordeelt deze aanvraag, toetst deze aan wet- en
regelgeving en bestaande plannen, beleid en van toepassing zijnde verordeningen en geeft
het oordeel of de aangevraagde activiteiten al dan niet vergund kunnen worden, in de vorm
van een vergunningsdocument (Besluit, Beschikking). Hierbij kan de vergunningverlener
advies inwinnen of samenwerken met interne vakspecialisten en juristen, dit verloopt via de
procesapplicatie door een gerelateerde (sub/deel-)zaak uit te zetten. Vaak is ook
afstemming met het bevoegd gezag of met de aanvrager nodig, dit kan via het landelijke
aanvraagloket (Omgevingsloket Online/OLO), maar verloopt nog ook vaak via traditionele
kanalen (mail, bestandsuitwisseling) en schriftelijk (in de meeste gevallen wordt formeel
aangeschreven per brief ivm de opschortende werking van de termijnen). In de toekomst
dient dit waar mogelijk via DSO-LV plaats te vinden, ondersteund door een ketenoplossing.
Daarnaast legt de vergunningverlener de aangevraagde activiteiten met bijbehorende
regelgeving en voorschriften (geografisch) vast in een Objectregistratie.


## Page 50

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 49 van 102
Na afronden wordt de zaak gesloten en gearchiveerd, eventueel na doorlopen en
behandelen van zienswijzen en bezwaar- en beroepsprocedures. Dit archiveren gebeurt op
verschillende plaatsen in de keten: zowel bij Bevoegd Gezag als bij uitvoeringsorganisaties.,
daardoor moet een zaak na afsluiten in veel gevallen worden overgedragen naar het
Bevoegd Gezag. Dit is (nog) niet geautomatiseerd en verloopt ook via traditionele kanalen.

Informatiebronnen
Voorbeelden:
Ruimtelijkeplannen.nl / DSO, gemeentelijke en provinciale verordeningen
Diverse Geo systemen (intern/extern)
Historische locatiegegevens (eerdere zaken)
Zwemwaterregister, Zwemwaterkwaliteitgegevens, Systeem ZIN (Zwemwaterkwaliteit in
Noord-Brabant)
Diverse vakspecifieke registers
(eigen) checklisten
Etc. Etc.

Mobiliteit
Beperkt, vergunningverleners werken vaak op kantoor en/of telewerken.  Zij hebben wel
vaak overleg met collega’s, adviseurs en betrokkenen. Of vertegenwoordigen het college
van B&W /GS bij bezwaar en beroepsprocedures.
Verbeterpunten
Gekozen terminologie in de procesapplicaties (spreken van de juiste taal)

Veranderingen
Omgevingswet
•
Meer adviserende rol dan toetsende functie
•
Toename aantal zaken onder reguliere procedure (8 weken)
•
Geen fatale termijnen meer (vervallen lex silencio positivo)
•
Meer samenwerking met externe partijen.
•
Integraal toetsingskader onder de OW (toets bouw-, milieu- en R.O.-aspecten);
onderzoeksplicht schuift door van planfase naar vergunningsfase en daarmee ook
de toets van de rapporten.
•
Vooroverleg wordt belangrijker, gelet op de korte proceduretermijnen; dus ook
een stap invoeren voor vooroverleg




## Page 51

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 50 van 102
Persona
Vergunningverlener Bouw/afwijking bestemmingsplannen,
aanleg- en monumentenvergunningen
Gemma
Verantwoordelijkheid voor besluiten op vergunningaanvragen en het waar nodig of gewenst
inschakelen van ketenpartners voor advies (al dan niet met instemming) en samenwerking.
Persona-omschrijving
Behandelt aanvragen van bedrijven, instellingen of burgers, die op een bepaalde locatie
bouwactiviteiten willen gaan uitvoeren, al dan niet met afwijken van bestemmingsplan.

Taak van de vergunningverlener is toetsen en beoordelen of de aanvraag binnen de wet- en
regelgeving valt, of er specifiek toestemming voor verleend moet worden – al dan niet met
aanpassingen in de aanvraag, of dat een aanvraag geweigerd wordt.

Ook kan de vergunningverlener voordat de aanvraag wordt ingediend betrokken
worden bij een vooroverleg (principe verzoek) waar door de aanvrager om verzocht
wordt. Ook zal de vergunningverlener dienstverlenende activiteiten uitvoeren (zowel
intern als extern). Bijvoorbeeld initiatiefnemers adviseren.

Proces op hoofdlijnen,
Informatieverwerking
Intake (administratie/DIV)
Check op indieningsvereisten
Eventueel verzoek om aanvullende gegevens
Inhoudelijk behandelen, uitzetten interne/externe adviezen, berekenen leges
CT (collega VV)
Besluit opstellen en ondertekenen
Publicatie
Bezwaar- en beroepsprocedure
Onherroepelijk maken vergunning

Elke aanvraag / melding vormt een zaak in de applicatie. Hierin is het proces van de zaak te
volgen, de vergunningverlener volgt bepaalde vastgelegde processtappen.
Aanvraag wordt beoordeeld en getoetst aan wet- en regelgeving.
Adviezen worden gevraagd via de applicatie aan interne en of externe adviseurs
Adviezen en oordeel worden verwerkt en geregistreerd in de applicatie en de
vergunningverlener maakt een beschikking of beschikking wordt in de zaak via een
sjabloon gegenereerd en (digitaal) verzonden naar aanvrager/gemachtigde.
Verzenddata van correspondentie wordt bijgehouden in de applicatie.

Informatiebronnen
DSO (Omgevingsloket)
WABO/Mor/Bor/Bouwbesluit (zelf in systeem gevulde checklisten, externe toetsingstools
(BRIStoets)
Geoviewer: vanuit OD ook de geoviewers van de gemeenten
Basisregistraties: BAG, BRP, NHR
Verordeningen
NEN-normen/Euro-codes (Abonnementen)
Mobiliteit
Beperkt
Verbeterpunten
Digitaal ondertekenen
Veranderingen
Omgevingswet
PKB (Private kwaliteitsborging bouw) en participatieplicht
integraal toetsingskader onder de OW (toets bouw-, milieu en R.O aspecten;
onderzoeksplicht schuift door van planfase naar vergunningsfase en daarmee ook de toets
van de rapporten. Vooroverleg wordt belangrijker, gelet op de korte proceduretermijnen;
dus ook een stap invoeren voor vooroverleg


## Page 52

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 51 van 102
Persona
Regievoerder
Gemma
Je voert de regie over de integrale inzet op de gemeentelijke taken welke voor een groot
deel worden uitgevoerd door in- en externe partner (OD’s)
Persona-omschrijving
Zet opdrachten uit bij externe partners voor advisering over en behandeling van VTH-
taken op het gebied van bouwen, afwijking bestemmingsplannen en aanleg- en
monumentenvergunning en milieu. Houdt regie op het tijdig aanleveren van de gevraagde
adviezen en het binnen wettelijke termijnen afhandelen van aanvragen. Houdt controle op
budgetten en afspraken/termijnen zoals die zijn vastgelegd in werkprogramma’s en de
daarbij horende toezichtprogramma’s. Adviseert college van burgemeester en
wethouders. Levert maandelijks overzichten aan voor MARAP’s betreffende ingediende en
verleende vergunningen, budgetverloop en doorlooptijden.
Proces op hoofdlijnen,
Informatieverwerking
Een aanvraag wordt altijd gericht aan het ‘bevoegd gezag’. Afhankelijk van de
werkafspraken met het betreffende bevoegd gezag komt een aanvraag 1-op-1 of
gedeeltelijk bij de ODZOB binnen ter behandeling. De werkafspraken en de wijze van
indienen bepalen of een aanvraag geautomatiseerd binnenkomt in de procesapplicatie
SquitXO, inclusief bijbehorende documenten. De aanvraag met alle documenten vormen
een ‘zaak’ (zaakgericht werken), die grotendeels procesmatig wordt afgehandeld, met een
vastgesteld zaakresultaat. Processtappen zijn in hoofdlijnen: De regievoerder beoordeeld
of de aanvraag doorgezet dient te worden naar de externe partner (ODZOB). Hierbij kan
de regievoerder advies inwinnen of samenwerken met interne vakspecialisten en juristen,
dit verloopt via de procesapplicatie door een ‘deelzaak’ uit te zetten. Na afronden wordt
de zaak gesloten en gearchiveerd. Dit archiveren gebeurt door het overgrote deel van de
gemeenten zelf, daardoor moet een zaak na afsluiten worden overgedragen naar de
gemeente. Dit is (nog) niet geautomatiseerd en verloopt via traditionele kanalen.
Informatiebronnen
Rapportagesysteem van uitvoeringsorganisatie t.b.v. (management)overzichten en
stuurinformatie. Directe toegang tot het operationele systeem ook wenselijk om op
casusniveau te sturen en monitoren.
Mobiliteit
Regievoerders werken zowel op eigen kantoor als bij de externe partners. Zij hebben vaak
overleg met collega’s en externe adviseurs.
Verbeterpunten

Vaak is uitwisseling van gegevens een probleem omdat niet alle deelnemers met de zelfde
zaaksystemen werken. Ook het naleven van de termijnen vraagt met regelmaat om
aandacht en bijsturing. Doordat er met verschillende systemen wordt gewerkt is het lastig
om correcte managementrapportages op te stellen die aansluiten bij de wensen van de
gemeente.
Direct ‘inschieten’ van een opdracht, i.p.v. via losse formulieren zonder koppeling met het
systeem (PDC)
Zie ook opmerkingen onder ‘Informatiebronnen’.
Veranderingen
Omgevingswet
Verwachting is dat dit positief kan uitpakken door het afstemmen en werken met één
Objectregistratie, met doorkoppeling naar de lopende zaken.
Integraal toetsingskader onder de OW (toets bouw-, milieu en R.O aspecten;
onderzoeksplicht schuift door van planfase naar vergunningfase en daarmee ook de toets
van de rapporten. Vooroverleg wordt belangrijker, gelet op de korte proceduretermijnen;
dus ook een stap invoeren voor vooroverleg en een stap voor participatie toevoegen





## Page 53

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 52 van 102
Persona
Toezichthouder (initiële controle + hercontrole) Handhaver
(Bestuurlijk, Strafrechtelijk (BOA))

Gemma
n.v.t.
Persona-omschrijving
Toezichthouder
Controleert de naleving van regelgeving/beleid.

Aanleidingen
Bijvoorbeeld: Initiële controle, opleverings-., klacht-, her-, thema-, administratieve-,
bestuurlijke-, vrijeveld-controle, etc. Er zijn derhalve vele verschillende aanleidingen…

Domeinen
APV, WABO (->omgevingswet) en Wnb en Vnb en PAS (agrarisch)
D&H, RO (bestemmingsplan check)
(in hoeverre gaan deze zaken integraal op in de omgevingswet?

Toezicht kan worden ingepland na het verlenen van een vergunning, maar kan ook
periodiek volgens een schema of per branche, bedrijfstak of per locatie plaatsvinden. Deze
vast geplande controles worden steeds meer vervangen door informatie- of risico-gestuurd
toezicht, zodat veel gerichter de overtreders in beeld komen en bedrijven die de regels
goed naleven niet onnodig bezocht worden.

Periodieke controles:
1.
Programmatische controle (gebaseerd op risico-analyses van branches)
2.
Op basis van klachten/meldingen
3.
Op basis van landelijke of lokale thema’s

Toezicht op basis van LHS (landelijk handhaving strategie)

Nadere toelichting bij: Handhaver (Bestuurlijk, Strafrechtelijk (BOA))
Draagt zorg voor oplossen/herstellen van overtredend gedrag

Aanleidingen
Alles wat als overtreding is geconstateerd in voorgaande controles, maar nog niet opgelost
is vanuit toezicht

Handhaving op basis van LHS (landelijke handhavingsstrategie)

Proces op hoofdlijnen,
Informatieverwerking
•
Programma planning controles
•
Bepalen strategie (welke objecten) incl. opleveringscontrole
•
Controles inplannen (door TZH)
•
Zaak aanmaken (door administratie of TZH)
•
Controle uitvoering
•
(Mobiel) verslaglegging in de zaak
•
Informatie aanpassen in zaak / omgevingsregistratie

Toezicht vindt ook plaats via zaken, procesmatig en met een vastgesteld zaakresultaat.
Alvorens een controle uit te voeren in het veld gaat een toezichthouder informatie over de
bestaande situatie verzamelen en zich inlezen. In principe zou al deze informatie in de
procesapplicatie en het locatie-/omgevingsdossier moeten staan. Dit is echter vaak niet het

## Page 54

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 53 van 102
geval en moet de toezichthouder (losse) documenten, tekeningen, etc. verzamelen en derde
systemen raadplegen om een goed beeld te vormen.
Oorzaak is enerzijds dat de ODZOB nog (lang) niet van alle situatie een sluitend beeld heeft
in de systemen, anderzijds omdat er ook veel informatie geregistreerd wordt / moet
worden in externe systemen en registers.
Deze voorbereiding voert de toezichthouder dan ook vaak uit vanaf de vaste werkplek, op
kantoor of via telewerken. Soms is het zelfs nodig fysieke stukken te raadplegen in
gemeentelijke archieven. Met deze diversiteit aan informatie wordt de controle op locatie
uitgevoerd, waarbij de toezichthouder de zaken controleert zoals eerder al beschreven bij
de vergunningverlener. Dit gebeurt aan de hand van checklisten en standaarddocumenten,
maar het is nadrukkelijk niet alleen een kwestie van alleen ‘afvinken’: goed inleven in de
situatie middels gesprekken of het geven van gerichte adviezen bij kleine
onvolkomenheden zijn minstens zo belangrijk. Vervolgacties zijn namelijk gebaseerd op
twee factoren:
Zijn er overtredingen, en zo ja: hoe zwaar (checklist);
Wat is de houding van de overtreder, dit kan variëren van onbewust gedrag tot aan
moedwillig en herhaaldelijk overtreden.
Deze factoren vormen samen de handhavingsstrategie, een centraal element in de output
van de controle: een bezoekverslag met een beschrijving, resultaten van de checklist en
aanbevelingen voor eventuele vervolgacties (hercontrole en/of handhaving). Daarnaast
verwerkt de toezichthouder de resultaten in het locatie-/omgevingsdossier

Informatiebronnen
BRP, BAG, BGT, (nagenoeg alle basisregistratie), KvK, OLO, AIM, Zaaksysteem,
omgevingsregistratie, ruimtelijke plannen, WebBvB, DigiMak, Bodemsysteem,
keuringsinstanties, Zwemwaterregister, Waterkwaliteitgegevens, etc.
Kortom: ook vele, veelal niet gekoppelde, externe systemen.
Mobiliteit
Groot, toezichthouders werken op veel verschillende plaatsen. Hoe meer informatie via een
mobiel device beschikbaar, hoe beter. Kanttekening: bij de feitelijke controle op locatie
geeft men vaak aan niet te veel op een device te willen werken: dat creëert afstand, maar
kan ook zeer onpraktisch zijn om snel aantekeningen te maken en onhandig bij het
inspecteren van grote installaties. Een klein notitieblok en de mobiele telefoon (foto’s)
blijken vaak handiger.
Verbeterpunten
Locatie moet aangemaakt kunnen worden zonder aanleiding. informatie moet geborgd
kunnen worden zonder ‘harde’ melding of klacht.

Bij overdragen van TZ naar LHS moet resultaat worden ingevuld, dan pas wordt verslag
gegenereerd. Beter: eerst verslag incl. CT, dan pas resultaat invullen, dan kan het als geheel
naar juristen toe.
Processtappen zijn niet altijd helder, gebruikers die minder thuis zijn in het systeem
ervaren dat als barrière en halen niet alles uit het systeem.

Veranderingen
Omgevingswet
Zal in eerste instantie qua uitvoering nog niet sterk wijzigen, afgezien uiteraard van de
nieuwe wetgeving van de verschuiving van ‘inrichtingen’ naar ‘activiteiten’. Bij verdere
vulling en nieuwe functies in het DSO wordt dat mogelijk wel anders.
Uitzondering: In TZ bouw verandert wel veel, o.m. via de introductie van privaat
bouwtoezicht.







## Page 55

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 54 van 102
Persona
Klachtenafhandeling/Consignatiedienst
Nb: betreft toevoegingen op de eerder opgenomen persona
Toezichthouder/Handhaver
Gemma

Persona-omschrijving

Proces op hoofdlijnen,
Informatieverwerking
Meldingen komen (24x7) binnen via diverse kanalen: de Milieuklachtencentrale,
Meldkamers Politie en Brandweer, specifieke (particuliere) meldkamers, en groeiend via
nieuwe kanalen zoals meldingen-apps (bijv. BuitenBeter app) en Social Media.

Klachten gebonden aan eenmalige activiteiten, zoals evenementen en concerten. Hiertoe is
goed inzicht vereist in mogelijk verleende ontheffingen specifiek voor een evenement, of
generiek voor een gebied (zoals bij algemene feestdagen)

Alleen reageren op incidenten vanuit bedrijven, overlast vanuit particulieren is een zaak
voor de politie (filteren)

Rol Uitvoeringsdiensten calamiteiten
De ODZOB (en VRBZO) is bronhouder van gegevens die van belang zijn bij een calamiteit bij
een activiteit met gevaarlijke stoffen. Hulpdiensten, waterschap en bestuurders willen bij
een calamiteit beschikken over informatie om de juiste beslissingen te kunnen nemen en
om goede communicatie naar omgeving en pers te kunnen uitvoeren. Het snel en
eenvoudig ter beschikking zijn van die informatie is van groot belang.

Informatiebronnen
DigiMak (regionale evenementenregistratie), S@men (klachtenregistratie), KNMI
weergegevens t.b.v. geluidsmetingen
Mobiliteit
Zeer groot
Verbeterpunten
Diverse losse systemen zijn niet geïntegreerd, betekent veel kopiëren/plakken van
informatie
Veranderingen
Omgevingswet
Potentiele functie van het DSO om specifieke omstandigheden – bijv. bij evenementen - in
te zien




## Page 56

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 55 van 102
Persona
Technisch adviseur (RO/EV/…)
Gemma
n.v.t.
Persona-omschrijving
Technisch adviseurs hebben doorgaans een specialisatie op een specifiek terrein,
bijvoorbeeld geluid, geur, bodem, energie, water, constructie, etc. Op deze terreinen
verstrekken zij adviezen, voeren berekeningen uit of geven mede vorm aan
uitvoeringsbeleid.
Dit doen zij ter ondersteuning van het VTH proces, maar ook geregeld in opdracht van
gemeenten en provincie of in samenwerking met andere instanties als de Veiligheidsregio
en het Waterschap.
Proces op hoofdlijnen,
Informatieverwerking
Opdracht van de opdrachtgever (provincie of gemeente) komt direct of indirect binnen bij
de werkverdeler. Het opdrachtformulier met informatie over inhoud toetsing, hoeveelheid
uren, verantwoordelijke medewerker, productcategorie, etc. en relevante stukken worden
via de werkverdeler aan het secretariaat/de proceduremedewerker gestuurd voor het
aanmaken van een projectnummer en het genereren van een zaak waarin de stukken ook
worden geplaatst. Hierbij wordt gecontroleerd of de juiste productcode uit de
productencatalogus is gebruikt.
De adviseur bekijkt de stukken en beslist of er ook deelzaken aangemaakt moeten worden
voor technisch adviseurs op een specifiek terrein. Er wordt een termijn en urenraming
afgesproken met de technisch adviseurs op een specifiek terrein waarbinnen de informatie
moet worden aangeleverd.
Ook wordt besloten of advies gevraagd moet worden bij de Veiligheidsregio en/of het
Waterschap.
Voor het proces wordt het zaaktype ‘advies overig’ gebruikt (HZ_ADV_OV).
Vanuit deze hoofdzaak worden de verschillende deelzaken aangemaakt (toets geur, toets
geluid, toets constructie, toets bodem, etc.).
Nadat de interne en externe adviezen binnen zijn wordt het totaaladvies opgesteld en
opgeslagen in de hoofdzaak. Indien nodig wordt er nog afgestemd op aspectniveau.
Het totaaladvies wordt ter ct aangeboden aan een collega.
Nadat het totaaladvies definitief is wordt het via het zaaksysteem aangeboden aan het
secretariaat waarna het verzonden wordt aan de opdrachtgever. Afhankelijk van het feit of
er nog informatie moet worden aangeleverd blijft de zaak open staan of wordt de zaak
afgesloten.

Bij ondersteuning van het VTH proces voegen zij de adviezen toe als onderdeel van een
zaak, zij handelen dan een (deel)zaak af die verder onder de verantwoordelijkheid van een
vergunningverlener loopt.
Bij andere opdrachten werkt de adviseur zelfstandiger. In alle gevallen kan de omvang van
een advies en daarmee benodigde hoeveelheden informatie enorm verschillen: van een
eenvoudig en kort advies dat als losse tekst wordt aangeleverd, tot aan grote berekeningen
waar vaak ook gespecialiseerde software voor nodig is.
Deze softwarepakketten zijn vaak dermate zwaar dat speciale werkplekken (reken-pc’s) zijn
ingericht op dit te hosten.
Informatiebronnen
BRIS warenhuis, NSL monitoringstool, Risicokaart, atlas.odzob.nl, ruimtelijkeplannen.nl,
Besluit NIBM, Besluit mer, Geitenmoratorium, VNG brochure ‘Bedrijven en milieuzonering’,
CAROLA, Safeti, Sites:
Algemeen en voor meerdere aspecten
www.pdok.nl
https://www.brabant.nl/subsites/kaarten.aspx
Atlas.odzob.nl
www.infomil.nl
www.wetten.nl
Ruimtelijke ordening

## Page 57

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 56 van 102
www.ruimtelijkeplannen.nl
Ruimtelijkeplannen.brabant.nl
Bedrijven en milieuzonering
https://vng.nl/onderwerpenindex/ruimte-en-
wonen/omgevingswet/publicaties/handreiking-bedrijven-en-milieuzonering
https://www.cbs.nl/nl-nl/onze-diensten/methoden/classificaties/activiteiten/sbi-
2008-standaard-bedrijfsindeling-2008
https://www.kvk.nl/zoeken/handelsregister/
Externe veiligheid
http://www.brabant.nl/dossiers/dossiers-op-thema/veiligheid/risicokaart.aspx
http://www.vrbzo.nl/VRBZ-taken.html
Geluid
http://www.geluidregisterspoor.nl/
https://www.rijkswaterstaat.nl/wegen/wetten-regels-en-vergunningen/geluid-
langs-rijkswegen/geluidregister.aspx
Zie algemeen
Bodem
www.bodemloket.nl
Zie algemeen
Water
https://www.dommel.nl/producten/watertoets.html
https://www.aaenmaas.nl/producten/watertoets-voor-ruimtelijkeplannen.nl
Zie algemeen
Luchtkwaliteit
http://www.nsl-monitoring.nl/
http://www.infomil.nl/onderwerpen/klimaat-
lucht/luchtkwaliteit/slag/hulpmiddelen/nibm-tool/
Geur
Zie algemeen
Flora en fauna
Zie algemeen
Archeologie en cultuurhistorie
Zie algemeen
Gezondheid
https://www.ggdghorkennisnet.nl/thema/gezondheid-en-milieu
Duurzaamheid
 http://www.handreikingdro.nl/
MER
www.commissiemer.nl
Nieuwsbrieven:
http://www.nieuweplannen.nl
http://www.omgevingsweb.nl/signup
Zwemwaterregister
Zwemwaterkwaliteitsgegevens
Mobiliteit
Kan heel groot zijn, zeker als de adviseur complexe berekeningen moet maken en er veel
partijen betrokken zijn een case.
Daarbij kan de noodzaak voor krachtige werkstations beperkend zijn: deze werkplekken
zijn vaak losse werkstations, los opgesteld van de standaard werkplekken van de
organisatie.
Verbeterpunten
Trage systemen, geen eenduidige manier van werken (zaaksysteem versus losse document-
en gegevensopslag op netwerkschijven), overschrijden maximale termijnen, overschrijden
afgesproken uren, koppeling tussen zaaksysteem en ondersteunende programma’s
verbeteren, zaaktype voldoet niet altijd aan toetsvoorwaarden.
Veranderingen
Omgevingswet
Uitgangspunt is omgevingsplan in plaats van bestemmingsplan. Verschillende belangen in
een gebied meewegen. Belangrijk om deze informatie beschikbaar te hebben tijdens
toetsing voor zowel casemanager als gespecialiseerde technische adviseur.







## Page 58

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 57 van 102
Persona
Vergunningverlener (APV / D&H / Bijzondere wetten)
Gemma
Verantwoordelijkheid voor besluiten op vergunningaanvragen en/of het
beoordelen van meldingen en het waar nodig of gewenst inschakelen van
ketenpartners voor advies (al dan niet met instemming) en samenwerking.
Persona-omschrijving
Verwerkt aanvragen en meldingen van bedrijven, instellingen of burgers, die in hun
bedrijfsvoering of op een bepaalde locatie activiteiten willen gaan uitvoeren binnen
bepaalde eerder in dit document genoemde domeinen.
Taak van de vergunningverlener is toetsen en beoordelen of de aanvraag/melding binnen
de wet- en regelgeving valt, of er specifiek toestemming/vergunning/ontheffing voor
verleend moet worden – al dan niet met aanpassingen in de aanvraag, of dat een aanvraag
geweigerd wordt.

Proces op hoofdlijnen,
Informatieverwerking
•
Aanvraag/Intake (snelbalie, administratie, KCC, DIV). Resulteert in zaak
•
Toetsing (ontvankelijkheid en inhoud)
•
Advisering (zowel in- als extern (politie, GGD, VR, OD..)
•
Leges bepalen en registreren (via koppeling/export naar financiën)
•
Besluitvorming
•
Registratie (in DigiMak bij evenementen)
•
Publicatie besluit en/of aanvraag
•
Schouw vooraf bij evenementen(Best) (controle verguninningen met werkelijkheid en
toepasbaarheid)
•
Overdracht aan Toezicht (aanmaken controlezaak)

(proces afhandeling in één zaak)

Elke aanvraag / melding vormt een zaak in de applicatie. Hierin is het proces van de zaak te
volgen, de vergunningverlener volgt bepaalde vastgelegde processtappen.
Aanvraag wordt beoordeeld en getoetst aan wet- en regelgeving.
Adviezen worden gevraagd via de applicatie aan interne en of externe adviseurs
Adviezen en oordeel worden verwerkt en geregistreerd in de applicatie,  en de
vergunningverlener maakt een beschikking of .
Beschikking wordt in de zaak via een sjabloon gegenereerd en (digitaal) verzonden naar
aanvrager/gemachtigde
Verzenddata van correspondentie en datum beschikking worden bijgehouden in de
applicatie.

Informatiebronnen
DigiMak, RIEC, wet BIBOB, Awb, APV, legesverordening, Bijzondere wetten zoals D&H-wet,
wegenverkeerswet, winkeltijdenwet, etc.
Mobiliteit
Mogelijk groot bij schouw op locatie
Verbeterpunten
Digitaal ondertekenen
Koppeling DigiMak in VTH applicatie
Mogelijkheid BIBOB informatie aan te vragen en te verwerken

Veranderingen
Omgevingswet
Verzoeken via DSO,
Is legesberekening volgens wisselende artikelen (jaarlijks) en verordening (per gemeente)
beschikbaar?




## Page 59

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 58 van 102

Persona
Administratie VTH
Gemma

Persona-omschrijving
Schept de basisvoorwaarden voor casemanagers/zaakverantwoordelijken, zodat deze zich
kunnen concentreren op hun inhoudelijke taak. Voert taken uit die voortvloeien uit de AVG.
Registreert aanvragen, meldingen, controles en klachten voor Wabo, APV, Bijzondere
wetten en andere zaken in het ruimtelijk domein. Verstrekt procedure informatie.
Publiceert aanvragen en besluiten. Stelt legesnota’s op en verstuurt deze naar aanvragers.
Exporteert facturen periodiek naar Financiële afdeling. Rondt de opgestelde
besluitdocumenten af. Communiceert besluiten met aanvrager en/of gemachtigde.
Signaleert de termijnen met een wekelijkse rapportage aan casemanagers en
leidinggevende. Registreert en onderhoudt gegevens omtrent inrichtingen in een
locatiedossier. Handelt eenvoudige APV-zaken zelfstandig af. Zoekt bestemmingsplan
informatie uit voor burgers en bedrijven.
Proces op hoofdlijnen,
Informatieverwerking
Hoofdproces:
Administratie werkt samen met casemanager/zaakverantwoordelijke binnen één proces.
Eerst zet administratie de aanvraag klaar en publiceert deze. Vervolgens behandelt de
casemanager/zaakverantwoordelijke de zaak op volledigheid; doet daarna de inhoudelijke
behandeling, waarna zij/hij komt tot een besluit en bijbehorend legesbedrag. Daarna
completeert en verzendt administratie besluit en legesaanslag.

•
Aanvragen/meldingen komen binnen via diverse kanalen. De administratie maakt  een
zaak aan in de applicatie of controleert de zaak indien deze via een koppeling
(OLO/Snelbalie) is aangemaakt. Waar nodig worden gegevens van de aanvraag in de
zaak aangevuld. Denk  hierbij aan het verder invullen van bepaalde velden, het
toevoegen van bijlagen, het registreren van relaties met andere zaken en/of
locatiedossiers, het maken van notities.
•
Bij elke zaak controle op authenticiteit, correspondentiegegevens en status (beëindigd
/overleden) van adres(sen), en niet natuurlijke en natuurlijke personen.
•
Opschoning van vervuiling van subjecten en (delen van) objecten.
•
Correspondentie met aanvrager/gemachtigde over procedure, leges en beschikkingen
m.b.v. in de applicatie gegenereerde sjablonen.
•
Via het proces wordt publicatie van aanvraag/melding/beschikking afgehandeld.
•
Leges worden doorgezet naar Financiën via een koppeling c.q. export.
•
Na afronding van de zaak worden stukken ter archivering aangeboden aan het DMS.
•
Bijbehorend locatiedossier wordt aangepast n.a.v. de beschikking.
•
Op verzoek wordt  bestemmingsplaninformatie verstrekt aan burgers en bedrijven via
mail of post.
Informatiebronnen
o.a. OLO, Snelbalie, Website e-formulieren, Digimak, ruimtelijkeplannen.nl, Geotheek,
Handelsregister KvK, DMS, DROP/GVOP, CBS, AIM, BRP, Metatopos.eu
Mobiliteit
Contact met casemanagers/zaakverantwoordelijken nodig voor afstemming.
Verbeterpunten
Digitaal ondertekenen.
Opschoning door verwijdering van zaken, nu vaak niet mogelijk door onzichtbare relaties.
(eigenlijk taak van de recordsmanager)
Persoonsgegevens lostrekken van zaken / gerichte autorisatie nodig, ook op thema.
(AVG!!).
Vergemakkelijken van bedekken persoonsinformatie op bijlagen van besluiten i.v.m.
bekendmaken. (AVG!!).
Per zaak mogelijk maken om correspondentie(mail)adres en telefoonnr. bij te houden,
tegelijk met koppeling met broker/landelijke voorziening basisregistraties.

## Page 60

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 59 van 102


Veranderingen
Omgevingswet
Zie proceduremedewerker


Persona
Proceduremedewerker

Gemma
n.v.t.
Persona-omschrijving
Proceduremedewerkers ondersteunen met primaire VTH proces, voornamelijk bij de start
van een zaak (intake) en bij de afronding (overdracht naar aanvrager of bevoegd gezag).
Proces op hoofdlijnen,
Informatieverwerking
Bij de start zorgen proceduremedewerkers dat de VTH-zaken aangemaakt worden in de
procesapplicatie en dat er in het financiële systeem een projectnummer is, zodat de aan de
zaak bestede uren verantwoord kunnen worden via het tijdschrijfsysteem.
Bij afronding van een zaak zorgen zij voor verwerking van de output (documenten):
verzending naar de betreffende aanvrager of gecontroleerd bedrijf en/of naar het
betreffende bevoegd gezag. Dit hangt af of de ODZOB de zaken wel of niet in mandaat
uitvoert voor het bevoegd gezag. Hoewel er steeds meer in mandaat gewerkt wordt, is het
zeker nog niet de standaard werkafspraak binnen de 22 opdrachtgevers van de ODZOB.
Proceduremedewerkers moeten dan ook voortdurend deze werkafspraken checken bij
starten en afronden van de zaken.
Informatiebronnen
Vnl. de interne systemen en de basisregistraties
Mobiliteit
Zeer beperkt
Verbeterpunten
Ruimere zoekmogelijkheden in de basisregistraties, m.n. BAG en NHR. In de praktijk is het
vaak lastig de werkelijke adressen en bedrijfsnamen te vinden en te koppelen

Koppeling processysteem naar financieel systeem, zie ook Veranderingen Omgevingswet.
Veranderingen
Omgevingswet
Door verkorting van de wettelijke termijnen mag er absoluut geen vertraging bij intake en
overdracht zitten. Een notificatie van zaken die openstaan maar nog niet opgepakt zijn is
zeer welkom. Bij overdracht terug naar bevoegd gezag of aanvrager is integratie met het
processysteem een must, i.p.v. het huidige handmatige versturen via traditionele kanalen
zoals e-mail, WeTransfer en fysieke poststukken.




## Page 61

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 60 van 102
Persona
Manager VTH

Gemma

Persona-omschrijving
De manager VTH  is verantwoordelijk voor het hiërarchisch aansturen van zijn afdeling en
eventueel (afdelingsoverstijgende) projecten zodat de gewenste bijdrage aan de
organisatiedoelstelling geleverd wordt en hierover rapporteren (jaarverslag, tussentijdse
rapportages, afdelingsplannen, uitvoeringsprogramma etc.) De manager is lid van het
Management Overleg (MO) en is budgethouder van toebedeelde budgetten. Hij is
verantwoordelijk voor het financieel beheer van toebedeelde middelen binnen de
vastgestelde kaders.
Hij heeft de verantwoordelijkheid voor de (kwaliteit van de) activiteiten en resultaten welke
vanuit de afdeling moeten worden bereikt. Sturing is ontwikkelings-, output- en
procesgericht.
Managementrapportages geven uitgangspunten voor het inzetten van mensen, middelen en
methoden (strategisch en tactisch niveau).
Binnen de kaders van het management formuleert de manager de te realiseren resultaten
op de geformuleerde resultaatgebieden en de persoonlijke ontwikkeling van de
medewerkers. De concretisering naar concrete resultaten en prestatie-indicatoren vindt
jaarlijks plaats binnen de personele jaarcyclus (planningsgesprekken).
Proces op hoofdlijnen,
Informatieverwerking
•
Beleidsontwikkeling en kaderstelling
•
Adviseert in MO over vaststelling van beleid en kaders (het bepalen van doelstellingen,
randvoorwaarden en uitgangspunten) of het inzetten van mensen, middelen en
methoden binnen de aan de afdeling toebedeelde werkzaamheden.
•
Signaleert ontwikkelingen en reikt verbetervoorstellen aan voor vernieuwing van
algemeen beleid, uitvoering en/of beheer (gevraagd en ongevraagd).
•
Stelt integrale beleidsadviezen en uitvoeringsnota’s op over het bepalen van
doelstellingen, randvoorwaarden en uitgangspunten of het inzetten van mensen,
middelen en methoden met betrekking tot aan de afdeling toegewezen taken, o.a. op
basis van vastgestelde jaarplannen en stimuleert de hiervoor benodigde samenwerking
binnen en buiten de afdeling en ook buiten de gemeente.
Informatiebronnen
VTH- en zaaksysteem en managementrapportages (vanuit Datawarehouse/BI-Omgeving)
Mobiliteit
Managers werken op eigen kantoor. Hebben vaak overleg met collega’s van eigen en
samenwerkende gemeenten. Voeren gesprekken met mensen van eigen afdeling en
externen.
Verbeterpunten
Doordat er met verschillende systemen wordt gewerkt is het lastig om correcte
managementrapportages op te stellen die aansluiten bij de wensen van de gemeente. Het
nieuwe VTH-systeem moet functionaliteiten bevatten die het mogelijk maken om
managementrapportages te genereren zonder gebruik te maken van meerdere/andere
applicaties.
Wat draagt de uitvoering van de VTH-taken bij aan de uitvoering van diverse beleid?
(bijdrage aan gezondheid, veiligheid, naleefgedrag etc.)
Veranderingen
Omgevingswet






## Page 62

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 61 van 102
Persona
Informatiebeheerder/recordsmanager (DIV, archivering)
Gemma
Niet in primair proces, maar wel vanuit het ondersteunende proces als specialist.
Verantwoordelijkheid voor het beheren van documenten, opgeslagen in het DMS/RMA in
het kader van de Omgevingswet. Hieronder vallen onder meer het toezien op een goede
registratie en dossiervorming en specifiek de borging op het duurzame behoud van de
dossiers conform wet- en regelgeving. De informatiebeheerder/recordsmanager zorgt
jaarlijks voor een tijdige procedurele vernietiging en op de lange termijn voor de
overbrenging van blijvend te bewaren archiefdossiers naar het e-depot van het regionaal
archief dan wel provinciaal archief.
Persona-omschrijving
Ziet toe op de kwaliteit, vindbaarheid, identificeerbaarheid en volledigheid van informatie
(metadata, dossiervorming, selectie, vernietiging en overbrenging).
Proces op hoofdlijnen,
Informatieverwerking
Een document wordt aangemaakt in het RO/VTH-pakket via de interne sjablonengenerator
en opgeslagen in het externe DMS/RMA. In het zaakdossier van het RO/VTH-pakket blijft
een link naar het opgeslagen document. Na afsluiten van een zaakdossier wordt getoetst op
kwaliteit, vindbaarheid, identificeerbaarheid en volledigheid van informatie. Vervolgens
wordt een bewaar- en/of vernietigingstermijn toegekend. Afhankelijk van de uitkomst
worden zaakdossiers op termijn vernietigd dan wel overgedragen aan het e-depot van de
desbetreffende archiefinstelling.

Een aanvraag wordt altijd gericht aan het ‘bevoegd gezag’ door een burger of een
bedrijf/instelling. Indien aangevraagd via OLO, komt deze via digikoppeling  in de
procesapplicatie, inclusief bijbehorende documenten. Indien analoog aangevraagd, wordt
deze ook analoog beantwoord, maar digitaal verwerkt door de organisatie. De aanvraag
met alle documenten start een ‘zaak’, die grotendeels procesmatig wordt afgehandeld, met
een vastgesteld zaakresultaat. Processtappen zijn in hoofdlijnen: de vergunningverlener
beoordeelt de aanvraag, toetst deze aan wet- en regelgeving en bestaande plannen, beleid
en van toepassing zijnde verordeningen en geeft het oordeel of de aangevraagde
activiteiten al dan niet vergund kunnen worden, in de vorm van een vergunningsdocument
→ Beschikking. Tijdens het behandelproces kan de vergunningverlener advies inwinnen of
samenwerken met interne en externe vakspecialisten en juristen. Dit verloopt via de
procesapplicatie door een ‘deelzaak’ uit te zetten. Vaak is ook afstemming met de
aanvrager nodig, dit kan via het landelijke aanvraagloket (Omgevingsloket Online/OLO),
maar verloopt nog ook vaak via traditionele kanalen (mail, beveiligde bestandsuitwisseling)
en schriftelijk (in de meeste gevallen wordt formeel aangeschreven per brief i.v.m. de
opschortende werking van de termijnen). Na onherroepelijk worden van de beschikking
wordt de zaak gesloten. Hierna start het eigenlijke archiefbeheer door de
informatiebeheerder/recordsmanager.
Informatiebronnen
Archiefwet 1995, Archiefbesluit 1995, Archiefregeling en aanpalende wet- en regelgeving
zoals Wob/Woo, AVG, BIO et cetera.
Mobiliteit
Beperkt
Verbeterpunten
1.
Inrichting ketenarchivering: goede afspraken maken welke ketenpartij voor welke
informatie archiefverantwoordelijk is.
2.
Dubbele dossiervorming voorkomen.
3.
Regiehouder/-deelnemer zijn voor de ZTC.
4.
Overdracht en vernietiging moeten mogelijk zijn in het nieuwe systeem.
5.
Opschonen moet mogelijk zijn zonder restanten, zoals metadata die momenteel in de
RO/VTH-software achterblijft.
Veranderingen
Omgevingswet
In de koppeling Procesapplicatie-Zaaksysteem kan de initiële relatie uitsluitend gelegd
worden vanuit de procesapplicatie. Een gebruiker wil dit soort beperkingen niet voelen,

## Page 63

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 62 van 102
maar zijn document maken op een logische plaats in het vertrouwen dat het op de
bestemde plaats wordt opgeslagen en bewaard.
Goede afspraken wie in de keten formeel de verantwoordelijkheid heeft voor het
archiefbeheer.
Grote mate van toegankelijkheid voor de andere ketenpartners.

## Page 64

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 63 van 102
Annex B
Eisen en wensen vanuit GEMMA requirements



## Page 65

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 64 van 102
1. Requirements Applicatiefunctie: Ondersteunen van generieke VTH-OW functionaliteit
Requirement
Documentatie
Eis/Wens
(Uitvraag)
Eis 10
VTH002 Kunnen registeren van de
beschikking
Voor toezicht, handhaving en monitoring is het van belang dat een beschikking wordt geregistreerd
inclusief belangrijke metadata. Hierbij wordt metadata opgeslagen zoals: - type beschikking
(Vergunning, maatwerkvoorschriften, handhaving) - datum beschikking - geldigheid (bv bij tijdelijke
omgevingsvergunning) - betrokken activiteiten. De beschikking wordt als document vastgelegd in de
Documentregistratiecomponent via de ZDS standaard of in het Documentenregister via de Documenten
API.
Eis
Eis 11
VTH004 Kunnen registreren van
(inkomende) correspondentie
Voor een goede audittrail moet inkomende correspondentie bij de zaak worden geregistreerd. De
correspondentie wordt vastgelegd in de Documentregistratiecomponent via de ZDS standaard of in het
Documentenregister via de Documenten API.
Eis
Eis 12
VTH005 Kunnen registreren van een
formeel, vastgesteld document
Een proces-verbaal, een advies, een verslag van een hoorzitting zijn voorbeelden van belangrijke
documenten die goed moeten worden vastgelegd nadat de inhoud (zonodig in overleg met
betrokkenen) is vastgesteld. De documenten worden vastgelegd in de Documentregistratiecomponent
via de ZDS standaard of in het Documentenregister via de Documenten API.
Eis
Eis 13
VTH006 Kunnen vastleggen en
registreren beslissing/advies voor
vervolg op basis van beoordeling
geconstateerde situatie
Inhoudelijk deskundige interne en/of externe adviseurs brengen een advies uit, waarin behalve de
conclusie of het past ook kan worden opgenomen welke aanpassingen aan het initiatief gedaan zouden
kunnen worden om het passend te maken. Het betreft hier tekstuele vastlegging in het systeem en niet
de eventueel bijhorende documenten, zoals het vastleggen/registreren van advies voor vervolg in relatie
tot handhavingsbeleid, bijvoorbeeld: Overtreding J/N, Ernst overtreding, Gedrag overtreder of Advies
sanctie. De documenten worden vastgelegd in de Documentregistratiecomponent via de ZDS standaard
of in het Documentenregister via de Documenten API.
Eis
Eis 14
VTH008 Kunnen starten, stoppen,
wijzigen en verwijderen van een
samenwerking in de
Samenwerkfunctionaliteit van het DSO-
LV
Indien het ingediende Verzoek leidt tot een samenwerking met een ketenpartner, moet het mogelijk zijn
om vanuit de VTH-software of Zaaksysteem een samenwerking in de Samenwerkfunctionaliteit van het
DSO-LV te kunnen starten. Naast het initiëren van een Samenwerking, moet het ook mogelijk zijn om
Samenwerkingen te stoppen, te wijzigen als de samenstelling van de samenwerking verandert en te
verwijderen als de documenten uit de samenwerking zijn gearchiveerd.
Eis
Eis 15
VTH009 Kunnen uitzetten en ontvangen
van actieverzoeken via de
Samenwerkfunctionaliteit van het DSO-
LV
Adviesaanvragen worden bij een (keten)partner uitgezet in de vorm van een actieverzoek. De VTH
software moet deze actieverzoeken in de Samenwerkfunctionaliteit kunnen uitzetten naar partners,
maar ook kunnen ontvangen van partners.
Eis

## Page 66

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 65 van 102
Eis 16
VTH013 Kunnen opslaan en opvragen
van documenten in de
Samenwerkfunctionaliteit van het DSO-
LV
Documenten (adviezen/rapporten/etc) die ketenpartners nodig hebben, moeten gedeeld kunnen
worden in de Samenwerking. De VTH software kan hiervoor documenten opslaan in de
Samenwerkfunctionaliteit. De documenten die door ketenpartners gedeeld worden via de
Samenwerkfunctionaliteit van het DSO-LV moeten door de VTH software opgehaald kunnen worden. Dit
kan nodig zijn bij het verder opstellen van het advies of bij het compleet maken van het dossier als de
zaak in afgehandeld. Indien documenten worden gedownload, worden deze opgeslagen in de
Documentregistratiecomponent via de ZDS standaard of in het Documentenregister via de Documenten
API.
Eis
Eis 17
VTH020 Kunnen opzoeken van
begrippen in de stelselcatalogus
De relevante begrippen uit het Omgevingsplan zijn een belangrijke basis voor de behandeling van een
VTH-zaak. Deze begrippen zijn opgenomen in de stelselcatalogus en moeten voor de behandeling van de
VTH-zaak daaruit kunnen worden geraadpleegd. Ook bij de uitvoering van Toezicht en Handhaving is het
gewenst om de juiste begrippen te kunnen hanteren.
Eis
Eis 18
VTH023 Kunnen opvragen van gegevens
in het monumentenregister bij de
Rijksdienst voor Cultureel Erfgoed
Als een Verzoek wordt ingediend, moet gecontroleerd kunnen worden in het monumentenregister bij
het RvCE of het om een Rijksmonument gaat of niet.
Eis
Eis 19
VTH024 Kunnen publiceren van een
besluit via het officiële
publicatiemechanisme (nu DROP, wordt
later LVBB)
Ontvangen aanvragen worden conform art. 16.63 Ow ten behoeve van belanghebbenden gepubliceerd
in een of meer dag-, nieuws- of huis-aan-huisbladen of op een andere geschikte wijze, onder vermelding
van de datum van ontvangst.
Eis
Wens 27
VTH029 Kunnen ophalen van gegevens /
documenten uit de
Archiefregistratiecomponent
Bij de behandeling van VTH-zaken kunnen gegevens/documenten uit gerelateerde zaken uit het
verleden van belang zijn of zelfs het uitgangspunt voor de behandeling van de zaak. De VTH software
haalt deze gegevens of documenten bijvoorbeeld uit een Archiefregistratiecomponent.
Wens
Eis 20
VTH030 Kunnen bevragen van gegevens
in de basis- of kernregistraties
Gegevens en bescheiden waarover de gemeente al beschikt, hoeven niet door de aanvrager te worden
geleverd. De VTH software heeft koppelingen naar relevante (landelijke) basisregistraties om dergelijke
gegevens te raadplegen.
Eis
Eis 21
VTH031 Kunnen bevragen en wijzigen
van gegevens in de
Zaakregistratiecomponent of het
Zakenregister
De VTH software kan een zaak registreren via de ZDS standaard in de Zaakregistratiecomponent of via
de Zaken API in het Zaakregister, de afhandeling (uitvoering en bewaking van het proces) gebeurt
vervolgens in de VTH software. Daarom moeten de gegevens kunnen worden uitgewisseld tussen deze
componenten. De Zaak- en Document Services is de huidige standaard om in het Zakenregister de zaak
te registreren met de status. Deze standaard wordt vervangen door de Zaken API.
Eis
Eis 22
VTH032 Kunnen bevragen van gegevens
in de Zaaktypecataloguscomponent of
het Catalogusregister
Bij het registreren van de zaak worden alleen zaaktypes gebruikt uit de zaaktypecatalogus.
Eis
Wens 28
VTH033 Kunnen bevragen van gegevens
in de financieel component
Bijvoorbeeld voor het factureren van opgelegde leges, verbeurd verklaarde dwangsommen of
uitvoeringskosten moeten de relevante gegevens kunnen worden uitgewisseld met de financiële
component.
Wens

## Page 67

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 66 van 102
Eis 23
VTH034 Kunnen bevragen en wijzigen
van gegevens in het Besluitenregister
Eerdere besluitvorming vormt een belangrijk kader voor een actuele VTH-zaak. Wanneer bijvoorbeeld
een ontheffing voor een bepaalde, afwijkende activiteit eerder is geweigerd, kan dat daarna niet zomaar
alsnog worden toegestaan.
Eis
Wens 29
VTH035 Kunnen aanbieden van
gegevens aan het data-analyse en
monitoringcomponent
VTH-besluiten hebben gevolgen voor de fysieke leefomgeving en brengen risico's in relatie tot het
naleefgedrag in beeld. Het is daarmee belangrijke informatie voor monitoring en analyse.
Wens
Eis 24
VTH036 Kunnen bevragen en wijzigen
van gegevens in de
Documentregistratiecomponent of het
Documentenregister
Documenten worden in de Documentregistratiecomponent opgeslagen en niet in de VTH software.
Bijhorende metadata worden in de Documentregistratiecomponent via de ZDS standaard of in het
Documentenregister via de Documenten API opgeslagen en kunnen door het VTH-systeem worden
bevraagd.
Eis
Eis 25
VTH041 Kunnen genereren van
brieven/besluiten aan indiener en
belanghebbende
Op verschillende momenten binnen diverse processen moeten brieven of besluiten kunnen worden
opgesteld voor een indiener of belanghebbende. De VTH software kan documenten aanmaken aan de
hand van vooraf gedefinieerde sjablonen in de huisstijl van de organisatie.
Eis
Eis 26
VTH042 Kunnen versturen van berichten
aan initiatiefnemer, indiener en
belanghebbende
De initiatiefnemer en eventuele specifieke belanghebbenden krijgen de stukken toegezonden of worden
uitgenodigd tot indienen van zienswijzen  (bv. informatieve of inhoudelijke brieven). Dit kan
bijvoorbeeld via e-mail, brief of Berichtenbox. Dit is afhankelijk van de wens van de aanvrager. Het is
wettelijk verplicht alle (gebruikelijke) kanalen hiervoor open te houden. Mogelijk dat deze berichten via
de Outputmanagementcomponent gestuurd worden, als de gemeente deze heeft.
Eis
Eis 27
VTH043 Kunnen afsluiten van het proces
opstellen van de (concept)beschikking
Na vaststelling door het bevoegde orgaan (met verwerking van eventuele aanpassingen), wordt het
document dat formeel is vastgesteld 'bevroren', waarmee een behandelingsfase is afgerond. Het kan
hierbij gaan om - Ontwerp beschikking omgevingsvergunning (college) - Ontwerp advies met
instemming (raad) - Definitieve beschikking omgevingsvergunning (college of gemandateerde
ambtenaar) - Definitief Advies met instemming (raad). In feite betreft het hier het afronden van een
processtap. Dit kan mogelijk leiden tot het aanpassen van een status van de zaak.
Eis
Wens 30
VTH045 Kunnen vastleggen van
resultaten van inhoudelijke toetsing van
de activiteiten
Bij de inhoudelijke toetsing worden de activiteiten waarvoor de vergunning wordt aangevraagd door het
bevoegd gezag vergeleken met de kaders van de geldende regelgeving. Daartoe wordt op alle relevante
deelgebieden van de regelgeving getoetst of het initiatief binnen de kaders blijft. De resultaten van de
toetsing kunnen in een risicogericht toetsingsprotocol worden vastgelegd.
Wens
Wens 31
VTH046 Kunnen laten accorderen van
de concept beschikking
Bij complexe en/of beleidsgevoelige vergunningaanvragen accordeert het College de
conceptbeschikking. Tevens wordt bepaald of advies aan de Gemeenteraad gevraagd zal worden. Het
daadwerkelijk accorderen wordt buiten het VTH-systeem gedaan. In feite betreft het hier het starten en
volgen van een processtap.
Wens
Eis 28
VTH049 Kunnen opstellen van een
concept beschikking
Op basis van de uitkomst van de integrale afweging wordt via de Documentcreatiecomponent een
concept voor de beschikking opgesteld (bij toepassing van de uitgebreide procedure spreken we van
'ontwerpbeschikking'). Hierin worden eventuele maatwerkvoorschriften opgenomen die de gemeente
wil verbinden aan het verlenen van de vergunning.
Eis
Wens 32
VTH054 Kunnen aangeven van een
risicoprofiel
Een risicoprofiel van de aanvraag (en de daarin aangevraagde activiteiten), op basis waarvan een
bijbehorende toetsings- en toezichtsprotocol van toepassing is waarin de diepgang overeenkomst met
het vastgelegde risicoprofiel.
Wens

## Page 68

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 67 van 102
VTH056 Kunnen bepalen en registreren van de te
volgen procedure
Uitgangspunt in de Omgevingswet is dat zowel voor binnenplanse als buitenplanse activiteiten de
reguliere procedure wordt gevolgd, tenzij sprake is van een bijzondere situatie. Van zo'n bijzondere
situatie kan sprake zijn op grond van internationaalrechtelijke verplichtingen (bijvoorbeeld de MER-
richtlijn of de Seveso-richtlijn), of als de aangevraagde activiteiten belangrijke nadelige gevolgen kunnen
hebben voor het milieu, of als er sprake is van een rijksmonumentenactiviteit.
Eis
Eis 29
VTH060 Kunnen controleren of de
aangevraagde of geconstateerde
activiteiten vergunningplichtig,
meldingplichtig of vergunningvrij zijn
Als aangevraagde activiteiten vergunningsvrij zijn, hoeft er geen behandeling te worden gestart.
Eis
Wens 33
VTH061 Kunnen ondersteunen in het
maken van een integrale afweging op
basis van verzamelde adviezen
Bij meervoudige/complexe zaken (VTH) zullen verschillende behandelaren en adviseurs input leveren.
De hoofdbehandelaar moet ondersteund kunnen worden om het overzicht te behouden bij de integrale
afweging, overwegingen en uiteindelijke resultaat van de integrale afweging. Bijvoorbeeld door vanuit
de deeltoetsingen (op hoofdlijnen) direct inzichtelijk te krijgen welke knelpunten er zijn en wat passend
is (en dus geen issue is). Dit kan dan direct de agenda voor de integrale afweging zijn.
Wens
Eis 30
VTH063 Kunnen opstellen van een
besluit
Afhankelijk van het aantal en de omvang van de zienswijzen en de complexiteit van de verwerking
daarvan kan de beantwoording van de zienswijzen opgenomen worden in het definitieve besluit of in
een separate nota van beantwoording zienswijzen. De oplossingen die tijdens de integrale afweging
gevonden zijn voor de eventuele geschilpunten uit de ingediende zienswijzen worden verwerkt in de
beschikking en daaruit wordt het definitieve besluit voor de aanvraag omgevingsvergunning opgesteld.
Tevens mogelijkheid om concreet aan te geven welke motivering in de tekst van de beschikking moet
worden opgenomen en welke voorschriften (indien van toepassing).
Eis
VTH064 Kunnen opstellen van een
toetsingsdocument
Een behandelaar toetst een activiteit binnen de VTH-zaak en moet de toetsing met het resultaat kunnen
vastleggen in een document. Het opstellen gebeurt via de Documentcreatiecomponent.
Wens
Wens 34
VTH069 Kunnen vastleggen van
afspraken met ketenpartners
Afspraken tussen de verschillende partners kunnen vastgelegd worden, zodat het proces goed
gecoördineerd verloopt en bij het opstellen van een besluit dit leidt tot een congruent geheel. De
afspraken kunnen vastgelegd zijn in de PDC Omgevingswet.
Wens
Wens 35
VTH070 Kunnen vastleggen van
samenhang met andere
procedures/besluitvorming
In sommige zaken is (positieve) besluitvorming randvoorwaardelijk om verder te kunnen gaan of om de
zaak af te kunnen ronden. Een voorbeeld: Een handhavingszaak kan worden afgerond als de overtreding
is opgeheven doordat de benodigde omgevingsvergunning is verleend.
Wens
Eis 31
VTH071 Kunnen genereren van
operationele rapportages (bv. overzicht
werkvoorraad, voortgang)
Voor de beheersing van de werkvoorraad, zowel op het niveau van een individuele medewerker als (een
onderdeel van) de organisatie, moeten periodiek rapportages kunnen worden gegenereerd. Verder
moeten rapportages kunnen worden gegenereerd voor monitoring van de resultaten van de uitvoering
als belangrijke informatie voor het opstellen van beleid en regelgeving. Ook het genereren van
managementrapportage valt hieronder.
Eis (m.u.v.
managementrap
portages)
Wens 36
VTH072 Kunnen genereren van
management rapportages
Om actief te kunnen sturen, ondersteunt de VTH software het kunnen genereren van rapportages ten
behoeve van het Managent. De VTH software biedt hiervoor een aantal voorgedefinieerde rapportages
(op basis van best practice).
Wens

## Page 69

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 68 van 102
Wens 37
VTH073 Kunnen samenstellen van eigen
rapportages
Bij de verschillende bevoegde gezagen zullen verschillende speerpunten of aandachtspunten zijn
vastgesteld voor de dienstverlening. Daarvoor moeten specifieke rapportages kunnen worden
opgesteld.
Wens
Wens 38
VTH075 Kunnen inplannen van
werkzaamheden
Om het team dat de vergunningaanvraag behandelt tijdig te kunnen voorzien van gevraagde adviezen is
het belangrijk om werkzaamheden aan de juiste medewerker(s) toe te wijzen en in te plannen in overleg
met de hoofdbehandelaar. Het Verzoek moet kunnen worden toegekend aan een (hoofd)behandelaar.
Deze is verantwoordelijk voor de verdere afhandeling van het Verzoek.
Wens
Eis 32
VTH079 Kunnen (flexibel) inrichten van
de werkprocessen
Afhandeling van zaken volgt lang niet altijd de 'happy flow' c.q. is lang niet altijd en lineair proces. Soms
moeten delen van het proces worden herhaald/opnieuw. Uitgangspunt is dat de hoofdbehandelaar
deskundig is, goed kan bepalen hoe het proces verder moet en daarbij dus flexibel keuzes kan maken.
Processen moeten dus slim modulair kunnen worden geïmplementeerd.
Eis
Eis 33
VTH080 Kunnen aanwijzen van
hoofdbehandelaar/behandelaren/advis
eurs
Een zaak moet kunnen worden toegewezen aan een specifieke medewerker als hoofdbehandelaar,
zodat de zaak in zijn/haar werkvoorraad wordt opgenomen en hij/zij de juiste rechten krijgt om de zaak
te afhandelen. Hetzelfde geldt voor behandelaren en adviseurs die worden gevraagd om specifieke
aspecten van de aanvraag te toetsen of daarop te adviseren.
Eis
Eis 34
VTH081 Kunnen bewaken van de status
van (interne en externe) adviesaanvraag
De hoofdbehandelaar van een zaak moet goed overzicht hebben over voortgang van de zaak. Daar hoort
bij dat de hoofdbehandelaar kan zien wat de voortgang is bij gevraagde adviezen (intern en extern) om
op tijd te kunnen zien of er een knelpunt in de planning van een zaak. Het totaaloverzicht van de
eindstatussen van de adviesvragen geeft een beeld op hoofdlijnen of er inhoudelijke knelpunten zijn en
daarop moet worden geschakeld.
Eis
Eis 35
VTH082 Kunnen bewaken van de status
van een zaak
Voor de monitoring van de bedrijfsvoering, zowel organisatiebreed als op individueel niveau, moeten de
statussen van de (lopende) zaken kunnen worden bijgehouden. Klant(en) hebben ook behoefte aan
inzicht in de voortgang van de eigen zaak. Afhankelijk van het type zaak, kan het daarbij gaan om een
aanvrager, overtreder en/of belanghebbende.
Eis
Eis 36
VTH083 Kunnen doen van
termijnbewaking zoals gedefinieerd
volgens de wet / conform eigen service
(instelbaar) termijnen
Aangezien de inhoudelijke toetsing belegd kan zijn bij diverse interne en externe adviseurs en
ketenpartners, is bewaken van de termijnen voor levering van de adviezen en/of instemmingen
noodzakelijk.
Eis
Eis 37
VTH086 Kunnen koppelen op basis van
de Standaard Zaak- en Documenten
Services
Voor het automatisch kunnen aanmaken en updaten van zaken, is een koppeling naar een Zaaksysteem
of Zakenregister nodig. Deze koppeling is gebaseerd op de huidige standaard en voldoet minimaal aan
de versie(s) zoals deze wordt beheerd door VNG Realisatie. Later wordt deze standaard Zaken API.
Eis
Eis 38
VTH087 Kunnen koppelen op basis van
de Standaard Zaakgericht Werken API
(ZGW API)
De nieuwe standaard Zaakgericht Werken API volgt de landelijke URI en API strategie. Deze nieuwe
standaard is gebaseerd op REST/JSON en wordt ingezet om geautomatiseerd Zaakgericht te kunnen
werken met informatiesystemen van gemeenten of uitvoeringorganisaties. Minimaal de versie(s) zoals
deze wordt beheerd door VNG Realisatie wordt hiervoor gebruikt.
Eis
Eis 39
VTH088 Kunnen koppelen van
documenten aan een Zaak in de
Zaakregistratiecomponent of in het
Zakenregister
De Zaakdocumenten die opgeslagen zijn in de Documentenregistratiecomponent, kunnen gekoppeld
worden aan de Zaak die is opgeslagen in de Zaakregistratiecomponent of het Zakenregister.
Eis

## Page 70

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 69 van 102
Wens 39
VTH089 Kunnen aanvragen van intern
advies
Inhoudelijk deskundige adviseurs kunnen vanuit de VTH software gevraagd worden om advies uit te
brengen in een VTH-zaak. De VTH software biedt hiervoor bijvoorbeeld de mogelijkheid tot het
versturen van een interne e-mail of gebruikt hiervoor een ander notificatiemechanisme.
Wens
Eis 40
VTH090 Kunnen agenderen van een
nieuwe (gerelateerde) zaak
De uitkomst van een zaak kan de aanleiding zijn om een andere zaak te starten. Bijvoorbeeld: de
behandeling van een melding van een incident kan als uitkomst hebben dat handhavend moet worden
opgetreden. Daarvoor moet dan een zaak worden gestart voor het opleggen van een sanctie. Deze
zaken moeten aan elkaar worden gerelateerd, zodat in de nieuwe zaak de voorgeschiedenis en
relevante informatie direct inzichtelijk is.
Eis
Eis 41
VTH091 Kunnen controleren op
bestaande (afgehandelde of lopende)
zaken (o.a. vergunning, toezicht,
handhaving, wijziging omgevingsplan)
Om te voorkomen dat er meerdere aanvragen of meldingen op hetzelfde object worden ingevoerd, is
inzage op eerdere ingediende of lopende zaken een hulpmiddel bij het beoordelen of de melding of
aanvraag in behandeling moet worden genomen.
Eis
VTH093 Kunnen registeren van een zaak
Het Verzoek wordt geregistreerd via de ZDS standaard in de Zaakregistratiecomponent of via de Zaken
API in het Zaakregister.
Functie van ZS-
DMS/RMA
VTH094 Kunnen relateren van een zaak aan één of
meer andere gerelateerde zaken
Verschillende zaken kunnen met elkaar samenhangen en dat moet voor een hoofdbehandelaar in één
oogopslag duidelijk zijn, inclusief de actuele status. Bijvoorbeeld: een melding incident leidt tot het
opleggen van een sanctie, waarbij toezicht wordt gehouden en uiteindelijk een sanctie wordt toegepast.
Dan zijn er vier zaken aan elkaar gerelateerd.
Functie van ZS-
DMS/RMA
Eis 42
VTH095 Kunnen samenwerken met
ketenpartners op basis van Zaakgericht
Werken
Zaakgericht werken is in het bestuursakkoord van 2015 als uitgangspunt vastgesteld voor de
samenwerking in de keten. De VTH software biedt de mogelijkheid via de Samenwerkfunctionaliteit van
het DSO-LV Zaakgericht te kunnen samenwerken. Dit geldt niet alleen voor planvorming en
vergunningverlening (via DSO-LV), maar ook voor toezicht en handhaving in de bestaande situatie (nog
niet via DSO-LV).
Eis
Wens 40
VTH096 Kunnen werken op basis van de
interbestuurlijke ZTC-Omgevingswet
Voor samenwerking in de keten is de randvoorwaarde dat zaakgericht wordt gewerkt op basis van de
interbestuurlijke ZTC-Omgevingswet, zodat de VTH-componenten het berichtenverkeer op de juiste
manier verwerken.
Wens
Eis 43
VTH099 Kunnen abonneren op en
ontvangen van notificaties van de
Samenwerkfunctionaliteit van het DSO-
LV
Door de Samenwerkfunctionaliteit worden notificaties gestuurd naar partners als er in de
Samenwerking iets is gewijzigd. Dit kan een uitnodiging voor een nieuwe samenwerking zijn, een
actieverzoek of een nieuwe status van het uitgezette actieverzoek of een notificatie als er een document
beschikbaar is gesteld in de Samenwerking.
Eis
Wens 41
VTH100 Kunnen opvragen, toevoegen,
wijzigen, verwijderen van rechten op
documenten in een Samenwerking in de
Samenwerkfunctionaliteit van het DSO-
LV
De VTH software moet rechten op documenten die in de Samenwerking worden gedeeld met partners
kunnen opvragen, toevoegen, wijzigen, verwijderen.
Wens

## Page 71

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 70 van 102
Eis 44
VTH101 Kunnen bevragen van gegevens
uit de lokale dan wel landelijke
Basisregistratie Adressen en Gebouwen
(BAG)
Adressen of gebieden (waar de aanvraag over gaat) die worden gebruikt in het Verzoek kunnen in de
Basisregistraties (zoals de BAG) bevraagd worden. Zo moet BAG (pand(-id) of vbo(-id)) opgehaald
kunnen worden en als relatie vastgelegd kunnen worden in het VTH systeem. Als er geen relatie is met
een bestaand BAG object dan moet een (tijdelijk) geometrie (punt of vlak) kunnen opnemen. Ook is het
wenselijk een BAG attribuut zoals status, bijvoorbeeld object in onderzoek of geconstateerd, op te
kunnen vragen. BAG beheerders geven aan welk nieuw verblijfsobject/adres gebruikt moet worden. Zo
kunnen deze adressen direct in het besluit opgenomen kunnen worden.
Eis
Wens 42
VTH102 Kunnen versturen van
notificaties aan andere systemen als er
gegevens in het VTH-systeem zijn
gewijzigd
Dit is nodig voor starten van BAG proces, verkrijgen brondocument (vergunning, bouwtekeningen, etc.)
voor de BAG, melding dat er een vergunning is verleend (gereedmelding), etc. Idealiter verloopt deze
notificatie via de Notificatierouteringcomponent.
Wens




## Page 72

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 71 van 102
2. Requirements Applicatiefunctie: Ondersteunen van aanvragen en meldingen
Requirement
Documentatie
Eis/Wens
(Uitvraag)
Eis 45
VTH010 Kunnen ontvangen van het
triggerbericht uit DSO-LV
De DSO-LV stuurt een triggerbericht dat er een Verzoek klaar staat. Dit bericht moet automatisch kunnen
worden ingelezen in het systeem op basis van de nieuwste standaard en zichtbaar zijn in ontvangen
Verzoeken. Het Bevoegd Gezag (of de Uitvoerende Instantie) kan het Verzoek doorsturen naar een ander
Bevoegd Gezag als zij concludeert dat het Verzoek niet juist is gerouteerd. Hiervoor wordt door het DSO-LV
een nieuw triggerbericht naar het nieuwe Bevoegd Gezag gestuurd, en indien van toepassing naar de nieuwe
uitvoerende instantie. Het nieuwe triggerbericht is identiek aan het oorspronkelijke bericht, behalve de
elementen heeftAlsVerantwoordelijkeVoorBehandeling en eventueel isUitbesteedVoorBehandelingAan. Aan
het verschil tussen de indienDatum en de berichtverzenddatum kan het nieuwe Bevoegd Gezag al
concluderen dat het om een doorgestuurd Verzoek gaat. Als het nieuwe Bevoegd Gezag het hele Verzoek
ophaalt ontvangt het de Verzoek XML met daarin de historieinformatie voor Bevoegd gezag en Uitvoerende
instantie. Het Verzoek wordt ingediend ten behoeve van vooroverleg (Vooroverleg), als start van het
behandelproces (Initiëren), als aanvulling op een eerder ingediend Verzoek (Aanvullen), of dat het Verzoek
wordt ingetrokken (Intrekken). Er zijn 7 soorten Type Verzoek onderkend in de Omgevingswet, veelal zijnde
een vergunningsaanvraag of melding: Aanvraag vergunning, Melding, Informatie, Informatie ongewoon
voorval, Aanvraag Maatwerkvoorschrift, Melding gelijkwaardige maatregel, Aanvraag toestemming
gelijkwaardige maatregel.
Eis
Eis 46
VTH011 Kunnen ophalen van het
Verzoek uit DSO-LV
Nadat er een triggerbericht is ontvangen, kan het Verzoek op basis van de nieuwste standaard (via de API
'Ophalen Verzoek') worden opgehaald uit het DSO-LV. Het Verzoek wordt ingediend ten behoeve van
Vooroverleg (Omgevingsoverleg), als start van het behandelproces (Initiëren), als aanvulling op een eerder
ingediend Verzoek (Aanvullen), of dat het Verzoek wordt ingetrokken (Intrekken).  Er zijn 7 soorten Type
Verzoek onderkend in de Omgevingswet, veelal zijnde een vergunningsaanvraag of melding: Aanvraag
vergunning, Melding, Informatie, Informatie ongewoon voorval, Aanvraag maatwerkvoorschrift, Melding
gelijkwaardige maatregel, Aanvraag toestemming gelijkwaardige maatregel.
Eis
Eis 47
VTH012 Kunnen ophalen van de bijlagen
bij het Verzoek uit het DSO-LV
Nadat er een triggerbericht is ontvangen, kunnen de bijlagen bij het Verzoek  op basis van de nieuwste
standaard worden opgehaald uit het DSO-LV (eveneens via de API 'Verzoek ophalen'). De documenten worden
vastgelegd in de Documentregistratiecomponent via de ZDS standaard of in het Documentenregister via de
Documenten API.
Eis
Wens 43
VTH014 Kunnen registreren van de
aanvraag of melding in het
Omgevingsloket
Als een aanvraag buiten het Omgevingsloket om, dus op papier, is ingediend, moet deze alsnog in het
Omgevingsloket geregistreerd worden, zodat de voorzieningen van het DSO, zoals de
Samenwerkfunctionaliteit, benut kunnen worden bij de verdere behandeling van de aanvraag. De VTH
software beschikt hiervoor over een dergelijke registratiefunctie.
Wens
Eis 48
VTH016 Kunnen aanbrengen van relatie
tussen DSO-LV Verzoeknummer met de
zaaknummer(s) van het betreffende
bevoegd gezag
Het zaaknummer bij een bevoegd gezag is een uniek nummer. Het DSO-LV Verzoeknummer is ook een uniek
nummer dat de aanvrager vanuit het Omgevingsloket heeft ontvangen.  Voor zowel aanvrager, bevoegd gezag
en alle betrokkenen bij de behandeling is het daarom noodzakelijk dat er een relatie kan worden gelegd
tussen het DSO-LV Verzoeknummer en het eigen interne zaaknummer (afkomstig van het Zaakregister), o.a.
voor heldere communicatie en goede koppeling naar andere gerelateerde zaken.
Eis

## Page 73

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 72 van 102
Eis 49
VTH017 Kunnen betekenisvol
overnemen van antwoorden op vragen
uit de vragenboom die meegestuurd zijn
in het Verzoek
De antwoorden bij de indieningsvereisten van de aanvrager geven al belangrijke informatie over
vergunningplichten in relatie tot de voorgenomen activiteiten. Dit is elementaire informatie bij de intake van
de aanvraag en de start van de behandeling.
Eis
Eis 50
VTH018 Kunnen ophalen van
indieningsvereisten uit het DSO-LV
Aanvragen moeten voldoen aan bepaalde indieningsvereisten. Om dit te kunnen toetsen moeten deze
indieningsvereisten opgehaald kunnen worden uit het DSO-LV.
Eis
Eis 51
VTH019 Kunnen doorsturen van het
Verzoek via DSO-LV naar ander bevoegd
gezag
Indien het Verzoek niet bij het juiste Bevoegd Gezag is ingediend, moet het Verzoek onverwijld kunnen
worden overgedragen aan een ander Bevoegd Gezag. Dit verloopt via het DSO-LV. Het koppelvlak die het
DSO-LV hiervoor beschikbaar stelt, wordt daarbij gebruikt.
Eis
Eis 52
VTH021 Kunnen overnemen van
begrippen uit de stelselcatalogus, met
een link daar naar toe
De relevante begrippen uit het Omgevingsplan zijn een belangrijke basis voor de behandeling van een VTH-
zaak. Deze begrippen zijn opgenomen in de stelselcatalogus en moeten voor de behandeling van de VTH-zaak
daaruit kunnen worden opgehaald. Ook bij de uitvoering van Toezicht en Handhaving is het gewenst om de
juiste begrippen te kunnen hanteren.
Eis
Wens 44
VTH026 Kunnen opvragen van de
gemeentelijke legesregeling
In de legesregeling zijn de berekeningsmethoden vastgelegd voor de activiteiten die binnen een aanvraag om
omgevingsvergunning kunnen worden aangevraagd. Om de leges voor een specifieke aanvraag te kunnen
berekenen, moet de regeling kunnen worden opgevraagd.
Wens
Eis 53
VTH027 Kunnen exporteren van
ontwerpbesluit ten behoeve van ter
inzagelegging
Ontwerpbesluiten moeten zowel analoog als digitaal ter inzage worden gelegd. In het VTH-systeem moet
aangegeven kunnen worden dat het een openbaar document is. Het daadwerkelijk publiceren van een
archiefwaardig document wordt niet door het VTH-systeem gedaan.
Eis
Eis 54
VTH044 Kunnen geheel of gedeeltelijk
buiten behandeling stellen van een
aanvraag
Een ingediend Verzoek moet geheel of gedeeltelijk buiten behandeling gesteld kunnen worden. Dit kan
voorkomen als er bijvoorbeeld voor het ingediende Verzoek geen vergunningsplicht is of als niet of in
onvoldoende mate aan de gestelde aanvraagvereisten is voldaan. Dit betreft de status van de zaak zetten via
de ZDS standaard in de Zaakregistratiecomponent of via de Zaken API in het Zaakregister.
Eis
Eis 55
VTH047 Kunnen laten toetsen van de
beschikking inclusief legesberekening
c.q. -beschikking
Bij eenvoudige vergunningaanvragen wordt op ambtelijk niveau besloten. Uit oogpunt van zorgvuldigheid is
het belangrijk de beschikking inclusief legesberekening c.q. -beschikking in elk geval door een tweede persoon
(een collega of teamleider) te laten toetsen.
Eis
Eis 56
VTH050 Kunnen opstellen van een
legesbeschikking
Op grond van de geldende legestarieven moet de aanvrager van een omgevingsvergunning leges betalen voor
de behandeling van de aanvraag. Het opleggen van de leges is een op zichzelf staande beschikking waartegen
bezwaar kan worden gemaakt. Het opstellen gebeurt via de Documentcreatiecomponent.
Eis
Wens 45
VTH051 Kunnen afhandelen van een
planschadeprocedure
Wanneer op basis van de toetsingsadviezen een planschaderisico geconstateerd wordt en er is geen
onderliggend plan of overeenkomst, is het afsluiten van een planschadeovereenkomst met de initiatiefnemer
wenselijk. Bij de inhoudelijke toetsing wordt ook onderzocht in hoeverre er planschaderisico bestaat. Mogelijk
dat hiervoor een deelzaak wordt gestart.
Wens
Eis 57
VTH057 Kunnen berekenen van leges op
basis van gemeentelijke legesregeling
Op grond van de vastgestelde legestarieven (berekeningsmethode) worden met behulp van specificaties
binnen de aanvraag (activiteiten, specifieke variabelen als bouwsom, vloeroppervlak) de verschuldigde leges
berekend voor de behandeling van een specifieke aanvraag.
Eis

## Page 74

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 73 van 102
Eis 58
VTH059 Kunnen controleren of de
aanvraag voldoet aan de
indieningsvereisten, of de
initiatiefnemer participatie heeft
georganiseerd en of alle noodzakelijke
bijlagen zijn aangeleverd
De indieningsvereisten voor aanvragen zijn gedeeltelijk landelijk en gedeeltelijk lokaal vastgesteld. Als
(essentiële) vereisten ontbreken, kan de aan vraag niet goed worden beoordeeld en kan er geen goed
afwegen besluit worden genomen op de aanvraag. Aanvragen die niet voldoen, kunnen daarom buiten
behandeling worden gesteld.
Eis
Eis 59
VTH062 Kunnen opstellen van een
advies
Inhoudelijk deskundige interne en/of externe adviseurs brengen een advies uit, waarin behalve de conclusie
of het past ook kan worden opgenomen welke aanpassingen aan het initiatief gedaan zouden kunnen worden
om het passend te maken. Ten behoeve van de integrale afweging moet kunnen worden aangegeven welke
knelpunten er zijn en wat passend is (en dus geen issue is). Dit vormt dan gelijk de input voor de agenda van
een gezamenlijke, integrale afweging.
Eis
Wens 46
VTH065 Kunnen opstellen van
verslagen/rapportages
De ingediende zienswijzen worden (tijdens een hoorzitting) besproken en een eindverslag wordt opgesteld.
Het verslag geeft een helder overzicht van de ingebrachte (bezwaar)punten met argumentatie.
Wens
Wens 47
VTH068 Kunnen samenstellen van
activiteiten tot een integraal besluit
De verschillende activiteiten worden (als deelzaken) in beginsel op zichzelf beoordeeld, waarna vervolgens
integrale afweging plaatsvindt. Uiteindelijk moet het geheel leiden tot één integraal besluit, waarbij
motiveringen van de verschillende activiteiten moeten worden samengevoegd en de integrale afweging wordt
toegevoegd.
Wens
Wens 48
VTH074 Kunnen agenderen van een
adviesvraag aan de Gemeenteraad
De Gemeenteraad heeft bij afwijkingen van het omgevingsplan adviesrecht maar geen instemmingsrecht.
Bovendien geldt dat een adviesvraag aan de Gemeenteraad geen reden is voor verlenging van de
proceduredoorlooptijd. Het is daarom zaak om de eventuele adviesaanvraag bij de Gemeenteraad vroegtijdig
te agenderen en zoveel mogelijk parallel uit te voeren met de verdere activiteiten in het proces. De
Gemeenteraad ontvangt de adviesaanvraag van het College en agendeert deze.
Wens
Eis 60
VTH076 Kunnen opschorten van de
beslistermijn
Conform art. 4.5 Awb stelt de gemeente een (redelijke) termijn voor het aanleveren van gegevens en
bescheiden: de beslistermijn wordt opgeschort tot de dag waarop de aanvraag is aangevuld of de gestelde
termijn daarvoor is verstreken.
Eis
Eis 61
VTH077 Kunnen sluiten van de aanvraag Als de behandeling van de vergunningaanvraag is overgedragen aan een ander bestuursorgaan, of wanneer de
vergunningaanvraag buiten behandeling is gesteld omdat er geen vergunningplicht is of omdat niet in
voldoende mate aan de aanvraagvereisten is voldaan, eindigt het bedrijfsproces na de intakefase.
Eis
Eis 62
VTH078 Kunnen verlengen van het
termijn van de te volgen procedure
In geval van instemming door andere bestuursorganen wordt de reguliere procedure verlengd met vier
weken. Bij enkel advies door andere bestuursorganen geldt deze verlenging niet. Ook bij Handhaving moet het
mogelijk zijn termijnen te kunnen verlengen.
Eis
Eis 63
VTH084 Kunnen instellen en bijhouden
van doorlooptijden gedurende het
aanvraagproces
Naast de wettelijke termijn, hanteren veel bevoegde gezagen servicetermijnen die korter zijn. Deze moeten
kunnen worden ingesteld en vervolgens moet per proces de doorlooptijd worden bijgehouden en behoeve
van rapportages.
Eis
Wens 49
VTH092 Kunnen doen van verzoek om
wijziging in omgevingsplan
Indien sprake is van een omgevingsvergunning voor een afwijkactiviteit waaraan geen termijn is verbonden,
dan moet binnen uiterlijk vijf jaar het omgevingsplan van de gemeente bijgewerkt worden zodat het met de
verleende omgevingsvergunning in overeenstemming is.
Wens

## Page 75

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 74 van 102
Eis 64
VTH097 Kunnen ontvangen van het
kopie-triggerbericht uit DSO-LV
Als Verzoeken door een andere (uitvoerende) organisatie dan het verantwoordelijke Bevoegd Gezag worden
uitgevoerd, dan gaat het originele triggerbericht naar die betreffende (uitvoerende) organisatie. Daarbij wordt
er een kopie-triggerbericht naar het Bevoegd Gezag gestuurd. De VTH software moet dit kopie-triggerbericht
kunnen ontvangen.
Eis
Eis 65
VTH098 Kunnen verwijderen van een
Verzoek uit de werkmap van het DSO-LV
Als het Verzoek volledig is afgehandeld, kan het Bevoegd Gezag de werkmap verwijderen in de DSO-LV. Dit
verwijderen staat los van het verzoek in mijn omgevingsloket van de indiener. Die staat nog in de zogenoemde
Projectmap.
Eis
Eis 66
VTH103 Kunnen verwerken van
meerdere activiteiten van hetzelfde
type in het Verzoek
In het Verzoek kunnen meerdere activiteiten van hetzelfde type worden opgenomen. Het VTH-systeem moet
deze verschillende activiteiten kunnen onderscheiden en kunnen verwerken.
Eis




## Page 76

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 75 van 102

3. Requirements Applicatiefunctie: Ondersteunen van toezicht
Requirement
Documentatie
Eis/Wens
(Uitvraag)
Eis 67
VTH003 Kunnen registreren van
(geconstateerd) naleefgedrag gekoppeld
aan (een) thema
Het is noodzakelijk om in een toezichts- of handhavingszaak het naleefgedrag te kunnen registreren en te
kunnen koppelen aan de thema's die zijn gecontroleerd om periodiek een goede risicoanalyse uit te kunnen
voeren.
Eis
Eis 68
VTH007 Kunnen doorsturen melding
incident naar ander bevoegd gezag of
een uitvoeringsorganisatie
Het kan voorkomen dat een incident onder regelgeving en/of bevoegdheid valt van een ander bevoegd gezag.
De melding incident moet dan kunnen worden doorgestuurd naar dat bevoegde gezag. Het kan ook
voorkomen dat een melding incident wel bij het juiste bevoegde gezag binnenkomt, maar dat binnen het
takenpakket van een uitvoeringsdienst valt. In dat geval moet het kunnen worden doorgestuurd naar die
uitvoeringsdienst.
Eis
VTH026 Kunnen opvragen van de gemeentelijke
legesregeling
In de legesregeling zijn de berekeningsmethoden vastgelegd voor de activiteiten die binnen een aanvraag om
omgevingsvergunning kunnen worden aangevraagd. Om de leges voor een specifieke aanvraag te kunnen
berekenen, moet de regeling kunnen worden opgevraagd.
Reeds genoemd
bij
Ondersteunen
van aanvragen
en meldingen
Eis 69
VTH052 Kunnen opstellen van een
proces-verbaal
Als een toezichthouder een overtreding constateert, moet de toezichthouder in tekst en beeldmateriaal
vastleggen en ondertekenen wat hij/zij heeft gezien, heeft besproken en met wie (overtreder, getuigen,
belanghebbenden, etc). Hieruit kan een formeel document - het proces-verbaal - worden gegenereerd.
Eis
Eis 70
VTH058 Kunnen categoriseren van
geconstateerde situatie/overtreding
m.b.t. landelijke handhavingsstrategie
Vanuit de Kwaliteitscriteria is de landelijk handhavingstrategie als handreiking vastgesteld voor landelijke
eenduidigheid in de uitvoering van toezicht en handhaving. Om de juiste sancties op te leggen en om de big-8-
cyclus goed sluitend te maken, is het noodzakelijk dat kan worden gemonitord en geanalyseerd wat bij de
uitvoering van toezicht (en handhaving) inhoudelijk wordt geconstateerd inclusief ernst en gedrag.
Eis
Eis 71
VTH066 Kunnen prioriteren van toezicht
op basis van lokaal uitvoeringsbeleid
Op basis van het uitvoeringsbeleid bepaalt het bevoegd gezag in welke volgorde toezicht wordt gehouden. De
prioritering kan gebeuren op basis van inspecties op thema's, onderwerpen en prioriteit.
Eis
Eis 72
VTH067 Kunnen prioriteren van de
geconstateerde overtredingen
Een bevoegd gezag bepaalt op basis van de prioriteiten in het uitvoeringsbeleid welke overtredingen wel of
niet worden opgepakt of in welke volgorde deze worden opgepakt. Bij de afweging biedt de VTH software de
mogelijkheid om bij de vastleggen te motiveren waarom overtreding niet, eerder of later wordt opgepakt.
Eis
4. Requirements Applicatiefunctie: Ondersteunen van handhaving
VTH058 Kunnen categoriseren van geconstateerde
situatie/overtreding m.b.t. landelijke
handhavingsstrategie
Vanuit de Kwaliteitscriteria is de landelijk handhavingstrategie als handreiking vastgesteld voor landelijke
eenduidigheid in de uitvoering van toezicht en handhaving. Om de juiste sancties op te leggen en om de big-8-
cyclus goed sluitend te maken, is het noodzakelijk dat kan worden gemonitord en geanalyseerd wat bij de
uitvoering van toezicht (en handhaving) inhoudelijk wordt geconstateerd inclusief ernst en gedrag.
Reeds genoemd
bij Toezicht

## Page 77

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 76 van 102
VTH065 Kunnen opstellen van
verslagen/rapportages
De ingediende zienswijzen worden (tijdens een hoorzitting) besproken en een eindverslag wordt opgesteld.
Het verslag geeft een helder overzicht van de ingebrachte (bezwaar)punten met argumentatie.
Reeds genoemd
bij
Ondersteunen
van aanvragen
en meldingen
VTH067 Kunnen prioriteren van de geconstateerde
overtredingen
Een bevoegd gezag bepaalt op basis van de prioriteiten in het uitvoeringsbeleid welke overtredingen wel of
niet worden opgepakt of in welke volgorde deze worden opgepakt. Bij de afweging biedt de VTH software de
mogelijkheid om bij de vastleggen te motiveren waarom overtreding niet, eerder of later wordt opgepakt.
Reeds genoemd
bij Toezicht
VTH068 Kunnen samenstellen van activiteiten tot
een integraal besluit
De verschillende activiteiten worden (als deelzaken) in beginsel op zichzelf beoordeeld, waarna vervolgens
integrale afweging plaatsvindt. Uiteindelijk moet het geheel leiden tot één integraal besluit, waarbij
motiveringen van de verschillende activiteiten moeten worden samengevoegd en de integrale afweging wordt
toegevoegd.
Reeds genoemd
bij
Ondersteunen
van aanvragen
en meldingen
VTH078 Kunnen verlengen van het termijn van de
te volgen procedure
In geval van instemming door andere bestuursorganen wordt de reguliere procedure verlengd met vier
weken. Bij enkel advies door andere bestuursorganen geldt deze verlenging niet. Ook bij Handhaving moet het
mogelijk zijn termijnen te kunnen verlengen.
Reeds genoemd
bij
Ondersteunen
van aanvragen
en meldingen



5. Requirements Applicatiefunctie: Ondersteunen van objecten en activiteiten

Requirement
Documentatie
Eis/Wens
(Uitvraag)
Eis 73
VTH001 Kunnen beheren van
leefomgevingsobjecten en -activiteiten
De fysieke leefomgeving verandert voortdurend, als gevolg van vergunningvrije, meldingsplichtige en
vergunningplichtige activiteiten. Dat moet voortdurend kunnen worden bijgehouden (monitoring) om cyclisch
of dynamisch te analyseren of de veranderingen in de fysieke leefomgeving passend zijn binnen de kaders die
in het omgevingsplan zijn vastgesteld (functies, omgevingswaarden, doelstellingen, etc).
Eis


## Page 78

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 77 van 102
6. Principes
Deze worden gebruikt om een bepaalde uitleg van de eisen te geven.

Nummer
Principe
Consequentie
GEMMA Principes
Deze principes zijn aanvullend aan de GEMMA requirements en gebaseerd op ‘Katern GEMMA Architectuurprincipes’ op
https://www.gemmaonline.nl/index.php/Overzicht_GEMMA_Architectuurprincipes
PR 1

Klanten hebben laagdrempelig toegang tot een actueel en correct
beeld van alle voor hen relevante gegevens waarover onze
organisatie beschikt.
Er ligt een koppeling naar het ‘Zaaksysteem’ zodat klanten de status van hun
aanvraag kunnen inzien;
Beschikbare informatie wordt ontsloten via de landelijke voorzieningen.
PR 2

Medewerkers hebben minimaal toegang tot dezelfde informatie als
klanten (voor zover dat relevant is voor de uitoefening van hun
taak).
Medewerkers van V,T en H kunnen de gegevens inzien;
Medewerkers van het KCC kunnen op hoofdlijnen de gegevens van de Zaak inzien,
welke zijn geüpdatet door het ICT-oplossing.
PR 3

Alle verzoeken van klanten die gevolgd moeten worden, worden
geregistreerd als zaak en wijzigingen in de status worden op een
centrale plaats geregistreerd.
Er is een koppeling met het ‘Zaaksysteem’ van de deelnemers.
PR 4

Medewerkers hebben alle voor hen relevante en toegankelijke
informatie over klanten beschikbaar, inclusief informatie over hun
contact met de gemeente en hun lopende en afgeronde zaken.
Er is een koppeling met het ‘Zaaksysteem’ van de deelnemers;
Er is een koppeling met de basisregistraties.
PR 5

Klanten wordt op relevante momenten gevraagd om hun
voorkeuren en specifieke wensen en daarmee wordt rekening
gehouden bij de diensten die worden geleverd.
Klanten kunnen hun (kanaal)keuze aangeven over de manier waarop met hen
gecommuniceerd wordt. Dit betekent dat er gebruik gemaakt moet worden van het
outputmanagementcomponent.
PR 6

Klanten wordt niet gevraagd naar gegevens die de organisatie zelf
al beschikbaar heeft of die toegankelijk zijn voor de organisatie
(m.u.v. gegevens om zichzelf te identificeren).
Er is een koppeling met de basis- en kernregistraties. Naar deze gegevens wordt
vanuit de ICT-oplossing verwezen.
PR 7

Digitale diensten voor klanten en medewerkers zijn toegankelijk
via verschillende apparaten, ook voor mensen met een
functiebeperking en waar nodig 24x7 beschikbaar
De ICT-oplossing is via verschillende kanalen te benaderen (desktop, laptop, tablet,
smartphone) afhankelijk van de behoefte en gevraagde functionaliteit. Dit kan per
doelgroep/medewerkers verschillen.

## Page 79

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 78 van 102
PR 8

Medewerkers worden gefaciliteerd in het digitaal aanbieden,
ontsluiten en bewerken van alle gegevens.
Relevantie documenten, notities, e.d., kunnen ontsloten worden naar en vanuit het
DMS van de deelnemers. Daarbij is het van belang dat deze documenten gekoppeld
worden aan een ‘Zaak’. Deze documenten kunnen ook door andere
medewerkers/partner opgevraagd worden, mits daarvoor de juiste autorisatie
aanwezig is.
PR 9

Handmatige invoer of uitwisseling van gegevens wordt zoveel
mogelijk voorkomen, met name als er sprake is van hoge volumes.
Gegevens worden niet overgetypt. De ICT-oplossing ondersteunt gegevensuitwisseling
met informatiesystemen van derden, gebruikmaken van uitwisselstandaarden en –
mechanismen (zoals REST/JSON API’s).
PR 10

Er zijn voorzieningen voor elektronische parafen en
handtekeningen beschikbaar voor medewerkers en klanten.
De ICT-oplossing is aangesloten op de voorziening zoals bijvoorbeeld ValidSign van
de deelnemende gemeente
PR 11

De voortgang van processen wordt digitaal bewaakt.
Per proces(stap) wordt de status bijgehouden en vastgelegd in het ‘Zaaksysteem’ van
de deelnemers. Per processtap vindt bewaking op afhandeltijden plaats, waarbij
actieve signalering naar medewerkers/partners of klanten wordt gebruikt.
PR 12

Alle toegang tot autorisatie-objecten wordt expliciet
geauthentiseerd en geautoriseerd, tenzij deze openbaar
toegankelijk zijn.
De ICT-oplossing voorziet in authenticatie mogelijkheden. Voor medewerkers wordt
aangesloten op de ActiveDirectory (ADFS) van de deelnemers. Voor
(ketensamenwerking) partners moet naar een passende oplossing gezocht worden.
PR 13

Alle toegang tot gevoelige gegevens wordt gelogd en regelmatig
beoordeeld.
De ICT-oplossing beschikt over een loggingfunctie, waarin wordt vastgelegd welke
personen, welke gegevens op welk moment met welke reden heeft geraadpleegd of
gemuteerd (opvoeren, muteren, verwijderen).
PR 14

Klanten wordt niet gevraagd naar gegevens die de gemeente zelf al
beschikbaar heeft of die eenvoudig toegankelijk zijn voor de
gemeente (en passen bij de doelbinding).
De ICT-oplossing is gekoppeld op en maakt gebruik van basis- en kernregistraties.
PR 15

De organisatie heeft een aantal kernregistraties ingericht voor
andere gegevens die breed binnen de organisatie worden gebruikt
(kerngegevens).
De ICT-oplossing is gekoppeld op en maakt gebruik van basis- en kernregistraties.
PR 16

Voor alle soorten gegevens is een bron aangewezen en afnemers
zorgen ervoor dat zij (direct of indirect) deze bron gebruiken voor
het raadplegen en muteren van deze gegevens.
De ICT-oplossing is aangesloten op basis- en kernregistraties waarvan verplicht
gebruik wordt gemaakt. Ook is bekend welke brongegevens bij
samenwerkingspartners staan waarvan gebruik wordt gemaakt.
PR 17

Verwijzen naar gegevens heeft de voorkeur boven kopiëren en
daarom wordt waar mogelijk alleen een verwijzing (URI) van de
hergebruikte gegevens opgenomen.
Er wordt zo weinig mogelijk gegevens gekopieerd. Er wordt gebruik gemaakt van
Linked Data, voor zover dat nu al mogelijk is.

## Page 80

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 79 van 102
PR 18

Er wordt aangesloten bij beschikbare landelijke of sectorale
voorzieningen voor de ontsluiting van specifieke open data zoals
PDOK voor geo-informatie.
De ICT-oplossing is aangesloten op de landelijke voorzieningen.
PR 19

Open data wordt ook kenbaar gemaakt op de daarvoor
beschikbare publicatiekanalen zoals dataoverheid.nl en het
Nationaal Georegister voor geo-informatie.
De ICT-oplossing is aangesloten op de landelijke voorzieningen.
Privacy Principes
PR 20
Een open en transparante verwerking van persoonsgegevens is
randvoorwaardelijk om te borgen dat betrokkenen geïnformeerd
en betrokken deelnemen aan de verwerking.
De ICT-oplossing beschikt over een loggingfunctie, waarin wordt vastgelegd welke
personen, welke gegevens op welk moment met welke reden heeft geraadpleegd of
gemuteerd (opvoeren, muteren, verwijderen). Deze gegevens kunnen opgevraagd
worden door de klant.
PR 21
Onderdeel van een transparante verwerking van persoonsgegevens
is het op de individuele basis mogelijk maken voor betrokkenen
om rechten ten aanzien van de verwerkte persoonsgegevens uit te
oefenen.
Indien een klant vraagt om zijn gegevens uit De ICT-oplossing te (laten) verwijderen,
dan is dit mogelijk. De interne werking van de ICT-oplossing ondervindt daar geen
hinder van.
PR 22
Met het verwerken van persoonsgegevens komt ook de plicht om
zorgvuldig met gegevens om te gaan en om passende maatregelen
te nemen om die gegevens te beschermen.
De ICT-oplossing heeft voldoende beveiligingsmaatregelen in zich, om misbruik van
gegevens te voorkomen.
Zaakgericht Werken Principes
PR 23
Alle deelnemers maakt bij de uitvoering van haar processen
gebruik van Zaakgericht Registreren.
De ICT-oplossing heeft een aansluiting op het ‘Zaaksysteem’ van de deelnemers.
Hierin worden de zaken geregistreerd en wordt de status van de zaken vastgelegd.
PR 24
Nieuwe aanvragen worden afgeleverd bij het juiste
Zaakafhandelcomponent.
De ICT-oplossing is een zaakafhandelcomponent. De melding of aanvraag wordt
aangeboden aan de ICT-oplossing, dat vervolgens de melding of aanvraag in
behandeling neemt.
PR 25
Het Zaakafhandelcomponent registreert en beheert de Zaak in het
Zaakregistratiecomponent.
De ICT-oplossing zorgt voor een registratie in het centrale, organisatiebrede
‘Zaaksystem’ van de deelnemers. Bij elke statuswijziging zorgt de ICT-oplossing
ervoor, dat de benodigde gegevens over de zaak worden bijgewerkt in het
‘Zaaksysteem’ van de deelnemers.
PR 26
Het Zaakafhandelcomponent registreert en beheert documenten
die bij een Zaak horen in het Documentregistratiecomponent.
De ICT-oplossing heeft een aansluiting op het ‘DMS’ van de deelnemers. Relevante
documenten worden in dit DMS opgeslagen. De ICT-oplossing maakt gebruik van dit
DMS en zorgt ervoor dat de documenten in relatie zijn gebracht met de ‘Zaak’ in het
‘Zaaksysteem’.

## Page 81

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 80 van 102
PR 27
De deelnemers gebruiken de laatste versie berichtenstandaarden
en koppelvlakstandaarden zoals deze door VNG Realisatie zijn
vastgesteld.
De ICT-oplossing gebruikt de laatste standaarden inzake het Zaakgericht Werken
volgens de GEMMA.
PR 28
De opdrachtgevers maken ieder gebruik van één
Zaakregistratiecomponent, één Documentregistratiecomponent en
één Zaaktypecatalogus.
De ICT-oplossing is geen ’Zaaksysteem’. Zaakgegevens en Zaakdocumenten worden
opgeslagen in daarvoor bestemde systemen.
Common Ground Principes
PR 29
De deelnemers volgen de 5 lagen structuur van de Common
Ground.
In de ICT-Oplossing is een scheiding aangebracht tussen de data-, de (web)services-,
de integratie-, processen- en interactielaag. Hierdoor is het mogelijk om andere
applicaties/kanalen toegang te verlenen tot de gegevens die de ICT-oplossing vastlegt
of registreert.
PR 30
Gegevensuitwisseling tussen informatiesystemen gebeurt op basis
van REST API’s.
De ICT-oplossing gebruikt en biedt koppelingen aan op basis van REST API’s voor
zover er geen andere landelijke koppelvlakstandaarden beschikbaar zijn.

## Page 82

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 81 van 102
Annex C
Begrippenlijst

BG
Bevoegd Gezag (gemeente, waterschap, provincie, rijk, en in bepaalde gevallen de VR)
Cloud
Cloud computing betreft het leveren van computingservices (servers, opslag, databases, netwerkfuncties, software,
analysefuncties en meer) via internet ('de cloud'). Deze zaken staan niet meer in de eigen ICT omgeving (‘on-premise’)
DMS/RMA
Document Management System/Records Management Application. Systeem voor het beheer van documenten ongeacht
de vorm en toegepaste techniek waarbij metadata is vastgelegd omtrent toegankelijkheid, beschikbaarheid,
vindplaats, zaaktype, resultaat, gevoeligheid en voortgang. Het document en de documentflow staan centraal.
DSO(-LV)
Digitaal Stelsel Omgevingswet (Landelijke voorzieningen)
GEMMA
GEMeentelijke Model Architectuur
ESB
Enterprise Service Bus
Ketenintegratie
De component die informatie-uitwisseling mogelijk maakt. Niet alleen aanvragen maar ook bijvoorbeeld adviezen, en
voor alle bevoegd gezagen en ketenpartners.
LRSO
Landelijke redactie standaardteksten omgevingsvergunning
NORA
Nederlandse Overheid ReferentieArchitectuur...

OD (RUD)
Omgevingsdienst (soms wordt benaming Regionale UitvoeringsDienst (RUD) nog gebruikt)
Omgevingsobject
Een object, via adres en/of xy-ccördinatoren adresseerbaar, waaraan kenmerken verbonden kunnen worden.
Objectregistratie
De centrale registratie van omgevingsobjecten en bijhorende gegevens
OW
Omgevingswet
PDC
Producten- en Diensten-Catalogus
PVS
Proces Volg Systeem: Systeem dat gebruiker door het proces leidt van het behandelen van een aanvraag of melding
vanaf het ontvangen van de aanvraag tot en met het sluiten van een zaak, waarna het vervolgens in het DMS/RMA
wordt gearchiveerd. Hierbij dient er aandacht te zijn voor termijnbewaking, rappelfunctie en een goede uitwisseling
met de collectieve componenten, zodat op efficiënte en effectieve wijze de procesafhandeling kan plaatsvinden.
RO
Het beleidsveld Ruimtelijke Ordening


VR
Veiligheidsregio
VTHA
Vergunning, Toezicht, Handhaving en Advies
WABO
Wet algemene bepalingen omgevingsrecht
Zaaksysteem (ZS)
Systeem ter ondersteuning van zaakgericht werken, waarbij een zaak is gedefinieerd als '… een samenhangende
hoeveelheid werk met een gedefinieerde aanleiding en een gedefinieerd resultaat waarvan kwaliteit en doorlooptijd
bewaakt moeten worden'.
ZTC
Zaaktypen Catalogus


## Page 83

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 82 van 102
Annex D

Overzichten Eisen, Specificaties en Wensen

1. Eisen
Eis 1
De meest recente PDC (van tijd tot tijd gewijzigd) maakt steeds onderdeel uit van de inrichting van de ICT-Oplossing. .................................................... 9
Eis 2
Ten minste de onderstaande vijftien (15) zaaktypen, overeenkomstig de landelijke ZTC, dienen standaard onderdeel uit te maken van de ICT-Oplossing. 9
Eis 3
Ten minste de onderstaande zes (6) aanvullende zaaktypen dienen aan de basisconfiguratie te worden toegevoegd en daarmee onderdeel uit te maken
van de ICT-Oplossing. ................................................................................................................................................................................................... 10
Eis 4
Ontwikkelingen t.a.v. blok 2 en 3 die hun weerslag hebben op procesondersteuning dienen na 2021 ingericht en ondersteund te worden. .................... 12
Eis 5
De ICT-Oplossing is in staat om adviezen bij een ketenpartner uit te zetten via DSO-LV door middel van de Samenwerkingsruimte (werkmap) of direct via
de Ketenintegratie als het oorspronkelijke verzoek niet via DSO-LV is ontvangen. In het PVS en/of Zaaksysteem van de ketenpartner wordt vervolgens
automatisch een zaak gestart. De Ketenintegratie geeft hier een terugkoppeling (alert/notificatie) op. De oplevering van het advies aan de aanvragende
ketenpartner verloopt eveneens via de Ketenintegratie, waarbij er via een notificatie wordt geattendeerd....................................................................... 18
Eis 6
De ICT-Oplossing volgt standaarden op de voet: binnen 6 maanden nadat een nieuwe (versie van een) standaard door een op de Nederlandse markt
verkrijgbaar softwareproduct wordt ondersteund, zal deze ook worden ondersteund door de ICT-Oplossing. Daarnaast ondersteunt de Leverancier - voor
zover nodig voor de integratie met applicaties van de Opdrachtgevers - ook ten minste de twee daaraan voorafgaande versies van die standaarden. ..... 30
Eis 7
Standaard services voor het ontsluiten en koppelen van Zaaksysteem (ZS) en Document Managementsysteem (DMS) zijn gebaseerd op StUF en CMIS. ... 33
Eis 8
De aansluiting op DSO-LV voldoet aan de specificaties zoals gepubliceerd op https://www.gemmaonline.nl/index.php/GAO_-_Koppelingen .................. 35
Eis 9
De ICT-Oplossing kan bij aanvang (bulk)data aanleveren ten behoeve van (lokale) datawarehouses/BI tools of gegevens sets. Hierbij is niet alleen de data
zelf van belang maar ook inzicht in het datamodel: De geleverde gegevens zijn duidelijk en inzichtelijk, bijv. door duidelijk beschreven kolommen in
tabellen en database-diagrammen/-views, en door bijgeleverde documentatie. De (bulk)data is niet limitatief en bevat alle velden en variabelen die door
de organisaties ingevoerd zijn/in te voeren zijn. De data wordt minimaal dagelijks aangeleverd, bijv. via nachtelijke batchjobs. .................................... 37
Eis 10
VTH002 Kunnen registeren van de beschikking ............................................................................................................................................................. 64
Eis 11
VTH004 Kunnen registreren van (inkomende) correspondentie ...................................................................................................................................... 64
Eis 12
VTH005 Kunnen registreren van een formeel, vastgesteld document ............................................................................................................................. 64
Eis 13
VTH006 Kunnen vastleggen en registreren beslissing/advies voor vervolg op basis van beoordeling geconstateerde situatie ......................................... 64
Eis 14
VTH008 Kunnen starten, stoppen, wijzigen en verwijderen van een samenwerking in de Samenwerkfunctionaliteit van het DSO-LV ................................ 64
Eis 15
VTH009 Kunnen uitzetten en ontvangen van actieverzoeken via de Samenwerkfunctionaliteit van het DSO-LV ................................................................ 64
Eis 16
VTH013 Kunnen opslaan en opvragen van documenten in de Samenwerkfunctionaliteit van het DSO-LV ......................................................................... 65
Eis 17
VTH020 Kunnen opzoeken van begrippen in de stelselcatalogus ................................................................................................................................... 65
Eis 18
VTH023 Kunnen opvragen van gegevens in het monumentenregister bij de Rijksdienst voor Cultureel Erfgoed .............................................................. 65
Eis 19
VTH024 Kunnen publiceren van een besluit via het officiële publicatiemechanisme (nu DROP, wordt later LVBB) ............................................................ 65
Eis 20
VTH030 Kunnen bevragen van gegevens in de basis- of kernregistraties ........................................................................................................................ 65

## Page 84

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 83 van 102
Eis 21
VTH031 Kunnen bevragen en wijzigen van gegevens in de Zaakregistratiecomponent of het Zakenregister .................................................................... 65
Eis 22
VTH032 Kunnen bevragen van gegevens in de Zaaktypecataloguscomponent of het Catalogusregister .......................................................................... 65
Eis 23
VTH034 Kunnen bevragen en wijzigen van gegevens in het Besluitenregister ................................................................................................................. 66
Eis 24
VTH036 Kunnen bevragen en wijzigen van gegevens in de Documentregistratiecomponent of het Documentenregister ................................................. 66
Eis 25
VTH041 Kunnen genereren van brieven/besluiten aan indiener en belanghebbende....................................................................................................... 66
Eis 26
VTH042 Kunnen versturen van berichten aan initiatiefnemer, indiener en belanghebbende ............................................................................................ 66
Eis 27
VTH043 Kunnen afsluiten van het proces opstellen van de (concept)beschikking ........................................................................................................... 66
Eis 28
VTH049 Kunnen opstellen van een concept beschikking ................................................................................................................................................ 66
Eis 29
VTH060 Kunnen controleren of de aangevraagde of geconstateerde activiteiten vergunningplichtig, meldingplichtig of vergunningvrij zijn .................... 67
Eis 30
VTH063 Kunnen opstellen van een besluit ..................................................................................................................................................................... 67
Eis 31
VTH071 Kunnen genereren van operationele rapportages (bv. overzicht werkvoorraad, voortgang) ................................................................................ 67
Eis 32
VTH079 Kunnen (flexibel) inrichten van de werkprocessen ............................................................................................................................................ 68
Eis 33
VTH080 Kunnen aanwijzen van hoofdbehandelaar/behandelaren/adviseurs .................................................................................................................. 68
Eis 34
VTH081 Kunnen bewaken van de status van (interne en externe) adviesaanvraag........................................................................................................... 68
Eis 35
VTH082 Kunnen bewaken van de status van een zaak ................................................................................................................................................... 68
Eis 36
VTH083 Kunnen doen van termijnbewaking zoals gedefinieerd volgens de wet / conform eigen service (instelbaar) termijnen ....................................... 68
Eis 37
VTH086 Kunnen koppelen op basis van de Standaard Zaak- en Documenten Services .................................................................................................... 68
Eis 38
VTH087 Kunnen koppelen op basis van de Standaard Zaakgericht Werken API (ZGW API) ............................................................................................... 68
Eis 39
VTH088 Kunnen koppelen van documenten aan een Zaak in de Zaakregistratiecomponent of in het Zakenregister ......................................................... 68
Eis 40
VTH090 Kunnen agenderen van een nieuwe (gerelateerde) zaak .................................................................................................................................... 69
Eis 41
VTH091 Kunnen controleren op bestaande (afgehandelde of lopende) zaken (o.a. vergunning, toezicht, handhaving, wijziging omgevingsplan) ............ 69
Eis 42
VTH095 Kunnen samenwerken met ketenpartners op basis van Zaakgericht Werken ...................................................................................................... 69
Eis 43
VTH099 Kunnen abonneren op en ontvangen van notificaties van de Samenwerkfunctionaliteit van het DSO-LV ............................................................. 69
Eis 44
VTH101 Kunnen bevragen van gegevens uit de lokale dan wel landelijke Basisregistratie Adressen en Gebouwen (BAG) ................................................. 70
Eis 45
VTH010 Kunnen ontvangen van het triggerbericht uit DSO-LV ....................................................................................................................................... 71
Eis 46
VTH011 Kunnen ophalen van het Verzoek uit DSO-LV .................................................................................................................................................... 71
Eis 47
VTH012 Kunnen ophalen van de bijlagen bij het Verzoek uit het DSO-LV ....................................................................................................................... 71
Eis 48
VTH016 Kunnen aanbrengen van relatie tussen DSO-LV Verzoeknummer met de zaaknummer(s) van het betreffende bevoegd gezag ............................ 71
Eis 49
VTH017 Kunnen betekenisvol overnemen van antwoorden op vragen uit de vragenboom die meegestuurd zijn in het Verzoek ...................................... 72
Eis 50
VTH018 Kunnen ophalen van indieningsvereisten uit het DSO-LV................................................................................................................................... 72
Eis 51
VTH019 Kunnen doorsturen van het Verzoek via DSO-LV naar ander bevoegd gezag...................................................................................................... 72
Eis 52
VTH021 Kunnen overnemen van begrippen uit de stelselcatalogus, met een link daar naar toe ...................................................................................... 72
Eis 53
VTH027 Kunnen exporteren van ontwerpbesluit ten behoeve van ter inzagelegging....................................................................................................... 72

## Page 85

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 84 van 102
Eis 54
VTH044 Kunnen geheel of gedeeltelijk buiten behandeling stellen van een aanvraag ..................................................................................................... 72
Eis 55
VTH047 Kunnen laten toetsen van de beschikking inclusief legesberekening c.q. -beschikking ...................................................................................... 72
Eis 56
VTH050 Kunnen opstellen van een legesbeschikking ..................................................................................................................................................... 72
Eis 57
VTH057 Kunnen berekenen van leges op basis van gemeentelijke legesregeling ............................................................................................................ 72
Eis 58
VTH059 Kunnen controleren of de aanvraag voldoet aan de indieningsvereisten, of de initiatiefnemer participatie heeft georganiseerd en of alle
noodzakelijke bijlagen zijn aangeleverd ........................................................................................................................................................................ 73
Eis 59
VTH062 Kunnen opstellen van een advies ..................................................................................................................................................................... 73
Eis 60
VTH076 Kunnen opschorten van de beslistermijn .......................................................................................................................................................... 73
Eis 61
VTH077 Kunnen sluiten van de aanvraag ....................................................................................................................................................................... 73
Eis 62
VTH078 Kunnen verlengen van het termijn van de te volgen procedure ......................................................................................................................... 73
Eis 63
VTH084 Kunnen instellen en bijhouden van doorlooptijden gedurende het aanvraagproces ........................................................................................... 73
Eis 64
VTH097 Kunnen ontvangen van het kopie-triggerbericht uit DSO-LV .............................................................................................................................. 74
Eis 65
VTH098 Kunnen verwijderen van een Verzoek uit de werkmap van het DSO-LV .............................................................................................................. 74
Eis 66
VTH103 Kunnen verwerken van meerdere activiteiten van hetzelfde type in het Verzoek ................................................................................................ 74
Eis 67
VTH003 Kunnen registreren van (geconstateerd) naleefgedrag gekoppeld aan (een) thema ............................................................................................ 75
Eis 68
VTH007 Kunnen doorsturen melding incident naar ander bevoegd gezag of een uitvoeringsorganisatie ......................................................................... 75
Eis 69
VTH052 Kunnen opstellen van een proces-verbaal ......................................................................................................................................................... 75
Eis 70
VTH058 Kunnen categoriseren van geconstateerde situatie/overtreding m.b.t. landelijke handhavingsstrategie ............................................................. 75
Eis 71
VTH066 Kunnen prioriteren van toezicht op basis van lokaal uitvoeringsbeleid .............................................................................................................. 75
Eis 72
VTH067 Kunnen prioriteren van de geconstateerde overtredingen ................................................................................................................................. 75
Eis 73
VTH001 Kunnen beheren van leefomgevingsobjecten en -activiteiten ............................................................................................................................ 76






## Page 86

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 85 van 102
2. Specificaties
Spec 1
De ICT-Oplossing voldoet aan de GEMMA-architectuur en kan de ‘Functionele schets VTH’ zoals weergegeven in Figuur 4 (inclusief bovenstaande
toelichting) invullen. ..................................................................................................................................................................................................... 14
Spec 2
De ICT-Oplossing biedt deelnemers die onderdeel uitmaken van ambtelijke samenwerkingsverbanden de mogelijkheid  om in een multi-tenant omgeving
dan wel in separate omgevingen per gemeente te werken. ............................................................................................................................................ 16
Spec 3
Ketenpartners kunnen digitaal (aan)vragen indienen bij een uitvoeringsorganisatie binnen de keten, inzage krijgen in opdrachten die binnen de keten
worden uitgevoerd dan wel in samenwerking met de ketenpartner. Relevante documentatie kan met uploaden en downloaden via de Ketenintegratie
uitgewisseld worden. Deze functionaliteit is uitsluitend toegankelijk voor geauthentiseerde partijen en ontsluit alleen functionaliteit en informatie
waarvoor de desbetreffende partij is geautoriseerd. De Ketenintegratie geeft voor ketenpartners zaakstatusinformatie weer, waaronder in elk geval de
stand van zaken in het proces, de behandelaar en de verzoeken om aanvullende informatie. ......................................................................................... 18
Spec 4
De Ketenintegratie kan volledige dossieroverdracht ondersteunen. Met andere woorden: naast procesgebonden documenten (archiefbescheiden) kan ook
het (volledige) zaakdossier en de erbij behorende metadata ten behoeve van de formele archiefplicht worden uitgewisseld. .......................................... 18
Spec 5
De Ketenintegratie heeft tezamen met het gekoppelde PVS en de Objectregistratie zowel administratieve als geo-zoekingangen naar objecten en de
daaraan gekoppelde zaken. .......................................................................................................................................................................................... 18
Spec 6
In de Ketenintegratie kan een gebruiker bij een aanvraag middels een selectie de gewenste bijlagen toevoegen aan de (advies)zaak. ............................. 18
Spec 7
De Ketenintegratie en de Objectregistratie bieden de mogelijkheid om de aanvrager en (medewerkers van) organisaties buiten de keten (externe
adviseurs, laboratoria etc.) toegang te geven tot specifieke dossiers. ............................................................................................................................. 18
Spec 8
De Ketenintegratie biedt duidelijk overzicht welke partijen zijn betrokken bij een zaak, ook als deze zich niet in de primaire keten bevinden. ............... 18
Spec 9
De ketenintegratie kan afgeronde zaken archiefwaardig overdragen, bijvoorbeeld van uitvoeringsorganisatie naar bevoegd gezag. Dit moet  op termijn
(uiterlijk voor 2024) ook een (common ground) functionaliteit zijn tussen de zaaksystemen/DMS-RMA’s. ...................................................................... 19
Spec 10
De ICT-Oplossing bevat een workflowmanagementcomponent waarmee de verschillende typen werkprocessen van de opdrachtgevers kunnen worden
ingericht. ...................................................................................................................................................................................................................... 19
Spec 11
De ICT-Oplossing beschikt over standaard werkprocessen die door de leverancier zijn geleverd en actueel worden gehouden als gevolg van
wetswijzigingen. Tot de standaard werkprocessen die de leverancier heeft ingericht, behoren in ieder geval de (basis)processen behorend bij de
regionaal afgesproken ZTC, opgenomen in deze aanbesteding. ..................................................................................................................................... 19
Spec 12
Indien een standaard werkproces door een wetswijziging verandert, moeten lopende zaken nog met het voorgaande werkproces, dat gebaseerd is op de
oude wetgeving, afgehandeld kunnen worden. .............................................................................................................................................................. 19
Spec 13
Documenten zijn digitaal te waarmerken, te ondertekenen en te annoteren tijdens het procesverloop. Vanuit het PVS is deze functionaliteit te initiëren,
feitelijke handeling vindt in het zaaksysteem of DMS plaats. .......................................................................................................................................... 19
Spec 14
Er dient bij de overheveling van (afgehandelde) zaakdossiers naar het DMS ten behoeve van de archiefplicht, controle- en correctieslagen in het PVS
mogelijk te zijn. ............................................................................................................................................................................................................ 19

## Page 87

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 86 van 102
Spec 15
Ten tijde van vernietiging van gegevens in het zaaksysteem, leidt dit ook tot een vernietiging van deze gegevens in de overige componenten van de ICT-
oplossing (Ketenintegratie en Objectregistratie) ............................................................................................................................................................ 19
Spec 16
De ICT-Oplossing kan geautomatiseerd, zowel als dataveld als in documenten, persoonsgegevens pseudonimiseren in de zin van artikel 32 lid 1 A AVG.
De brongegevens c.q. –documenten blijven hierbij in tact. ............................................................................................................................................. 20
Spec 17
De ICT-Oplossing ondersteunt tijdens het procesverloop het overstappen van een reguliere naar een uitgebreide (gefaseerde) aanvraag voor een
omgevingsvergunning. ................................................................................................................................................................................................. 20
Spec 18
De ICT-Oplossing bevat ten behoeve van de volledigheidstoets van een aanvraag checklists, conform de wettelijk geldende indieningsvereisten. De
leverancier onderhoudt deze lijsten en past deze bij wetswijzigingen onverwijld (uiterlijk binnen 2 maanden) aan. ........................................................ 20
Spec 19
De ICT-Oplossing biedt een integrale voorschriftenbibliotheek, welke (aan)gevuld kan worden via externe bibliotheken, met name met de content van
LRSO. Eventueel vanuit derde partijen als BRIS en SesomWeb. ........................................................................................................................................ 20
Spec 20
De ICT-Oplossing ondersteunt de veranderingen als gevolg van de aanstaande inwerkingtreding van de Wkb. ............................................................... 20
Spec 21
De ICT-Oplossing kan bij advieszaken de hierna gespecificeerde gegevens c.q. overzichten tonen. ................................................................................ 20
Spec 22
Resultaten uit toezicht moeten landen in het VTH systeem en direct in een sjabloon op te nemen zijn. .......................................................................... 21
Spec 23
De ICT-Oplossing is in staat de status van het uitvoeren van bestuursdwang, het voornemen tot het opleggen van c.q. het vorderen van een dwangsom
en gedogen te registreren. Geldt eveneens voor bezwaar en beroep en zienswijzen. ...................................................................................................... 21
Spec 24
Zaken kunnen ook starten vanuit (mobiel) toezicht, bijvoorbeeld bij een constatering of een klacht. De ICT-Oplossing maakt het daartoe mogelijk naast
zaakgericht ook locatiegericht te werken....................................................................................................................................................................... 21
Spec 25
Toezichtsprogramma’s zijn te plannen en prioriteren op basis van (combinaties van) kenmerken van inrichtingen. ........................................................ 21
Spec 26
Toezichtszaken zijn te plannen op basis van/te koppelen aan een financiële verantwoording en/of planning. ................................................................ 21
Spec 27
De ICT-oplossing is in te zetten als registratiemiddel (bundeling) bij bulkmeldingen. ..................................................................................................... 21
Spec 28
Met de ICT-Oplossing kan mobiel toezicht worden uitgeoefend met behulp van een portable device. Op locatie kan een medewerker hierdoor controle
uitvoeren, registreren en afhandelen. ............................................................................................................................................................................ 21
Spec 29
Een medewerker kan op locatie zelf een controle(zaak) aanmaken, als die nog niet is aangemaakt. Bijvoorbeeld naar aanleiding van een waarneming ‘in
het veld’. ...................................................................................................................................................................................................................... 21
Spec 30
Bij het aanmaken van een werkvoorraad kunnen de documenten en tekeningen geselecteerd worden die tijdens de controle op locatie beschikbaar
moeten zijn. Daarnaast moeten de contactgegevens van aannemers en constructeurs op locatie beschikbaar zijn en moet de status van
(bouw)tekeningen en andere documenten duidelijk te zien zijn. .................................................................................................................................... 21
Spec 31
Synchronisatie van de gegevens van een werkvoorraad c.q. van uitgevoerde controles moet op minimaal 4G-verbinding en WiFi werken. Om bandbreedte
te besparen heeft de gebruiker de keuze welke gegevens (bijv. hoeveelheid controles, wel/geen foto’s, tijdspanne) gesynchroniseerd moeten worden. . 21
Spec 32
Een controle moet offline uitgevoerd kunnen worden en de controlebevindingen worden automatisch gesynchroniseerd zodra er weer een
internetverbinding is. .................................................................................................................................................................................................... 21
Spec 33
Met de ICT-Oplossing moeten controlebevindingen op een (bouw)tekening vastgelegd kunnen worden zodat direct duidelijk is op welke locatie deze
betrekking hebben. Het gaat hierbij om ten minste een bevinding, een aantekening en één of meerdere foto's. ............................................................. 21

## Page 88

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 87 van 102
Spec 34
De ICT-Oplossing moet de controlelijsten van het integraal Toezicht Protocol (iTP van de vereniging Bouw-en Woningtoezicht Nederland) ondersteunen
voor wat betreft bouwen en slopen. Zodra er nieuwe versies van het iTP beschikbaar zijn, draagt de leverancier er zorg voor dat deze beschikbaar komen
in De ICT-Oplossing. ..................................................................................................................................................................................................... 22
Spec 35
De ICT-Oplossing ondersteunt controlelijsten die door de Opdrachtgevers zelf ontwikkeld en beheerd kunnen worden of van andere instanties afkomstig
zijn zoals van ODnl (Omgevingsdienst NL) voor bijvoorbeeld sloop en monumenten. Controlelijsten zijn ook tussen organisaties te delen binnen het
systeem. ....................................................................................................................................................................................................................... 22
Spec 36
De Landelijke HandhavingsStrategie (LHS) moet ondersteund worden. Dat houdt ten minste in dat de gekozen strategie als bedoeld in de
interventiematrix, per constatering vastgelegd kan worden en er verandering/opschaling mogelijk is, ook als dit later in het proces, bijvoorbeeld door
een juridisch medewerker, wordt vastgesteld. De (uiteindelijk) gekozen strategie (bijv B4) moet als data inzichtelijk in een monitoring kunnen worden
opgeleverd. .................................................................................................................................................................................................................. 22
Spec 37
Van de controle kan een automatisch gegenereerd controlerapport met bevindingen worden verkregen. In brieven die naar aanleiding van een controle
worden opgesteld, kunnen controlegegevens zoals bezoekdatum en controleresultaat automatisch verwerkt worden. ................................................... 22
Spec 38
De ICT-Oplossing is in staat om genomen besluiten te registreren. Van de besluiten kunnen minimaal de hierna opgesomde gegevens worden
geregistreerd. ............................................................................................................................................................................................................... 22
Spec 39
Voor bouw: voorwaarden die gesteld worden bij vergunningverlening dienen in de ICT-Oplossing geregistreerd en bewaakt te worden. Toelichting: het
gaat hier onder andere om constructiegegevens. ........................................................................................................................................................... 22
Spec 40
Na definitieve besluitvorming en het sluiten van de zaak moet de ICT-Oplossing via de koppeling de gegevens van de betreffende zaak in het
Zaaksysteem kunnen vergrendelen (freeze), zodat documenten en metadata niet meer gewijzigd kunnen worden door de gebruikers, m.u.v. een
recordsmanager............................................................................................................................................................................................................ 22
Spec 41
Het publiceren van kennisgevingen en bekendmakingen naar DROP moet vanuit de ICT-Oplossing met behulp van sjablonen ondersteund worden zodat
een vergunningverlener dit eenvoudig zelf kan doen. .................................................................................................................................................... 22
Spec 42
De ICT-Oplossing heeft een door de applicatiebeheerder aanpasbare rekenmodule voor leges. ...................................................................................... 22
Spec 43
De ICT-Oplossing ondersteunt meerdere legesverordeningen van meerdere gemeenten (multi-tenant). .......................................................................... 22
Spec 44
De legesmodule van de ICT-Oplossing moet de hierna gespecificeerde typen legesartikelen ondersteunen. .................................................................... 22
Spec 45
De ICT-Oplossing kan vastleggen gedurende welke periode een legesverordening geldig is. .......................................................................................... 23
Spec 46
Alleen een daartoe geautoriseerde medewerker (applicatiebeheerder) kan de parameters voor legesberekeningen aanpassen. ....................................... 23
Spec 47
De ICT-Oplossing levert de CBS W011 export (= opgave gegevens verleende omgevingsvergunningen bouwen, bouwkosten > € 50.000,-), volgens het
format van het CBS). ..................................................................................................................................................................................................... 23
Spec 48
De ICT-Oplossing heeft een eigen interne sjabloonapplicatie voor het maken van standaardbrieven. .............................................................................. 23
Spec 49
Er bestaat de mogelijkheid om de ICT-Oplossing te koppelen met sjablonengeneratoren die verbonden zijn met de Kantoorautomatisering van
opdrachtgevers. Voorbeelden van gangbare documentgeneratoren zijn iWriter, SmartDocuments en Xential. ................................................................. 23
Spec 50
De ICT-Oplossing is in staat om het zaaknummer (kenmerk), NAW-gegevens, referenties en datums uit het gekoppelde zaaksysteem op te halen en in te
voegen in de standaardbrieven. .................................................................................................................................................................................... 23

## Page 89

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 88 van 102
Spec 51
De ICT-Oplossing is in staat om zelf te kiezen variabelen en velden toe te voegen aan standaardbrieven. ....................................................................... 23
Spec 52
De ICT-Oplossing is in staat om tekstblokken toe te voegen aan standaardbrieven, afhankelijk van een voorwaarde (als-dan constructie). ...................... 23
Spec 53
De ICT-Oplossing is in staat om de huisstijl van de betreffende opdrachtgevers toe te passen op de door het systeem gegenereerde standaardbrieven. . 23
Spec 54
De ICT-Oplossing is in staat om wijzigingen van de huisstijl op één plaats te beheren. ................................................................................................... 23
Spec 55
De ICT-Oplossing is in staat om standaard tekstblokken in meerdere sjablonen te kunnen gebruiken. ........................................................................... 23
Spec 56
De ICT-Oplossing is in staat om metadata van de standaardbrieven uit te wisselen met de metadata van het document in het gekoppelde
Zaaksysteem/DMS-RMA. ................................................................................................................................................................................................ 23
Spec 57
De Objectregistratie kent een logische gelaagdheid van registratie: object/locatie – activiteiten – voorzieningen, of direct: object/locatie – voorzieningen.
Onder de Omgevingswet kan dit een model worden als: activiteitstype – activiteiten – kenmerken. De lijst van activiteiten is gelijk aan de activiteiten
zoals die gedefinieerd zijn in het DSO-LV. ..................................................................................................................................................................... 24
Spec 58
De Objectregistratie levert van de objecten een integraal beeld op. Dat wil zeggen dat de Objectregistratie activiteiten koppelt aan een object/locatie, die
door verschillende ketenpartners worden afgehandeld als één geheel. De verantwoordelijke binnen de keten heeft exclusief mutatierechten (beheer) op
eigen te behandelen activiteiten en kan deze rol overdragen aan een andere ketenpartner. Een ketenpartner heeft hiertoe standaard alleen toegang tot de
objecten/locaties waar de ketenpartner Bevoegd Gezag is of de aangewezen uitvoeringsorganisatie is. Betreffende ketenpartner kan aan een
object/locatie wel een andere ketenpartner toegang verlenen, bijv. bij een object op de grens van twee gemeenten....................................................... 24
Spec 59
De Objectregistratie volgt statusgewijs de VTH-processen, ofwel: bij een object zijn hierna gespecificeerde statussen minimaal te onderscheiden. ........ 24
Spec 60
NAW-gegevens zijn tussen de objecten en de zaken te synchroniseren, binnen de ICT-oplossing óf met het generieke zaaksysteem. ............................. 25
Spec 61
Gegevens(velden) en statussen in de Objectregistratie zijn te vullen vanuit de processen/workflows in het gekoppelde PVS. Dit geldt eveneens voor
additionele gegevens(velden), die later op verzoek van de opdrachtgevers zijn toegevoegd. Waarbij deze additionele gegevensvelden per opdrachtgever
in het datamodel in te passen zijn, en niet als zgn. vrije velden worden toegevoegd. ..................................................................................................... 25
Spec 62
De Objectregistratie kan relationele verbanden leggen tussen objecten op één locatie of dicht bij elkaar gelegen, met globaal dezelfde of vergelijkbare
activiteiten, maar wel met verschillende eigenaren/drijvers/Kamer van Koophandel-inschrijvingen. Met name voor toezicht, maar soms ook voor
vergunningverlening, moeten deze als één object te benaderen zijn. ............................................................................................................................. 25
Spec 63
De ICT-oplossing is in staat een adres te herkennen als een adres met de aanwezigheid van een Rijksmonument of een Gemeentelijk Monument dan wel
een Karakteristiek pand en legt dit vast in de Objectregistratie. ..................................................................................................................................... 25
Spec 64
Kadastrale gegevens (BRK) worden geïmporteerd in de Objectregistratiecomponent van de ICT-Oplossing via de Landelijke Voorziening of het
gemeentelijk beheersysteem. ........................................................................................................................................................................................ 25
Spec 65
Gegevens in de Objectregistratie zijn direct uit het systeem te halen voor gebruik in andere toepassingen  van de opdrachtgevers, bijvoorbeeld via GEO
(WMS/WFS) en als ruwe data. Dit staat los van de monitoring in het kader van de beleidscyclus (Big8). Voor operationele taken moeten soms ook analyses
gemaakt worden op basis van gegevens uit objectdossiers. Voor de minder complexe vraagstukken is dit zelfstandig mogelijk. .................................... 25
Spec 66
De ICT-oplossing voorziet in de mogelijkheid de volgende gevoeligheden vast te leggen: .............................................................................................. 25
Spec 67
Locatie moet aangemaakt kunnen worden zonder (directe) aanleiding in de vorm van een verzoek. De informatie moet geborgd kunnen worden zonder
‘harde’ melding of klacht, maar bijvoorbeeld op basis van een waarneming of mutatie in derde systemen, zoals de basisregistraties. ............................ 25

## Page 90

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 89 van 102
Spec 68
De ICT-oplossing ondersteunt gedurende de looptijd van de overeenkomst het hier geschetste model, inclusief de onderlinge relaties, of landelijke
ontwikkelingen in dit model. ......................................................................................................................................................................................... 32
Spec 69
Te allen tijde is traceerbaar wat versie/actualiteit van achterliggende gegevens, datalijsten en bronnen zijn. Denk aan SBI codes, RAV codes, tabellen
activiteitenbesluit, gebruikersnamen, et cetera. ............................................................................................................................................................. 33
Spec 70
Bij stappen in het proces waar een gegevensbron wordt geraadpleegd, ingevoerd of gewijzigd, vindt altijd verificatie plaats en is er de mogelijkheid een
nul- of dummywaarde in te voeren of te kiezen, zodat gebruiker altijd bewust/verplicht een keuze maakt en daarmee de invoer traceerbaar en
rapporteerbaar is. ......................................................................................................................................................................................................... 33
Spec 71
De ICT-Oplossing zal alle ongestructureerde informatie, zijnde de documenten in een zaakdossier van de ICT-Oplossing, aanbieden aan de functionaliteit
voor het beheer van documenten en dossiers (Document Management Systeem, Records Management Systeem) van een Opdrachtgever o.b.v. de Zaak- en
Documentservices. Vice versa is het mogelijk om ongestructureerde informatie die voor de ICT-Oplossing relevant is, maar die niet binnen de ICT-
Oplossing is gecreëerd, beschikbaar te maken binnen de ICT-Oplossing. Voor deze koppeling is het Toepassingskader Metadatering Lokale Overheid
(TMLO) het uitgangspunt. ............................................................................................................................................................................................. 34
Spec 72
De ICT-oplossing realiseert de aansluitingen op Zaaksystemen en/of DMS-RMA op de beschreven wijze, met dien verstande dat de leverancier de stekker
‘levert’, en de derde partij de ‘contrastekker’ ................................................................................................................................................................ 34
Spec 73
De ICT-oplossing dient aan te sluiten op een aantal vooraf gespecificeerde ESB- of data-distributievoorzieningen, met dien verstande dat de leverancier
de stekker ‘levert’, en de derde partij de ‘contrastekker’ ............................................................................................................................................... 34
Spec 74
De ICT-Oplossing zal integreren met de decentrale functionaliteit voor kantoorautomatisering (Microsoft Office-applicaties) en decentrale
printvoorzieningen. ...................................................................................................................................................................................................... 34
Spec 75
De ICT-Oplossing kan voor elke procesgang (zaak) de identificerende zaak- en/of productinformatie aan het Tijdverantwoordings- en/of
Planningssysteem van een Opdrachtgever leveren, zodat tijd kan worden verantwoord ‘per zaak’ of in te zetten resources kunnen worden
geprognotiseerd. .......................................................................................................................................................................................................... 34
Spec 76
De ICT-Oplossing zal de financiële transacties (ten minste: te incasseren leges, optioneel: te vorderen of te betalen dwangsommen, te vorderen kosten,
te betalen producten en diensten, et cetera) voor een Opdrachtgever moeten kunnen genereren op een wijze die door het financiële systeem van de
Opdrachtgever geautomatiseerd kan worden verwerkt, bijvoorbeeld op basis van StUF-FIN. ........................................................................................... 35
Spec 77
De ICT-Oplossing integreert met de huidige en toekomstige landelijke publicatievoorzieningen, zoals Decentrale Regelgeving en Officiële Publicaties en
toekomstige voorzieningen binnen het Digitaal Stelsel Omgevingswet voor het kenbaar maken van individuele (bijv. zaakspecifieke) of collectieve
informatie, zoals  plannen, verordeningen, besluiten. .................................................................................................................................................... 35
Spec 78
De ICT-Oplossing draagt er zorg voor dat alle voor IvM benodigde gegevens binnen de ICT-Oplossing kunnen worden bijgehouden en geautomatiseerd
worden geëxporteerd naar het stelsel van Inspectieviews. ............................................................................................................................................. 35
Spec 79
De ICT-Oplossing – specifiek het PVS – is gekoppeld aan het BIS dat bij de ODZOB en een groeiend aantal gemeenten in gebruik is c.q. wordt genomen,
dit betreft (de meest recente versie van) Squit iBis van Roxit. ......................................................................................................................................... 35
Spec 80
De ICT-Oplossing integreert met minimaal de volgende basisregistraties: NHR, BAG, BGT, BRO en BRP ........................................................................... 36

## Page 91

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 90 van 102
Spec 81
De oplossing is een Cloud applicatie, door of onder beheer van de leverancier gehost en met een absoluut minimum aan onderdelen  on-premise bij de
afnemers, in ieder geval geen componenten on-premise die een directe interface met de standaard gebruikers bieden. ................................................. 37
Spec 82
De leverancier zorgt voor een backup- en restore mogelijkheid binnen de ICT-Oplossing, die minimaal voldoet aan de hier opgenomen uitgangspunten –
vast te stellen in de na gunning op te leveren SLA. ........................................................................................................................................................ 37
Spec 83
De backup/restore voorziening voldoet aan de Baseline Informatiebeveiliging Overheid (BIO) “of gelijkwaardig”. ............................................................ 37
Spec 84
Authenticatie aan de applicatie(s) is geïntegreerd met de lokale authenticatievoorziening van de afnemers. Indien deze is gebaseerd op Microsoft Active
Directory, op basis van ADFS versie 3.0 of hoger of Azure Active Directory. Voor specifieke situaties waar ADFS geen optimale situatie oplevert is een
alternatieve authenticatiemethode voorhanden. ............................................................................................................................................................ 37
Spec 85
Er zijn rollen beschikbaar in de ICT-Oplossing die de juiste rechten verlenen aan alle gebruikers en beheerders van het systeem. .................................. 37
Spec 86
De ICT-Oplossing kan door elke medewerker op onderdelen naar eigen behoefte ingedeeld worden. Medewerkers kunnen zelf de opbouw van schermen
beïnvloeden, zoals de te tonen velden en de indeling en breedte van kolommen. Deze instellingen worden ook opgeslagen. Medewerkers kunnen
knoppen wel of niet tonen. ........................................................................................................................................................................................... 37
Spec 87
De ICT-oplossing ondersteunt het gebruik van twee beeldschermen (functie “uitbreiden” in Windows). Hierbij maakt de applicatie logisch gebruik van
browsertabbladen, groepering van tabbladen en van een minimum aan pop-up browserschermen. ................................................................................ 38
Spec 88
Ondersteuning dient er te zijn voor gangbare browsers. Ten tijde van de gunning zijn dat Mozilla Firefox, Google Chrome en Microsoft Edge (Chromium
based). Leverancier is verantwoordelijk voor continue ondersteuning van de oplossing onder de laatste drie (3) hoofdversies van de browsers. De
afnemers zijn verantwoordelijk voor het aan de eindgebruikers ter beschikking stellen van deze versies. ....................................................................... 38
Spec 89
De webapplicaties werken conform de laatste courante HTML standaarden (HTML5 of hoger) en kennen geen afhankelijkheden van 3rd party of eigen
plug-ins (Java, Adobe Flash, Silverlight, et cetera), tenzij dit toegevoegde waarde biedt voor de integratie met lokale (kantoorautomatisering-)applicaties,
bijvoorbeeld Office plug-ins ten behoeve van Outlook-integratie. Zie ook standaarden. .................................................................................................. 38
Spec 90
Informatie met een Geo-component moet (ook) op een kaart binnen ICT-oplossing en eventueel aanvullende mobiele toepassing (bijvoorbeeld app)
getoond worden.  Denk hierbij aan het tonen van de historie, van verleende vergunningen, toezicht en handhavingszaken, op BAG objecten
(verblijfsobject, pand, stand- en ligplaats). .................................................................................................................................................................... 38
Spec 91
Kaartlagen binnen de ICT-oplossing zijn te ontsluiten in andere Geo/GIS-toepassingen. Omgekeerd zijn eigen Geo/GIS-kaartlagen in de ICT-oplossing te
tonen, gebruik makende van in de GEO wereld geldende standaarden (zoals WMS/WFS standaard). ............................................................................... 38
Spec 92
Het systeem dient ook autonoom te kunnen functioneren. Concreet, bij (incidentele) uitval van een koppeling naar een Zaaksysteem en/of DMS, dient de
voortgang van de verwerking niet in gevaar te komen. .................................................................................................................................................. 38
Spec 93
De ICT-Oplossing heeft de hierna opgenomen non-functionele specificaties bij mobiel gebruik (mobiel toezicht) ........................................................... 38




## Page 92

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 91 van 102
3. Wensen en Doorontwikkeling
Wens 1
In de basis wordt de inrichting van de zaaktypen overgenomen zoals de landelijke ZTC deze kent. Het kan echter zijn dat er per deelnemende organisatie
andere eisen  bestaan voor lokale aanpassingen (de zgn. Coulour Locale). De ICT-Oplossing ondersteunt dit bij de hier opgenomen elementen. ............ 10
Wens 2
Er is sprake van een directe overdracht van Vergunningverlening naar Toezicht & Handhaving tussen organisaties, met name van Bevoegd Gezag naar
uitvoeringsorganisaties. ................................................................................................................................................................................................ 19
Wens 3
Het is mogelijk om e-formulieren te koppelen, inclusief het opstellen van en verwerken van de output van vragenbomen. ............................................. 19
Wens 4
Er is sprake van een centraal binnenkomend kanaal met signalering indien niet op tijd geacteerd wordt, waar dan ook in de keten. ............................... 19
Wens 5
Op het gebied van metadata kan de ICT-Oplossing aanvullende gegevens registreren, zoals hier opgenomen: ............................................................... 20
Wens 6
Tijdens de procesafhandeling van bijvoorbeeld een bouw- of een inritvergunning kan in het PVS een stap worden opgenomen waarbij een BAG- of een
BGT-bericht (door middel van bijv. een geautomatiseerde mail) wordt gestuurd naar de betreffende beheerder bij een regiogemeente ter actualisatie van
de basisregistratie. ....................................................................................................................................................................................................... 20
Wens 7
De vergunningverlener kan adviezen die extern worden afgehandeld via de ICT-Oplossing (en eventueel DSO-LV) uitzetten, volgen en weer ontvangen.. 20
Wens 8
De ICT-Oplossing biedt de mogelijkheid BIBOB informatie op te vragen en te verwerken. ............................................................................................... 20
Wens 9
De ICT-Oplossing ondersteunt mogelijkheden om vervolgacties en monitoring in te plannen ......................................................................................... 21
Wens 10
(Basis-)Gegevens over inrichtingen moeten ter plekken kunnen worden aangepast in de tablet en daarmee automatisch geregistreerd in de
Objectregistratie. .......................................................................................................................................................................................................... 22
Wens 11
Controlelijsten zijn ‘slim’ en/of te filteren, bijv. op basis van de activiteiten van een bedrijf komen de juiste vragen (als eerste) naar voren en hoeft niet
een volledige lijst te worden doorlopen. ........................................................................................................................................................................ 22
Wens 12
De Objectregistratie kent ook een status om informatie (vanuit derde systemen) te verwerken die niet via het ‘reguliere’ VTH proces binnenkomt. In het
PVS kunnen dergelijk informatiestromen als een eenvoudige toezichtszaak (geautomatiseerd) verwerkt en daarmee gearchiveerd worden. .................... 25
Wens 13
Voor wat betreft zaakgerelateerde informatie volgt de Objectregistratie het gekoppelde PVS en het Zaaksysteem/DMS-RMA ten behoeve van
documentmanagement en archieffunctionaliteit. ........................................................................................................................................................... 25
Wens 14
Ten behoeve van de gegevenskwaliteit kan de Objectregistratie in bulk gegevens verifiëren en hierover rapporteren en benodigde correcties
voorbereiden.  Voorbeeld: voor alle locaties van een industrieterrein in één keer de NHR- en BAG-gegevens checken, eventueel in combinatie met een
bulkcontrole (‘gevelcontroles’) via (mobiel) toezicht. Afwijkingen kunnen vervolgens administratief, en mogelijk ook zaakgericht, verwerkt worden. ..... 25
Wens 15
De Objectregistratie biedt een logische registratiewijze van objecten (inrichting – activiteiten – voorzieningen) en sluit hierbij in de toekomst aan op de
wijze van registratie onder de Omgevingswet/DSO en/of een nog te ontwikkelen landelijke standaard. ......................................................................... 25
Wens 16
De ICT-Oplossing zal alle binnen de ICT-Oplossing bijgehouden objectgegevens waarvoor een Opdrachtgever formeel bronhouder is, als
Informatieproduct leveren aan het Digitaal stelsel Omgevingswet. De ICT-Oplossing zal alle gegevens die relevant zijn voor de uitoefening van de
(wettelijke) taken van Opdrachtgevers als Informatieproducten betrekken uit het Digitaal Stelsel Omgevingswet. ........................................................... 35

## Page 93

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 92 van 102
Wens 17
In gevallen waarin een Opdrachtgever deze integratie met eigen functionaliteit, bijvoorbeeld met het eigen zaaksysteem, wenst te realiseren, ondersteunt
de ICT-Oplossing deze integratie maximaal. Bijvoorbeeld door de inhoudelijke informatie die moet worden gepubliceerd, te genereren binnen de ICT-
Oplossing en deze aan de component die de feitelijke publicatie verzorgt, beschikbaar te stellen. ................................................................................. 35
Wens 18
Koppelingen, al dan niet geautomatiseerd, naar overige informatiebronnen. Hetzij om gegevens in te zien, hetzij om gegevens over te halen naar de ICT-
oplossing. Voorkeur is dat de gegevens bij de bronnen blijven. ..................................................................................................................................... 36
Wens 19
Koppelingen tussen Plan-/Toepasbare Regels-software en de ICT-oplossing. .................................................................................................................. 36
Wens 20
De ICT-oplossing maakt de gebruikers opmerkzaam op de verplicht te registreren gegevens, bijvoorbeeld door het hanteren van een andere kleur voor
verplichte velden .......................................................................................................................................................................................................... 38
Wens 21
De ICT-oplossing sorteert voor op deze toekomstige API ontwikkeling. Deze is ingericht uiterlijk in januari 2024. ......................................................... 39
Wens 22
De ICT-oplossing biedt mogelijkheden om, naast bekendmakingen e.d. op mijnoverheid.nl, ook beschikkingen en bijlagen extern digitaal te raadplegen.
 .................................................................................................................................................................................................................................... 40
Wens 23
De ICT-Oplossing ondersteunt op termijn (uiterlijk januari 2024)  de monitoringsfunctie in de Big-8 systematiek. .......................................................... 41
Wens 24
Uw ICT-oplossing levert binnen een termijn van uiterlijk 24 maanden een bijdrage aan de ontwikkeling van lokaal en regionaal omgevingsbeleid, kijkend
naar de doorontwikkeling van de Omgevingswet in combinatie met de mogelijkheden en roadmap van uw productielijn. ............................................... 41
Wens 25
U garandeert binnen een termijn van uiterlijk 24 maanden toe te groeien naar het Common Ground model. U kunt op verzoek een concreet plan
overhandigen hoe u van de huidige situatie naar het Common Ground  model toewerkt, inclusief groeipad en planning. ............................................... 42
Wens 26
U levert onderstaande toegevoegde waarde op het vlak van geavanceerde zoekmogelijkheden en de functies die u hierin ziet binnen de ICT-oplossing. 42
Wens 27
VTH029 Kunnen ophalen van gegevens / documenten uit de Archiefregistratiecomponent ............................................................................................ 65
Wens 28
VTH033 Kunnen bevragen van gegevens in de financieel component ............................................................................................................................. 65
Wens 29
VTH035 Kunnen aanbieden van gegevens aan het data-analyse en monitoringcomponent.............................................................................................. 66
Wens 30
VTH045 Kunnen vastleggen van resultaten van inhoudelijke toetsing van de activiteiten ................................................................................................ 66
Wens 31
VTH046 Kunnen laten accorderen van de concept beschikking ...................................................................................................................................... 66
Wens 32
VTH054 Kunnen aangeven van een risicoprofiel ............................................................................................................................................................ 66
Wens 33
VTH061 Kunnen ondersteunen in het maken van een integrale afweging op basis van verzamelde adviezen .................................................................. 67
Wens 34
VTH069 Kunnen vastleggen van afspraken met ketenpartners ....................................................................................................................................... 67
Wens 35
VTH070 Kunnen vastleggen van samenhang met andere procedures/besluitvorming ..................................................................................................... 67
Wens 36
VTH072 Kunnen genereren van management rapportages ............................................................................................................................................. 67
Wens 37
VTH073 Kunnen samenstellen van eigen rapportages .................................................................................................................................................... 68
Wens 38
VTH075 Kunnen inplannen van werkzaamheden ........................................................................................................................................................... 68
Wens 39
VTH089 Kunnen aanvragen van intern advies ................................................................................................................................................................ 69
Wens 40
VTH096 Kunnen werken op basis van de interbestuurlijke ZTC-Omgevingswet............................................................................................................... 69
Wens 41
VTH100 Kunnen opvragen, toevoegen, wijzigen, verwijderen van rechten op documenten in een Samenwerking in de Samenwerkfunctionaliteit van het
DSO-LV ......................................................................................................................................................................................................................... 69

## Page 94

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 93 van 102
Wens 42
VTH102 Kunnen versturen van notificaties aan andere systemen als er gegevens in het VTH-systeem zijn gewijzigd ...................................................... 70
Wens 43
VTH014 Kunnen registreren van de aanvraag of melding in het Omgevingsloket............................................................................................................ 71
Wens 44
VTH026 Kunnen opvragen van de gemeentelijke legesregeling ...................................................................................................................................... 72
Wens 45
VTH051 Kunnen afhandelen van een planschadeprocedure ........................................................................................................................................... 72
Wens 46
VTH065 Kunnen opstellen van verslagen/rapportages ................................................................................................................................................... 73
Wens 47
VTH068 Kunnen samenstellen van activiteiten tot een integraal besluit ......................................................................................................................... 73
Wens 48
VTH074 Kunnen agenderen van een adviesvraag aan de Gemeenteraad ......................................................................................................................... 73
Wens 49
VTH092 Kunnen doen van verzoek om wijziging in omgevingsplan ............................................................................................................................... 73




## Page 95

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 94 van 102
Annex E
Koppelingen aan bestaande systemen

Deze bijlage bevat een lijst van de, op het moment van aanbesteden, aanwezige systemen bij de deelnemers.

Omgevingsdienst Zuidoost-Brabant

Koppeling naar welk zaaktype
Nvt
Versie

Koppeling naar welk DMS
Nvt
Versie

Koppeling aan ESB of direct aan vak-applicatie
Nvt
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)

Overige koppelingen (financiële systemen e.d.
Axapta (Microsoft Dynamics)

A2-Gemeenten (Valkenswaard, Heeze-Leende, Cranendonck)

Koppeling naar welk zaaktype
Exxellence
Versie
7.2
Koppeling naar welk DMS
nvt; Via het zaaksysteem gaan de documenten naar het DMS
Versie

Koppeling aan ESB of direct aan vak-applicatie
Rechtstreeks aan de interne vak-applicaties?
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Ja, Exxellence datadistributie

Overige koppelingen (financiële systemen e.d.
Azure Active Directory
Snelbalie Berkeley Bridge (voor de vergunningen die niet via DSO gaan (drank / horeca /
evenement) (VW/CR)
Cognos (rapportage tool)
Key2Financien Centric (exportfunctie)
CBS W11 (exportfunctie)
Mogelijkheid om te koppelen met plansoftware. Nu hebben RObeheer, Tercera en Dezta
planmonitor. Nog niet duidelijk welke het gaat worden in de toekomst.


## Page 96

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 95 van 102

Dommelvallei (Son en Breugel, Nuenen en Geldrop-Mierlo)

Koppeling naar welk zaaktype
Koppeling met het zaaksysteem Djuma
Versie
(Nu versie 118 om de 3 weken een update) realiseren. Het over zowel de zaken als de
zaakdocumenten. Deze koppeling zal via, het nog te realiseren, ESB (service Bus)
verlopen
Koppeling naar welk DMS
Koppeling met het zaaksysteem Djuma
Versie
(Nu versie 118 om de 3 weken een update) realiseren. Het over zowel de zaken als de
zaakdocumenten. Deze koppeling zal via, het nog te realiseren, ESB (service Bus)
verlopen
Koppeling aan ESB of direct aan vak-applicatie
We hebben verder geen interne vak-applicaties die we willen koppelen. Mocht dit later
wel het geval zijn dan via de ESB.
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Ja, minimaal voor de persoonsgegevens moet er gekoppeld gaan met één multi-tenant
distributiesysteem. Deze koppelingen zullen gelegd moeten worden op de laatste versies
van StUF BG. Het distributiesysteem zit in een aanbestedingsprocedure en wordt in 2020
na de zomer geïmplementeerd.
Overige koppelingen (financiële systemen e.d.
Alleen de koppeling naar het financiële systeem Key2Financiën van Centric is van belang.
Dit zal gebeuren met bestanden (“memoriaal”) per organisatie.

SCC De kempen (Oirschot, Reusel-de Mierden, Bladel, Eersel, Bergeijk)

Koppeling naar welk zaaktype
iZaaksuite (alleen Oirschot)
Versie

Koppeling naar welk DMS
Corsa van BCT
Versie

Koppeling aan ESB of direct aan vak-applicatie
Waar mogelijk wordt gebruik gemaakt van:
-          Makelaar van PinkRoccade voor interne koppelingen/distributie
-          CLIQ van PinkRoccade voor externe koppelingen
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Ja, de Makelaar (MKS) van PinkRoccade

Overige koppelingen (financiële systemen e.d.
De Kempen maken gebruik van GeoWeb van Sweco als viewer.

## Page 97

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 96 van 102
Voor financiën wordt gebruik gemaakt van Key2Finance van Centric, behalve Oirschot, hier
wordt CiVision Middelen van PinkRoccade gebruikt

Best

Koppeling naar welk zaaktype
Squit XO (aangaande milieu)
Versie

Koppeling naar welk DMS
Corsa
Versie

Koppeling aan ESB of direct aan vak-applicatie
Onbekend
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Onbekend
Overige koppelingen (financiële systemen e.d.
Geotheek (Ondergrond)

Veldhoven

Koppeling naar welk zaaktype
Djuma van Circle
Versie
Saas versie
Koppeling naar welk DMS
Djuma van Circle en MyCorsa NxT Versie: 2018 UCR 11 (2019) (r15707) van BCT op basis
van DMS-zaaksysteem
Versie

Koppeling aan ESB of direct aan vak-applicatie
ESB van Enable-U
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
DDS an Centric
Overige koppelingen (financiële systemen e.d.
DSO, Software voor toepasbare regels, Plansoftware, Squit XO/2020 van Roxit, iBis,
Cognos, Nedmagazijn van Nedgraphics, Digitale handtekening van Valid Sign, MS
Sharepoint/Office365

Helmond

Koppeling naar welk zaaktype
Djuma van Circle Software Group BV)
Versie
laatste

## Page 98

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 97 van 102
Koppeling naar welk DMS
Djuma van Circle Software Group BV)
Versie
laatste
Koppeling aan ESB of direct aan vak-applicatie
ESB  – (Enable U 2Secure & Enable U 2Orchestrate van Enable-U).
Alle koppelingen die gerealiseerd worden gaan via deze ESB oplossing
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Makelaarsuite (van PinkRoccade Local Government)

Overige koppelingen (financiële systemen e.d.
Niet bekend

Deurne

Koppeling naar welk zaaktype
OneGov Dynamics 365 SaaS
Versie

Koppeling naar welk DMS
Share Point online, laatste Microsoft versie
Versie

Koppeling aan ESB of direct aan vak-applicatie
Enable You SaaS
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Ja, Civision makelaar Suite van Pink Roccade versie 2.9.39 - A

Overige koppelingen (financiële systemen e.d.
Koppeling met het financieel pakket
BRIStoets
SIM
DROP, publicatie afhankelijk van keuze VTH applicatie (op dit moment Squit 20/20
Publiceren)
DSO

Asten

Koppeling naar welk zaaktype
Op dit moment wordt Verseon 2.4 gebruikt. In de loop van 2020 wordt de overstap
gemaakt naar Verseon 2.5.
Versie

Koppeling naar welk DMS
zie zaaksysteem
Versie

Koppeling aan ESB of direct aan vak-applicatie
Voor BG koppeling via ESB, CGS van PinkRoccade, Makelaarsuite.
Voor ZKN koppeling via ESB, VSB van Circle (Verseon). Deze is van Enable-U

## Page 99

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 98 van 102
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Ja, Makelaarsuite van PinkRoccade.

Overige koppelingen (financiële systemen e.d.
Voor wat betreft de financiële systemen was er een semi-automatische koppeling. Dat wil
zeggen dat er een export werd gemaakt uit SquitXO en dat deze werd
ingelezen in CiVision Innen. CiVision Innen wordt niet meer gebruikt. De
export vanuit SquitXO wordt nog wel steeds gemaakt, maar de gegevens
daaruit worden nu handmatig in Civision Middelen opgevoerd. Een koppeling
tussen het VTH-systeem en CiVision Middelen zou wat ons betreft een goede
aanvulling zijn.
Voor GEO moet er een koppeling gelegd worden naar het GEO gegevensmagazijn van
Vicrea en Neuron Stroomlijn.

Someren

Koppeling naar welk zaaktype
Djuma
Versie

Koppeling naar welk DMS
Djuma
Versie

Koppeling aan ESB of direct aan vak-applicatie
Via een ESb
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
CiVision Gegevensmakelaar MKS (van Pinkroccade)
Neuron Stroomlijn (van Vicrea; voor de geo-informatie)
Overige koppelingen (financiële systemen e.d.
Optioneel: documentgeneratie SmartDocuments

Gemert-Bakel (niets ontvangen)

Koppeling naar welk zaaktype

Versie

Koppeling naar welk DMS

Versie

Koppeling aan ESB of direct aan vak-applicatie

Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)


## Page 100

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 99 van 102
Overige koppelingen (financiële systemen e.d.


Laarbeek (niets ontvangen)

Koppeling naar welk zaaktype

Versie

Koppeling naar welk DMS

Versie

Koppeling aan ESB of direct aan vak-applicatie

Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)

Overige koppelingen (financiële systemen e.d.


Uden

Koppeling naar welk zaaktype
Liber versie 1.105.2 - 101020191836 van BCT
Versie

Koppeling naar welk DMS
Corsa versie 7.2, 2018 UCR 11 (2019)  van BCT
Versie

Koppeling aan ESB of direct aan vak-applicatie
Bij voorkeur via ESB, echter waar dit functioneel beperkingen c.q. bezwaren met zich
meebrengt of anderszins niet de voorkeur heeft moet een rechtstreekse koppeling o.b.v.
vigerende open standaarden ook tot de mogelijkheid behoren.
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Key2Datadistrubitie van Centric

Overige koppelingen (financiële systemen e.d.
Koppeling met Key2Financiën van Centric t.b.v. doorgeleiding legesberekening en
facturering legeskosten.
Koppeling met sjablonengenerator iWriter.  Bij voorkeur ook goede sjablonen in de
applicatie zelf.
Koppeling met Cognos of export kunnen maken tbv. het maken van data analyse en
rapportages in applicaties als Cognos of FME (Geo gerelateerde rapportages)
en toegang tot database met bijv. PL-SQL tbv rapportages.

## Page 101

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 100 van 102
Mogelijk toekomstige GEO koppeling t.b.v. publicatie vergunningen in omgevingsplannen
DSO i.h.k.v. omgevingswet. Vooralsnog i.v.m. huidige onduidelijkheid eisen
aan functionaliteit nader te bepalen.
Algemene kanttekening:
Alle koppelingen moeten  o.b.v. vigerende open standaarden worden ingericht

De hierboven vermelde gegevens representeren de huidige situatie.
Genoemde versies kunnen verschillen ten tijde dat een daadwerkelijk implementatie traject
gaat starten.
Daarnaast zitten de gemeenten Landerd en Uden in een gemeentelijk herindelingstraject.
Gemeenten Landerd en Uden worden daarmee per 01-01-2022 één nieuwe gemeente.
Dat houdt in dat in de periode 2020 en 2021 qua applicatielandschap een slag gemaakt
moet worden met rationalisatie en harmonisatie van dit landschap.
I.r.t. bovenvermelde gegevens betekent dat concreet dat deze in de loop van 2020 en/of
2021  kunnen gaan veranderen.

Landerd

Koppeling naar welk zaaktype
Atos eSuite (nu versie 4.22, bij implementatie VTH oplossing waarschijnlijk 4.23).
Versie

Koppeling naar welk DMS
Atos eSuite (nu versie 4.22, bij implementatie VTH oplossing waarschijnlijk 4.23).
Versie

Koppeling aan ESB of direct aan vak-applicatie
Koppelingen tussen de VTH SaaS oplossing en ons netwerk lopen bij voorkeur via onze
ESB (Jnet). Jnet kan ook SaaS naar SaaS koppelingen inrichten (b.v. met ons zaaksysteem)
maar het is niet zeker of de eSuite dat ook mogelijk maakt.
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Key2Datadistributie (Centric).

Overige koppelingen (financiële systemen e.d.
Koppeling met documentgenerator SmartDocuments.
Wens: koppeling met Key2Financiën voor facturen leges. Dit gebeurt nu handmatig
vanwege het lage volume, maar als er een kwalitatief goede koppeling is
willen we die wel gebruiken.

## Page 102

BIJLAGE 3 ARCHITECTUUR & ONTWERP, INCLUSIEF PROGRAMMA VAN EISEN, SPECIFICATIES EN WENSEN
14-1-2020
pagina 101 van 102
Wens: koppeling met BAG voor gereed melding vergunningen . Dit wordt nu via e-mail
doorgegeven aan de BAG medewerker maar als er een goede koppeling
beschikbaar is, is dat mogelijk wel interessant.
Wens: koppeling met Cognos voor managementrapportages. Wordt bij ons nu nauwelijks
gebruikt maar wordt later samen met Uden mogelijk wel een eis

Druten-Wijchen

Koppeling naar welk zaaktype
Decos JOIN Zaak en document versie 6.27 (voor Druten én Wijchen)
Versie

Koppeling naar welk DMS
Decos JOIN Zaak en document versie 6.27 (voor Druten én Wijchen)
Versie

Koppeling aan ESB of direct aan vak-applicatie
Via ESB of via Key2DDS
De vorm van onze werkorganisatie (gemeente Wijchen, gemeente Druten en de
Werkorganisatie zelf als juridische entiteiten) vereist dat wij zogenaamde
‘meer gemeente functionaliteit’ nodig hebben.
Koppeling met lokale BRP applicatie (Wijchen) via gegevensdistributiesysteem (Key2DDS
van Centric) want dit is wettelijk verplicht. Koppeling met lokale BRP applicatie (Druten) via
gegevensdistributiesysteem (Pink Roccade Makelaarsuite). BAG, BGT, BRK, NHR bij
voorkeur
Dient de ICT-oplossing ook te koppelen aan
een lokale gegevensmakelaar (zo ja, welke)
Ja, Wijchen aan Key2DDS van Centric. Voor Druten aan Makelaarsuite van Pink

Overige koppelingen (financiële systemen e.d.
key2financien (Centric)




---

*This document was automatically converted from PDF. Some formatting may have been lost in the conversion process.*
