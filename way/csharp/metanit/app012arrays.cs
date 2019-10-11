using System;

namespace Arrays
{
    class App
    {
        static void Main()
        {
            int[] nums = new int[4];
            int[] nums1 = new int[4] { 1, 2, 3, 5 };
            int[] nums2 = new[] {1,2,3,5};
            int[,] nums3 = {{1,5,9,13}, {2,6,10,14}, {3,7,11,15}, {4,8,12,16}};
            nums[0] = 1;
            nums[1] = 2;
            nums[2] = 3;
            nums[3] = 5;

            foreach (int i in nums)
            {
                Console.Write(i*i + ' ' + " " + ' ');
            }
            Console.WriteLine('a' + 10 - 10);

            for (int i = 0; nums.Length > i; i++)
            {
                nums[i] *= ' ';
                Console.Write(nums[i] + " ");
            }
            Console.WriteLine();

            int rows = nums3.GetUpperBound(0) + 1;
            int columns = nums3.Length / rows;

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    Console.Write(nums3[i, j] + "\t");
                }
                Console.WriteLine();
            }
            Console.WriteLine();

            int[][] numbers = new int[3][];
            numbers[0] = new int[] {1,2};
            numbers[1] = new int[] {1,2,3};
            numbers[2] = new int[] {1,2,3,4,5};

            foreach (int[] row in numbers)
            {
                foreach (int number in row)
                {
                    Console.Write(number + "\t");
                }
                Console.WriteLine();
            }
            Console.WriteLine();

            int[] numbers1 = {-4,-3,-2,-1,0,5,1,2,3,4};
            int result = 0;

            foreach (int number in numbers1)
            {
                if (number > 0) result++;
            }
            Console.WriteLine("Numbers of positive elements: {0}\n", result);

            int temp;
            int len = numbers1.Length-1;
            for(int i=0;;i++)
            {
                temp = numbers1[i];
                numbers1[i] = numbers1[len-i];
                numbers1[len-i] = temp;
                if (len-2*i <= 1) break;
            }

            foreach(int item in numbers1)
            {
                Console.Write(item + " ");
            }

            Console.WriteLine();
            double p = Convert.ToDouble(Console.ReadLine());
            if (p == 3.14)
            {
                Console.WriteLine("Success!");
            }
            Console.WriteLine(~-23456);
        }
    }
}