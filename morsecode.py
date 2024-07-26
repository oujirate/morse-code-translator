import sys
import argparse
import morsekit
class CommandLine:
    def run():
        parser = argparse.ArgumentParser(
            description="Morse Code Translate by oujirate",
            usage='python %(prog)s [options] "<text/file>" -o "<output file>"',
            epilog='''Example:
            python morsecode.py -c "Lorem Ipsum" |
            python morsecode.py -df "C:/text.txt" -o "output.txt"''' 
        )
        group = parser.add_mutually_exclusive_group()

        group.add_argument(
            "-c", "--code",
            type=str,
            help="Code text to morse code",
        )
        group.add_argument(
            "-d", "--decode",
            type=str,
            help="Decode morse code to text"
        )
        group.add_argument(
            "-cf", "--codefile",
            type=str,
            help="Code text in file to morse code"
        )
        group.add_argument(
            "-df", "--decodefile",
            type=str,
            help="Decode morse code in file to text"
        )
        parser.add_argument(
            "-o", "--output",
            type=str,
            help="File output location"
        )
        args = parser.parse_args()

        if not len(sys.argv) > 1:
            parser.print_help()
            sys.exit()

        if args.code:
            code = morsekit.core.code(args.code)
            print(code) if code else None
            
        elif args.decode:
            decode = morsekit.core.decode(args.decode)
            print(decode) if decode else None

        elif args.codefile:
            if args.output:
                morsekit.core.codefile(args.codefile,args.output)
            else:
                morsekit.core.codefile(args.codefile)
        
        elif args.decodefile:
            if args.output:
                morsekit.core.codefile(args.codefile,args.output)
            else:
                morsekit.core.decodefile(args.decodefile)
        

if __name__ == "__main__":
    CommandLine.run()