using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using ProjectEuler.Helpers;

namespace ProjectEuler.P21_to_30
{
    /// <summary>
    /// https://projecteuler.net/problem=21
    /// </summary>
    internal class P21
    {
        private const int Max = 10000;

        /// <summary>
        /// Calculates the sum of all amicable numbers under 10,000
        /// </summary>
        public int Solve()
        {
            var total = 0;

            for (var i = 1; i < Max; i++)
            {
                var sum = SumOfDivisors(i);
                if (sum != i && SumOfDivisors(sum) == i)
                {
                    // Found amicable pair; add i to total
                    total += i;
                }
            }

            return total;
        }

        /// <summary>
        /// Returns the sum of the proper divisors of a given number.
        /// Proper divisors are all numbers less than n that evenly divide n.
        /// </summary>
        private int SumOfDivisors(int n)
        {
            // Exclude n as a divisor since it is not a proper divisor
            return PrimeHelpers.Divisors(n).Sum() - n;
        }
    }
}