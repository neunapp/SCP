(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ObservationAddCtrl", ['observationservice', ObservationAddCtrl]);

    function ObservationAddCtrl(observationservice){
        var self = this;


        //funcion que agrega observacion
        self.observation_add = function(pk){

            var json = {
                'process':pk,
                'description': self.description,
                'type_observation':self.type_observation
            };
            console.log(json);
            console.log(observationservice.observation_add(json));
            console.log('agregado correctamente')
        };

    }
}());
