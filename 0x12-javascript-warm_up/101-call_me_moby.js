#!/usr/bin/node
exports.callmemoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
