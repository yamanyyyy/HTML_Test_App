# 01 example.pyを作成して「hello world」と出力してください。
print("hello world")


# 02 greet関数を実装し、「こんにちは」と出力するようにしてください。関数を呼び出して、実際に出力されることを確認してください。
def greet():
    print("こんにちは")

greet()

#03 nameを引数に取り、「私の名前は{name}です」と出力するprint_name関数を実装し、関数を呼び出して動作を確認してください。
def print_name(name):
    print(f"私の名前は{name}です")

print_name("やまん＠51期")

# 04「おはようございます」という文字列を戻り値として返すget_greet関数を実装し、戻り値をprint関数で出力してください。
def get_greet():
    return "おはようございます"
greeting = get_greet()
print(greeting)

# 05 a, bを引数に取り、その足し算の結果を戻り値として返すadd関数を実装し、関数を呼び出して結果をprint関数で出力してください。
def add(a, b):
    return a + b
result = add(3, 5)
print(result)


