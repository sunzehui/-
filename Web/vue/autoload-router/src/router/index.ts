import { createRouter, createWebHistory } from "vue-router";
import autoLoadRoutes from "./autoload";
import customRoutes from "./route";

const router = createRouter({
  history: createWebHistory(),
  routes: [...autoLoadRoutes, ...customRoutes],
});

export default router;
