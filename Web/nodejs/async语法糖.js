function next_step(action,gen,resolve,reject,args,_next,_throw){
    try{
        const {done,value} = gen[action](args);
        if(!done){
            Promise.resolve(value).then(_next,_throw)
        }else{
            resolve(value)
        }
    }catch(e){
        reject(e)
    }
}
function _async(fn){
    return function(...args){
        const self = this;
        return new Promise((resolve,reject)=>{
            const gen = fn.apply(self,args)

            function _next(...args){
                next_step("next",gen,resolve,reject,args,_next,_throw)
            }
            function _throw(...args){
                next_step("throw",gen,resolve,reject,args,_next,_throw)

            }
            _next()
        })
    }
}

const asyncfun = _async(function*(){
    yield new Promise((resolve,reject)=>{
        resolve(1)
    })
})
asyncfun().then(res=>{
    console.log(res);
})