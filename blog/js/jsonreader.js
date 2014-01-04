var customInterpolationApp = angular.module('customInterpolationApp', []);
 
customInterpolationApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{/');
  $interpolateProvider.endSymbol('/}');
});
customInterpolationApp.controller('JsonViewer',function JsonViewer($scope,$http,$templateCache){
    $scope.method = 'GET';
    $scope.url = 'http://localhost:8080/json/list.json';
    //$scope.url = "http://localhost:8080/json/view.json/5118776383111168";
    $scope.articles = new Object();
    $scope.fetch = function() {
	$scope.code = null;
	$scope.response = null;
	
	//$scope.articles['5118776383111168'] = new Object();
	$http({method: $scope.method, url: $scope.url, cache: $templateCache}).
	    success(function(data, status) {
		$scope.status = status;
		var temp = eval(data);
		for(key in temp){
		    var t = "\'"+key.toString()+"\'";
		    var t1 = new Object();
		    t1[t] = temp[key];
		    $scope.articles = extend($scope.articles,t1);

		}
		console.log($scope.articles[t]);		
	    }).
	    error(function(data, status) {
		$scope.articles = data || "Request failed";
		$scope.status = status;
	    });
    };

    $scope.updateModel = function(method, url) {
	$scope.method = method;
	$scope.url = url;
    };
    $scope.readJson = function(ID){
	$scope.url = "http://localhost:8080/json/view.json/"+ID;
	var t = "\'"+ID+"\'";
	// 文字列が少ない(Loadされていない)ならばjsonを読み込む。
	if($scope.articles[t].text.length < 5){
	    $scope.fetch();
	}
    };
    $scope.goView = function(ID){
	var url = "/view/"+ID;
	document.location = url;
    };
    $scope.readMore = function(q){
	$scope.url = "http://localhost:8080/json/list.json?q="+q;
	console.log($scope.url);
	$scope.fetch();
    }
    $scope.fetch();
});

