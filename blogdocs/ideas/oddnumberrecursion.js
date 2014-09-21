var odd = function(num) {
  if (num === 1 ) {
    return "odd";
  } else if (num === 0) {
    return "even";
  } else {
    odd((num - 1));
  }
};