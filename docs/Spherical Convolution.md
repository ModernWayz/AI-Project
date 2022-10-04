---
layout: default
title: Spherical Convolution
nav_order: 4
has_toc: false
---

# Spherical Convolution
## Yu-Chuan Su & Kristen Grauman
### The University of Texas at Austin

{: .warning }
> Deze code repo maakt gebruikt van Caffe wat zeer moeilijk te installeren is.

[Github Repo]((https://github.com/sammy-su/Spherical-Convolution)){: .btn .fs-5 .mb-4 .mb-md-0 }

## Korte samenvatting

Bij Spherical convolution wordt er een bestaand en getraind CNN gebruikt om verschillende ML technieken zoals Object Recognition toe te passen
op 360 graden afbeeldingen.

Spherical convolution is een techniek die draait rond twee dingen: 1) het aanpassen van de vorm van de kernel om de vervormingen 
die optreden bij het omzetten van Afstandsgetrouwe cilinderprojectie (Equirectangular projection). 2) Het aantal max pooling layers verkleinen om ervoor te zorgen
dat de pixel grote hetzelfde blijft.
Daarbij zorgt deze techniek ervoor dat het aantal lagen hetzelfde is als het aantal lagen bij het gebruikte input netwerk.

## Bruikbare informatie

**Knowledge distillation** is het leren van een nieuw model door andere bestaande model(len) te gebruiken. 
