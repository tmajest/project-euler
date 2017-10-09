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
            // 1 to 9
            [1] = "one", [2] = "two", [3] = "three", [4] = "four", [5] = "five",
            [6] = "six", [7] = "seven", [8] = "eight", [9] = "nine",

            // 10 to 19
            [10] = "ten", [11] = "eleven", [12] = "twelve", [13] = "thirteen", [14] = "fourteen",
            [15] = "fifteen", [16] = "sixteen", [17] = "seventeen", [18] = "eighteen", [19] = "nineteen",

            // 30, 40, 50, ..., to 90 by 10s
            [20] = "twenty", [30] = "thirty", [40] = "forty", [50] = "fifty", [60] = "sixty",
            [70] = "seventy", [80] = "eighty", [90] = "ninety",

            // 100, 200, 300, ... to 1000 by skipping 100s
            [100] = "onehundred", [200] = "twohundred", [300] = "threehundred", [400] = "fourhundred", [500] = "fivehundred",
            [600] = "sixhundred", [700] = "sevenhundred", [800] = "eighthundred", [900] = "ninehundred", [1000] = "onethousand"
        };

        private static readonly string AndString = "and";
        
        /// <summary>
        /// Calculates the number of letters used when writing out the numbers 1 to 1000 inclusive.
        /// </summary>
        /// <returns></returns>
        public int Solve()
        {
            return Enumerable.Range(1, 1000)
                .Select(GetNumberString)
                .Sum(number => number.ToString().Length);
        }

        /// <summary>
        /// Returns the string that represents the number when written out with the spaces and hyphens removed.
        /// </summary>
        public string GetNumberString(int number)
        {
            var result = new StringBuilder();

            while (number > 0)
            {
                if (number > 100)
                {
                    // The number is greater than 100; calculate the 100s part of the string
                    var part = number - (number % 100);
                    result.Append(NumberMap[part]);
                    number -= part;

                    // Add 'and' to the result for numbers greater than 100 that are not a multiple of 100.
                    if (number > 0)
                    {
                        result.Append(AndString);
                    }
                }
                else if (number > 20)
                {
                    // Number is between 21 and 99; calculate the string for the 10's part
                    var part = number - (number % 10);
                    result.Append(NumberMap[part]);
                    number -= part;
                }
                else
                {
                    // Number is less than or equal to 20; we have the exact number in the map
                    result.Append(NumberMap[number]);
                    number = 0;
                }
            }

            return result.ToString();
        }

    }
}
