"""
超级转换器 (国际版)
作者: XiaoYao
组织: AlfaNet
功能: 支持多语言界面，并提供进制转换、字符编码转换以及文本与二进制流的相互转换。
"""

# ==============================================================================
# 1. 语言资源中心 (Language Resource Center)
#    所有面向用户的文本都定义在这里。
# ==============================================================================
LANGUAGES = {
    "en": {
        "welcome_banner": "Super Converter (International Edition)",
        "author_line": "Author: XiaoYao",
        "org_line": "Organization: AlfaNet",
        "lang_prompt": "Please select a language:",
        "lang_options": "1. English\n2. 中文 (Chinese)\n3. Русский (Russian)",
        "invalid_choice": "Invalid choice, please try again!",
        "menu_prompt": "\nPlease select an operation:",
        "menu_options": [
            "Arbitrary Base Number Conversion",
            "String -> ASCII (Decimal)",
            "String -> Hexadecimal",
            "ASCII (Decimal) -> String",
            "Hexadecimal -> String",
            "Text -> 8-bit Binary Stream",
            "8-bit Binary Stream -> Text",
            "Exit"
        ],
        "input_from_base": "Enter the source base (2-62): ",
        "input_to_base": "Enter the target base (2-62): ",
        "input_number": "Enter the number to convert (base {base}): ",
        "input_string": "Enter the string to convert: ",
        "input_ascii": "Enter the space-separated ASCII decimal values: ",
        "input_hex": "Enter the space-separated hexadecimal values: ",
        "input_binary_stream": "Enter the 8-bit binary stream (spaces are allowed): ",
        "result_label": "Result: ",
        "binary_stream_sep": "8-bit binary stream (space-separated): ",
        "binary_stream_cont": "Continuous binary stream: ",
        "decoded_text": "Decoded text: ",
        "error_input": "Input Error: {error}",
        "error_generic": "An unexpected error occurred: {error}",
        "error_format": "Please ensure the input format is correct!",
        "error_base_range": "Error: Base must be between 2 and 62.",
        "error_binary_length": "Binary string length must be a multiple of 8.",
        "goodbye": "Thank you for using the Super Converter!"
    },
    "zh": {
        "welcome_banner": "超级转换器 (国际版)",
        "author_line": "作者: XiaoYao",
        "org_line": "组织: AlfaNet",
        "lang_prompt": "请选择语言:",
        "lang_options": "1. English\n2. 中文 (Chinese)\n3. Русский (Russian)",
        "invalid_choice": "无效选择，请重新输入！",
        "menu_prompt": "\n请选择要执行的操作:",
        "menu_options": [
            "任意进制数字转换",
            "字符串 -> ASCII (十进制)",
            "字符串 -> 十六进制",
            "ASCII (十进制) -> 字符串",
            "十六进制 -> 字符串",
            "文本 -> 8位二进制流",
            "8位二进制流 -> 文本",
            "退出"
        ],
        "input_from_base": "请输入源进制 (2-62): ",
        "input_to_base": "请输入目标进制 (2-62): ",
        "input_number": "请输入要转换的数字 (基数为 {base}): ",
        "input_string": "请输入要转换的字符串: ",
        "input_ascii": "请输入以空格分隔的ASCII十进制值: ",
        "input_hex": "请输入以空格分隔的十六进制值: ",
        "input_binary_stream": "请输入8位二进制码流 (可以用空格分隔): ",
        "result_label": "转换结果: ",
        "binary_stream_sep": "8位二进制流表示 (按字节分隔): ",
        "binary_stream_cont": "连续二进制流: ",
        "decoded_text": "解码后的文本: ",
        "error_input": "输入错误: {error}",
        "error_generic": "发生未知错误: {error}",
        "error_format": "请确保输入的数据格式正确！",
        "error_base_range": "错误: 进制数必须在 2 和 62 之间。",
        "error_binary_length": "二进制字符串的长度必须是8的倍数。",
        "goodbye": "感谢使用超级转换器！"
    },
    "ru": {
        "welcome_banner": "Супер Конвертер (Международная версия)",
        "author_line": "Автор: XiaoYao & Manus",
        "org_line": "Организация: AlfaNet",
        "lang_prompt": "Пожалуйста, выберите язык:",
        "lang_options": "1. English\n2. 中文 (Chinese)\n3. Русский (Russian)",
        "invalid_choice": "Неверный выбор, попробуйте еще раз!",
        "menu_prompt": "\nПожалуйста, выберите операцию:",
        "menu_options": [
            "Преобразование чисел между любыми системами счисления",
            "Строка -> ASCII (десятичный)",
            "Строка -> Шестнадцатеричный",
            "ASCII (десятичный) -> Строка",
            "Шестнадцатеричный -> Строка",
            "Текст -> 8-битный двоичный поток",
            "8-битный двоичный поток -> Текст",
            "Выход"
        ],
        "input_from_base": "Введите исходную систему счисления (2-62): ",
        "input_to_base": "Введите целевую систему счисления (2-62): ",
        "input_number": "Введите число для преобразования (основание {base}): ",
        "input_string": "Введите строку для преобразования: ",
        "input_ascii": "Введите десятичные значения ASCII, разделенные пробелами: ",
        "input_hex": "Введите шестнадцатеричные значения, разделенные пробелами: ",
        "input_binary_stream": "Введите 8-битный двоичный поток (пробелы допускаются): ",
        "result_label": "Результат: ",
        "binary_stream_sep": "8-битный двоичный поток (разделенный пробелами): ",
        "binary_stream_cont": "Непрерывный двоичный поток: ",
        "decoded_text": "Декодированный текст: ",
        "error_input": "Ошибка ввода: {error}",
        "error_generic": "Произошла непредвиденная ошибка: {error}",
        "error_format": "Пожалуйста, убедитесь, что формат ввода правильный!",
        "error_base_range": "Ошибка: Основание системы счисления должно быть от 2 до 62.",
        "error_binary_length": "Длина двоичной строки должна быть кратна 8.",
        "goodbye": "Спасибо за использование Супер Конвертера!"
    }
}

