#!/usr/bin/node
const arg = process.argv[2];
if(!isNaN(arg)){		
    console.log("My number : "+ parseInt(arg));
}
else{
    console.log("not a number");   
}
