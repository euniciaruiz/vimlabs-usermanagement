angular
    .module('app.profile')
    .controller('profileListController', profileListController);

function profileListController($scope, $http, $resource, $state, authService){
    $scope.title = "User Profiles";
    $scope.getProfiles = getProfiles;
    $scope.deleteProfile = deleteProfile;
    $scope.logout = logout;

    getProfiles();

    function getProfiles(){
        $http.get('/api/profiles')
            .then(function(response){
                $scope.profiles = response.data;
            });
    }

    function deleteProfile(id){
        var con = confirm("Are you sure you want to delete this user?");
        if(con == true){
            $http.delete('/api/users/'+id).then(function(response){
                $state.go('profile', {}, {reload:true});
            });
        }else{
            $state.go('profile', {}, {reload: true});
        }
    }

    function logout(){
        authService.unauthenticate();
    }
}
