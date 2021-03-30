*/ Diff Two Arrays
Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both.
In other words, return the symmetric difference of the two arrays.

Note: You can return the array with its elements in any order.

*/

function diffArray(arr1, arr2) {
  var arr = arr1.concat(arr2);

  function symmetricDifference(x, y, word) {
    if ((x.includes(word) === true && y.includes(word) === false) 
    || (x.includes(word) === false && y.includes(word) === true)) {
      return true;
    }

  }

  var newArr = arr.filter(value => symmetricDifference(arr1, arr2, value));

  return newArr;

}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);