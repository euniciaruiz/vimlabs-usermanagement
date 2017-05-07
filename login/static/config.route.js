angular
    .module('app')
    .config(routeConfig)
    .config(jwtConfig)
    .run(run)
    .controller('loginController', loginController);

function jwtConfig($httpProvider, $localStorageProvider, jwtOptionsProvider) {
    jwtOptionsProvider.config({
        tokenGetter: function () {
            return localStorage.getItem('token');
        },
        loginPath: '/login',
        unauthenticatedRedirectPath: '/login'
    });

    $httpProvider.interceptors.push('jwtInterceptor');
}


function routeConfig($stateProvider, $urlRouterProvider, $httpProvider){
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('profile',{
            url: '/',
            templateUrl: 'profile/profileList.html',
            controller: 'profileListController'
        })
        .state('profile.create', {
            url:'/create',
            templateUrl: 'profile/create-profile.html',
            controller: 'createProfileController'
        })
        .state('profile.details', {
            url: 'edit/:id',
            templateUrl: 'profile/profile-detail.html',
            controller: 'profileController'
        })
        .state('login', {
            url: "/login",
            templateUrl: "login/login.html",
            controller: loginController
        });
}

function run($state, $rootScope, $localStorage, $location, authManager, authService){
    authManager.checkAuthOnRefresh();

    $rootScope.$state = $state;

    $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams){
        if( !$localStorage.isAuthenticated){
            $location.path('/login');
        }
    });
}

function loginController($scope, $state, $window, $localStorage,
                         $sessionStorage, authManager, authService) {
    $scope.logged = true;
    $scope.login = function () {
        var username = $scope.username;
        var password = $scope.password;
        authService.obtainToken(username, password)
            .then(function (result) {
                if (result.success) {
                    authManager.authenticate();
                    authService.authenticate(result.token, result.user);
                }
        });
    }
}


