#Write a program which accepts one character and checks whether it is vowel or consonant.
def CheckVowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False
def main():
    Ch = input("Enter a Character : ")
    result = CheckVowel(Ch)
    if result == True:
        print(Ch, "is a Vowel")
    else:
        print(Ch, "is a Consonant")
if __name__ == "__main__":
    main()
    