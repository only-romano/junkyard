using System; 
using System.Collections.Generic; 

namespace OlympProg {
	class Program { 
		static int n = int.Parse(Console.ReadLine()), k = int.Parse(Console.ReadLine()), size_2 = k;
		static List<List<int» array = new List<List<int»(); 

		static void jmp(int _n, List<int> a) { 
			if (_n < n) 
				for (int i = 1; i <= k; i++) { 

					/*

					1,1,1,1,1


					 */
					List<int> arr = new List<int>(); 
					for (int h = 0; h < a.Count; h++) 
						arr.Add(a[h]); 
					arr.Add(i); 
					jmp(_n + i, arr); 
				} 
			else if(_n == n) array.Add(a); 
		} 

		static void Main(string[] args) { 
			jmp(0, new List<int>()); 
			for(int i = 0; i < array.Count; i++) { 
				Console.Write("Массив №" + (i+1) + "\n{"); 
				for (int j = 0; j < array[i].Count; j++) 
					Console.Write(array[i][j] + ", "); 
					Console.Write("}\n"); 
			} 
		Console.ReadKey(); 
		} 
	} 
}