
class mHello:
    def __init__(self, message):
        self.message = message

    def __format__(self, format_spec: any) -> str:
        match format_spec:
            case 'u':
                return self.message.upper()
            case 'l':
                return self.message.lower()
            case _:
                raise ValueError(f"Unknown specifier for mHello()")



m = mHello("Hello guys!")
print(f"{m:u} | {m:l}")
