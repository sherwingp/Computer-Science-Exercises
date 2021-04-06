function palindrome(str) {
  let reverseStr = [];
  let newStr = str.replace(/[^A-Za-z0-9]/g,"").toLowerCase();
  console.log(newStr);
  for (let i = 0; i < newStr.length; i++) {
    reverseStr.unshift(newStr[i]);
  }
  if (reverseStr.join("") === newStr) {
    return true;
  }
  return false;
}



palindrome("eye");