from stats import analyze_book
import sys


def main():
    print("Usage: python3 main.py <path_to_book>")
    print(sys.argv[1])
    analyze_book(sys.argv[1])
    
    

if __name__ == "__main__":
    main()
    