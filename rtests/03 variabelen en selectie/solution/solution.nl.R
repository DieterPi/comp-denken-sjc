# nauwkeurigheid
a <- 0.99
# verhouding
p <- 0.5
# foutenmarge
d <- 0.04

if ( a == 0.90 ){
  lambda <- 1.68
}
if ( a == 0.95){
  lambda <- 1.96
} 
if ( a == 0.99){
  lambda <- 2.58
}

# bereken hier n
n <- round( lambda^2 * p * ( 1 - p ) / ( d^2 ) )

print( n )