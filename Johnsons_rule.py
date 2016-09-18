# This is the code for solving a two-server scheduling problem using Johnson's Rule

def JohnRule(L):
    flag = 0
    for i in range (0,len(L)):
        if L[0]==L[i]:
            flag =1
        else:
           flag = 0
    if flag == 1:
        return "Johnsons rule can not be excecuted if all the jobs times are the same"
    for i in range (0,len(L)):
        if L[i][0]<0 or L[i][1]<0:
            return "The time taken for a job can not be 0"
            
    output = [None] * len( L )

  
    
    
    leftmost = 0
    rightmost = -1
#code to implement johnsons rule 
    while len( L ) > 0:
        # find the index of the job with a minimum processing time at one of the servers
        index_to_schedule = 0
        for i in range( 0, len( L ) ):
            if min( L[ index_to_schedule ] ) > min( L[ i ] ):
                index_to_schedule = i
    
        # find out where to put it - at the beginning or end of the schedule
        if L[ index_to_schedule ][ 0 ] <  L[ index_to_schedule ][ 1 ]:
            # schedule the job indexed by index_to_schedule as early as possible
            output[ leftmost ] = L[ index_to_schedule ]
            leftmost = leftmost + 1
        else:
            # schedule the job indexed by index_to_schedule as late as possible
            output[ rightmost ] = L[ index_to_schedule ]
            rightmost = rightmost - 1
    
        # remove the scheduled job from the list of the remaining jobs (i.e., L) 
        L.remove( L[ index_to_schedule ] )
    return totaltimeofjobs(output)
    
 #The following code is used to calculate the total time for completing the job by both the operators/machines
def totaltimeofjobs(output):
    totaltime1=0
    dummy=[]
    for tuple in output:
        dummy.append(list(tuple))
        
    
    

    for i in range (0,len(dummy)-1) :
      
       totaltime1=totaltime1+max(dummy[i+1][0],dummy[i][1])
       
       if dummy[i][1]>dummy[i+1][0]:
           if(i+2>len(dummy)-1):
               break
           dummy[i+2][0]= dummy[i+2][0]-(dummy[i][1]-dummy[i+1][0])
       
   
    totaltime1= totaltime1 + output[0][0] + output[-1][1]
         
    return output,totaltime1   
   
  
#Problem 3
  
  
import math



# The other approach is to build the matrix with correct numbers, adding them one by one

def distancematrix(coord):
    my_matrix = []
    for city_from in range( len( coord  ) ):
        my_matrix.append( [] )
        for city_to in range( len( coord ) ):
            my_matrix[ city_from ].append( math.sqrt( (coord[city_to][0] - coord[city_from][0]) ** 2 + (coord[city_to][1] - coord[city_from][1]) ** 2) )
    return my_matrix
# code that returns the objective function of TSP - a tour's length
def obj( tour,my_matrix ):
    tour_length = 0
    for i in range( len( tour ) - 1 ):
        tour_length = tour_length + my_matrix[ tour[ i ] ][ tour[ i+1 ] ]
    return tour_length + my_matrix[ tour[ len(tour) - 1 ] ][ tour[ 0 ] ]
def totallength(P,co):
    tlmatrix = []
    for i in range (len(P)) :
        tlmatrix.append(obj(P[i],co))
    return tlmatrix
#the following code returns the optimal tour and it's length by brute force calculations
def brutForceTSP(C):
    coord = distancematrix(C)
   
    elements=[]
    for i in range (len(C)):
        elements.append(i)
    permuted_list = list( all_perms( elements ))
    
    tourlengths = totallength(permuted_list,coord)
    mindist= min(tourlengths)
    index =tourlengths.index(mindist)
    
    return permuted_list[index],mindist
# This function gets all the permutations of a given list
# In order to convert its output into a list, write
# permuted_list = list( all_perms( list_to_be_permuted ) )
def all_perms( elements ):
    if len( elements ) <= 1:
        yield elements
    else:
        for perm in all_perms( elements[ 1: ] ):
            for i in range( len( elements ) ):
                yield perm[ :i ] + elements[ 0:1 ] + perm[ i: ]