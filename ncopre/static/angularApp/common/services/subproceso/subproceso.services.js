(function(){
    "use strict"
    angular.module("common.services")
        .factory("subprocesoservice", Subprocesoservice);
        function Subprocesoservice($http){
          var self = {};

          //servicio para agregar un sub proceso de un proceso
          self.subproceso_add = function(json) {
            return $http.post("/api/sub-proceso/add/", json)
                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
               });
          };

          return self;
        }

}());
