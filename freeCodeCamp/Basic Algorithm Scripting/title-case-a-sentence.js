function titleCase(str) {
  let newString = "";

  // Splits string into array of words
  let arr = str.split(" ");

  // Iterates through array of words
  for (let i = 0; i < arr.length; i++) {

    // Changes each word to lower case
    arr[i] = arr[i].toLowerCase();
    
    // Changes first word to upper case and glues rest of word back on
    arr[i] = arr[i].charAt(0).toUpperCase() + arr[i].substr(1);;
  }

  // Joins array of words back together as string
  newString = arr.join(" ");
  return newString;
}

titleCase("I'm a little tea pot");