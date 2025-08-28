#Cheapter : 03  Lists and Tuples

# list and Tuples  are almost same as : array

marks =[94.4, 87.5, 95.2, 66.4, 45.1]
print ( marks)
print( type( marks))
print( marks[0])
print(marks[1])

#slice of list ***** topic***** same as string.

print( marks[1:4])
print( marks[ :4])
print( marks[ 1: ])

# we can store multiple type data in a single list.
student =[ "karan", 95.4, 17, "Delhi"]

#***** in python  string are => immutable ( means : can't change )

str="hello"
print(str[0])
 # str[0]="y"   ( it gives error . because string are immutable)

# ***** but  in python list are => mutable  ( means: can change )

print ( student[0])
student[0]="ranok" # change the value because mutable.

print ( student[0])
# NOte: string are  fix size , list not fixed size.

# list Method ================================
# 1.
list =[2,1,3]
list.append(4 )
print ( list)   # [2, 1, 3, 4]

list.sort ( )  # sort the list
print ( list.sort()) # ans: None
print( list)  # ans: 1 2 3 4
print ( )

# descending order sort
list.sort( reverse=True)    # ===>> print the list in descending
print( list)   # ans: [4, 3, 2, 1]


list1 = [ "ranok", "nobata", "doramon", "sujuki"]
list1.sort( )
print( list1)  # ['doramon', 'nobata', 'ranok', 'sujuki']

list1.sort( reverse =True)
print( list1)  # ['sujuki', 'ranok', 'nobata', 'doramon']


# reverse method  :  opposite the list

list2= ['b', 'c', 'g', 'd',  'x', 'r']
list2.reverse()
print( list2)   # ans: ['r', 'x', 'd', 'g', 'c', 'b']

# insert  : list2.insert( idx, value)
list2.insert( 1,'j')
print (list2)   # ['r', 'j', 'x', 'd', 'g', 'c', 'b']

#pop : pop the 1st occurance value

list3=[ 3,6,7,4,6,6,4]
list3.pop(6)
print( list3)  # ans: [3, 6, 7, 4, 6, 6]

# search : pthone documentation  , google search

# =======================================
# =====TUPLES =================
# IT IS  BUILT IN DATA TYPE.  create immutable sequence of value.

# here, use ( )
tup = ( 2, 5, 5, 3)
print ( type( tup))  # <class 'tuple'>
print( tup[1]) # ans: 5

# since tuple are immutable , so doesn't support assign new value
# tup[0]= 9    => it gives wrong  because of immutable.

tup1=()
print( tup1)  # ans: ()
print( type( tup1))  # ans: <class 'tuple'>
tup2= ( 1,)
print( tup2)     # ans: (1,)
print( type(tup2))  #ans:  <class 'tuple'>

tup3=( 1)
print( type( tup3))  # ans: <class 'int'>
print( tup3)  # ans: 1



#======================================

#  methods: slice,  tup.index( element_which_we_search), tup.count( element-which_we_search)

tup4=( 4,7,2,8,7,8,8,9)
print( tup4.index(7))    # ans: 1  ( give 1st occurance value)
print( tup4.count(8))  # ans: 3  ( no_of_times comes the 8)

#===========================
#Question: take 3 user input movie name and store in the list
movie=[]
mov1=input("enter 1st movie:")
mov2=input( "enter 2nd movie:")
mov3=input("enter 3rd movie: ")

# now append them
movie.append( mov1)
movie.append(mov2)
movie.append(mov3)
print( "movie name are: ", movie) #ans: movie name are:  ['sjfo sofh', 'sfo sof', 'osjf']


# another way :
movies=[]
mov=input("enter 1st movie: ")
movies.append(mov)
mov=input("enter 2nd movie: ")
movies.append(mov)
mov=input("enter 3rd movie: ")
movies.append(mov)

print(movies)

# another way :
drama=[]
drama.append( input( "enter 1st drama: "))
drama.append( input("enter 2nd drama: "))
drama.append( input( " enter 3rd drama :"))

print( drama)  # ans: ['ssj sjo', 'slfj ', 'go']
#=====

#question: WAP  to check if a list contain a palindrome of elements. ( Hints: use  copy() method )

# example of palindrome: [ 1,2,3,2,1] , [ a,b,b,a]

list1=[1,2,1]
list2=[ 1,2,5]

copy_list1=list1.copy()
copy_list2=list2.copy()

if( list1 == copy_list1):
    print( "palindrome")
else:
    print( "Not palindrome")
