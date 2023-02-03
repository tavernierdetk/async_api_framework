import json
def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config
    

def main():
    print(load_config())

if __name__ == "__main__":
    main()
