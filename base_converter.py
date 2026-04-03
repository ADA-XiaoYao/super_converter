"""
超级转换器
作者: XiaoYao
组织: AlfaNet
功能: 支持进制转换、字符编码转换以及文本与二进制流的相互转换。
"""

class SuperConverter:
    """
    一个功能强大的转换器，集成了进制、字符编码和文本-二进制流转换。
    """
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # --- 核心进制转换逻辑 ---
    def to_decimal(self, number_str: str, from_base: int) -> int:
        """将任意进制的字符串转换为十进制整数。"""
        decimal_value = 0
        for char in number_str:
            if self.ALPHABET.index(char) >= from_base:
                raise ValueError(f"字符 '{char}' 对于 {from_base} 进制是无效的")
            decimal_value = decimal_value * from_base + self.ALPHABET.index(char)
        return decimal_value

    def from_decimal(self, decimal_num: int, to_base: int) -> str:
        """将十进制整数转换为任意进制的字符串。"""
        if decimal_num == 0:
            return "0"
        result_str = ""
        while decimal_num > 0:
            result_str = self.ALPHABET[decimal_num % to_base] + result_str
            decimal_num //= to_base
        return result_str

    def convert_base(self, number_str: str, from_base: int, to_base: int) -> str:
        """在任意两个进制之间转换数字字符串。"""
        if not (2 <= from_base <= 62 and 2 <= to_base <= 62):
            return "错误: 进制数必须在 2 和 62 之间。"
        decimal_value = self.to_decimal(number_str, from_base)
        return self.from_decimal(decimal_value, to_base)

    # --- 字符编码转换 ---
    def string_to_ascii_dec(self, text: str) -> str:
        return ' '.join(str(ord(char)) for char in text)

    def string_to_hex(self, text: str) -> str:
        return ' '.join(hex(ord(char))[2:].upper() for char in text)

    def ascii_dec_to_string(self, ascii_str: str) -> str:
        return ''.join(chr(int(num)) for num in ascii_str.split())

    def hex_to_string(self, hex_str: str) -> str:
        return ''.join(chr(int(h, 16)) for h in hex_str.split())

    # --- 新增：文本与二进制流转换 ---
    def text_to_binary_stream(self, text: str, separator: str = ' ') -> str:
        """将文本字符串转换为由8位二进制码组成的流。"""
        binary_chunks = []
        for char in text:
            # 1. ord(char) 获取字符的ASCII十进制值
            # 2. bin() 转换为二进制字符串 (例如 '0b1010001')
            # 3. [2:] 去掉前缀 '0b'
            # 4. .zfill(8) 在左侧补0，确保总是8位长度
            binary_chunks.append(bin(ord(char))[2:].zfill(8))
        return separator.join(binary_chunks)

    def binary_stream_to_text(self, binary_str: str) -> str:
        """将8位二进制码组成的流转换回文本字符串。"""
        # 移除所有可能的空格或分隔符
        cleaned_binary_str = binary_str.replace(' ', '').replace('\n', '')
        
        if len(cleaned_binary_str) % 8 != 0:
            raise ValueError("二进制字符串的长度必须是8的倍数。")
            
        text_chars = []
        # 每8个字符切分一次
        for i in range(0, len(cleaned_binary_str), 8):
            byte = cleaned_binary_str[i:i+8]
            # 1. int(byte, 2) 将二进制字符串转换为十进制整数
            # 2. chr() 将整数转换为对应的ASCII字符
            text_chars.append(chr(int(byte, 2)))
        return ''.join(text_chars)


def main():
    """主函数，处理用户交互。"""
    converter = SuperConverter()
    print("=" * 50)
    print("超级转换器")
    print("作者: XiaoYao")
    print("组织: AlfaNet")
    print("=" * 50)
    
    while True:
        print("\n请选择要执行的操作:")
        print("1. 任意进制数字转换")
        print("2. 字符串 -> ASCII (十进制)")
        print("3. 字符串 -> 十六进制")
        print("4. ASCII (十进制) -> 字符串")
        print("5. 十六进制 -> 字符串")
        print("6. 文本 -> 8位二进制流 (例如 'A' -> '01000001')")
        print("7. 8位二进制流 -> 文本 (例如 '01000001' -> 'A')")
        print("8. 退出")
        
        choice = input("请输入选择 (1-8): ")
        
        try:
            if choice == '1':
                from_base = int(input("请输入源进制 (2-62): "))
                to_base = int(input("请输入目标进制 (2-62): "))
                number_str = input(f"请输入要转换的数字 (基数为 {from_base}): ")
                result = converter.convert_base(number_str, from_base, to_base)
                print(f"转换结果: {result}")

            elif choice == '2':
                text = input("请输入要转换的字符串: ")
                result = converter.string_to_ascii_dec(text)
                print(f"ASCII (十进制) 表示: {result}")

            elif choice == '3':
                text = input("请输入要转换的字符串: ")
                result = converter.string_to_hex(text)
                print(f"十六进制表示: {result}")

            elif choice == '4':
                ascii_str = input("请输入以空格分隔的ASCII十进制值: ")
                result = converter.ascii_dec_to_string(ascii_str)
                print(f"转换后的字符串: {result}")

            elif choice == '5':
                hex_str = input("请输入以空格分隔的十六进制值: ")
                result = converter.hex_to_string(hex_str)
                print(f"转换后的字符串: {result}")

            elif choice == '6':
                text = input("请输入要转换为二进制流的文本: ")
                result = converter.text_to_binary_stream(text)
                print(f"8位二进制流表示 (按字节分隔): {result}")
                # 也显示一个不带空格的版本
                print(f"连续二进制流: {result.replace(' ', '')}")

            elif choice == '7':
                binary_str = input("请输入8位二进制码流 (可以用空格分隔): ")
                result = converter.binary_stream_to_text(binary_str)
                print(f"解码后的文本: {result}")

            elif choice == '8':
                print("感谢使用超级转换器！")
                break
            
            else:
                print("无效选择，请重新输入！")

        except ValueError as e:
            print(f"输入错误: {e}")
            print("请确保输入的数据格式正确！")
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()
