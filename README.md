# Super Converter

Developed by `XiaoYao`, Super Converter is a powerful, multi-functional command-line utility. It began as a simple number base converter and has evolved into a comprehensive toolkit for a wide range of numerical and text-based encoding and decoding tasks.

## ✨ Features

This tool provides a simple, menu-driven interface that supports the following conversion categories:

### 1. Arbitrary Base Conversion
- **Universal Base Support**: Convert numbers between any two bases from **base-2 to base-62**.
- **Common Bases Covered**: Effortlessly handle standard binary (base-2), octal (base-8), decimal (base-10), and hexadecimal (base-16) conversions.
- **Extended Character Set**: Uses `0-9`, `a-z`, and `A-Z` to represent digits, enabling support for up to base-62.

### 2. Text to Binary Stream Conversion
- **Text-to-Binary**: Encodes any text string (e.g., "Hello") into its corresponding 8-bit ASCII binary stream.
  - *Example*: `A` → `01000001`
- **Binary-to-Text**: Decodes an 8-bit binary stream back into its original, human-readable text.
  - *Example*: `01000001` → `A`

### 3. Text Encoding Conversion
- **ASCII Conversion**: Convert back and forth between a text string and its corresponding ASCII decimal values.
  - *Example*: `ABC` ↔ `65 66 67`
- **Hexadecimal Conversion**: Convert back and forth between a text string and its corresponding hexadecimal representation.
  - *Example*: `ABC` ↔ `41 42 43`

### 4. Robust and User-Friendly
- **Clear Interactive Menu**: Use simple number selections to access all features.
- **Detailed User Guidance**: Provides clear instructions and format requirements at every step.
- **Intelligent Error Handling**: Catches invalid inputs gracefully and provides friendly error messages instead of crashing.

## 🚀 How to Use

### 1. Prerequisites
- **Python 3.x**

### 2. Running the Program
Launch the interactive menu by running the Python script directly in your terminal:
```bash
python your_script_name.py
```
*(Please replace `your_script_name.py` with the actual name of your file)*

### 3. Example Usage
Once the program starts, you will see a list of available operations.

```
==================================================
Super Converter
Author: XiaoYao & Manus
Organization: AlfaNet
==================================================

Please select an operation:
1. Arbitrary Base Number Conversion
2. String -> ASCII (Decimal)
3. String -> Hexadecimal
4. ASCII (Decimal) -> String
5. Hexadecimal -> String
6. Text -> 8-bit Binary Stream (e.g., 'A' -> '01000001')
7. 8-bit Binary Stream -> Text (e.g., '01000001' -> 'A')
8. Exit

Enter your choice (1-8):
```

Simply type the number corresponding to the feature you wish to use and follow the on-screen prompts.

**For example, to convert the text "QAX" to a binary stream:**
1. Enter `6` and press Enter.
2. When prompted with `Enter the text to convert to a binary stream:`, type `QAX` and press Enter.
3. The program will display the result:
   ```
   8-bit binary stream (space-separated): 01010001 01000001 01011000
   Continuous binary stream: 010100010100000101011000
   ```

## Future Development & Contributions

Contributions and feature suggestions are always welcome! Potential future enhancements include:
-   **Graphical User Interface (GUI)**: Creating a desktop application using Tkinter or PyQt.
-   **Web Application**: Deploying the tool online using a framework like Flask or Django.
-   **Batch File Processing**: Adding the ability to read content from a file and convert it in bulk.
-   **More Encoding/Encryption Schemes**: Implementing algorithms like Base64, URL encoding, or Caesar cipher.

Feel free to open an issue or submit a pull request if you have any ideas!
