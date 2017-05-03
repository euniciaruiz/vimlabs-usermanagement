angular
    .module('app.profile')
    .controller('profileListController', profileListController);

function profileListController($scope, $http, $resource){
    $scope.title = "User Profiles";
    $scope.getProfiles = getProfiles;

    getProfiles();

    function getProfiles(){
        $http.get('/api/users')
            .then(function(response){
                $scope.profiles = response.data;
            });
    }
}