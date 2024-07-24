from datetime import datetime
import time
import locale

n  = 1.818
x = f"{n:.2f}".replace('.', ',' )
print(x)


n  = 0.0088
x = f"{n:.2%}".replace('.', ',' )
print(x)


print('==>\n')
name = "Ivan"
print(f"{name} | {name:<10} | {name:>10}:")
print(f"|{name:^10}|")
print(f"|{name:#^20}|{name:_^20}")
alignment = '^'
print(f"|{name:{alignment}10}|")


print(f"-{name:*<10}")
print(f"Hello {name=}")
print(f"Hello {name.upper()=}")

s = " Now, do you know about the formatting mini-language?"
print(f"{s:<10.10}  -- {s:<10}")
print(f"{s:>10.10}  -- {s:>10}")


# x = 1234567890
# fst = f"{x:_} руб.".replace("_", "'")
# print(f"Итого: {fst}\nНапишите сумму прописью: ________________")

# num = 2323
# neg = -3232
# print(f"{num:>+5} | {num:> 5} | {neg:>+5} | {neg:> 5} |")
# print(f"{num:0>8} | {num:_>8} | {num:>+08} | {num:=+08} | {num:< 8n} |")
# num = 127825
# print(f"| {num:b} | {num:#b} | {num:#_b} | {num:x} | {num:c} |")

# # locale.setlocale(locale.LC_NUMERIC, 'sv_SE')
# # print(f"{num:0>8} | {num:_>8} | {num:>+08} | {num:=+08} | {num:< 8n} |")
# # locale.setlocale(locale.LC_NUMERIC, 'en_US')
# # print(f"{num:0>8} | {num:_>8} | {num:>+08} | {num:=+08} | {num:< 8n} |")






# # ppl = 1
# # num_str = f'{num:.2f}' if ppl else f'{num}'
# # final_str = f'I am {num_str}'
# # print(final_str)



# # n: int = 1_600_000_000
# # print(f"{n:_} | {n:,}")
# # print(f"{n:e} | {n:.2e}")

# # nf: float = 1.6e9
# # print(f"{nf:e} | {nf:.2e} | {nf:,.2f} | {nf:_.0f}")

# # nf: float = 1_000_000.123456
# # float_format: str = "_.2f"
# # print(f"{nf} | {nf:{float_format}}")


# # a: float = 0.1
# # b: float = 0.2
# # print(f"{a + b = :.1f}")


# # d: datetime = datetime.now()
# # print(f"{d} | {d:%d.%m.%y} | {d:%d.%m.%y (%H:%M:%S)} ")
# # print(f"{d:%c}")
# # print(f"{d:%I%p}")

# # date_spec: str = "%Y.%m.%d"
# # print(f"{d} | {d:{date_spec}}")



# # folder = 'Heap'
# # print(f"{folder = !s} | {folder = !r}")



# # path = fr"F:\Python_projects\MyTrials\F_string\{folder}"
# # print(path)

# # Eyes = '👀'     # https://glyphy.io/cool-symbols
# # look = 'Look'
# # d: datetime = datetime.now().date()
# # print(f"{d} {look} {Eyes}")
# # print(f"[{d!s}] {look!s} {Eyes!s}")
# # print(f"[{d!r}] {look!r} {Eyes!r}")
# # print(f"[{d!a}] {look!a} {Eyes!a}")


# # n = 7534.3595
# # print(f"*{f'${n:.3f}' :>15s}*")

# # l_device = "note"
# # width = 10
# # print(f'*{l_device:{width}}*')

# # n = 15
# # print(f'{"=" * n}')
# # print(f"{'':->40} ")
print(f"{'-' * 40}")

# # num_doors = 5
# # print(f"Shut the door{'s' if num_doors > 1 else ''}.")

# # f = False
# # d = 'rrrr'
# # c = 'sss'

# # print(f"{c if f else d}.")

# # print(f"{'11111' if f else '55555'}.")


# # number = 254.3463
# # print(f"{f'${number:.3f}':>10s}")

# # # for x in range(1, 11):
# # #     print(f'{x:02} {x * x:3} {x * x * x:4}')

# # # print(f"{70 + 4}")
# # # print(f"{{70 + 4}}")

# # # # бегущая строка
# # # for x in range(100):
# # #     print(f"Progress {(x/10):2.1%}", end="\r")
# # #     time.sleep(0.02)
# # # print()

# # # print (u"\u001b[31mHelloWorld")
# # # print (u"\u001b[38;5;11mHelloWorld")

