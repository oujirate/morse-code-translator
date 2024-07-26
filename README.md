# Morse Code Translator
Script Python CLI yang digunakan untuk menerjemahkan sandi morse ke text maupun text ke sandi morse. Selain itu, juga bisa digunakan untuk code atau encode file yang berisi teks maupun sandi morse. Script dijalankan pada Command Line Interface(CLI) dengan petunjuk yang mudah untuk dimengerti. Semoga dengan adanya script ini dapat membantu atau memudahkan pengguna untuk menerjemahkan sandi morse.

## Batasan
- Hanya bisa dijalankan pada Terminal atau Command Prompt dan sejenisnya.
- Kode Morse hanya mendukung alphabet, numerik dan beberapa simbol sebagai berikut: `?` , `!` , `.` , `;` , `:` , `+` , `-` , `/` , `=` , `,`.
- Hanya bisa menerjemahkan sandi morse dalam bentuk text atau text di dalam file, belum bisa menerjemahkan melalui audio.
- Penulisan spasi pada sandi morse menggunakan tanda `/`
  
## Instalasi & Penggunaan script
1. Install python pada microsoft store atau pada website resmi [python.org](https://www.python.org/downloads/).
2. salin repo `morse-code-translator` ke local directory.
    ```sh
    git clone https://github.com/oujirate/morse-code-translator.git
    ```
3. Buka terminal dan jalankan script pada file `morsecode.py`
   ```sh
   python morsecode.py
   ```
   Maka akan diarahkan kepada petunjuk penggunaan dari script dan contohnya.
   
## Dokumentasi Argumen 
**USAGE** :
```sh
python morsedecode.py [options] <teks/file> -o <output>`
```
(Argumen `-o` dapat digunakan optional pada codefile atau decodefile. Apabila tidak memakai `-o` secara otomatis hasil dari de/code akan berada pada `morse-code-translator/output.txt`)
- `-c` , `--code` : Mengubah teks menjadi sandi morse dan menampilkannya pada terminal.
- `-d` , `--decode` : Mengubah sandi morse menjadi teks dan menampilkannya pada terminal.
- `-cf` , `--codefile` : Mengubah file yang berisi kumpulan teks menjadi sandi morse tanpa merubah posisi baris dari file.
- `-df` , `--decodefile` : Mengubah file yang berisi kumpulan sandi morse menjadi teks tanpa mengubah posisi baris dari file.
- `-h` , `--help` : Menampilkan pesan untuk membantu pengguna menggunakan script.

## Contoh Penggunaan
```sh
python morsecode.py -c "Lorem Ipsum"
```
```sh
python morsecode.py -df "sandi.txt" -o "D:/data/output.txt"
```

## Build-In
- Windows 10 Pro 64-Bit 10.0.19045 Build 19045
- Visual Studio Code 1.19.1
- Python 3.12.2
<br>

**Created date: Jum'at, 26 Juli 2024**
