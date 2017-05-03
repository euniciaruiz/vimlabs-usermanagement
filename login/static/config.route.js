angular
    .module('app')
    .config(function($stateProvider, $urlRouterProvider, $httpProvider){
        $urlRouterProvider.otherwise('/profile');

        $stateProvider
            .state('profile',{
                url: '/profile',
                templateUrl: 'profile/profileList.html',
                controller: 'profileListController'
            })
            .state('profile.create', {
                url:'/create',
                templateUrl: 'profile/create-profile.html',
                controller: 'createProfileController'
            });
    });