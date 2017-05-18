(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("SubprocesoAddCtrl", ['subprocesoservice', SubprocesoAddCtrl]);

    function SubprocesoAddCtrl(subprocesoservice){
        var self = this;

        //variables globales
        self.fields = [];
        self.items = [];

        //funcion para agregar nuvas columnas a un sub proceso
        self.columns_add = function(){
          var field = {
            'name':self.name_field,
            'type_field':self.type_field,
            'required':self.required_field,
          };
          self.fields.push(field);
        };

        //funcion para agregar una nueva fila
        self.rows_add = function(){
          var row = [];
          for (var i = 0; i < self.fields.length; i++) {
            var field = {
              'name_field':self.fields[i].name,
              'id':i,
            };
            row.push(field);
          }
          var item = {
            'colums':row,
          }
          //
          self.items.push(item);
          //
        };

        //funcion que agrega process
        self.subproceso_add = function(pk){
            //creamos serializador para sub proceso
            var sub_process = {
              'pk_proceso':pk,
              'name':self.name_subproceso,
              'description':self.description_subproceso,
            };

            //creamos serializador para campos
            console.log(self.fields);

            //creamos serialziador para items
            var items = [];
            for (var i = 0; i < self.items.length; i++) {
              for (var j = 0; j < self.items[i].colums.length; j++) {
                var item = {
                  'field_key':self.items[i].colums[j].name_field,
                  'value':self.items[i].colums[j].valor[j],
                };
                items.push(item);
              }
            }
            console.log(items);

            //creamos json pra sub proceso
            var json = {
              'sub_process':sub_process,
              'fields':self.fields,
              'items':items,
            };

            //enviamos al servidor
            subprocesoservice.subproceso_add(json);

        };
    }
}());
