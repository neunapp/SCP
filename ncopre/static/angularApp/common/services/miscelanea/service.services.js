(function(){
    "use strict";
    angular.module("common.services")
        .factory("serviceservice", Serviceservice);
        function Serviceservice($http){
          var self = {};

          //funcion que lista observacion por proceso

          self.service_add = function(json){
            return $http.post("/api/servicio/add/", json)
                .success(function(res){
                    return res.id;
                })
                .error(function(res){
                    return '0'
                });
          };



          return self;
        }




}());
