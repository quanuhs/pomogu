import { createRouter, createWebHistory } from 'vue-router'
import {authorised} from './api'

const routes = [
    {path: '/:pathMatch(.*)*', name: 'not-found', component:  () => import('./views/NotFoundPage.vue'), meta:{protected: false}},
    {path: '', name:'main', component: () => import('./views/MainPage.vue'), meta:{protected: false}},
    {path: '/search', name:'search', component: ()=> import("./views/CatalogPage.vue"), meta:{protected: false}},
    {path: '/call/:id', name:'videocall', component: () => import("./views/VideoCallPage.vue"), meta:{protected: true}},
    {path: '/me', name:'me', component: () => import("./views/Profile.vue"), meta:{protected: true}},
    {path: '/profile/:id', name:"profile", component: () => import('./views/TherapistProfile.vue'), meta:{protected: false}},
    // {path: '/sign/:id', name:"sign", component: () => import('./views/SignSessionPage.vue'), meta:{protected: true}},
]

const router = createRouter({
    routes,
    history: createWebHistory(),
}
)

router.beforeEach(async (to, from, next) => {
    let isProtected = to.matched.some(record => record.meta.protected);

    if (isProtected && !authorised){
        next("/");
        return;
    }

    
    next()
})

export default router