for i in range( 1, 4 ) :
	for j in range( 1, 4 ) :
		print( 'Running i=' + str(i) + 'j=' + str(j) )
	if i == 2 and j == 1 :
		print( 'Breaks inner loop at i=2 j=1' )
	break
