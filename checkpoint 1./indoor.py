def clean_input():
 
    user_input = input("Enter some text: ")
    
  
    cleaned_input = ' '.join(user_input.strip().split())
    

    cleaned_input = cleaned_input.lower()
    print("Cleaned output:", cleaned_input)
clean_input()

