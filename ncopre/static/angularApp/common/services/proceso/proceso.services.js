(function(){
    "use strict"
    angular.module("common.services")
        .factory("procesoservice", procesoservice);
        function procesoservice($http){
          var self = {};

          //agregar a la tabla proceso
          self.proceso_add = function(json) {
            return $http.post("/api/proceso/nuevo/", json)

                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
               });
          };

          //lista usuario para agregar proceso
          self.procesousuario_list = function () {
              return $http.get("/api/userproceso/list/");
          };

          //listar proceso por unidad de negcio
          self.procesobunit_list = function (pk) {
              return $http.get("/api/proceso/list/"+pk+"/");
          };

          //listar proceso que estan en proceso
          self.procesofiltro_list = function (pk, flat) {
              return $http.get("/api/filtroproceso/listar/"+pk+"/"+flat+"/")
          };

          return self;
        }

}());
