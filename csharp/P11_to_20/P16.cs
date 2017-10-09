using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using MoreLinq;
using ProjectEuler.Helpers;

namespace ProjectEuler.P11_to_20
{
    /// <summary>
    /// https://projecteuler.net/problem=16
    /// </summary>
    internal class P16
    {
        /// <summary>
        /// Calculate the sum of the digits for the number 2^1000
        /// </summary>
        /// <returns></returns>
        public int Solve()
        {
            // Calculate 2^1000
            var product = Enumerable.Range(1, 1000)
                .Select(x => new BigInteger(2))
                .Product();

            // Return sum of its digits
            return product
                .ToString()
                .Select(c => int.Parse(c.ToString()))
                .Sum();
        }

    }
}
