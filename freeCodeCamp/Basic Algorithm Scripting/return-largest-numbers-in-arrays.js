function largestOfFour(arr) {

  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    newArr.push(Math.max(...arr[i]));
  }

  return newArr;
}

