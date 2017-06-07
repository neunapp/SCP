(function(){
    "use strict";
    angular.module("CopreApp")
        .controller("SubprocesoAddCtrl", ['subprocesoservice', SubprocesoAddCtrl]);

    function SubprocesoAddCtrl(subprocesoservice){
        var self = this;

        //variables globales
        self.show_aad_avtivity = false;
        self.show_add_field = false;
        self.json_row = [];


        //funcion para mostrar cuadro de formulario
        self.show_form = function(value){
          if (value == '1') {
            self.show_aad_avtivity = true;
            self.show_add_field = false;
          }
          else if (value == '2') {
            self.show_aad_avtivity = false;
            self.show_add_field = true;
          }
          else {
            self.show_aad_avtivity = false;
            self.show_add_field = false;
          }
        }


        //funcion para recuperar actividades de un proceso
        self.get_process_activitys = function(pk){
            console.log('recuperamos actividades del proceso-----');
            //recuperamos actividades del servidor
            subprocesoservice.get_process_activitys(pk)
              .then(function(response){
                  self.activitys = response.data;
              });
        };


        //funcion para agregar actividad de proceso
        self.activityproceso_add = function(pk){
            self.show_aad_avtivity = false;
            //creamos serializador para sub proceso
            var activity = {
              'pk_proceso':pk,
              'name':self.name_subproceso,
              'description':self.description_subproceso,
            };
            //
            subprocesoservice.activityproceso_add(activity);
            //
            window.location.href = '/sub-proceso/agregar/'+pk+'/';
        };

        //funcion para agregar nuvas columnas a un sub proceso
        self.field_add_subprocess = function(pk,proceso){
          self.show_add_field = false;
          //pk es de subproceso
          var field = {
            'sub_process':pk,
            'name':self.name_field,
            'type_field':self.type_field,
            'required':self.required_field,
          };
          subprocesoservice.field_add_subprocess(field);
          window.location.href = '/sub-proceso/agregar/'+proceso+'/';
        };

        //funcion para agregar una nueva fila
        self.row_add = function(pk_subproceso){
          console.log('nueva columna para: '+pk_subproceso);
          //ceamos un json nuevo con tamaño=#columnas
          self.json_row = [];
          var lista = self.activitys;
          for (var i = 0; i < lista.length; i++) {
            if (lista[i].sub_proceso.sub_process == pk_subproceso) {
              console.log('--1--');
              //generamos el json
              for (var f in lista[i].fields) {
                console.log('--2--');
                var item = {
                  'detail_process':lista[i].sub_proceso.pk,
                  'field':f.field,
                  'sub_process':pk_subproceso,
                  'value':'',
                };
                self.json_row.push(item);
              }
            }
          }
          console.log(self.json_row);
        };
    }
}());
