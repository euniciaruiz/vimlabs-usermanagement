'use strict';

angular
    .module('app.profile')
    .controller('createProfileController', createProfileController);

function createProfileController($scope, $http, $resource, $state){
    $scope.createProfile = createProfile;

    function createProfile(){
        var data = {
            first_name: $scope.first_name,
            last_name: $scope.last_name,
            username: $scope.username,
            email: $scope.email,
            password: $scope.password,
            role: $scope.role
        };
        console.log($scope.role);
        $http.post('/api/users/', data)
            .then(function(response){
                $state.go('profile', {}, {reload:true});
        });
    }
}