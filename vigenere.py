import string
from collections import Counter

# Step 1: Function to calculate the frequency of letters in the text
def frequency_analysis(text):
    frequencies = Counter(text)
    return frequencies

# Step 2: Function to calculate the Index of Coincidence (IC)
def calculate_ic(text):
    frequencies = frequency_analysis(text)
    N = len(text)
    ic = sum(f * (f - 1) for f in frequencies.values()) / (N * (N - 1))
    return ic

# Step 3: Function to split text into groups based on key length
def split_text_by_key_length(text, key_length):
    groups = ['' for _ in range(key_length)]
    for i, char in enumerate(text):
        groups[i % key_length] += char
    return groups

# Step 4: Kasiski method to estimate key length
def estimate_key_length(text):
    probable_lengths = []
    for key_length in range(1, 21):  # Try key lengths up to 20
        groups = split_text_by_key_length(text, key_length)
        ics = [calculate_ic(group) for group in groups]
        avg_ic = sum(ics) / len(ics)
        if avg_ic > 0.06:  # IC close to 0.068 indicates natural language
            probable_lengths.append((key_length, avg_ic))
    return probable_lengths

# Step 5: Function to decrypt the Vigenère cipher given a key
def decrypt_vigenere(ciphertext, key):
    alphabet = string.ascii_uppercase
    decrypted_text = []
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char in alphabet:
            shift = alphabet.index(key[i % key_length])
            new_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# Step 6: Brute force frequency analysis to find key
def find_key(ciphertext, key_length):
    alphabet = string.ascii_uppercase
    key = ''
    
    # Split the ciphertext into key_length groups
    groups = split_text_by_key_length(ciphertext, key_length)
    
    # English letter frequency for comparison
    english_letter_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    
    for group in groups:
        group_freq = frequency_analysis(group)
        most_common = group_freq.most_common(1)[0][0]  # Get the most frequent letter
        shift = (alphabet.index(most_common) - alphabet.index('E')) % 26  # Assume 'E' is the most common letter
        key += alphabet[shift]
    
    return key

# Step 7: Main process
if __name__ == "__main__":
    print('enter the ciphertext : ')
    ciphertext = "XUKW LGEE YINN WBVL BWKU VXUC XLQY FJSH NHNV PRCW GQRP GMAA SHTP VHIO TSJU IGJI JGFS QVFQ QRMM AFIE IEEV IAEV LRXB VSBN WNUC BWWR GWRX IECP BHXU GQNT INXE VNEO NINP HNTI DWMG GEON IGQT RTJB TQNH VRSY RPGL CRNN CFKW NPHG JYFV SRXI AIYR UWGJ IFGG EGXX GCBH XUKW PKTU GVCN ELKR TCVB WRQY MGJX UGQP CROG EYQX BHJH PFHV RBYT YGEF GJBT KRVE OQYG VLVU EAEM RPXF VYSH JBTX UGVR UXBH XUKW PQYE UIVP XUGV ROEV PHRT SSVL RESH TWRY IJKP YHSP WWBP QBTI RNEO QVNV ISQV ZUSS UIPW VVVC GJEG EEAP SGDI OTSX GROA WHEL NUMZ RPRV IPJR VSYR"

    # Remove spaces and punctuation for analysis
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()

    # Step 1: Estimate key length using the Kasiski method
    probable_lengths = estimate_key_length(ciphertext)
    print("Probable key lengths: ", probable_lengths)

    # Step 2: Choose the most likely key length (based on Kasiski method)
    key_length = probable_lengths[0][0]  # For example, choose the first one (key length 6)

    # Step 3: Find the key based on the most frequent letters
    key = find_key(ciphertext, key_length)
    print(f"Estimated key: {key}")

    # Step 4: Decrypt the ciphertext using the key
    decrypted_text = decrypt_vigenere(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")
