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
    /// https://projecteuler.net/problem=15
    /// </summary>
    internal class P15
    {
        private const int GridLength = 21;

        /// <summary>
        /// Find the number of lattice paths in a 20x20 grid, starting from the top left and
        /// ending at the bottom right by only going down or to the right.
        /// </summary>
        public long Solve()
        {
            // Initialize the grid.
            // There is only one way to get to each of the locations on the top-most row
            // and left-most column.
            var grid = new long[GridLength, GridLength];
            for (var i = 0; i < GridLength; i++)
            {
                grid[i, 0] = 1;
                grid[0, i] = 1;
            }

            // The number of paths from the current position in the grid is equal to the number
            // of ways to get to the position above plus the number of ways to get the position
            // to the left.
            for (var i = 1; i < GridLength; i++)
            {
                for (var j = 1; j < GridLength; j++)
                {
                    grid[i, j] = grid[i, j - 1] + grid[i - 1, j];
                }
            }

            return grid[GridLength - 1, GridLength - 1];
        }

    }
}
