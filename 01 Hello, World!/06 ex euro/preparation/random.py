import random

# set fixed seed for generating test cases
random.seed(123456789)

# generate test data
cases = []
for i in range(1,10):
    cases.append( random.randint( 10, 1000 ) )

print(cases)

def euro(bedrag):
  biljet50 = bedrag // 50
  rest50 = bedrag % 50
  biljet20 = rest50 // 20
  rest20 = rest50 % 20
  biljet10 = rest20 // 10
  rest10 = rest20 % 10
  biljet5 = rest10 // 5
  rest5 = rest10 % 5
  munt2 = rest5 // 2
  rest2 = rest5 % 2

  print( 'biljet 50:', biljet50 )
  print( 'biljet 20:', biljet20 )
  print( 'biljet 10:', biljet10 )
  print( 'biljet 5:', biljet5 )
  print( 'munt 2:', munt2 )
  print( 'munt 1:', rest2 )

# generate unit tests
for bedrag in cases:
  euro(bedrag)