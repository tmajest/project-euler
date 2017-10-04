using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ProjectEuler.Helpers;

namespace ProjectEuler.P11_to_20
{
    /// <summary>
    /// https://projecteuler.net/problem=12
    /// </summary>
    internal class P12
    {
        /// <summary>
        /// Find the first triangle number to have over 500 divisors.
        /// </summary>
        public long Solve()
        {
            var counter = 1;
            var triangleNumber = 1L;

            while (true)
            {
                var divisors = PrimeHelpers.Divisors(triangleNumber);
                if (divisors.Length > 500)
                {
                    return triangleNumber;
                }

                counter++;
                triangleNumber += counter;
            }
        }
    }
}
