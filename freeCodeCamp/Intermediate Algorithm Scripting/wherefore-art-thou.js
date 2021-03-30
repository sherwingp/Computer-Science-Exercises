function whatIsInAName(collection, source) {
  var arr = [];
  // Only change code below this line
   // Checks for properties
  let newArr = [];
  for (let i = 0; i < collection.length; i++) {
    if (Object.keys(source).every(prop => collection[i].hasOwnProperty(prop))) {
      newArr.push(collection[i]);
    }
  }

    // Checks for values
  for (let i = 0; i < newArr.length; i++) {
    if (Object.values(source).every(value => Object.values(newArr[i]).includes(value))) {
      arr.push(newArr[i]);
    }
  }

  console.log(arr)
  // Only change code above this line
  return arr;
}

whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });