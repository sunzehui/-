import _ from "lodash";
import { RouteRecordRaw } from "vue-router";
const layoutRoutes = import.meta.globEager("../layouts/*.vue");
const viewRoutes = import.meta.globEager("../views/**/*.vue");

const getViewRoutes = (filename: string, component: any): RouteRecordRaw => {
  const name = filename.match(/\.\.\/views\/(?<name>.+?)(index)?\.vue/i)?.groups
    ?.name;

  return {
    path: "/" + name,
    name: name,
    component: component.default,
    children: [],
  };
};

const getLayoutRoutes = (filename: string, component: any): RouteRecordRaw => {
  const name = filename.match(/\.\.\/layouts\/(?<name>.+?)\.vue/i)?.groups
    ?.name;

  return {
    path: "/" + name,
    name: name,
    component: component.default,
    children: [],
  };
};
const getChildRoutes = (layoutRoute: RouteRecordRaw) => {
  const routes: RouteRecordRaw[] = [];
  _.toPairs(viewRoutes).map(([filename, module]) => {
    if (filename.includes(layoutRoute.name as string)) {
      routes.push(getViewRoutes(filename, module));
    }
  });
  return routes;
};
const getRoutes = () => {
  const routes = _.toPairs(layoutRoutes).map(([file, module]) => {
    const layoutRoute = getLayoutRoutes(file, module);
    layoutRoute.children = getChildRoutes(layoutRoute);
    return layoutRoute;
  });
  console.log(routes);
  return routes;
};

export default getRoutes();
