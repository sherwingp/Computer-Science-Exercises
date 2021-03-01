function findLongestWordLength(str) {
  let longest = 0;
  let currentWord = 0;

  // Iterates through string
  for (let i = 0; i < str.length; i++) {

    // Counts current word until space
    if (str[i] != (" ")) {
      currentWord++;

    } else {
      
      // Updates longest word
      if (currentWord > longest) {
        longest = currentWord;
        
      }

      // Resets current word counter
      currentWord = 0;
    }
  }

  // Returns longest word
  if (currentWord > longest) {
    return currentWord;
  }
  return longest;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");