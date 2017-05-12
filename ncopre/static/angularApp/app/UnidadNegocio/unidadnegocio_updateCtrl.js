(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("UnidadnegocioUpdateCtrl", ['unidadnegocioservice', UnidadnegocioUpdateCtrl]);

    function UnidadnegocioUpdateCtrl(unidadnegocioservice){
        var self = this;
        
        //funcion para recuperar unidad de negocio
        self.unidadnegocio_retrieve = function(pk) {
           unidadnegocioservice.unidadnegocio_retrieve(pk)
             .then(function(response){
                 var unidad_negocio = response.data;
                 self.ruc = unidad_negocio.ruc;
                 self.razon_social = unidad_negocio.razon_social;
                 self.addresses = unidad_negocio.addresses;
                 self.phone = unidad_negocio.phone;
             })
        };

        //funcion para actualizar unidad de negocio
        self.unidadnegocio_update = function(pk){
            var json = {
                "pk":pk,
                'ruc': self.ruc,
                'razon_social': self.razon_social,
                'addresses': self.addresses,
                'phone': self.phone

            };
            unidadnegocioservice.unidadnegocio_update(json);
            console.log('transaccion conforme');
        }
        
  }
}());
