(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ProcesoAddCtrl", ['procesoservice', ProcesoAddCtrl]);

    function ProcesoAddCtrl(procesoservice){
        var self = this;


        //funcion que agrega process
        self.proceso_add = function(pk){

            var json = {
            'bussinesunit':pk,
            'name': self.name,
            'attendant': self.attendant,
            'responsible': self.responsible,
            'date_start':self.date_start,
            'date_end':self.date_end,
            'budget_estimated':self.budget_estimated,
            'budget_real': self.budget_real
            };
            console.log(json);
            console.log(procesoservice.proceso_add(json));
            console.log('agregado correctamente')
        };


        //lista de usuarios
        self.procesousuario_list = function(){
          procesoservice.procesousuario_list()
            .then(function(response){
                self.proceso_usuario = response.data;
            });
        };
    }
}());
