using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Helpers
{
    internal static class EnumerableHelpers
    {
        /// <summary>
        /// Generates a sequence of long values up to Long.MaxValue.
        /// </summary>
        /// <param name="start">The number to start on</param>
        /// <param name="end">The number to end on, exclusive</param>
        /// <param name="skip">The amount to skip</param>
        /// <returns>The IEnumerable of long values</returns>
        public static IEnumerable<long> Range(long start, long end, long skip = 1)
        {
            while (start < end)
            {
                yield return start;
                start += skip;
            }    
        }

        /// <summary>
        /// Extension method to calculate the product of an IEnumerable of integer values.
        /// </summary>
        /// <param name="numbers">The numbers to calculate the product of</param>
        /// <returns>The product of those numbers</returns>
        public static long Product(this IEnumerable<int> numbers)
        {
            return numbers.Aggregate(1L, (product, curr) => product * curr);
        }
    }
}
