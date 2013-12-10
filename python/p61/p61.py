# http://projecteuler.net/problem=61

P = { 3: lambda n: n * (n + 1) / 2,
      4: lambda n: n * n,
      5: lambda n: n * (3 * n - 1) / 2,
      6: lambda n: n * (2 * n - 1),
      7: lambda n: n * (5 * n - 3) / 2,
      8: lambda n: n * (3 * n - 2) }


triangle_nums   = { P[3](n) for n in range(1000) if 1000 <= P[3](n) <= 9999 }
square_nums     = { P[4](n) for n in range(1000) if 1000 <= P[4](n) <= 9999 }
pentagonal_nums = { P[5](n) for n in range(1000) if 1000 <= P[5](n) <= 9999 }
hexagonal_nums  = { P[6](n) for n in range(1000) if 1000 <= P[6](n) <= 9999 }
heptagonal_nums = { P[7](n) for n in range(1000) if 1000 <= P[7](n) <= 9999 }
octagonal_nums  = { P[8](n) for n in range(1000) if 1000 <= P[8](n) <= 9999 }
