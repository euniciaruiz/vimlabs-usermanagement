'use strict';

angular
    .module('app.profile')
    .controller('createProfileController', createProfileController);

function createProfileController($scope, $http, $resource, $window){
    $scope.createProfile = createProfile;

    function createProfile(){
        var data = {
            first_name: $scope.first_name,
            last_name: $scope.last_name,
            username: $scope.username,
            email: $scope.email,
            password: $scope.password
        };
        $http.post('/api/users/', data)
            .then(function(response){
                $window.location.href="/";
        });
    }
}