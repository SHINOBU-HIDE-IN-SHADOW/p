class a():
    @overload
    def printer(a: int) -> int:
        print("int")
    @overload
    def printer(a: bytes) -> str:
        print("Sring")
    def printer(a):
        print(a)
printer(2)