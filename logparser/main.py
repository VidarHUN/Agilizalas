from logparser.parser import Parser


def main():
    parser: Parser = Parser()
    parser.parse('../logs/WCG100140624.txt')
    parser.print()


if __name__ == '__main__':
    main()
