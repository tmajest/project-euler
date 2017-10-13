using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;

namespace ProjectEuler.P11_to_20
{
    /// <summary>
    /// https://projecteuler.net/problem=19
    /// </summary>
    internal class P19
    {
        /// <summary>
        /// Calculates how many sundays fell on the first of the month during the 20th century.
        /// </summary>
        public int Solve()
        {
            var count = 0;
            var curr = new DateTime(1901, 1, 1);
            var end = new DateTime(2000, 12, 31);

            // For each of the months in the 20th century, find the ones that begin on a Sunday
            while (curr < end)
            {
                if (curr.DayOfWeek == DayOfWeek.Sunday)
                {
                    count++;
                }

                curr = curr.AddMonths(1);
            }

            return count;
        }
    }
}