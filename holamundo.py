import os 

def main():
    name = os.getenv("USERNAME")
    print(f"Hola {name} mundo desde Github Actions!")

if __name__ == "__main__":
    main()