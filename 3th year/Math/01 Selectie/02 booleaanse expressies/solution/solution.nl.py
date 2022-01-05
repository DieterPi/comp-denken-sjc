#!/usr/bin/python
# -*- coding: utf-8 -*-

def deelbaar_door_zes_en_acht( getal ):
    deelbaar_door_zes = getal % 6 == 0
    deelbaar_door_acht = getal % 8 == 0

    return deelbaar_door_zes and deelbaar_door_acht

if __name__ == '__main__':
    import doctest
    doctest.testmod()