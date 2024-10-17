# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Rifqi Maulana

Kelas : TI.24.A.5

NIM : 312410529

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## Flowchart Program
![Foto](https://github.com/Shikilukeki/Foto/blob/main/flowchart.png?raw=true)

## Penjelasan kode Program
```python
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

```

## Screenshot Hasil Eksekusi Program
![Screenshot](screenshot.png)
