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
```
Perintah `def find_max():` adalah bagian dari sintaks dalam bahasa pemrograman Python yang digunakan untuk mendefinisikan sebuah fungsi bernama `find_max()`. Fungsi ini untuk menulis serangkaian instruksi yang dapat dipanggil berkali-kali dalam program.

```python
MAX = int('0')
```
Inisialisasi variabel MAX dengan nilai integer `0`. `int('0')` memastikan bahwa nilai `0` adalah integer

```python
while True:
```
Memulai loop while yang akan terus berjalan hingga dihentikan dengan perintah `break`.

```python
x = int(input("Inputkan Bilangan x : "))
```
Meminta pengguna untuk menginputkan bilangan. Input ini kemudian diubah menjadi integer dan disimpan dalam variabel `x`

```python
if x == 0:
```
Mengecek apakah nilai `x` adalah `0`. Jika iya, maka program akan keluar dari loop.

```python
break
```
Menghentikan eksekusi loop while jika kondisi `if x == 0:` terpenuhi.

```python
if x > MAX:
```
Mengecek apakah nilai `x` lebih besar dari nilai `MAX` saat ini.

```python
MAX = x
```
Jika kondisi `if x > MAX` terpenuhi, nilai `MAX` diperbarui menjadi nilai `x`.

```python
print("Bilangan terbesar adalah :", MAX)
```
Setelah loop berhenti (ketika pengguna menginput 0), program mencetak nilai `MAX` yang merupakan bilangan terbesar yang diinputkan pengguna.

```python
find_max()
```
Memanggil fungsi `find_max` untuk menjalankan semua instruksi yang ada di dalamnya.

## Contoh Hasil Eksekusi Program
![Foto](https://github.com/Shikilukeki/Foto/blob/main/screenshoot.png?raw=true)
