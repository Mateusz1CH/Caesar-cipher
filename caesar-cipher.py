alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while not (direction == "encode" or "decode"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
text_to_list = []
for i in range(0,len(text)):
    text_to_list.append(text[i])
#print("selected letters: {}".format(text_to_list))

def encrypt():
    message_encrypted = []
    for i in range (0,len(text_to_list)):
        if text_to_list[i] not in alphabet:
            message_encrypted.append(text_to_list[i])
        elif (alphabet.index(text_to_list[i]) + shift) < len(alphabet):
            index_to_be_found = alphabet.index(text_to_list[i]) + shift 
            message_encrypted.append(alphabet[index_to_be_found])
        elif (alphabet.index(text_to_list[i]) + shift) >= len(alphabet) : 
            index_to_be_found = ((alphabet.index(text_to_list[i]) + shift) - 26)
            message_encrypted.append(alphabet[index_to_be_found])
    return message_encrypted

def decode():
    message_decoded = []
    for i in range (0,len(text_to_list)):
        if text_to_list[i] not in alphabet:
            message_decoded.append(text_to_list[i])
        elif (alphabet.index(text_to_list[i]) - shift) >= 0:
            index_to_be_found = alphabet.index(text_to_list[i]) - shift 
            message_decoded.append(alphabet[index_to_be_found])
        elif (alphabet.index(text_to_list[i]) - shift) < 0: 
            index_to_be_found = ((alphabet.index(text_to_list[i]) - shift) + 26)
            message_decoded.append(alphabet[index_to_be_found])
    return message_decoded
    
if direction == "encode":
    message_encrypted= encrypt()
    #print(message_encrypted)
    output = ''.join(map(str, message_encrypted))
    print("\nYou message encrypted with Ceaser cipher:\n{}".format(output))
else:
    message_decoded = decode()
    output = ''.join(map(str, message_decoded))
    print("\nYou message decoded with Ceaser cipher:\n{}".format(output))