import os 

def main():
    name = os.getenv("USERNAME")
    language = os.getenv("LANGUAGE")
    print(f"Hola {name} mundo desde Github Actions y mi lenguage favorito es {language}!")

if __name__ == "__main__":
    main()