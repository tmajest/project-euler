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
    /// https://projecteuler.net/problem=7
    /// </summary>
    internal class P7
    {
        /// <summary>
        /// Calculate the 10,001st prime number
        /// </summary>
        public long Solve()
        {
            return PrimeHelpers.AllPrimes()
                .Skip(10000)
                .Take(1)
                .Single();
        }
    }
}
