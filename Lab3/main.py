def park_miller(seed: int, n: int) -> list:
    """
    Implementation of Park-Miller generator.

    Args:
        seed (int): The seed value for the generator.
        n (int): The number of numbers to generate.

    Returns:
        list: A list of n pseudorandom number generated by the Park-Miller generator.
    """

    # Set constants
    a = 16807
    m = 2_147_483_647
    q = m // a  # 127_773
    r = m % a  # 2836

    # list generate numbers
    numbers = []

    for i in range(n):
        hi = seed // q
        lo = seed - q * hi
        seed = a * lo - r * hi
        if seed < 0:
            seed += m

        numbers.append(seed)

    return numbers


def lecuyer(seed1: int, seed2: int, n: int) -> list:
    """
    Implementation of L'Ecuyer generator.

    Args:
        seed1 (int): The seed value for the first generator.
        seed2 (int): The seed value for the second generator.
        n (int): The number of numbers to generate.

    Returns:
        list: A list of n pseudorandom numbers generated by the L'Ecuyer generator.
    """

    # Initialize constants
    m1 = 2 ** 31 - 1
    m2 = 2 ** 29 - 1
    a1 = 16807
    a2 = 48271
    q1 = m1 // a1
    q2 = m2 // a2
    r1 = m1 % a1
    r2 = m2 % a2

    # Initialize state
    x1 = seed1 % m1
    x2 = seed2 % m2

    # list generate numbers
    numbers = []

    for i in range(n):
        # Compute new states
        k1 = x1 // q1
        x1 = a1 * (x1 % q1) - r1 * k1
        if x1 < 0:
            x1 += m1

        k2 = x2 // q2
        x2 = a2 * (x2 % q2) - r2 * k2
        if x2 < 0:
            x2 += m2

        # Compute pseudorandom number
        numbers.append((x1 - x2) % m1)

    return numbers


def lcg(a: int, c: int, m: int, seed: int, n: int) -> int:
    """
    Implementation of linear congruential generator.

    Args:
        a (int): Multiplier.
        c (int): Increment.
        m (int): Modulus.
        seed (int): The seed value for the generator.
        n (int): The number of numbers to generate.

    Returns:
        list: A list of n pseudorandom number generated by the LCG.
    """
    # list generate numbers
    numbers = []

    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers


def bbs(p: int, q: int, seed: int, n: int) -> int:
    """
    Implementation of Blum-Blum-Shub generator.

    Args:
        p (int): A large prime number.
        q (int): Another large prime number (not equal to p).
        seed (int): The seed value for the generator.
        n (int): The number of bits to generate.

    Returns:
        list: A list of n pseudorandom numbers generated by the BBS generator.
    """
    # generate number
    numbers = []

    # generate bits
    bits = []

    # Blum integer
    m = p * q

    seed = (seed ** 2) % m

    for _ in range(n):
        length = park_miller(seed, 1)[0] % 30
        for _ in range(length):
            seed = (seed ** 2) % (p * q)
            bit = seed % 2
            bits.append(bit)
        numbers.append(int(''.join(map(str, bits)), 2))
        bits.clear()

    return numbers


def main():
    # set constant
    seed = 123456789
    n = 10
    #
    # Park-Miller
    print(f"Park-Miller generator {park_miller(seed, n)}")

    # L'Ecuyer
    seed1 = 123456789
    seed2 = 987654321

    print(f"L'Ecuyer generator: {lecuyer(seed1, seed2, n)}")

    # Linear congruential generator (LCG)
    a = 1_103_515_245
    c = 12_345
    m = 2 ** 31

    print(f"Linear congruential generator: {lcg(a, c, m, seed, n)}")

    # Blum-Blum-Shub (BBS)
    p = 24672462467892469787
    q = 396736894567834589803

    print(f"Blum-Blum-Shub (BBS): {bbs(p, q, seed, n)}")


if __name__ == '__main__':
    main()