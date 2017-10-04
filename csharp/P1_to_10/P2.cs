using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;
using ProjectEuler.Helpers;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=2
    /// </summary>
    internal class P2
    {
        private const long Max = 4000000;

        /// <summary>
        /// Find sum of fibonacci numbers that are even and under 4,000,000
        /// </summary>
        public long Solve()
        {
            return FibonacciHelper.FibonacciNumbers()
                .TakeWhile(x => x < Max)
                .Where(x => x % 2 == 0)
                .Sum();
        }
    }
}
