using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler.Helpers
{
    /// <summary>
    /// Helper functions to generate prime numbers and prime factors.
    /// </summary>
    internal class PrimeHelpers
    {
        /// <summary>
        /// Generate prime numbers less than the given max.
        /// </summary>
        /// <param name="max">The limit of numbers to consider</param>
        /// <returns>An array of prime numbers</returns>
        public static int[] PrimesLessThan(int max)
        {
            var sieve = PrimeSieve(max);

            // Return only the prime numbers from the sieve
            return sieve
                .Select((isPrime, i) => new { Number = i, IsPrime = isPrime })
                .Where(tuple => tuple.IsPrime)
                .Select(tuple => tuple.Number)
                .ToArray();
        }

        /// <summary>
        /// Returns the prime factors of a given number.
        /// </summary>
        /// <param name="num">The number to calculate prime factors for</param>
        /// <returns>An array of prime factors of the given number</returns>
        public static int[] PrimeFactors(long num)
        {
            // Only consider primes less than the sqrt of the number (the limit for largest prime factor)
            var max = (int) (Math.Sqrt(num) + 1);

            // Return primes that divide the number
            return PrimesLessThan(max)
                .Where(prime => num % prime == 0)
                .ToArray();
        }

        /// <summary>
        /// Returns all divisors (prime and composite) for a number.
        /// </summary>
        public static long[] Divisors(long num)
        {
            if (num < 0)
            {
                return new long[0];
            }

            var divisors = new List<long>();
            var divisor = 1;
            var complement = num;

            // Calculate divisors and their complements
            while (divisor <= complement)
            {
                if (num % divisor == 0)
                {
                    divisors.Add(divisor);    

                    // Don't add a divisor twice if the divisor is equal to its complement
                    if (divisor != complement)
                    {
                        divisors.Add(complement);
                    }
                }

                divisor++;
                complement = num / divisor;
            }

            // Sort the divisors and return as an array
            return divisors
                .OrderBy(x => x)
                .ToArray();
        }

        /// <summary>
        /// Generates a prime sieve of the given size.
        /// </summary>
        /// <param name="size">The size of the sieve</param>
        /// <returns>The prime sieve boolean array</returns>
        private static bool[] PrimeSieve(int size)
        {
            var sieve = Enumerable.Repeat(true, size).ToArray();
            sieve[0] = false;
            sieve[1] = false;

            // Compute sieve - mark multiples of prime numbers as composite
            for (var i = 2; i < Math.Sqrt(size) + 1; i++)
            {
                if (!sieve[i])
                {
                    continue;
                }

                for (var j = i * i; j < size; j += i)
                {
                    sieve[j] = false;
                }
            }

            return sieve;
        }
    }
}
