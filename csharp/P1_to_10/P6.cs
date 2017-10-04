using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=6
    /// </summary>
    internal class P6
    {
        private const int Max = 100;

        /// <summary>
        /// Calculate the difference between the square of sums of the numbers 1-100 and the 
        /// sum of squares of the numbers 1-100.
        /// </summary>
        public long Solve()
        {
            var squareOfSums = (long) Math.Pow(Enumerable.Range(1, Max).Sum(), 2);

            var sumOfSquares = Enumerable.Range(1, Max)
                .Select(x => x * x)
                .Sum();

            return squareOfSums - sumOfSquares;
        }
    }
}
