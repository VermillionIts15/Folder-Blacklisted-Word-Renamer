import os
import json
import random
import string
import datetime

def load_config():
    try:
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        return config_data
    except FileNotFoundError:
        print("Error: config.json not found. Please create a config file.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the config file. {str(e)}")
        return None

def generate_random_sequence():
    return ''.join(random.choices(string.digits, k=5))

def rename_files(directory, blacklist, whitelist):
    log_directory = os.path.join(directory, "log")
    os.makedirs(log_directory, exist_ok=True)
    log_file_name = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".log"
    log_file_path = os.path.join(log_directory, log_file_name)
    with open(log_file_path, "w") as log_file:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            for blacklisted_name, replacement in blacklist.items():
                if blacklisted_name in filename:
                    whitelisted_name = whitelist.get(blacklisted_name, None)
                    if whitelisted_name is None:
                        new_filename = filename.replace(blacklisted_name, replacement)
                        if not new_filename:
                            new_filename = (
                                whitelist.get("default_name", "default_name")
                                + generate_random_sequence()
                            )
                        new_path = os.path.join(directory, new_filename)
                        os.rename(file_path, new_path)
                        log_file.write(
                            f"Old Name: {filename} | New Name: {new_filename} ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n"
                        )
                        print(f"Renamed: {filename} -> {new_filename}")
                    else:
                        print(f"Skipped: {filename} (Whitelisted)")

def main():
    config = load_config()
    if config is None:
        return

    blacklist = config.get("blacklist", {})
    whitelist = config.get("whitelist", {})
    IsFolderPath = config.get("IsFolderPath", True)
    
    if not IsFolderPath:
        directory = os.path.dirname(os.path.abspath(__file__))
    else:
        directory = config.get("folder_path", os.path.dirname(os.path.abspath(__file__)))

    while True:
        print("(1) Start Renaming")
        print("(2) Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            rename_files(directory, blacklist, whitelist)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
