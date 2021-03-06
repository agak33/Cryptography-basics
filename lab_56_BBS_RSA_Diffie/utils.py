

def modular_exp(num: int, power: int, mod_num: int) -> int:
    """
    Calculates num^power % mod_num in O(log(power)) time.
    """
    result: int = 1
    num %= mod_num

    if not num % mod_num:
        return 0

    while power > 0:
        if power % 2:
            result = (result * num) % mod_num

        power >>= 1
        num = (num * num) % mod_num

    return result


def inverse_under_modulo(a: int, n: int, minimum: int = 1000) -> int:
    """
    Calculates x in (a * x === 1 mod n) expression
    """
    for x in range(minimum, n):
        if (a % n) * (x % n) % n == 1:
            return x
    return 0
