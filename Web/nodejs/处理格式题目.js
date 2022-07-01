const r = [
    {pro:"广东省",city:"广州",dis:"天河"},
    {pro:"广东省",city:"广州",dis:"白云"},
    {pro:"广东省",city:"东莞",dis:"常平"}
]
const keys = ["pro","city","dis"]
const structure = {
    name:"",
    child:[
        {
            name:"",
            child:[{name:""}]
        }
    ]
}

const res = [];
function track(obj,key,deep=3){
    if(deep==0){
        res.push({name:obj[key],child:[]})
        return res
    }
    const result = track(obj,keys[0],deep-1)

    result.push({name:obj[keys[3 - deep]],child:[]})
    return result.child
}
const o = track(r[0],keys[0])
console.log(o[0]);