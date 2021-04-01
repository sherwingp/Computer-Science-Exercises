function addTogether(a, b) {
  if (arguments.length === 1 && Number.isInteger(a)) {
    return b => Number.isInteger(b) ? a + b : undefined;
  } else if ([...arguments].every(num => Number.isInteger(num))){
    return a + b;
  } else {
    return undefined;
  }
  
}

addTogether(2),([3]);