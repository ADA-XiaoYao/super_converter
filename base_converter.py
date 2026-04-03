"""
进制转换器
作者: XiaoYao
组织: AlfaNet
功能: 支持二进制、八进制、十进制和十六进制之间的相互转换
"""

def binary_to_decimal(binary_str):
    """二进制转十进制"""
    return int(binary_str, 2)

def octal_to_decimal(octal_str):
    """八进制转十进制"""
    return int(octal_str, 8)

def hexadecimal_to_decimal(hex_str):
    """十六进制转十进制"""
    return int(hex_str, 16)

def decimal_to_binary(decimal_num):
    """十进制转二进制"""
    return bin(decimal_num)[2:]

def decimal_to_octal(decimal_num):
    """十进制转八进制"""
    return oct(decimal_num)[2:]

def decimal_to_hexadecimal(decimal_num):
    """十进制转十六进制"""
    return hex(decimal_num)[2:].upper()

def convert_number(number, from_base, to_base):
    """通用转换函数"""
    # 先将输入转换为十进制
    if from_base == 2:
        decimal_num = binary_to_decimal(number)
    elif from_base == 8:
        decimal_num = octal_to_decimal(number)
    elif from_base == 10:
        decimal_num = int(number)
    elif from_base == 16:
        decimal_num = hexadecimal_to_decimal(number)
    else:
        return "不支持的源进制"
    
    # 再从十进制转换为目标进制
    if to_base == 2:
        return decimal_to_binary(decimal_num)
    elif to_base == 8:
        return decimal_to_octal(decimal_num)
    elif to_base == 10:
        return str(decimal_num)
    elif to_base == 16:
        return decimal_to_hexadecimal(decimal_num)
    else:
        return "不支持的目标进制"

def main():
    print("=" * 50)
    print("进制转换器")
    print("作者: XiaoYao")
    print("组织: AlfaNet")
    print("=" * 50)
    
    while True:
        print("\n请选择源进制:")
        print("1. 二进制")
        print("2. 八进制")
        print("3. 十进制")
        print("4. 十六进制")
        print("5. 退出")
        
        from_choice = input("请输入选择 (1-5): ")
        
        if from_choice == '5':
            print("感谢使用进制转换器！")
            break
        
        if from_choice not in ['1', '2', '3', '4']:
            print("无效选择，请重新输入！")
            continue
        
        to_choice = input("请选择目标进制 (1-4): ")
        
        if to_choice not in ['1', '2', '3', '4']:
            print("无效选择，请重新输入！")
            continue
        
        # 映射选择到进制
        base_map = {'1': 2, '2': 8, '3': 10, '4': 16}
        from_base = base_map[from_choice]
        to_base = base_map[to_choice]
        
        number = input(f"请输入要转换的数字 (基数为{from_base}): ")
        
        try:
            result = convert_number(number, from_base, to_base)
            print(f"转换结果: {result}")
        except ValueError as e:
            print(f"输入错误: {e}")
            print("请确保输入的数字与所选进制匹配！")

if __name__ == "__main__":
    main()
