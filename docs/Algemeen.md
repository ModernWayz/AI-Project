---
layout: default
title: Equirectangular/Cube_Map/Blending
nav_order: 3
---

# Algemeen

![Original 360](../images/360.jpg "360 graden") ![Style transfer](../images/styletransfer.png "style transfer image")

Door gebruik te maken van [Neural Style Transfer](https://doi.org/10.48550/arXiv.1508.06576) adhv een bestaand [repo](https://github.com/crowsonkb/style-transfer-pytorch)
op een afstandegetrouwe cilinderprojectie zien we dat er op de resulterende afbeelding (in 360° beeld) een duidelijke scheiding is.

![Scheiding](../images/scheiding.png "scheiding") 

Dit wordt veroorzaakt doordat het algorithme geen rekening houd met het feit dat de linker- en rechterzijde moeten worden samengebracht in 360° beeld. Daarbij is er op het
standpunt van de observeerder (centrum van 360° afbeelding) een vervorming die het doet lijken of alles aanzichten convergeren naar één punt.

![Convergentie](../images/Convergentie.png "Convergentie")

## Kubus map

![Kubus map](../images/kubus.jpg "kubus map")

Een mogelijke oplossing hiervoor kan een kubus map zijn waarbij de afstandsgetrouwe projectie wordt uitgevouwen naar de 6 vlakken van een kubus. 
Hierna wordt de style transfer toegepast op elk vlak. 

*afstandsgetrouwe cilinderprojectie --> kubus map (https://jaxry.github.io/panorama-to-cubemap/)

*kubus map --> afstandsgetrouwe cilinderprojectie (https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html)

### Resultaat

![Kubus map style transfer](../images/kubusmaptransfer.png "kubusmaptransfer")

### Nieuwe artefacten

![kubus 360](../images/kubus360.png "kubus 360 hoek")

Deze uitvoering zorgt ervoor dat de convergerende lijnen in het centrum verdwijnen maar hierdoor duiken er nieuwe artefacten op bij de samenvoeging van de kubus vlakken.
Deze lijnen geven de indruk dat de observeerder zich in een kubus bevind.

### Blending

Door een afstandsgetrouwe cilinderprojectie met overlappende uiteinden te gebruiken voor style transfer kunnen we de stitch-lijn proberen wegwerken.
Deze afbeeldingen wordt met overlap gestyled en daarna worden de overlappende uiteinden over elkaar geblend.

![Afstandsgetrouwe cilinderprojectie](../images/equirectangular_og_test_overlap.png "afstandsgetrouwe cilinderprojectie met overlap")

![Afstandsgetrouwe cilinderprojectie style](../images/monet_overlap.png "afstandsgetrouwe cilinderprojectie met overlap")

![Afstandsgetrouwe cilinderprojectie style](../images/manuel_blended_equirect.png "afstandsgetrouwe cilinderprojectie zonder overlap")

## Blended Cube Map

Door simpele blending toe te passen op overlappende kubus-gezichten kunnen we de bestaande artefacten minimaliseren en de convergentie afhouden.

![Kubus_style_transfer](../images/styled_cube_map.png "Kubus Style Transfer")

Resultaat:
![Kubus_equirect_style_transfer](../images/Cubemap_equirectangluar_styled.png "Kubus_equirect Style Transfer")

###Cube map uitbreiden

Met enkele gezichten te repliceren kunnen we dit process versnellen en het blenden minder tijdrovend maken.

![Idea_expanded](https://user-images.githubusercontent.com/60694521/210592705-c8979797-465c-4832-b7d2-fdf8279475ae.png)

Resultaat:
![image](https://user-images.githubusercontent.com/60694521/210591876-7b680c02-acb1-4deb-b588-512caba279be.png)








