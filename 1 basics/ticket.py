def ticket1(age):
    if age<15:
        print("children")
    elif age<65:
        print("aldults")
    else :
        print("seniors")

def ticket2(age):
    ticketType="children" if age<15 else "adults" if age<65 else "seniors"
    print(ticketType)        
def test():
    ticket1(20)
    ticket2(66)
test()