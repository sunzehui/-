---
title: vue3.0笔记
date: 2020-12-06 12:02:39
tags:
---
```js
// vue.config.js
const path = require('path')
// 拼接当前路径
const resolve = dir => path.join(__dirname, dir)

module.exports = {
  // 保存时eslint检查
  lintOnSave: true,
  chainWebpack: config => {
    config.resolve.alias
      // 设置文件中的@路径，添加_c为components路径
      .set('@', resolve('src'))
      .set('_c', resolve('src/components'))
  },
  // 加快打包速度
  productionSourceMap: false
}
```

# 命名视图

```js
{
  path: '/named_view',
  components: {
    default: () => import('@/views/About'),
    email: () => import('@/views/child')
  }
}

```

- 注意components加了s
- components传入对象

## 路由重定向

```js
{
  path: '/index',
  redirect: to => '/'
}
```

- redirect可以传入to，路由守卫

## 路由别名

```js
{
  path: '/',
  name: 'Home',
  alias: 'index',
  component: Home
},
```



##  History操作

```js
// 后退
this.$router.go(-1)
this.$router.back()

// 跳转到路由（会记录到history）
this.$router.push('/about')
// 替换路由（不会记录history）
this.$router.replace('/about')

// 传递参数
this.$router.push({
    name: 'argu',
    params: {
        name: 'haha'
    }
})
// 或
this.$router.push({
    path: '/argu/haha'
})
```



## 路由解耦



- 普通写法

```vue
// route.js
{
  path: '/argu/:name',
  name: 'argu',
  component: () => import('@/views/getname.vue'),
  props: true	//设置props属性为true
},
    
// getname.vue
<template>
  <div class="root">
    {{ name }}
  </div>
</template>

<script>
export default {
  name: 'getname',
  props: {
    name: {
      type: String,
      default: 'None'
    }
  }
}
</script>
```

- 函数式写法

```js
  // route.js
{
    path: '/argu',
    name: 'argu',
    component: () => import('@/views/getname.vue'),
    props: route => ({
      name: route.query.name
    })
  }
```

  

