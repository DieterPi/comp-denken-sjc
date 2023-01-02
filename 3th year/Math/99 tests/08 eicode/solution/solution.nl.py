#!/usr/bin/python
# -*- coding: utf-8 -*-

def eicode( tekst ):
    oorsprong1 = int(tekst[0:1])
    if(oorsprong1 == 0):
        oorsprong1 = 'Biologisch ei'
    if(oorsprong1 == 1):
        oorsprong1 = 'Vrije-uitloopei'
    if(oorsprong1 == 2):
        oorsprong1 = 'Scharrelei'
    if(oorsprong1 == 3):
        oorsprong1 = 'Koloniehuisvesting'  
    oorsprong2 = tekst[2:4]
    if(oorsprong2 == 'NL'):
        oorsprong2 = 'Nederland'
    if(oorsprong2 == 'BE'):
        oorsprong2 = 'België'
    if(oorsprong2 == 'DE'):
        oorsprong2 = 'Duitsland'
    if(oorsprong2 == 'UK'):
        oorsprong2 = 'Verenigd Koninkrijk'
    if(oorsprong2 == 'FR'):
        oorsprong2 = 'Frankrijk'
    if(oorsprong2 == 'LU'):
        oorsprong2 = 'Luxemburg'
    oorsprong3 = tekst[5:-2]
    oorsprong4 = tekst[-2:12]
    
    print(oorsprong1)
    print('Afkomst:', oorsprong2)
    print('Bedrijf- en stalcode:', oorsprong3, '-', oorsprong4)

if __name__ == '__main__':
    import doctest
    doctest.testmod()