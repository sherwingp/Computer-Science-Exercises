function spinalCase(str) {
  str = str.replace(/\W|_/g, '-')
  str = str.split(/(?=[A-Z])/).join("-")  
  str = str.replace(/--/g, '-')
  console.log(str)
  str = str.toLowerCase()
  return str;
}

spinalCase('This Is Spinal Tap');