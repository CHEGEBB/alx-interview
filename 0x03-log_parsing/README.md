# Log Parsing

This script is designed to parse log entries from standard input (stdin), compute metrics, and print statistics based on the parsed data. It reads log entries in a specific format and calculates the total file size along with the count of each HTTP status code encountered.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow PEP 8 style guidelines (version 1.7.x)
- All files must be executable
- The length of your files will be tested using `wc`

### Tasks
- **Log parsing**:
  - **Mandatory**
  - Write a script that reads stdin line by line and computes metrics:
    - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
    - After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics:
      - Total file size: `File size: <total size>`
      - Number of lines by status code:
        - Status codes: 200, 301, 400, 401, 403, 404, 405, 500

## Usage

To use this script, follow these steps:

1. **Clone the repository:**

   ```
   git clone https://github.com/username/repo.git
   cd repo/0x03-log_parsing
   ```

2. **Generate log data using the provided generator script:**

   ```
   ./0-generator.py | ./0-stats.py
   ```

   This command pipes the output of `0-generator.py` (which generates random log entries) into `0-stats.py` for processing.

3. **Output Example:**

   ```
   File size: 5213
   200: 2
   401: 1
   403: 2
   404: 1
   405: 1
   500: 3
   ```

   The output shows the accumulated file size and the count of each status code encountered so far, updated after every 10 lines or a keyboard interruption.

## Example

For example, running `./0-generator.py | ./0-stats.py` will produce an output similar to the following:

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

This output reflects the accumulated file size and status code counts at different points during script execution.

## Author

- **CHEGEBB**
