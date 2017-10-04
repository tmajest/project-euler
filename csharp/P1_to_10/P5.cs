using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using ProjectEuler.Helpers;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=5
    /// </summary>
    internal class P5
    {
        /// <summary>
        /// Calculates the first number that is divisible by all numbers 1-20.
        /// Equivalent to calculating the LCM of all 20 numbers.
        /// </summary>
        public long Solve()
        {
            return EnumerableHelpers.Range(1, 20).Aggregate(MathHelpers.Lcm);
        }
    }
}
