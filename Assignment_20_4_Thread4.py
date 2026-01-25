
import threading

def count_lowercase(s):
    small_count = 0
    for ch in s:
        if 'a' <= ch <= 'z':   
            small_count += 1
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)
    print("Lowercase characters count:", small_count)

def count_uppercase(s):
    capital_count = 0
    for ch in s:
        if 'A' <= ch <= 'Z':   
            capital_count += 1
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)
    print("Uppercase characters count:", capital_count)

def count_digits(s):
    digit_count = 0
    for ch in s:
        if '0' <= ch <= '9':   
            digit_count += 1
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)
    print("Digits count:", digit_count)

def main():

    print("Enter Alpha Numeric String")
    text = input()

    t1 = threading.Thread(target=count_lowercase, args=(text,), name="Small")
    t2 = threading.Thread(target=count_uppercase, args=(text,), name="Capital")
    t3 = threading.Thread(target=count_digits, args=(text,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
