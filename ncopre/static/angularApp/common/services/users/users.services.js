(function(){
    "use strict"
    angular.module("common.services")
        .factory("userservice", Userservice);
        function Userservice($http){
          var self = {};

          //servicio que lista usuarios
          self.users_list = function(){
            return $http.get("/api/user-list/");
          };

          return self;
        }
}());
