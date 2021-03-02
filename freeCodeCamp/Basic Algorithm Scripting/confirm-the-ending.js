function confirmEnding(str, target) {
  
  // Variable for slice index
  let slice = -1 * target.length;

  // Compares slice with target string
  if (str.slice(slice) == target) {
    return true;
  } else {
    return false;
  }
}
