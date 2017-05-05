angular
    .module('app.auth', [])
    .factory('authService', function($state, $filter, $http, $window, $resource, $localStorage,
                                     $sessionStorage, jwtHelper){

    return {
        obtainToken: function(username, password){
            return $http.post('/api-token-auth/', {username: username, password: password})
                .then(function(result){
                    if(result.status == 404 || result.status == 400){
                        return {success:false};
                    }
                    else{
                        return {success: true, token: result.data.token, user: result.data.user};
                    }
                });
        },
        authenticate: function(token, user){
            $localStorage.isAuthenticated = true;
            $localStorage.token = token;
            $localStorage.user = user;
            $state.go('profile', {}, {reload: true});
        },
        unauthenticate: function(){
            $localStorage.$reset({
                isAuthenticated: false,
                user: null,
                token: null
            });
            $state.go('login', {}, {reload: true});
        }
    }
});