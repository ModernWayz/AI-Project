---
layout: default
title: SIFT
nav_order: 2
---

## SIFT 

Door gebruik te maken van SIFT om kenmerkende eigenschappen uit gelijkaardige afbeeldingen te halen kunnen we afbeeldingen samenvoegen zonder een lijn te genereren.
Een simpele toepassing van deze techniek op een rectilineaire afbleedingenspaar geeft als resultaat zeer veel correcte kenmerkende eigenschappen (correct duidt hier op
dezelfde plek op beide afbeeldingen).

![Normale SIFT](../images/siftnorm.jpg "SIFT normale")

Maar na een style transfer toe te passen op rectilineaire afbeeldingen zien we dat de kenmerkende eigenschappen zo goed als verdwijnen. 
Dit heeft als gevolg dat het samenvoegen van de afbeeldingen niet correct verloopt.

![Style transfer SIFT](../images/siftstyle.jpg "SIFT styleTransfer")

### SIFT advanced

In plaats van kenmerkende eigenschappen te zoeken op een afbeelding die getransformeerd is met de style transfer nemen we de eigenschappen van de originele afbeeldingen om een mask te maken en de afbeeldingen te blenden. Hiervoor maken we gebruik van een bestaand [repo](https://github.com/StijnWillemen/stitching) met enkele kleine aanpassingen. 

Door een afstandsgetrouwe cilinderprojectie met uitbreiding aan de zijkant (om overlap te generen) te nemen en deze te splitsen in het midden en de zijkanten
terug aan elkaar te stitchen kunnen we het lijn artefact van hierboven proberen wegwerken.

1. Originele afbeelding met uitbreiding (overlap)
![Original overlap equirectangular](../images/equirectangular_og_test_overlap.png "Original overlap equirectangular")
2. Originele afbeelding gesplit
![Original overlap equirectangular split1](../images/original_images_overlap.png "Original overlap equirectangular split")
4. Style transfer afbeeldingen 
![styled overlap equirectangular split](../images/styled_images_overlap.png "Styled overlap equirectangular split")
5. Resultaat
![Styled overlap equirectangular](../images/charcoal_equirectangular_styled_stitched.jpg "Styled overlap equirectangular")


#### Sift met rectilineaire afbeeldingen

Voor onderstaande afbeelding zijn er 16 rectilineaire afbeeldingen gebruikt als een test van deze blending/stitching methode op meerdere afbeedlingen vanuit
verschillende hoeken.

![Style Transfer SIFT advanced](../images/advancedsiftstyle.jpg "Advanced SIFT styletransfer")

de volgende stap is nu deze methode toepassen op genoeg afbeeldingen om een volledig 360° afbeeldingen te vormen en te evalueren.
