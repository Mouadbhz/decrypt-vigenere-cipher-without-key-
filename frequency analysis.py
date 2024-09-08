from collections import Counter

def frequency_analysis(ciphertext):
    # Remove spaces and punctuation for the frequency analysis
    cleaned_text = ''.join(filter(str.isalpha, ciphertext))
    
    # Perform frequency analysis
    freq_count = Counter(cleaned_text)
    
    # Sort by frequency
    sorted_freq = freq_count.most_common()
    
    print("Letter Frequency Analysis:")
    for letter, freq in sorted_freq:
        print(f"{letter}: {freq}")

if __name__ == "__main__":
    ciphertext = "ugvhjbkuhjv ygjbv"
    frequency_analysis(ciphertext)
