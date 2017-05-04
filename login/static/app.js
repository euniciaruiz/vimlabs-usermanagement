angular
    .module('app', [

        'ui.bootstrap',
        'ui.router',
        'ngResource',
        'angular-storage',
        'angular-jwt',
        'ngStorage',
        'app.auth',
        'app.profile',
    ])
    .config(function($stateProvider, $urlRouterProvider, $httpProvider, jwtInterceptorProvider){
        jwtInterceptorProvider.tokenGetter = function(store){
            return store.get('token');
        };

        $httpProvider.interceptors.push('jwtInterceptor');
    });