# Mass Remove From File Name Script

This Python script allows you to perform mass renaming of files in a directory based on a blacklist and whitelist. It also handles errors gracefully and provides configuration options for customization.

## How It Works

1. **Configuration**

   - The script loads settings from a `config.json` file in the same directory. If the `config.json` file doesn't exist, it will display an error message and exit.
   
   - The `config.json` file contains the following settings:
     - `"blacklist"`: A dictionary of names to be replaced and their corresponding replacements.
     - `"whitelist"`: A dictionary of files that should not be altered during renaming.
     - `"IsFolderPath"`: A boolean toggle. If `true`, the script will use the folder path specified in `"folder_path"`; if `false`, it will use its own directory as the target folder.
     - `"folder_path"`: The path to the directory containing the files to be renamed. This is used only when `"IsFolderPath"` is `true`.
     - `"create_backup"`: A boolean toggle. If `true`, the script will create a backup of original files before renaming.
   
   - Modify the `config.json` file to customize the blacklist, whitelist, folder path, backup settings, and other options.

2. **Renaming Files**

   - When you run the script, it will display options:
     - `(1) Start Renaming`: Initiates the renaming process.
     - `(2) Exit`: Exits the script.
   
   - If you choose to start renaming, the script will:
     - Rename files in the specified directory based on the blacklist and whitelist settings.
     - Create a log folder if it doesn't exist, and write a log file with the changes made, including the old and new file names and timestamps.
     - If a file would end up without a name, it will generate a new name based on the whitelist and a random 5-digit number sequence.
     - Display renaming progress in the console.
   
3. **Error Handling**

   - The script includes error handling to catch and display exceptions without revealing sensitive information.
   
   - If any errors occur during operation, the script will print error messages with details about the issue, allowing you to diagnose and address the problem.

## Usage

1. Clone this repository or download the script and the `config.json` file.

2. Modify the `config.json` file to customize the settings for your renaming needs.

3. Run the script by executing it with Python:

   ```bash
   python script.py
    ```

4. Follow the on-screen prompts to start renaming or exit the script.

## Example `config.json`

```json
{
    "blacklist": {
        "blacklisted_name1": "replacement1",
        "blacklisted_name2": "replacement2"
    },
    "whitelist": {
        "file_to_keep1": "file_to_keep1"
    },
    "IsFolderPath": true,
    "folder_path": "/path/to/your/directory",
    "create_backup": true
}
```

Replace the values in `"blacklist"`, `"whitelist"`, `"IsFolderPath"`, `"folder_path"`, and `"create_backup"` with your desired configuration.

## Notes
- Always make backups of your files before running the script to avoid data loss.

- Review the log files in the log folder to track changes made by the script.

- It should be easy to do modifications to the code.

- Before opening an issue, make sure you have the logs or anything to help identify the source of the error.

- I added a new feature that allows you to create backups of your original files, enhancing file renaming safety. (Someone had a problem so I think this could help anyone in the near future.)

### Version: 0.7 - "Backup"
