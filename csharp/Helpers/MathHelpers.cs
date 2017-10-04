using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Helpers
{
    /// <summary>
    /// Helper functions for math operations
    /// </summary>
    internal static class MathHelpers
    {
        /// <summary>
        /// Calculates the greatest commmon divisor of two numbers.
        /// </summary>
        public static long Gcd(long a, long b)
        {
            while (b > 0)
            {
                var temp = a % b;
                a = b;
                b = temp;
            }

            return a;
        }

        /// <summary>
        /// Calculates the least common multiple of two numbers.
        /// </summary>
        public static long Lcm(long a, long b)
        {
            return (a * b) / Gcd(a, b);
        }
    }
}
