(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ProcesoAddCtrl", ['procesoservice','userservice', ProcesoAddCtrl]);

    function ProcesoAddCtrl(procesoservice,userservice){
        var self = this;


        //funcion que agrega process
        self.proceso_add = function(pk){

            var date_start = new Date(self.date_start);
            date_start = date_start.getFullYear() + "-" + (date_start.getMonth() +1) + "-" + date_start.getDate()
            var date_end = new Date(self.date_end);
            date_end = date_end.getFullYear() + "-" + (date_end.getMonth() +1) + "-" + date_end.getDate()

            var json = {
              'bussinesunit':pk,
              'name': self.name,
              'origin':self.origin,
              'destination':self.destination,
              'attendant': self.attendant,
              'responsible': self.responsible,
              'date_start':date_start,
              'date_end':date_end,
              'budget_estimated':self.budget_estimated,
            };
            var proceso = procesoservice.proceso_add(json);
            proceso.then(function(response){
                console.log(response.data);
                window.location.href = '/sub-proceso/agregar/'+response.data.pk+'/';
            });
          }

        //lista de usuarios
        self.users_list = function(){
          userservice.users_list()
            .then(function(response){
                self.usuarios = response.data;
            });
        };
    }
}());
