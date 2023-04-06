import re

def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\b\W*um\b\W", s)
    return(len(match))





if __name__ == "__main__":
  main()