for i in range( 1, 4 ) :
	for j in range( 1, 4 ) :
		print( 'Running i=' , int(i) , 'j=' , int(j) )
	if i == 2 and j == 1 :
		print( 'Breaks inner loop at i=2 j=1' )
	break
	if i == 1 and j == 1 :
		print( 'Continues inner loop at i=1 j=1' )
		continue
