import "reflect-metadata";
import { createConnection } from "typeorm";
import { User } from "./entity/User";

// 生成随机姓名
function createUserName() {
  // 生成随机数：[n, m)
  function random(n, m) {
    return (Math.random() * (m - n) + n) >> 0;
  }
  return new Array(5).fill("").reduce((prev, cur) => {
    return prev + String.fromCharCode(random(97, 123));
  }, String.fromCharCode(random(65, 91)));
}

// 创建 user实例
function createUser() {
  let user = new User();
  user.firstName = createUserName();
  user.lastName = createUserName();

  user.age = Math.random() * 100;
  return user;
}

createConnection()
  .then(async (connection) => {
    const userRepositroy = await connection.getRepository(User);

    // let photoToRemove = await userRepositroy.find();
    // await userRepositroy.remove(photoToRemove);
    for (let index = 0; index < 10; index++) {
      const user = createUser();
      await userRepositroy.save(user);
    }

    console.log("Loading users from the database...");
    const saveRepository = await userRepositroy.find();
    console.log("Loaded users: ", saveRepository);
    console.log("Here you can setup and run express/koa/any other framework.");
  })
  .catch((error) => console.log(error));