# ==============================================================================
# 2. 转换器核心逻辑 (Converter Core Logic)
#    这部分代码保持不变，因为它不涉及用户界面文本。
# ==============================================================================
class SuperConverter:
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def to_decimal(self, number_str: str, from_base: int) -> int:
        decimal_value = 0
        for char in number_str:
            if self.ALPHABET.index(char) >= from_base:
                raise ValueError(f"Character '{char}' is not valid for base {from_base}")
            decimal_value = decimal_value * from_base + self.ALPHABET.index(char)
        return decimal_value

    def from_decimal(self, decimal_num: int, to_base: int) -> str:
        if decimal_num == 0: return "0"
        result_str = ""
        while decimal_num > 0:
            result_str = self.ALPHABET[decimal_num % to_base] + result_str
            decimal_num //= to_base
        return result_str

    def convert_base(self, number_str: str, from_base: int, to_base: int, lang_dict: dict) -> str:
        if not (2 <= from_base <= 62 and 2 <= to_base <= 62):
            return lang_dict["error_base_range"]
        decimal_value = self.to_decimal(number_str, from_base)
        return self.from_decimal(decimal_value, to_base)

    def text_to_binary_stream(self, text: str, separator: str = ' ') -> str:
        return separator.join(bin(ord(char))[2:].zfill(8) for char in text)

    def binary_stream_to_text(self, binary_str: str, lang_dict: dict) -> str:
        cleaned_binary_str = binary_str.replace(' ', '').replace('\n', '')
        if len(cleaned_binary_str) % 8 != 0:
            raise ValueError(lang_dict["error_binary_length"])
        return ''.join(chr(int(cleaned_binary_str[i:i+8], 2)) for i in range(0, len(cleaned_binary_str), 8))
    
    # 其他转换函数保持不变，因为它们不直接与用户交互或抛出面向用户的错误
    def string_to_ascii_dec(self, text: str) -> str:
        return ' '.join(str(ord(char)) for char in text)

    def string_to_hex(self, text: str) -> str:
        return ' '.join(hex(ord(char))[2:].upper() for char in text)

    def ascii_dec_to_string(self, ascii_str: str) -> str:
        return ''.join(chr(int(num)) for num in ascii_str.split())

    def hex_to_string(self, hex_str: str) -> str:
        return ''.join(chr(int(h, 16)) for h in hex_str.split())

# ==============================================================================
# 3. 主程序与用户交互 (Main Program & User Interaction)
# ==============================================================================
def main():
    converter = SuperConverter()

    # --- 语言选择 ---
    print("=" * 50)
    print(LANGUAGES["en"]["lang_prompt"]) # Use a default for the initial prompt
    print(LANGUAGES["en"]["lang_options"])
    print("=" * 50)
    
    lang_choice = input("Enter your choice (1-3): ")
    if lang_choice == '2':
        lang_code = 'zh'
    elif lang_choice == '3':
        lang_code = 'ru'
    else: # Default to English
        lang_code = 'en'
        
    # 加载选定的语言字典
    T = LANGUAGES[lang_code]

    # --- 显示欢迎横幅 ---
    print("=" * 50)
    print(T["welcome_banner"])
    print(T["author_line"])
    print(T["org_line"])
    print("=" * 50)
    
    while True:
        # --- 显示主菜单 ---
        print(T["menu_prompt"])
        for i, option in enumerate(T["menu_options"], 1):
            print(f"{i}. {option}")
        
        choice = input(f"Enter your choice (1-{len(T['menu_options'])}): ")
        
        try:
            if choice == '1':
                from_base = int(input(T["input_from_base"]))
                to_base = int(input(T["input_to_base"]))
                number_str = input(T["input_number"].format(base=from_base))
                result = converter.convert_base(number_str, from_base, to_base, T)
                print(f"{T['result_label']}{result}")

            elif choice == '2':
                text = input(T["input_string"])
                result = converter.string_to_ascii_dec(text)
                print(f"{T['result_label']}{result}")

            elif choice == '3':
                text = input(T["input_string"])
                result = converter.string_to_hex(text)
                print(f"{T['result_label']}{result}")

            elif choice == '4':
                ascii_str = input(T["input_ascii"])
                result = converter.ascii_dec_to_string(ascii_str)
                print(f"{T['result_label']}{result}")

            elif choice == '5':
                hex_str = input(T["input_hex"])
                result = converter.hex_to_string(hex_str)
                print(f"{T['result_label']}{result}")

            elif choice == '6':
                text = input(T["input_string"])
                result = converter.text_to_binary_stream(text)
                print(f"{T['binary_stream_sep']}{result}")
                print(f"{T['binary_stream_cont']}{result.replace(' ', '')}")

            elif choice == '7':
                binary_str = input(T["input_binary_stream"])
                result = converter.binary_stream_to_text(binary_str, T)
                print(f"{T['decoded_text']}{result}")

            elif choice == str(len(T['menu_options'])): # 退出选项
                print(T["goodbye"])
                break
            
            else:
                print(T["invalid_choice"])

        except ValueError as e:
            print(T["error_input"].format(error=e))
            print(T["error_format"])
        except Exception as e:
            print(T["error_generic"].format(error=e))

if __name__ == "__main__":
    main()
