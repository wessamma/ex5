# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn



#############     Task 1  #########################



'''

first_number = int(input('First number :'))
second_number = int(input('Second number :'))
third_number = int(input('Third number :'))

if first_number == second_number == third_number :
    print ('The triple sum is : ',first_number * 9)
else :
    print('The sum is :', first_number + second_number + third_number)  


'''


#################  Task 2  ##################


'''


first_number = int(input('First number :'))
second_number = int(input('Second number :'))

if (first_number - second_number) > 0 :
    print ('The result of calculation is ',(first_number - second_number) * 2 )

else :
    print ('The result of calculation is ',abs (first_number - second_number) )

    

'''



##################  Task 3  #################################



'''

number = int(input('Number TO CHECK: '))

if number % 2 :
    print (number ,'is an odd number!')
else :
    print (number ,'is an even number!')    


'''





##################   Task 4 #########################


'''

from math import pi

radios = float(input ('Input the radius of the circle :'))
area = pi * (radios ** 2)
print ('The area of the circle with radius ',radios ,'is :', round (area ,2 ))


'''




#################     Task 5 ############################




'''

from random import randrange  

number = randrange (0,10,1)

while 1 :


      g_number = int( input ('Guess a number between 1 and 10 until you get it right :')) 

      if g_number == number :

        print ('Well guessed!')
        break 

      
'''



####################  Task 6 ######################

'''

scale_s = input('Input the scale shortcut you d like to convert (F - Fahrenheit, C - Celsius: C ) :')

temp = int(input(" Input the value of temperature you 'd like to convert  :"))

if scale_s == 'C' :

 temp_c = temp 
 temp_f = (9*temp_c)/5 + 32
 print ('The temperature in Fahrenheit is',temp_f, 'degrees.')

elif :
    temp_f = temp 
    temp_c = 5*((temp_f-32)/9)
    print ('The temperature in Celsius  is',temp_c, 'degrees.')

'''



##################  Task 7 #######################

'''

print( '*',2* '* ', 3* '* ',4*'* ',5* '* ',sep ='\n')











'''
#################  Task 8  ############################


'''



number_1 = 0
number_2 = 1
number_3 = 1

while number_3 < 50 :

    print (number_3)

    number_3 = number_1 + number_2

    number_1 = number_2

    number_2 = number_3




    '''
     


