def main():
    list = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]
    list.remove ("Princess Peach")
    for sender in list:
        list(sender)
    

def invitation(sender):
    print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {sender},
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       Princess Peach
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """)
    
main()