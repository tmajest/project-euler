using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using ProjectEuler.Helpers;

namespace ProjectEuler.P11_to_20
{
    /// <summary>
    /// https://projecteuler.net/problem=20
    /// </summary>
    internal class P20
    {
        /// <summary>
        /// Calculates the sum of the digits in 100 factorial
        /// </summary>
        public int Solve()
        {
            // Calculate 100!
            var product = Enumerable.Range(1, 100)
                .Select(x => new BigInteger(x))
                .Product();

            // Return sum of its digits
            return product
                .ToString()
                .Sum(c => int.Parse(c.ToString()));
        }
    }
}