using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;
using ProjectEuler.Helpers;

namespace ProjectEuler.P1_to_10
{
    /// <summary>
    /// https://projecteuler.net/problem=9
    /// </summary>
    internal class P9
    {
        /// <summary>
        /// Calculate the product of the Pythagorean triplet whose sum is 1000.
        /// </summary>
        public int Solve()
        {
            for (var i = 1; i < 1000; i++)
            {
                for (var j = 1; j < 1000; j++)
                {
                    for (var k = 1; k < 1000; k++)
                    {
                        if (IsPythagoreanTriplet(i, j, k) && i + j + k == 1000)
                        {
                            return i * j * k;
                        }

                        if (i + j + k > 1000)
                        {
                            break;
                        }
                    }
                }
            }

            return 0;
        }

        /// <summary>
        /// Returns true if the triplet is a Pythagorean triplet.
        /// </summary>
        private bool IsPythagoreanTriplet(int x, int y, int z)
        {
            return (x * x) + (y * y) == (z * z);
        }
    }
}
