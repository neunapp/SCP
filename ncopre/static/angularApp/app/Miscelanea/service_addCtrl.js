(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("ServiceAddCtrl", ['serviceservice', ServiceAddCtrl]);

    function ServiceAddCtrl(serviceservice){
        var self = this;


        //funcion que agrega servicio
        self.service_add = function(pk){

            var json = {
                'name':self.name,
                'ruc': self.ruc,
                'razon_social':self.razon_social,
                'phone':self.phone,
                'description':self.description,
                'process':pk
            };
            console.log(json);
            console.log(serviceservice.service_add(json));
            console.log('agregado correctamente')
        };

    }
}());
