'use strict';

angular
    .module('app.profile')
    .controller('profileController', profileController);

function profileController($scope, $http, $stateParams, $state, $location){
    $scope.loadDetails = loadDetails;
    $scope.updateProfile = updateProfile;
    $scope.updated = false;
    loadDetails();

    function loadDetails(){
        if($stateParams.id && $state.params.id != 'create'){
            $http.get('/api/profiles/'+$stateParams.id)
                .then(function(response){
                    $scope.first_name = response.data.first_name;
                    $scope.last_name = response.data.last_name;
                    $scope.username = response.data.username;
                    $scope.email = response.data.email;
                    $scope.password = response.data.password;
                    $scope.role = response.data.role;
                });
        }else{
            console.log('create');
        }
    }

    function updateProfile(){
        var data = {
            username: $scope.username,
            first_name: $scope.first_name,
            last_name: $scope.last_name,
            email: $scope.email,
            password: $scope.password,
            role: $scope.role
        };

        $http.put('/api/profiles/'+$stateParams.id+'/', data)
            .then(function(response){
                console.log(response);
                $state.go('profile', {}, {reload:true});
            });
    }

    
}