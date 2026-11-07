HR_max = float( input( 'Geef de maximale hartslag in:' ) )
HR_rest = float( input( 'Geef de hartslag in rust in:' ) )

VO2max = 15 * HR_max / HR_rest

print(f"VO2max: {round(VO2max, 1)}")
