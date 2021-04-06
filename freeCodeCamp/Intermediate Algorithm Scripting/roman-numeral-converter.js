function convertToRoman(num) {

  let str = '';
  const roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M'];
  const dec = [1,4,5,9,10,40,50,90,100,400,500,900,1000];

  for (let i = dec.length - 1; i >= 0; i--)
    while(num >= dec[i]) {
      str += roman[i];
      num -= dec[i]
    }

 return str;
}

convertToRoman(36);