//import { Chess } from './chess.js'

//Chess = require('chess')
// imported from only legal moves file 

var board = null
var game = new Chess()
var $status = $('#status')
var $fen = $('#fen')
var $pgn = $('#pgn')


function onDrop(source, target, piece, orientation) {
    
  console.log("Entering the Move in ... hitting the query now")  
  console.log("From Source :", source , "to Taget :" , target)  
  var pn = piece.includes('b')
    ? piece.toUpperCase().substring(1, 2)
    : piece.substring(1, 2);
  pn = piece.includes('P') ? '' : pn;
  var move = piece.includes('P')
    ? source + target
    : pn + source.substring(0, 1) + target;
  move =
    piece.includes('P') && target.includes('8')
      ? target.substring(0, 1) + '8Q'
      : move; // pawn promotion

      // illegal move
      //document.querySelector('tbody#pgn-moves');
      //document.querySelector('#pgn').innerText = data.pgn;
      if (move === null) return 'snapback'
    
      updateStatus()
  var move_repr = source + target
      $.get('/move', {move: move_repr}, function(data) {
        console.log(data);
      
      moves = data.moves;
    });
    
    game.move({ from: source, to: target })

  }
  
  // to fix player with white/black peices from messing arround with other player's pieces.
  // can be bypassed tho., that's why its also validated in back-end too.
  
  // Temporarily hiding this to replace with the only leagl moves part 
  
  // function onDragStart(source, piece, position, orientation) {
  //   if (
  //     (orientation === 'white' && piece.search(/^w/) === -1) ||
  //     (orientation === 'black' && piece.search(/^b/) === -1)
  //   ) {
  //     return false;
  //   }
  // }  
  
  function onDragStart (source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    if (game.game_over()) return false
  
    // only pick up pieces for the side to move
    if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
        (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
        console.log("It's not your turn Mate")  
        return false
    }
  }
  
  
  $('#reset').click(function() {
    $.get('/reset', function(data) {
      board.position(data.fen);
      document.querySelector('#pgn').innerText = data.pgn;
    });
  });
  
  $('#undo').click(function() {
    if (!$(this).hasClass('text-muted')) {
      $.get('/undo', function(data) {
        board.position(data.fen);
        document.querySelector('#pgn').innerText = data.pgn;
      });
    } else {
      //
    }
  });
  
  $('#redo').click(function() {
    if (!$(this).hasClass('text-muted')) {
      $.get('/redo', function(data) {
        board.position(data.fen);
        document.querySelector('#pgn').innerText = data.pgn;
      });
    } else {
      //
    }
  });

  
  
  // imported from only legal moves file
  function updateStatus () {
    var status = ''
    console.log("Update Status Triggered")
    console.log("It's ",game.turn(), "to move now ")
    
    var moveColor = 'White'
    if (game.turn() === 'b') {
      moveColor = 'Black'
    }
  
    // checkmate?
    if (game.in_checkmate()) {
      status = 'Game over, ' + moveColor + ' is in checkmate.'
    }
  
    // draw?
    else if (game.in_draw()) {
      status = 'Game over, drawn position'
    }
  
    // game still on
    else {
      status = moveColor + ' to move'
  
      // check?
      if (game.in_check()) {
        status += ', ' + moveColor + ' is in check'
      }
    }
  
    console.log("Current Status of the game",status)
    $status.html(status)
    $fen.html(game.fen())
    $pgn.html(game.pgn())
  }
  
  function onSnapEnd () {
    console.log("OnSnapEnd Triggered")  
    board.position(game.fen())
  }
  