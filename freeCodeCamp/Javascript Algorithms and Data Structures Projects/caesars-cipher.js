function rot13(str) {
  let newStr = "";
  
  for (let i = 0; i < str.length; i++) {
    if (str.charCodeAt(i) < 65 || str.charCodeAt(i) > 90) {
      newStr += str[i];

    } else {

      let ascii = str.charCodeAt(i) + 13
      if (ascii > 90) {
        ascii = ((ascii - 65) % 26) + 65
      }
      newStr += String.fromCharCode(ascii);

    }

  }
  return newStr;
}

rot13("SERR PBQR PNZC");