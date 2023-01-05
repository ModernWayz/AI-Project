---
layout: default
title: Kubus Map
nav_order: 3
---

## Kubus map

![image](../images/Cube-Folding.gif "kubus map")


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

## Blended Cube Map

Door simpele blending toe te passen op overlappende kubus-gezichten kunnen we de bestaande artefacten minimaliseren en de convergentie afhouden.

![Kubus_style_transfer](../images/styled_cube_map.png "Kubus Style Transfer")

Resultaat:
![Kubus_equirect_style_transfer](../images/Cubemap_equirectangluar_styled.png "Kubus_equirect Style Transfer")

### Cube map uitbreiden

Met enkele gezichten te repliceren kunnen we dit process versnellen en het blenden minder tijdrovend maken.

![Idea_expanded](https://user-images.githubusercontent.com/60694521/210592705-c8979797-465c-4832-b7d2-fdf8279475ae.png)

Resultaat:
![image](https://user-images.githubusercontent.com/60694521/210591876-7b680c02-acb1-4deb-b588-512caba279be.png)



