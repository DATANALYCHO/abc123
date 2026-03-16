def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("0으로는 나눌 수 없습니다.")
    return a / b


def calculate(expression: str) -> float:
    """
    간단한 이항 연산 표현식만 지원:
      - 예) "1 + 2", "3 - 4", "5 * 6", "8 / 2"
    """
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("입력 형식은 '숫자 연산자 숫자'여야 합니다. 예: 1 + 2")

    left_str, op, right_str = parts

    try:
        left = float(left_str)
        right = float(right_str)
    except ValueError as exc:
        raise ValueError("숫자 부분을 해석할 수 없습니다.") from exc

    if op == "+":
        return add(left, right)
    if op == "-":
        return subtract(left, right)
    if op == "*":
        return multiply(left, right)
    if op == "/":
        return divide(left, right)

    raise ValueError("지원하지 않는 연산자입니다. +, -, *, /만 사용할 수 있습니다.")


def main() -> None:
    print("파이썬 계산기 (종료하려면 q 입력)")
    while True:
        expr = input("수식을 입력하세요 (예: 1 + 2): ").strip()
        if expr.lower() in {"q", "quit", "exit"}:
            print("계산기를 종료합니다.")
            break

        if not expr:
            continue

        try:
            result = calculate(expr)
            print(f"결과: {result}")
        except Exception as e:  # noqa: BLE001
            print(f"에러: {e}")


if __name__ == "__main__":
    main()

