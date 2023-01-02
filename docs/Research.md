---
layout: default
title: Research
nav_order: 4
---

## Kernel transformer network & Spherical Convolution (Su & Grauman, 2017)

Bij de Spherical Convolution van Su & Grauman worden bestaande CNN's gebruikt en omgezet om hun originele functionaliteit toe te passen op 
Spherical images. Bij deze paper gaat het om feature recognition, de originele code werd later bijgewerkt om minder computionele kracht nodig te hebben 
onder de naam Kernel Transformer Network.
Alhoewel dit een zeer goede oplossing is voor de distorties in equirectangular projections terug recht te zetten zodat deze herkend kunnen worden door bestaande
object of feature recognition algorithmes, wordt er niet gekeken naar de stitching lines waar ons onderzoek om draait. 


Boundary Problem
"The projection given in Section 4.2 is primarily introduced
to deal with the distortion problem. As we treat the spherical
image as a signal on the sphere during projection, it also naturally solves the boundary problem of spherical images, which
is not touched in [Su and Grauman, 2017]." 

van (Qiang Zhao, Chen Zhu, Feng Dai, Yike Ma, Guoqing Jin, and Yongdong Zhang. 2018. Distortion-aware CNNs for spherical images. 
In Proceedings of the 27th International Joint Conference on Artificial Intelligence (IJCAI'18). 
AAAI Press, 1198–1204.)


## SphereNet: Learning Spherical Representations for Detection and Classification in Omnidirectional Images (Coors & Condurache & Geiger, 2018)

![image](https://user-images.githubusercontent.com/60694521/210258364-97e7e1a1-6550-4010-8f53-6ab0628ac93c.png)

Op deze afbeelding uit de paper van Coors & Condurache & Geiger, 2018 is te zien dat de filter in plaats van stopt aan de rand door gaat naar de andere kant
van de afbeelding. 

In onze experimenten met de code van deze paper is er geen bespreekbaar resultaat gekomen.


## Distortion-Aware Convolutional Filters for Dense Prediction in Panoramic Images (Keisuke & Navab & Tombari, 2018)

Deze paper claimt het 'boundary problem' op te lossen door de tradionele convoluties te vervangen door 'Disortion-aware' convoluties die rekening houden met de
distorties in equirectangular projections en ook met de overgang van links en rechts op 180°.

![image](https://user-images.githubusercontent.com/60694521/210259222-129084ba-67be-4f30-8959-743228115678.png)

"4.5 Application to panoramic style transfer
Being our distortion-aware convolution general purpose in terms of tasks and independent from the specific network architecture, we apply our proposed convolution to
a different task named panoramic style transfer, i.e. an extension to equirectangular
panoramic images of the style transfer on perspective images proposed in [6]. Here
we do not employ the FCRN network but the modified VGG architecture proposed in
[6], where the part of the network used to encode the input image content is modified
by replacing standard convolutions with distortion-aware ones. Since the style images
that we use are normal perspective images, the network layers which encode the style
image rely on the original convolutions. The middle row in Fig.12 shows the result of
style transfer while the bottom row shows the perspective image projected from the
style transfered equirectangular image. As the red highlights show, some border and
discontinuity can be seen on the results by standard convolution and the result on Cube
map, because the style transfer by standard convolution does not consider the distortion
and continuity of equirectangular image. On the other hand, the projected images from
our method do not show such discontinuities and appear more natural." 





Van Distortion-Aware Convolutional Filters for Dense Prediction in Panoramic Images (Keisuke & Navab & Tombari, 2018)


Jammer genoeg is hier geen openbaar beschikbare code van dus het reproduceren van deze resultaten is niet mogelijk.


## Conclusie

In veel bestaande onderzoeken worden de distorties in equirectangular projections aangepakt om vervormde objecten terug in hun orginele vorm te zien
en hierdoor bestaande algorithmen te kunnen gebruiken om de verwachte resultaten te behalen.

Er zijn ook onderzoeken die bestaande modellen trainen op equirectangular projections om de kenmerken van dit soort afbeeldingen mee in rekening te kunnen nemen

Meestal zijn deze oplossingen genoeg in het domein van object-recognition en semantic segmentation waarbij de filter over de afbeelding rekening houdt met de 
distorties maar niet verder kijkt over het 180° punt waar ons onderzoek ligt.



