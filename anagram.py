def anagram():
    print("-----Are those words Anagrams?-----")
    word1 = input("Enter first word: ").lower()
    word2 = input("Enter second word: ").lower()
    print("----------------------------------")

    if len(word1) != len(word2):
        return "They are not Anagrams!"
    char1 = {}
    char2 = {}

    #counts the chanractes of each word
    for char in word1:
        char1[char] = char1.get(char, 0) + 1
        #print(char1[char])
    
    for char in word2:
        char2[char] = char2.get(char, 0) + 1
        

    #compares the dictionaris
    if char1 == char2:
        return f"✅{word1} and {word2} are Anagrams✅"
    else:
        return f"❌{word1} and {word2} are NOT Anagrams❌"
    
print(anagram())