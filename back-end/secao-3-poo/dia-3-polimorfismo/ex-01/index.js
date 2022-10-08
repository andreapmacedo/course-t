"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Person_1 = require("./Person");
// const maria = new Person('Maria da Consolação', new Date('1980/01/25'));
var maria = new Person_1.default('Ma', new Date('1980/01/25'));
var luiza = new Person_1.default('Luiza Andrade', new Date('2005/10/02'));
console.log(maria);
console.log(luiza);
