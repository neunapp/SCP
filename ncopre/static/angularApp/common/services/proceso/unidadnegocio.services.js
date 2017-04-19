(function(){
    "use strict"
    angular.module("common.services")
        .factory("unidadnegocioservice",unidadnegocioservice)
        function unidadnegocioservice($http){
          var self = {};

          //servicio que lista equipos de un usuario delgado
          self.unidadnegocio_lista = function(){
            return $http.get("/api/unidadnegocio/list/");
          }
          return self;
        }
}());
