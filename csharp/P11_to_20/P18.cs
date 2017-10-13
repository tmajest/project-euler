using System;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;

namespace ProjectEuler.P11_to_20
{
    /// <summary>
    /// https://projecteuler.net/problem=18
    /// </summary>
    internal class P18
    {
        private static readonly int[][] Numbers =
        {
            new int[] {75},
            new int[] {95, 64},
            new int[] {17, 47, 82},
            new int[] {18, 35, 87, 10},
            new int[] {20, 04, 82, 47, 65},
            new int[] {19, 01, 23, 75, 03, 34},
            new int[] {88, 02, 77, 73, 07, 63, 67},
            new int[] {99, 65, 04, 28, 06, 16, 70, 92},
            new int[] {41, 41, 26, 56, 83, 40, 80, 70, 33},
            new int[] {41, 48, 72, 33, 47, 32, 37, 16, 94, 29},
            new int[] {53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14},
            new int[] {70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57},
            new int[] {91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48},
            new int[] {63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31},
            new int[] {04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23}
        };

        /// <summary>
        /// </summary>
        public int Solve()
        {
            var cache = new int[20, 20];
            return MaxPathSum(Numbers, cache, 0, 0);
        }

        /// <summary>
        /// Computes the max path sum for the the number at the given position i and j.
        ///
        /// Will attempt to cache the max path sum to avoid computing the sum for i and j
        /// multiple times.
        /// </summary>
        private int MaxPathSum(int[][] numbers, int[,] cache, int i, int j)
        {
            if (i >= numbers.Length || j >= numbers[i].Length)
            {
                return 0;
            }
            else if (cache[i, j] > 0)
            {
                return cache[i, j];
            }

            var left = MaxPathSum(numbers, cache, i + 1, j);
            var right = MaxPathSum(numbers, cache, i + 1, j + 1);

            var result = numbers[i][j] + Math.Max(left, right);
            cache[i, j] = result;

            return result;
        }
    }
}