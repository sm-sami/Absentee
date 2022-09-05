# Absentee
## About:
Absentee is a command line tool to clean the attendance data obtained from Google Meet 

## Absentee v2.0
### What's new in v2.0:
- **Settings** in `config.json` to configure **delimiters** and **sleep time**
- `README.md` contains the about the app, changelog of the version, troubleshooting methods and the default values for `config.json`
- Improved user interface and readability
- Minor bug fixes
### Changes in v2.0:
- **No major change** that has an effect on the end-user
### Known Issues:
- There is **no known issue** in this version
## Troubleshooting
>**Note:** The `.exe` file and `config.json` must be in the same folder. 
>
>**Warning:** Changing the `optCode`or `optIndex` may result in errors

If none of the above solved your issue, try reverting `config.json` to its default values
### Default values for `config.json`:
``` json
{
  "app_name": "Absentee",
  "version": "v2.0",
  "available_opts" : ["Quick View", "CSV Cleaner", "CSV Cleaner (Override OG File)", "Quick View & CSV Cleaner"],
  "settings": {
    "delimiters": {
      "find": ["(RA", "RA"],
      "split": ["(", " "]
    },
    "sleepTime": {
      "desc": 10,
      "menu": 15,
      "exit": 5
    }
  },
  "opts": {
    "Quick View": {
      "inMenu": true,
      "optCode": "qv",
      "optIndex": "1",
      "desc": "To view only the RegNo of the absentees"
    },
    "CSV Cleaner": {
      "inMenu": true,
      "optCode": "cc",
      "optIndex": "2",
      "desc": "To clean the CSV and sort the RegNo in ascending order, the cleaned/sorted RegNo is written in a different file"
    },
    "CSV Cleaner (Override OG File)": {
      "inMenu": false,
      "optCode": "cco",
      "optIndex": "3",
      "desc": "To clean the CSV and sort the data in ascending order, the cleaned/sorted data is overwritten in the same file "
    },
    "Quick View & CSV Cleaner": {
      "inMenu": false,
      "optCode": "qvcc",
      "optIndex": "4",
      "desc": "To get the functionality of both Quick View & CSV Cleaner"
    }
  }
}
```
If the problem still persists then it might be a bug!
