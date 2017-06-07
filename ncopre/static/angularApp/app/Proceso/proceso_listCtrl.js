(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ProcesoListCtrl", ['procesoservice','unidadnegocioservice',
                      ProcesoListCtrl]);

    function ProcesoListCtrl(procesoservice,unidadnegocioservice){
        var self = this;

        //variables globales
        self.flat_new_process = false;

        //funcion que lista proceso por undada de negocio
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

        //----------------------------------------------------------------------

        //funcion que lista unid de negocio
        self.unidadnegocio_lista = function(){
          unidadnegocioservice.unidadnegocio_lista()
              .then(function (response) {
                  self.bussiness = response.data;
                }
              )
        }
        //funcion que lista procesos recientes
        self.process_recent = function () {
            //listamos unidad de negocio
            self.unidadnegocio_lista();
            //consulta a bd
            procesoservice.process_recent()
                .then(function (response) {
                    self.lits_process = response.data;
                  }
                )
        };

        //proceso que filtra procesos por nombre
        self.process_search = function (name) {
          console.log('entro aquisito 2');
            //convertimos el valor name a kword para url
            var kword = '';
            for (var i = 0; i < name.split(" ").length; i++) {
              if (kword == '') {
                kword = name.split(" ")[i];
              }
              else {
                kword = kword +'-'+ name.split(" ")[i];
              }

            }
            //re-inicializamos
            self.search = '';
            //consultamos al servidor
            procesoservice.process_search(kword)
              .then(function (response) {
                  self.lits_process = response.data;
              })
        };

        //funcion que lista procesos agrupados por unidad de negocio
        self.process_by_bussiness = function(){
            procesoservice.process_by_bussiness()
              .then(function(response) {
                  self.lits_process = response.data;
              }
            );
        }

    }


}());
