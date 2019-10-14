/*
    Heart App by Katik.
    It draws a heart from words "I Love You".
*/

let width: Int = 14 * 4 + 4
let height: Int = 19 + 2
let letters: [String] = ["I", "L", "o", "v", "e", "Y", "o", "u"]

let index: [[Int]] = [
    [11, 22, 39, 49], [7, 25, 36, 53], [4, 27, 34, 56], [3, 28, 33, 57],
    [2, 29, 32, 58], [2, 58], [2, 58], [3, 57], [3, 57], [5, 55], [7, 53],
    [9, 51], [11, 49], [13, 47], [15, 45], [17, 43], [20, 40], [24, 36],
    [29, 31],
    [],[]
]

var i = 0
var now = 0
var max = 7

var heart: String = "My love to You :) \n\n"

while i < height {
    var start = 0

    var startsAt, endsAt: Int
    var compose = false

    if index[i].count == 4 {
        compose = true
        startsAt = index[i][0]
        endsAt = index[i][1]
    } else if index[i].count == 2 {
        startsAt = index[i][0]
        endsAt = index[i][1]
    } else {
        while start < width {
            heart += " "
            start += 1
        }
        i += 1
        continue
    }

    while start < width {
        if start < startsAt || start > endsAt {
            if compose && start > startsAt {
                startsAt = index[i][2]
                endsAt = index[i][3]
                compose = false
            }

            heart += " "

        } else {
            heart += letters[now]
            now += 1

            if now > max {
                now = 0
            }
        }

        start += 1
    }

    heart += "\n"
    i += 1
}


print(heart)
