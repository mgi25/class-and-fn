// let ; const; var

var student = {
    "name": "Alen",
    "Class": "BscDS",
    "RollNo": 23112001
};

console.log(student);
console.log(student.name);

for(let i=0; i<5;i++){
    console.log("Joel Is GAY")
}

let names = ["Alen","Joel","Rosh","max","MGI"];
console.log(names);
console.log(typeof(names));
console.log(names[0]);


for(let i=0; i<names.length;i++){
    console.log(names[i]);
}


names.forEach(name=>{
    console.log("****",name,"****");
})

// https://developer.mozilla.org/en-US/docs/Web/JavaScript

function Hello(name){
    console.log("Hello",name, "*!");
}
Hello("Alen")
names.forEach(name=>{
    Hello(name);
})


// Inserting

names.push("Tarith");
console.log(names);
console.log(names.length);


names.pop("Tarith");
console.log(names);
console.log(names.length);


var sample_data = {
    "names": names
}

sample_data.length = names.length;
console.log(sample_data);