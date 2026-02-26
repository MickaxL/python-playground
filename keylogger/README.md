# Educational Keylogger (Python)

A **purely educational** mini-project to understand how keyboard event capturing works using the `pynput` library.

**Important notice:**  
This code is created **only for learning purposes** (understanding listeners, keyboard events, file handling).  
Using this kind of code for malicious purposes is illegal and strictly forbidden.

## Current status (very early / beginner version)

- Captures **only** alphanumeric characters and punctuation
- **Does NOT handle**: space, enter, backspace, special keys (Ctrl, Shift, arrows, function keys…)
- Writes to `keyfile.txt` (or `keyfile.txt` depending on version)
- Prints every key to the console (for debugging)
- Extremely basic – learning / first-step version

## Requirements

```bash
pip install pynput