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

        //funcion que lista procesos por unidad de negocio segun flat
        self.procesofiltro_list = function (pk, flat) {
            procesoservice.procesofiltro_list(pk, flat)
              .then(function (response) {
                  self.respuesta = response.data;
                })
        };


        //funcion que lista procesos recientes
        self.procesoreciente_list = function (pk) {
            procesoservice.procesoreciente_list(pk)
                .then(function (response) {
                    self.procesoreciente = response.data;

                })

        };


        //proceso que filtra procesos por nombre
        self.procesonombre_list = function (pk, name) {
            procesoservice.procesonombre_list(pk, name)
                .then(function (response) {
                    self.procesonombre = response.data;
                })
        };

    }


}());