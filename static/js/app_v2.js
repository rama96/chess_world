function onDrop(source, target, piece, orientation) {
    
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
    
      $.get('/move', {move: move}, function(data) {
        console.log(data);
      
      moves = data.moves;
    });
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

// Copied from only legal moves chessboard.js

var $status = $('#status')
var $fen = $('#fen')
var $pgn = $('#pgn')

function onDragStart (source, piece, position, orientation) {
  // do not pick up pieces if the game is over

  // only pick up pieces for the side to move
  if ((orientation === 'w' && piece.search(/^b/) !== -1) ||
      (orientation === 'b' && piece.search(/^w/) !== -1)) {
    return false
  }
}


// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd (source, piece, position, orientation) {
  console.log('Piece: ' + piece)
  //console.log('Square: ' + square)
  console.log('Position: ' + position)
  console.log('Orientation: ' + orientation)
  console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
}

function updateStatus (orientation) {
  var status = ''

  var moveColor = 'White'
  if (orientation === 'b') {
    moveColor = 'Black'
  }

  // checkmate?
  // if (game.in_checkmate()) {
  //   status = 'Game over, ' + moveColor + ' is in checkmate.'
  // }

  // draw?
  // else if (game.in_draw()) {
  //   status = 'Game over, drawn position'
  // }

  // game still on
  // else {
  //   status = moveColor + ' to move'

  //   // check?
  //   if (game.in_check()) {
  //     status += ', ' + moveColor + ' is in check'
  //   }
  //}

  // $status.html(status)
  // $fen.html(game.fen())
  // $pgn.html(game.pgn())
}

