m = float( input( 'Geef de massa in:' ) )
d_v = float( input( 'Geef de dosis in:' ) )

d_k = round( m / 68.04 * d_v, 1)

print('')
print( 'kinderdosis:', d_k )