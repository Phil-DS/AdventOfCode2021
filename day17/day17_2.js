xLow = 282
xHigh = 314
yLow = -80
yHigh = -45

vels = 0

for(let _vx = 0;_vx<=500; _vx++){
    for(let _vy = -500; _vy < 500; _vy++){
        vx = _vx
        vy = _vy
        x=0
        y=0
        while(true){
            x += vx
            y += vy
            if(x >= xLow && x <= xHigh && y >= yLow && y<= yHigh){
                vels++
                break;
            }
            if(x > xHigh || y < yLow) break;
            vx = Math.max(0,vx-1)
            vy -= 1
        }
    }
}
console.log(vels)

