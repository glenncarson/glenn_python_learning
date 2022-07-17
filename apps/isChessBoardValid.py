# really good use of dictionaries with counts using dict.setdefault
# only creates new entry if not already exisitng
# then on next line you can add +1 count to observed value

chess_dict = {'a1':'BkIng','h8':'wqing','a6':'bbishop',
'a2':'wpawn','a3':'wpawn','a4':'wpawn','a5':'wpawn','a7':'wpawn','b1':'wpawn',
'b2':'wpawn','b3':'wpawn',
}

def isValidChessBoard(chess_dict):
    piece_types = ['pawn','knight','rook','queen','bishop','king']
    count_dict = {}
    count_dict['bpawn'] = 0
    count_dict['wpawn'] = 0
    valid = True
    for key in chess_dict.keys():
        if not key[0].lower() in 'abcdefgh':
            valid = False
        if not str(key[1]) in '12345678':
            valid = False

    for key in chess_dict:
        chess_dict[key] = chess_dict[key].lower()

    if not 'bking' in chess_dict.values() and 'wking' in chess_dict.values():
        valid = False
    for value in chess_dict.values():
        if not value[1:].lower() in piece_types:
            valid = False
        count_dict.setdefault(value[0],0)
        count_dict[value[0]] = count_dict[value[0]] + 1
        if 'pawn' in value:
            count_dict[value] = count_dict[value] + 1
    if count_dict['b'] > 16 or count_dict['w'] > 16:
        valid = False
    if count_dict['bpawn'] > 8 or count_dict['wpawn'] > 8:
        valid = False
    return valid  

print(isValidChessBoard(chess_dict))

# only 1-16 piece {done}
# one black king, one white king {done}
# max 8 white pawns, 8 black pawns {done]}
# piece starts with w or b,followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king' {done}
