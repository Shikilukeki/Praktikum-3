# Praktikum 3 

Nama : Rifqi Maulana

Kelas : TI.24.A.5

NIM : 312410529

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari serangkaian bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga menginputkan `0` untuk mengakhiri perulangan input dan menetapkan bilangan terbesar. 

Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## Flowchart 
![Foto](https://github.com/Shikilukeki/Foto/blob/main/Flowchart%20mencari%20bilangan%20terbesar.png?raw=true)

## Penjelasan kode Program
```python
def find_max():
    MAX = float('-inf')  # Inisialisasi MAX dengan nilai negatif tak terhingga
    while True: # Perulangan hingga syarat terpenuhi
        x = float(input("Input x (bilangan): "))  # Penginputan bilangan
        if x == 0:
            break  # Keluar dari loop jika x adalah 0
        if x > MAX:
            MAX = x  # Update MAX jika x lebih besar dari MAX
    print("Output =", MAX)  # Output nilai MAX terbesar

find_max()

```

## Contoh Hasil Eksekusi Program
![Foto](https://github.com/Shikilukeki/Foto/blob/main/screenshoot.png?raw=true)
