using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=4
    /// </summary>
    internal class P4
    {
        /// <summary>
        /// Finds the largest product of two 3-digit numbers that is also a palindrome number.
        /// </summary>
        public int Solve()
        {
            var products = from x in Enumerable.Range(100, 899)
                           from y in Enumerable.Range(100, 899)
                           select x * y;

            return products.Where(IsPalindromeNumber).Max();
        }

        /// <summary>
        /// Returns true if the number is a palindrome number, otherwise false.
        /// </summary>
        private bool IsPalindromeNumber(int number)
        {
            var str = number.ToString();
            for (var i = 0; i < str.Length/2; i++)
            {
                if (str[i] != str[str.Length - i - 1])
                {
                    return false;
                }
            }

            return true;
        }
    }
}
