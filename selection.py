def selection_sort( array ) :
	for index in range( 0 , len( array ) -1 ) :
		value = array[ index ]
		current = index
# Algorithm sequence to be added here.
	for element in range( index+1 , len( array ) ) :
		if array[ element ] < array[ current ] :
			current = element
	array[ index ] = array[ current ]
	array[ current ]= value
	print( '\tResolving element[' , index , '] to ' , array )