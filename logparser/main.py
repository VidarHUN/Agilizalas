from logparser.parser import Parser
def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(sum([1,2,3,4]))

def main():
    parser: Parser = Parser()
    parser.parse('../logs/WCG100140624.txt')
    parser.print()

if __name__ == '__main__':
    main()
