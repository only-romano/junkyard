import comebackpython0530module as cb


def main():
  x = 0b101; y = 0x0a; age = 22; isMarried = False; str1 = "Tom";
  print(7//2, 7%2, ord(str1[2]))  # целочисленное деление, остаток от деления
  print(age > 0 and isMarried is True, age > 0 or isMarried is True)
  print(not age > 0 or isMarried is False, x+y)
  print(str1.lower(), str1.upper(), str1.lower() > str1.upper())
  print(cb.factorial_rec(4), cb.factorial_while(5), cb.factorial_for(6))
  print(cb.sum_of_nums(1,2,3,4,5), cb.sum_of_nums(3,5,7,9))
  print(list(range(1, 10)) == [1,2,3,4,5,6,7,8,9])
  print("{:,.2f}".format(10023.8589578), "{:.1%}".format(.12345),
  	"{:.1e}".format(12345.6789), "\tName: %s \t Age: %d" % ("Kato", 27))
  cb.account_calculate(12, 100000, 24)
  cb.division(1, "3"); cb.division(2, 0), cb.division('carl', '11')
  cb.exchange_money(60000)
  cb.exchange(63, 10000)
  cb.get_circle_square(50)
  cb.test_list_methods()
  cb.csv_reader()
  cb.binary_reader()
  cb.shelve_reader()
  cb.shuffle_list()
  cb.count_words()
  cb.multiply_matrix()


if __name__ == "__main__":
  main()
