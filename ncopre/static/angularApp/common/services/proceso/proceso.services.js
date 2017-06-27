(function(){
    "use strict"
    angular.module("common.services")
        .factory("procesoservice", procesoservice);
        function procesoservice($http){
          var self = {};
          self.respuesta;
          //agregar a la tabla proceso
          self.proceso_add = function(json) {
            return $http.post("/api/proceso/nuevo/", json)

                .success(function(res){
                  self.respuesta = res;
                  console.log('---------');
                  console.log(self.respuesta);
                  return res;
                })
                .error(function(res){
                  return '0'
               });
          };

          //listar proceso por unidad de negcio
          self.procesobunit_list = function (pk) {
              return $http.get("/api/proceso/list/"+pk+"/");
          };

          //listar proceso que estan en proceso
          self.procesofiltro_list = function (pk, flat) {
              return $http.get("/api/filtroproceso/listar/"+pk+"/"+flat+"/");
          };

          //------------------------------------------------------------------------------

          //listar procesos buscados
          self.process_search = function (kword) {
              return $http.get("/api/proceso/buscar/"+kword+"/");
          };


          //listar procesos recientes
          self.process_recent = function () {
              return $http.get("/api/procesoreciente/listar/");
          };

          //listar procesos agrupados por unidad de negocio
          self.process_by_bussiness = function () {
              return $http.get("/api/proceso/por-unidad-negocio/");
          };

          
          //cambiar estados de un proceso
          self.procesostate_change = function (json) {
            return $http.post("/api/procesoestado/cambiar/", json)
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
