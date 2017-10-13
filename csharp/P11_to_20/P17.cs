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
    /// https://projecteuler.net/problem=17
    /// </summary>
    internal class P17
    {
        private static readonly Dictionary<int, string> NumberMap = new Dictionary<int, string>
        {
            [1] = "one", [2] = "two", [3] = "three", [4] = "four", [5] = "five",
            [6] = "six", [7] = "seven", [8] = "eight", [9] = "nine",
            [10] = "ten", [11] = "eleven", [12] = "twelve", [13] = "thirteen", [14] = "fourteen",
            [15] = "fifteen", [16] = "sixteen", [17] = "seventeen", [18] = "eighteen", [19] = "nineteen",
            [20] = "twenty", [30] = "thirty", [40] = "forty", [50] = "fifty", [60] = "sixty",
            [70] = "seventy", [80] = "eighty", [90] = "ninety", [1000] = "onethousand"

        };
        
        /// <summary>
        /// Calculates the number of letters used when writing out the numbers 1 to 1000 inclusive.
        /// </summary>
        /// <returns></returns>
        public int Solve()
        {
            // Add numbers 21-99 to the map
            for (var i = 20; i < 100; i += 10)
            {
                for (var j = 1; j < 10; j++)
                {
                    NumberMap[i + j] = $"{NumberMap[i]}{NumberMap[j]}";
                }    
            }

            // Add 100, 200, 300, ..., 900 to the map
            for (var i = 1; i < 10; i++)
            {
                NumberMap[i*100] = $"{NumberMap[i]}hundred";
            }

            // Add 101 - 999 to the map
            for (var i = 100; i < 1000; i += 100)
            {
                for (var j = 1; j < 100; j++)
                {
                    NumberMap[i + j] = $"{NumberMap[i]}and{NumberMap[j]}";
                }    
            }

            // Count the total number of letters
            return NumberMap.Values.Sum(x => x.ToString().Length);
        }
    }
}
