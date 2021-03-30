function dropElements(arr, func) {
  // Creates copy of array
  let newArr = [...arr];

  // Loops through original array
  for(let i =  0; i < arr.length; i++) {
    if (func(arr[i])) {
      return newArr;
    
    // Unshifts copied array
    } else {
      newArr.shift();
    }
  } 
  return newArr;
}

dropElements([1, 2, 3, 4, 5], function(n) {return n >= 3; });