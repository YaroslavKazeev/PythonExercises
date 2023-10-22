# Create a function that gets a number as a parameter, and then prints the multiplication table for that number from 1 to 10. E.g., when the parameter is 12, the first line printed is “1 x 12 = 12” and the last line printed is “10 x 12 = 120.”

def multiply( x ):
    for i in range( 10 ):
        print( float(x) * (i+1) )

x = input( "Please, enter an integer or float number: " )
multiply(x)