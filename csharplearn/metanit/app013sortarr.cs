using System;

namespace Sort
{
    class App
    {
        static void Main()
        {
            int[] nums = new int[7];
            int temp, i, j;
            Console.WriteLine("Input seven numbers!");
            for (i = 0; i < 7;i++)
            {
                Console.Write("Input {0}-th number: ", i+1);
                nums[i] = Int32.Parse(Console.ReadLine());
            }

            for (i=0;i<6;i++)
            {
                for (j=i+1; j < 7; j++)
                {
                    if (nums[j] < nums[i])
                    {
                        temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                    }
                }
            }

            Console.WriteLine("Sorted array: ");
            for (i=0; i < nums.Length; i++)
            {
                Console.WriteLine(nums[i]);
            }
            Console.ReadLine();

        }
    }
}