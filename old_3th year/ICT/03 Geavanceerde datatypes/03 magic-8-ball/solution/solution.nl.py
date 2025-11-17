#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

antwoord = [ 'Dat is zeker', 'Het is zeker zo', 'Zonder twijfel', 'Ja, zeker', 'Je kunt erop vertrouwen', 'Zoals ik het zie, ja', 'Waarschijnlijk', 'Ziet er goed uit', 'Ja', 'Lijkt van wel', 'Vaag, probeer het nog eens', 'Vraag later nog eens', 'Kan ik beter niet zeggen', 'Kan ik nu niet voorspellen', 'Concentreer je en vraag nog eens', 'Reken er maar niet op', 'Ik zeg van niet', 'Mijn bronnen zeggen van niet', 'Lijkt er niet op', 'Zeer twijfelachtig' ]

vraag = input('Stel je vraag: ')
print( antwoord[random.randint(0, len(antwoord)-1)])