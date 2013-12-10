# http://projecteuler.net/problem=61

def solve(curr_sequence, all_num_lists, used):
    if len(used) == 6 and curr_sequence[-1][-2:] == curr_sequence[0][:2]:
        return sum(map(int, curr_sequence))

    for pos, num_list in enumerate(all_num_lists):
        if pos in used:
            continue

        used.add(pos)
        for num in num_list:
            if len(curr_sequence) == 0 or curr_sequence[-1][-2:] == num[:2]:
                curr_sequence.append(num)
                ret = solve(curr_sequence, all_num_lists, used)
                if ret:
                    return ret
                curr_sequence.pop()

        used.remove(pos)

    
P = { 3: lambda n: n * (n + 1) / 2,
      4: lambda n: n * n,
      5: lambda n: n * (3 * n - 1) / 2,
      6: lambda n: n * (2 * n - 1),
      7: lambda n: n * (5 * n - 3) / 2,
      8: lambda n: n * (3 * n - 2) }

triangle_nums   = [ str(P[3](n)) for n in range(1000) if 1000 <= P[3](n) <= 9999 ]
square_nums     = [ str(P[4](n)) for n in range(1000) if 1000 <= P[4](n) <= 9999 ]
pentagonal_nums = [ str(P[5](n)) for n in range(1000) if 1000 <= P[5](n) <= 9999 ]
hexagonal_nums  = [ str(P[6](n)) for n in range(1000) if 1000 <= P[6](n) <= 9999 ]
heptagonal_nums = [ str(P[7](n)) for n in range(1000) if 1000 <= P[7](n) <= 9999 ]
octagonal_nums  = [ str(P[8](n)) for n in range(1000) if 1000 <= P[8](n) <= 9999 ]

all_nums = [triangle_nums, square_nums, pentagonal_nums, 
            hexagonal_nums, heptagonal_nums, octagonal_nums]     

print solve([], all_nums, set())
