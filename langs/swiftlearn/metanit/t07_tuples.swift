// Кортежи
let props = (88, "skill")
var userInfo: (Bool, Int, String) = (false, props.0, "Ridj")
let (isMarried, _, name) = userInfo
let skill = userInfo.1
userInfo.2 = "Katik"
print(name, skill, isMarried, userInfo)

let gingerUserInfo = (married: false, skill: 13, name: "Ginger")
let gingerSkill = gingerUserInfo.skill
var gingername = gingerUserInfo.name
print(gingerUserInfo)
