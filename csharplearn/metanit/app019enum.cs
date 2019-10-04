using System;

namespace Enum
{
    enum Operation
    {
        Add = 1,
        Substract,
        Multiply,
        Divide
    }

    class App
    {
        enum Days
        {
            Monday,
            Tuesday,
            Wednesday,
            Thursday,
            Friday,
            Saturday,
            Sunday
        }

        enum Time : byte
        {
            Morning,
            Afternoon,
            Evening,
            Night
        }

        static void Main(string[] args)
        {
            Operation op;
            op = Operation.Add;
            Console.WriteLine(op);
            Console.WriteLine((int)(Operation.Multiply));

            MathOp(10, 5, Operation.Add);
            MathOp(11, 5, Operation.Multiply);
        }

        static void MathOp(double x, double y, Operation op)
        {
            double result = 0.0;

            switch(op)
            {
                case Operation.Add:
                    result = x + y;
                    break;
                case Operation.Substract:
                    result = x - y;
                    break;
                case Operation.Multiply:
                    result = x * y;
                    break;
                case Operation.Divide:
                    result = x / y;
                    break;
            }

            Console.WriteLine("Result of operation: {0}", result);
        }
    }
}