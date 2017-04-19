(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("UnidadnegocioListCtrl", ['unidadnegocioservice', UnidadnegocioListCtrl]);

    function UnidadnegocioListCtrl(unidadnegocioservice){
        var self = this;

        //funcion que lista unidad de negocio
        self.unidadnegocio_lista = function(){
          equiposervice.unidadnegocio_lista()
            .then(function(response){
                self.unida_negocio = response.data;
            });
        };
  }
}());
