function orbitalPeriod(arr) {
  var GM = 398600.4418;
  var earthRadius = 6367.4447;
  let newArr = [...arr];
  for (let i = 0; i < newArr.length; i++) {
    newArr[i].orbitalPeriod = Math.round((2 * Math.PI) * Math.sqrt(Math.pow(newArr[i].avgAlt + earthRadius, 3) / GM))
    delete newArr[i].avgAlt;
  }

  return newArr;
}

orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}]);