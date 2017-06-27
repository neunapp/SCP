(function(){
    "use strict"
    angular.module("common.services")
        .factory("subprocesoservice", Subprocesoservice);
        function Subprocesoservice($http){
          var self = {};


          //listar actividades de un proceso
          self.get_process_activitys = function (pk) {
              return $http.get("/api/get-process-activity/"+pk+"/");
          };

          //listar Field de un subproceso
          self.get_subprocess_fields = function (pk) {
            //pk de sub proceso
            return $http.get("/api/get-subprocess-fields/"+pk+"/");
          };

          //servicio para agregar una actividad de proceso
          self.activityproceso_add = function(json) {
            return $http.post("/api/activity-proceso/add/", json)
                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
               });
          };

          //servicio para agregar Field de un subproceso
          self.field_add_subprocess = function(json) {
            return $http.post("/api/field-subprocess/add/", json)
                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
               });
          };

          //servicio para agregar un sub proceso de un proceso
          self.subproceso_add = function(json) {
            return $http.post("/api/sub-proceso/add/", json)
                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
               });
          };
            
          
          //servicio para agregar una factura
          self.itemfactura_add = function (json) {
             return $http.post("/api/field-voucher/add/", json)
                .success(function(res){
                  return res.id;
                  //$location.href
                })
                .error(function(res){
                  return '0'
               });
          };

          //servicio para listar factura por Proceso
           self.itemfactura_list = function (pk) {

              return $http.get("/api/field-voucher/return/"+pk+"/");
            };

           //servicio que cuenta cantidad de facturas por proceso
           self.factura_count = function (pk) {
               return $http.get("/api/field-voucher/count/"+pk+"/");
           };


           return self;
        }

}());
