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
    /// https://projecteuler.net/problem=23
    /// </summary
    internal class P23
    {
        private const int Max = 28123;

        /// <summary>
        /// Calculates the sum of all positive integers that cannot be written as the sum of
        /// two abundant numbers.
        /// </summary>
        public int Solve()
        {
            var abundantNumbers = Enumerable.Range(1, Max).Where(IsAbundant).ToArray();
            var set = new HashSet<int>(abundantNumbers);
            var sum = 0;

            for (var i = 0; i <= Max; i++)
            {
                if (!abundantNumbers.Any(x => set.Contains(i - x)))
                {
                    // i cannot be expressed as sum of two abundant numbers; add it to the total
                    sum += i;
                }
            }

            return sum;
        }

        /// <summary>
        /// Returns true if the sum of the proper divisors of n is greater than n.
        /// </summary>
        private bool IsAbundant(int n)
        {
            return PrimeHelpers.Divisors(n).Sum() - n > n;
        }
    }
}