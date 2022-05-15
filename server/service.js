var Service = require('node-windows').Service;
var svc = new Service({
 name:'remoteQCAPI',
 description: 'Node.js service exposing API for reading remoteQC results',
 script: 'E:\\progetti\\DIY_remoteQC\\server\\api.js'
});

svc.on('install',function(){
 svc.start();
});

svc.install();