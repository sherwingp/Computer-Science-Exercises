function frankenSplice(arr1, arr2, n) {
  let arr3 = arr2.slice()
  for (let i = arr1.length - 1; i >= 0; i--) {
    arr3.splice(n, 0, arr1[i]);
  }

  return arr3;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);