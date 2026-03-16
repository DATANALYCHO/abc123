OPS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b}


def calc(expr: str) -> float:
    a, op, b = expr.split()
    if op not in OPS:
        raise ValueError("연산자는 +, -, *, /만 가능합니다.")
    a, b = float(a), float(b)
    if op == "/" and b == 0:
        raise ValueError("0으로는 나눌 수 없습니다.")
    return OPS[op](a, b)


if __name__ == "__main__":
    print("파이썬 계산기 (예: 1 + 2, 종료: q)")
    while (s := input("> ").strip()) not in {"q", "quit", "exit"}:
        if not s:
            continue
        try:
            print(calc(s))
        except Exception as e:
            print(f"에러: {e}")

