def encode_message(message):
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    
    encoded_message = ""
    index = 0
    while index < len(message):
        char = message[index]
        
        char = char.lower()
        
        if char in normal_alphabet:
            char_index = normal_alphabet.find(char)
            encoded_message += reversed_alphabet[char_index]
        elif '0' <= char <= '9':
            encoded_message += char
        
        index += 1
        
    return encoded_message

def decode_message(message):
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    
    decoded_message = ""
    index = 0
    
    while index < len(message):
        char = message[index]
        
        if char == " ":
            index += 1
            continue
        
        char_index = reversed_alphabet.find(char)
        
        if char_index != -1:
            decoded_message += normal_alphabet[char_index]
        elif '0' <= char <= '9':
            decoded_message += char
        
        index += 1
        
    return decoded_message

def main():
    message = input("Ingresa un mensaje para codificar: ")
    encoded = encode_message(message)
    
    grouped_message = ""
    for i in range(0, len(encoded), 5):
        grouped_message += encoded[i:i+5] + " "
    
    print("\nMensaje codificado:")
    print(grouped_message.strip())
    
    print("\nDecodificando el mensaje anterior...")
    decoded = decode_message(grouped_message)
    print("Mensaje decodificado:")
    print(decoded)

if __name__ == "__main__":
    main()