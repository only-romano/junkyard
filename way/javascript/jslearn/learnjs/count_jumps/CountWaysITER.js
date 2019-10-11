/*params = [steps, maxJump, tempVarm, sumOfJumps]
[3, 2, [], 0]

params[3,2,[],0, [2,1],]
params[2] = []
params[3] = 0
!__iter__ = 2

*/

const CountWays = function (params) {
    for (let jump = params[1]; jump > 0; jump--) {      //      jump = 1;
        params[3] += jump;                              //      params[3] += 2
        if (params[3] === params[0]) {                  //      +++
            params[2].push(jump);                       //      params[2].push[1]
            params.push(params[2]);                     //      params.push[2,1]
            params[2] = [];                             //      params[2] = []
            params[3] = 0;                              //      
            break;                                   //
        } else if (params[3] > params[0]) {             //      ---
            params[3] -= jump;                          //
            continue;                                   //
        } else {                                        //      +++
            params[2].push(jump);                       //      params[2] = [2,]
            CountWays(params);                          //      !2
        }
    }
    return params                                       //
};

params = [5, 2, [], 0];
console.log(CountWays(params));