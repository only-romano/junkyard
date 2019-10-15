function convertToRoman(num) {
  var l = ['I','V','X','L','C','D','M','O','Z'];
  num = num.toString().split('').reverse();
  var start = 0;
  var final = [];
  for (var i = 0; i < num.length; i++) {
    var tempResult = "";
    var n = num[i];
    switch (n) {
      case "1":case "2":case "3":
        for (var j = 0; j < +n; j++) {
          tempResult += l[start];
        }
        break;
      case "4":
        tempResult = l[start] + l[start+1];
        break;
      case "5":
        tempResult = l[start+1];
        break;
      case "6":case "7":case "8":
        tempResult = l[start+1];
        for (var j = 0; j < (+n)-5; j++) {
          tempResult += l[start];
        }
        break;
      case "9":
        tempResult = l[start] + l[start+2];
        break;
    }
    start += 2;
    final.push(tempResult);
  }
 return final.reverse().join('');
}

convertToRoman(36);