def Farey_generation(order):
	n=order
	A=0  /* A is an array of 2 columns which store the angles		                
	A[0]=[0,1] /* the first term of the sequence
  	A[1]=[1,1] /* the last term of the sequence
  	A[2]=[1,0]  /* The first term of the next sequence
	A[3]=[-1,1] /*The last term of the next sequence
  	Count=4
 	for I in range(0,n):
 	    for   j in range (i+1,n):
		  If (gcd(i, j)==1):
		  	A [count]=[i, j]	
			A[count+1]=[j,i]
			A[count+2]=[-j,i]
			A[count+3]=[-i,j]
			Count=count+4
