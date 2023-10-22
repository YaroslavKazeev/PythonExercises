# A first-in-first-out (FIFO) structure, also called a “queue,” is a list that gets new elements added at the end, while elements from the front are removed and processed. Write a program that processes a queue. In a loop, ask the user for input. If the user just presses the Enter key, the program ends. If the user enters anything else, except for a single question mark (?), the program considers what the user entered a new element and appends it to the queue. If the user enters a single question mark, the program pops the first element from the queue and displays it. You have to take into account that the user might type a question mark even if the queue is empty.

print("The program saves inputs in an queue. '?' as an input means deletion of the first element. Pressing 'Enter' without any input ends the program.")
loop=True
array=[]

while loop:
    entry=input("Make your entry in the queue or type '?' then 'Enter' to delete an element. ")
    if entry == "":
        loop=False
        print("The end of the program")
    else: 
        if entry == "?":
            if len(array) == 0:
                print("The queue is empty, you need to enter at least one element to the queue to delete from")
            else:
                print("The deleted element is", array.pop(0))
        else:
            array.append(entry)
            
