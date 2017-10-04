using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ProjectEuler.Helpers;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=3
    /// </summary>
    internal class P3
    {
        private const long Number = 600851475143;

        /// <summary>
        /// Returns the largest prime factor of the number 600851475143
        /// </summary>
        public int Solve()
        {
            return PrimeHelpers.PrimeFactors(Number).Max();
        }
    }
}
