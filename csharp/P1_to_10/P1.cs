using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=1
    /// </summary>
    internal class P1
    {
        private const int Start = 1;
        private const int Count = 999;

        /// <summary>
        /// Return sum of numbers under 1000 that are divisible by 3 or 5.
        /// </summary>
        public int Solve()
        {
            return Enumerable
                .Range(Start, Count)
                .Where(x => x % 3 == 0 || x % 5 == 0)
                .Sum();
        }
    }
}
