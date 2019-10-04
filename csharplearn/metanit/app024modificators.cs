using System;

namespace Mod
{
    class App
    {
        static void Main(string[] args)
        {
            State state = new State();
            // a/b/c - failed
            state.d = 5;
            state.e = 8;
            state.f = 10;

            // Display_f/e - failed
            state.Display_a();
            state.Display_b();
            Console.WriteLine("new d = {0}, e = {1}, f = {2}", state.d, state.e, state.f);
        }
    }

    public class State
    {
        int a;
        private int b;
        protected int c;
        internal int d;
        protected internal int e;
        public int f;

        private void Display_f()
        {
            Console.WriteLine("Variable f = {0}", f);
        }

        public void Display_a()
        {
            Console.WriteLine("Variable a = {0}", a);
        }

        internal void Display_b()
        {
            Console.WriteLine("Variable b = {0}", b);
        }

        protected void Display_e()
        {
            Console.WriteLine("Variable e = {0}", e);
        }
    }
}