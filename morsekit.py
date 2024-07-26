import json
class core:
    def code(text):
        try:
            result = ""
            with open("morse-code.json","r") as mc:
                morse = json.load(mc)
                for i in text:
                    if not text.isspace() and any(morse.keys()):
                        if i.isspace():
                            result += "/"
                            continue
                        result += morse[i.lower()]
                    else:
                        raise ValueError("Morse code must be alphanumeric or one of following symbols (?,!,'.',',',';',:,+,-,/,=)")
                    
                    result += " "
            return result

        except Exception as ex:
            print(f"Error: {ex}. Morse code must be alphanumeric or one of following symbols (?,!,'.',',',';',:,+,-,/,=)")

    def decode(text):
        try:
            result = ""
            with open("morse-code.json","r") as md:
                morse = json.load(md)
                morse_list = morse.items()

                if not text.isspace():
                    for word in text.split("/"):
                        for value in word.split(" "):
                            if value:
                                if value in morse.values():
                                    for keys,values in morse_list:
                                        if value == values:
                                            key = keys
                                            result += key
                                else:
                                    raise ValueError("Morse code Invalid!")
                        result += " "
                    return result
        except ValueError as ex:
            print(f"Error: {ex}")

    def codefile(file,path_file="output.txt"):
        try:
            result = ""
            with open(file,"r") as txt:
                textfile = txt.read()
                for lines in textfile.split("\n"):
                    if lines.isspace():
                        continue
                    line_code_txt = core.code(lines)
                    result += line_code_txt
                    result += "\n"

            with open(path_file, "w") as txt:
                txt.write(result)
            print(f"Code successful! Save on '{path_file}'")

        except Exception as ex:
            print(f"Eror: {ex}")

    def decodefile(file,path_file="output.txt"):
        try:
            result = ""
            with open(file,"r") as txt:
                textfile = txt.read()
                for lines in textfile.split("\n"):
                    if lines.isspace():
                        continue
                    line_decode_txt = core.decode(lines)
                    result += line_decode_txt
                    result += "\n"

            with open(path_file, "w") as txt:
                txt.write(result)
            print(f"Code successful! Save on '{path_file}'")

        except Exception as ex:
            print(f"Eror: {ex}")