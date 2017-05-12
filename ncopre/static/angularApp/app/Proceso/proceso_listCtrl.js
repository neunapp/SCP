(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ProcesoListCtrl", ['procesoservice', ProcesoListCtrl]);

    function ProcesoListCtrl(procesoservice){
        var self = this;

        //funcion que lista proceso por undada de negocoi
        self.procesobunit_list = function (pk) {
            procesoservice.procesobunit_list(pk)
             .then(function(response){
                self.proceso_for_unidadnegocio = response.data;
            });
        };

        //funcion que lista proceso en proceso

        //funcion que lista procesos eliminados
        self.procesofiltro_list = function (pk, flat) {
            procesoservice.procesofiltro_list(pk, flat)
              .then(function (response) {
                  self.respuesta = response.data;
                })
        };
    }


}());