(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("UnidadnegocioListCtrl", ['unidadnegocioservice', UnidadnegocioListCtrl]);

    function UnidadnegocioListCtrl(unidadnegocioservice){
        var self = this;

        //funcion que lista unidad de negocio
        self.unidadnegocio_lista = function(){
          unidadnegocioservice.unidadnegocio_lista()
            .then(function(response){
                self.unidad_negocios = response.data;
            });
        };

        //funcion para recuperar unidad de negocio
        self.unidadnegocio_retrieve = function (pk) {
           unidadnegocioservice.unidadnegocio_retrieve(pk)
             .then(function(response){
                 self.unidad_negocio = response.data;
             })
        };

        //funcion para actualizar estado de unidad de negocio
        self.unidadnegocio_stateupdate = function (pk, bolean) {
           var json = {
               "pk":pk,
               "anulate": bolean
           };
           console.log(unidadnegocioservice.unidadnegocio_stateupdate(json));
           console.log("agregado correctamente");
        };


        
  }
}());
