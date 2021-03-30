function smallestCommons(arr) {
  
  // Create array of range
  for(let i = Math.min(...arr) + 1; i < Math.max(...arr); i++) {
    arr.splice(-1, 0, i);
  }
  // Calculate upper bound
  let upperBound = arr.reduce((x, y) => x * y);

  // Initialize variables
  let multiple = arr[0];
  let answer = arr[0];

  // Loop through multiples of min
  for (let i = 1; i <= upperBound; i++) {
    answer = multiple * i;

    // Check if evenly divisible
    if(arr.every(num => answer % num === 0)) {
      return answer;
    }  
  }

}


smallestCommons([1,5]);

