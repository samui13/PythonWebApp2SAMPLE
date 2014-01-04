var customInterpolationApp = angular.module('customInterpolationApp', []);
 
customInterpolationApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{/');
  $interpolateProvider.endSymbol('/}');
});
//http://d.hatena.ne.jp/memory_agape/20120203/1328245142
var extend=function(){for(var d={},b=0,a=0,c=arguments.length;b<c;b++){for(a in arguments[b]){d[a]=arguments[b][a]}}return d};
