/** product: calculate the product of an array of numbers. */

function product(nums) {
  if (nums.length === 0) return 1;
  return nums[0] * product(nums.slice(1))
}

/** longest: return the length of the longest word in an array of words. */

function longest(words) {
  //[a,hi,hello,awesome]  should return the length of the longest word
  if (words.length === 1) return words[0].length;
  console.log(words)
  if (words[0].length >= words[1].length) {
    words.splice(1, 1)
  } else {
    words.splice(0, 1)
  }
  return longest(words)
}

/** everyOther: return a string with every other letter. */

function everyOther(str, i = 0) {
  //"hxexlxlxo"  should return hello
  //BASE
  if (i >= str.length) return "";

  return str[i] + everyOther(str, i + 2)

}

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str) {
  // need to reverse the string, then compare it and return T/F
  if (str.length === 1 || str.length === 0) return true;

  if (str[0] === str[str.length - 1]) {
    isPalindrome(str.slice(1, -1))
    return true
  } else {
    return false
  }
}

/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, val, i = 0) {
  if (i >= arr.length) {
    return -1
  } else if (arr[i] === val) {
    return i
  } else {
    return findIndex(arr, val, i + 1)
  }
}

/** revString: return a copy of a string, but in reverse. */

function revString(str, i = str.length - 1) {

  if (i < 0) return "";

  return str[i] + revString(str, i - 1);

}

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj, out = []) {
  Object.keys(obj).forEach(key => {
    if (typeof obj[key] === 'string') {
      out.push(obj[key]);
    } else if (typeof obj[key] === 'object' && obj[key] !== null) {
      gatherStrings(obj[key], out);
    }
  });
  return out
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val, start = 0, end = arr.length - 1) {

  if (start > end) return -1

  let middle = Math.floor((start + end) / 2);

  if (arr[middle] === val) {
    return middle;
  } else if (arr[middle] < val) {
    return binarySearch(arr, val, middle + 1, end)
  } else {
    return binarySearch(arr, val, start, middle - 1)
  }


}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};
