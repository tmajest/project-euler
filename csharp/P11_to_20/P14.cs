using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using MoreLinq;

namespace ProjectEuler.P11_to_20
{
    /// <summary>
    /// https://projecteuler.net/problem=14
    /// </summary>
    internal class P14
    {
        /// <summary>
        /// Find the starting value under 1 million that yields the longest collatz sequence.
        /// </summary>
        public int Solve()
        {
            return Enumerable.Range(1, 999999).MaxBy(CollatzSequenceLength);
        }

        /// <summary>
        /// Calculates the length of the collatz sequence that starts at the given number.
        /// </summary>
        public int CollatzSequenceLength(int start)
        {
            var count = 1;
            var value = (long) start;
            while (value > 1)
            {
                count++;
                value = value % 2 == 0
                    ? value / 2
                    : (value * 3) + 1;
            }

            return count;
        }
    }
}
