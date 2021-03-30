function translatePigLatin(str) {
  var vowels = /^[aeiou]/g;
  var consonants = /^[bcdfghjklmnpqrstvwxyz]+/g;
  let newStr = "";
  if (str.match(vowels)) {
    newStr = str.concat("way");
  } else {

    newStr = str.replace(consonants, "");
    newStr = newStr.concat(str.match(consonants)).concat("ay")
}
  console.log(newStr)
return newStr;
}
translatePigLatin("consonant");