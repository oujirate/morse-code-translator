# Morse Code Translator
Python CLI script used to translate morse code to text or text to morse code. In addition, it can also be used to code or encode files that contain text or morse code. The script is run on the Command Line Interface (CLI) with instructions that are easy to understand. Hopefully, this script can help or make it easier for users to translate the morse password.

## Restrictions
- Can only be run on Terminal or Command Prompt and the like.
- Morse code only supports alphabetic, numeric and some symbols as follows: `?` , `!` , `.` , `;` , `:` , `+` , `-` , `/` , `=` , `,`.
- It can only translate morse ciphers in text or text in a file, it cannot translate through audio.
- Writing spaces in morse code using the `/` sign.
  
## Installation & Usage of the script
1. Install python in the microsoft store or on the official website [python.org](https://www.python.org/downloads/).
2. copy the `morse-code-translator` repo to the local directory.
    ```sh
    git clone https://github.com/oujisan/morse-code-translator.git
    ```
3. Open a terminal and run the script in the file `morsecode.py`
   ```sh
   python morsecode.py
   ```
   This will lead to the instructions for using the script and an example.
   
## Argument Documentation
**USAGE** :
```sh
python morsedecode.py [options] <teks/file> -o <output>`
```
(The `-o` argument can be used optionally in the codefile or decodefile. If no `-o` is used, the result of de/code will automatically be in `morse-code-translator/output.txt`)
- `-c`, `-code`: Convert text into morse code and display it on the terminal.
- `-d` , `-decode` : Converts morse cipher to text and displays it on the terminal.
- `-cf`, `-codefile` : Convert a file containing a collection of text to morse cipher without changing the line position of the file.
- `-df`, `-decodefile` : Convert a file containing a collection of morse ciphers to text without changing the line position of the file.
- `-h`, `--help` : Display a message to help the user use the script.

## Usage Example
```sh
python morsecode.py -c “Lorem Ipsum”
```
```sh
python morsecode.py -df “sandi.txt” -o “D:/data/output.txt”
```

## Build-In
- Windows 10 Pro 64-Bit 10.0.19045 Build 19045
- Visual Studio Code 1.19.1
- Python 3.12.2
<br>

**Created date: Jum'at, 26 Juli 2024**
