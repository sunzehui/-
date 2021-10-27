interface Object {
    Getter: Function,
    Setter: Function
}

Object.prototype.Getter = function (path: String, defaultValue: string | undefined) {
    const keys = path.split(".")
    let result = this[keys[0]];

    for (let i = 1; i < keys.length; i++) {
        if (result === void 0) {
            return defaultValue;
        } else {
            result = result[keys[i]]
        }
    }
    return result || defaultValue;
}

Object.prototype.Setter = function (path: String, value: any) {
    const keys = path.split(".")
    let result = this;
    for (var i = 0; i < keys.length - 1; i++) {


        if (result[keys[i]] === void 0) {
            result[keys[i]] = {}
        }
        if (!(result[keys[i]] instanceof Object)) {
            throw new Error("can't set property on no-object at " +
                keys.slice(0, i + 1).join("."));
        }
        result = result[keys[i]];
    }

    return result[keys[i]] = value;
}

const obj: any = {
    client: {
        user: {
            username: "sunzehui",
            age: "20"
        }
    }
}
// import _ from "lodash"
// _.set(obj, "client.user", 89)
console.log(obj.Setter("client.data.value", 899));
console.log(obj);
