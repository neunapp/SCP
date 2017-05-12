(function(){
    "use strict"
    angular.module("common.services")
        .factory("unidadnegocioservice", unidadnegocioservice)
        function unidadnegocioservice($http){
          var self = {};
            //servicio que lista unidades de negocio
          self.unidadnegocio_lista = function(){
            return $http.get("/api/unidadnegocio/list/");
          };
          //servicio que lista unidades de negocio eliminadas
          /*self.unidadnegocio_by_anulate = function(){
            return $http.get("/api/unidadnegocio/list_anulados/");
          };*/


          self.unidadnegocio_add = function(json) {
             return $http.post("/api/unidadnegocio/nuevo/", json)
                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
                });
          };


          //funcion para recuperar una unidad de negocio
          self.unidadnegocio_retrieve = function(pk){
            return $http.get("/api/unidadnegocio/retrieve/"+pk+'/');
          };


          // funcion para actualizar una unidad de negocio
          self.unidadnegocio_update = function(json){
            return $http.post("/api/unidadnegocio/update/", json)
                .success(function(res){
                    return res.id;
                })
                .error(function(res){
                    return '0'
                });
          };


          //funciones para actualizar estado de una unidad de negoio
          self.unidadnegocio_stateupdate = function (json) {
              return $http.post("/api/unidadnegocio/estado/", json)
                  .success(function (res) {
                      return res.id;

                  })
                  .error(function () {
                      return '0'
                  });

          };



          return self;
        }

}());
