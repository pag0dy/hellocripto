$(document).ready(function(){

    var socket = io();
  
    // Run event 'start' on server
    socket.emit('start');
  
    // Run this function when event 'update' is recieved from server
    socket.on('update', function(crypto){
      $('#name').text(crypto['name']);
      $('#rank').text(crypto['rank']);
      $('#price').text(crypto['quotes']['USD']['price']);
      $('#updated').text(crypto['last_updated']);
    });
  
  });