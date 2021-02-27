function reverseString(str) {
  let reverseStringArray = [...str];
  reverseStringArray = reverseStringArray.slice(0).reverse();
  let newString = "";
  for (let i = 0; i < reverseStringArray.length; i++) {
    newString += reverseStringArray[i];
  }
  return newString;
}

