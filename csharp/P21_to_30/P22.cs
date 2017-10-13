using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using ProjectEuler.Helpers;

namespace ProjectEuler.P21_to_30
{
    /// <summary>
    /// https://projecteuler.net/problem=22
    /// </summary>
    internal class P22
    {
        private const string NamesFilePath = @"P21_to_30\InputFiles\p22.txt";

        /// <summary>
        /// Returns the sum of scores of the names in the text file.
        /// </summary>
        public long Solve()
        {
            // Calculate the score for the name and multiply it by its position
            // in the list.  Finally calculate the sum of all scores
            return File.ReadAllLines(NamesFilePath)
                .Select(ScoreName)
                .Sum();

        }

        /// <summary>
        /// Returns the score for the name.
        ///
        /// The score is computed by finding the sum of the letters in the given name
        /// multiplied by its position in the list.
        ///
        /// 'A' is worth 1 point, 'B' is worth 2 points, etc.  Positions begin at 1.
        /// </summary>
        private long ScoreName(string name, int position)
        {
            return name.ToLower().Sum(c => c - 'a' + 1) * (position + 1L);
        }
    }
}