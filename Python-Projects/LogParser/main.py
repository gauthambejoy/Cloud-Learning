from LogParser import get_journalctl,parse_log

def main():
    logs=get_journalctl()
    result=parse_log(logs)
    print(result)

if __name__ == "__main__":
    main()