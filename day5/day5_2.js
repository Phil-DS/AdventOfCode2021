const fs = require('fs');

const data = fs.readFileSync('day5\\day5.txt').toString().split('\n').map(
    line => {
        const matches = line.match(/^(\d*),(\d*) -> (\d*),(\d*)/).slice(1).map(val => parseInt(val));
        return [[matches[0],matches[1]],[matches[2],matches[3]]]
    }
)

let usedData = data.filter(
    d => ((d[0][0] == d[1][0]) || (d[0][1] == d[1][1]))
)

let unusedData = data.filter(
    d => ((d[0][0] != d[1][0]) && (d[0][1] != d[1][1]))
)

let m = Array.from({length: 1000}, (k,v)=>Array.from({length: 1000}, (k2,v2)=>0))

data.forEach(
    d => {
        let ydir = d[1][0] - d[0][0]
        let xdir = d[1][1] - d[0][1]
        ydir = Math.sign(ydir)
        xdir = Math.sign(xdir)
        if(d[0][0] == d[1][0]){
            for(let i=d[0][1]; i!=d[1][1]+xdir; i+=xdir){
                m[i][d[0][0]] += 1
            }
        } else {
            if(d[0][1] == d[1][1]){
                for(let i=d[0][0]; i!=d[1][0]+ydir; i+=ydir){
                    m[d[0][1]][i] += 1
                }
            } else {
                for(let i=d[0][1],j=d[0][0]; i!=d[1][1]+xdir,j!=d[1][0]+ydir; i+=xdir,j+=ydir){
                    m[i][j]+=1
                }
            }
        }
    }
)

const val = m.reduce(
    (prev,curr) => {
        const s = curr.filter(v => v > 1)
        prev += s.length
        return prev
    }, 0
)

console.log(val)