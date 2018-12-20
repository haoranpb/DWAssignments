import Vue from 'vue'
import Router from 'vue-router'
import MovieQuerier from './views/MovieQuerier.vue'
import RelationQuerier from './views/RelationQuerier.vue'
import Graph from './views/Graph.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'moviequerier',
      component: MovieQuerier
    },
    {
      path: '/relation',
      name: 'relation',
      component: RelationQuerier
    },
    {
      path: '/graph',
      name: 'graph',
      component: Graph
    }
  ]
})
