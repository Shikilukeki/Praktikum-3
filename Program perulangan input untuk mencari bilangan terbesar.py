def find_max():
    MAX = float('-inf')  # Inisialisasi MAX dengan nilai negatif tak terhingga
    while True:
        x = float(input("Input x (bilangan): "))  # Input bilangan
        if x == 0:
            break  # Keluar dari loop jika x adalah 0
        if x > MAX:
            MAX = x  # Update MAX jika x lebih besar dari MAX
    print("Output =", MAX)  # Output nilai MAX terbesar

find_max()

