
(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("SubprocesoListCtrl", ['subprocesoservice', SubrocesoListCtrl]);

    function SubrocesoListCtrl(subprocesoservice){
        var self = this;

        //funcion que recupera voucher factura
        self.itemfactura_list = function (pk) {
            subprocesoservice.itemfactura_list(pk)
             .then(function(response){
                self.proceso_factura = response.data;
            });
        };


        self.factura_count = function (pk) {
            subprocesoservice.factura_count(pk)
                .then(function (response) {
                   self.facturas =response.data;
                });

        };


                //funcion para agregar actividad de proceso
        self.itemfactura_add = function(pk){
            var date_broadcastI = self.date_broadcast;
            var date_broadcast = new Date(date_broadcastI);
            date_broadcast = date_broadcast.getFullYear() + "-" + (date_broadcast.getMonth() +1) + "-" + date_broadcast.getDate();
          /*  var date = new Date(self.date_broadcast);
            console.log(date.toDateString());
            var date_broad = date.toDateString();
            var date_broadcast = date_broad.split('/');*/
            var json = {
              'type_voucher':1,
              'number':self.number,
              'amount':self.amount,
              'description':self.description,
              'date_broadcast':date_broadcast,
              'process':pk
            };
            console.log(json);
            console.log(self.date_broadcast);
            console.log(subprocesoservice.itemfactura_add(json));
            console.log('agregado correctamente');
        };

        self.retrieve = function (objeto) {
            angular.fromJson(objeto)
            console.log(objeto.description)
        }
    }





}());
