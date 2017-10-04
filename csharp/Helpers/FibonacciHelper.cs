using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Helpers
{
    /// <summary>
    /// Helper functions for calculating Fibonacci numbers
    /// </summary>
    internal class FibonacciHelper
    {
        public static IEnumerable<long> FibonacciNumbers()
        {
            var num1 = 1;
            var num2 = 2;

            yield return 1;
            yield return 2;

            while (true)
            {
                var newNum = num1 + num2;
                num1 = num2;
                num2 = newNum;

                yield return newNum;
            }
        }
    }
}
