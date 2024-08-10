/*  

 abc ->  cba
-dca-asd)vat -> -tav)dsa-acd




*/


const pattern = /[a-z]/
let val = "-dca-asd)vat"
val = [...val]
let char = []
let spec = []


for (i in val){

    if (pattern.test(val[i])){
        char.push(val[i])
    }

    spec.push([i,val[i]])

}

char = char.reverse()

console.log(char)

for (index in spec){
    char.splice(spec[index][0],0,spec[index][1])
}

console.log(char.join(""))






