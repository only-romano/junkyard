/*
n - ступеньки       2 3 4 5
k - max jump    

k    n  2       3       4           5           6
1       1       1       1           1           1
2       1+1     1+2     1+4         1+7         1+12
3       ===     1+2+1   1+4+2       1+7+5       1+12+11
4       ===     ===     1+4+2+1     1+7+5+2     1+12+11+5
5       ===     ===     ===         1+7+5+2+1   1+12+11+5+2
6       ===     ===     ===         ===         1+12+11+5+2+1

k / n   2   3   4   5   6   7
1       1   1   1   1   1   1
2       2   3   5   8   13  21
3       =   4   7   13  24  44
4       =   =   8   15  29  56
5       =   =   =   16  31
6       =   =   =   =   32
7

k = 1 (const 1)
k = 2 (fibonachi)
l = 3 (tri)

1 +
111112 + 111121 + 111211 + 11122 + 112111 + 11212 + 11221 + 121111 +
12112 + 12121 + 12211 + 1222 + 211111 + 21112 + 21121 + 21211 + 2122 +
22111 + 2212 + 2221

def x(a):
    if k == 1:
        return 1

if (N <= K || K === 1) { steps = 2^(K-1) }
ladder = 6; jump = 4;
step[1] = 1
step[0] = 1
step[2] = step[0] + step[1] (2^1 = 2 = 1 + 1)
step[3] = step[0] + step[1] + step[2] (2^2 = 4 = 2 + 1 + 1)
step[4] = step[0] + step[1] + step[2] + step[3] (2^3 = 8 = 4 + 2 + 1 + 1)
...
step[n] = sum([step[x] for x in range(0, n)]);

if (N > K && K > 1) {
        step[n] = sum([step[x] for x in range(0, n)]) - sum([step[x] for x in range(0, i - jump)]);
}
(15) = 1 + 1 + 2 + 4 + 8 - 1  (ladder = 5; jump = 4)
step[5] = step[0] + step[1] + step[2] + step[3] + step[4] - step[0]
step[5] = sum([step[x] for x in range(0, 5)]) - step[5 - jump]
(29) = 1 + 1 + 2 + 4 + 8 + 15 - 2
step[6] = step[0] + step[1] + step[2] + step[3] + step[4] + step[5] - step[0] - step[1]
step[6 - jump] = 2
step[6] = sum([step[x] for x in range(0, 6)]) - step[6 - jump]

(56) = 1 + 1 + 2 + 4 + 8 + 15 + 29 - 4
step[7] = step[0] + step[1] + step[2] + step[3] + step[4] + step[5] - step[0] - step[1] - step[2]


def steps(n, k):
    step = [1]
    for i in range(1, k + 1):
        step.append(2**(i-1))
    for i in range(k + 1, n + 1):
        step.append(sum([step[x] for x in range(0, i)]) - sum([step[x] for x in range(0, i-k)]))
    return step[n]

56 = 29*2(58) - 1-1-2....56 = 29*2 - 1-1
step[7] = step[6]*2 - (step[0]+step[1]+step[2]) (range(1, i-jump))
step[7] = step[6]*2 - (step[0] + step[1]) (range(1, i-))

def countSteps(ladder, jump):
    step = [1, 1] + [None] * (ladder - 1)
    for i in range(2, jump + 1):
        step[i] = step[i-1]*2
    for i in range(jump + 1, ladder + 1):
        step[i] = step[i-1]*2 - step[(i-1) -jump]
    return step[ladder]

*/



const countRabbitWays = (steps, maxJump) => {
    /*
     Массив для хранения колличества путей до каждой ступеньки с заложенным дефолтом,
     включающий в себя положение "с места": possibleCounts[0] = 1; а также значение
     колличества путей до 1-ой ступеньки possibleCounts[1] = 1.
     */
    let possibleCounts = [1,1];
    /*

    Первый цикл вычисляет колличество путей к i-ой ступеньки, при условии, что i не
    превышает maxJump, начиная со 2 ступеньки (1 < i <= maxJump) по формуле:

     possibleCounts[i] = sum([possibleCounts[x] for x in range(0, i)]);

     - т.е.:
       колличество путей до каждой следующей ступеньки равен сумме колличеству путей
       для всех предыдущих ступенек (включая и положение на 0 ступеньке "с места").
     - т.к.:
       possibleCounts текущего шага равно сумме possibleCounts всех предыдущих шагов,
       то:

     possibleCounts[i] = possibleCounts[i-1](1) + possibleCounts[i-1](2);

     - где:
       первый possibleCounts[i-1] = сумма колличеств путей до ступенек меньше 'i-1';
       второй possibleCounts[i-1] = колличество путей до ступеньки 'i-1';

       итого, финальная формула:

     possibleCounts[i] = possibleCounts[i-1] * 2;

    */
    for (let i = 2; i <= maxJump; i++) {
        /*
        Так как i всегда соответствует длинне текущего массива, то значение
        possibleCounts[i] можно добавить в конец массива и оно будет соответствовать
        нужной ступеньке при доступе по индексам, при этом не затирая собой никакие
        предыдущие значения.
        */
        possibleCounts.push(possibleCounts[i-1] * 2);
    }

    /*

    Второй цикл вычисляет колличество путей к i-ой ступеньки, когда i становится больше
    maxJump (maxJump < i <= steps) по формуле:

     possibleCounts[i] = possibleCounts[i-1] * 2 - possibleCounts[i - 1 - maxJump]

     - т.е.:
       колличество путей до каждой следующей ступеньки равен сумме колличеству путей
       для всех предыдущих ступенек (включая и положение на 0 ступеньке "с места").
     - т.к.:
       possibleCounts текущего шага равно сумме possibleCounts всех предыдущих шагов,
       то:

    */
    for (i = maxJump + 1; i <= steps; i++) {
        possibleCounts.push(possibleCounts[i-1] * 2 - possibleCounts[i-1 - maxJump]);
    }
    return possibleCounts[steps];
}

console.log(countRabbitWays(3, 3));