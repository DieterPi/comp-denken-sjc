#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_prime( n: int ) -> bool:
    for i in range( 2, n ):
        if ( n % i ) == 0:
            return False
    return True

def goldbach( n: int ) -> None:
    if n <= 2 or n % 2 != 0:
        print( 'Het vermoeden is hier niet van toepassing.')
    else:
        primes = []
        for i in range( 2, n ):
            if is_prime( i ):
                primes.append( i )
        
        flag = True
        i = 0
        while flag:
            a = primes[ i ]
            t = 0
            inner_flag = True
            while inner_flag:
                b = primes[ i + t]
                t += 1
                inner_flag = n != a + b and i + t < len( primes )
            i += 1
            flag = n != a + b and i < len( primes )
        
        print('{} = {} + {}'.format( n, a, b ) )
