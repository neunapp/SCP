(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ObservationListCtrl", ['observationservice', ObservationListCtrl]);

    function ObservationListCtrl(observationservice){
        var self = this;

       //funcion que lista observacion por proceso
        self.observation_lista = function(pk){
          observationservice.observation_lista(pk)
            .then(function(response){
                self.observation = response.data;
            });
        };

        self.observation_stateupdate= function (pk, bolean) {
           var json = {
               "pk":pk,
               "anulate": bolean
           };
           console.log(observationservice.observation_stateupdate(json));
           console.log("agregado correctamente");
        };

  }
}());
