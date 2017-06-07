(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("UnidadnegocioAddCtrl", ['unidadnegocioservice', UnidadnegocioAddCtrl]);

    function UnidadnegocioAddCtrl(unidadnegocioservice){
        var self = this;

        //funcion que valida datos del formulario
        self.validate_fields = function() {
          if(self.ruc.length != 11){
              self.msj_ruc = 'ruc debe tener 11 digitos ';
              self.bool_ruc = false;
          }
          else{
              self.msj_ruc = '';
              self.bool_ruc = true;
          }

        };

        //funcion que agrega unidad de negocio
        self.unidadnegocio_add = function(){
            var json = {
                'ruc': self.ruc,
                'razon_social': self.razon_social,
                'addresses': self.addresses,
                'phone': self.phone
            };


            console.log(unidadnegocioservice.unidadnegocio_add(json));
            console.log('agregado correctamente')
        };
    }
}());
