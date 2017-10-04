using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;
using ProjectEuler.Helpers;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=10
    /// </summary>
    internal class P10
    {
        private static readonly int Max = 2000000;
        /// <summary>
        /// Calculates the sum of all primes below 2 million.
        /// </summary>
        public long Solve()
        {
            return PrimeHelpers.PrimesLessThan(Max).Select(x => (long) x).Sum();
        }
    }
}
