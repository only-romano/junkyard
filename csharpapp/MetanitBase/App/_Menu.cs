using System;
using System.Collections.Generic;

namespace MetanitBase.App
{
    public static class Menu
    {
        public static bool Cycle(string info, string[,] actions, IReadOnlyList<Func<bool>> functions, string final="", Func<string> stat=null)
        {
            var check = true;
            while (check)
            {
                var key = Methods.GetString(info).ToLower();

                var rows = actions.GetUpperBound(0) + 1;
                var columns = actions.Length / rows;
                for (var i = 0; i < rows; i++)
                {
                    for (var j = 0; j < columns; j++)
                    {
                        if (key == actions[i, j]) check = functions[i]?.Invoke() ?? false;
                    }
                }
            }

            return Methods.CheckString(stat?.Invoke() ?? final);
        }
    }
}
