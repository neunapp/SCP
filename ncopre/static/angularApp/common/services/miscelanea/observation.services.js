(function(){
    "use strict";
    angular.module("common.services")
        .factory("observationservice", Observationservice);
        function Observationservice($http){
          var self = {};

          //funcion que lista observacion por proceso
          self.observation_lista = function (pk) {
              return $http.get("/api/observacion/listar/"+pk+"/");
          };


          self.observation_stateupdate = function(json){
            return $http.post("/api/observacion/update/", json)
                .success(function(res){
                    return res.id;
                })
                .error(function(res){
                    return '0'
                });
          };



          self.observation_add = function (json) {
              return $http.post("/api/observacion/add/", json)
                  .success(function (res) {
                      return res.id
                  })
                  .error(function (res) {
                      return '0'
                  })
          };


          return self;
        }




}());
