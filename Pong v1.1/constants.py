BLACK   = '40m'
RED     = '41m'
GREEN   = '42m'
YELLOW  = '43m'
BLUE    = '44m'
MAGENTA = '45m'
CYAN    = '46m'
WHITE   = '47m'

BACKGROUND_COLOUR = BLACK
SCORE_COLOUR = MAGENTA
PLAYER1_COLOUR = BLUE
PLAYER2_COLOUR = RED
NET_COLOUR = CYAN
BALL_COLOUR = WHITE



WIDTH = 80
HEIGHT = 40

SCORE1 = (30, 2)
SCORE2 = (49, 2)



NUMBERS = [
    [# 0
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [# 1
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [# 2
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1]
    ],
    [# 3
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [# 4
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [# 5
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [# 6
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [# 7
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [# 8
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [# 9
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ]
]



CHARS = {
    'A':
    [
        [0, 0, 1, 0, 0],
	[0, 1, 0, 1, 0],
	[1, 1, 1, 1, 1],
	[1, 0, 0, 0, 1],
	[1, 0, 0, 0, 1]
    ],
    'E':
    [
        [1, 1, 1, 1, 1],
	[1, 1, 0, 0, 0],
	[1, 1, 1, 1, 1],
	[1, 1, 0, 0, 0],
	[1, 1, 1, 1, 1]
    ],
    'G':
    [
        [1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0],
	[1, 0, 1, 1, 1],
	[1, 0, 0, 1, 0],
	[1, 1, 1, 1, 0]
    ],
    'I':
    [
	[0, 1, 1, 1, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 1, 1, 1, 0]
    ],
    'L':
    [
        [1, 1, 0, 0, 0],
	[1, 1, 0, 0, 0],
	[1, 1, 0, 0, 0],
	[1, 1, 0, 0, 0],
	[1, 1, 1, 1, 1]
    ],
    'M':
    [
	[0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1], 
	[1, 0, 1 ,0, 1],
	[1, 0, 1, 0, 1]
    ],
    'N':
    [
	[1, 1, 0, 0, 1],
	[1, 1, 1, 0, 1],
	[1, 0, 1, 0, 1],
	[1, 0, 1, 1, 1],
	[1, 0, 0, 1, 1]
    ],
    'P':
    [
        [1, 1, 1, 1, 1],
	[1, 1, 0, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 0, 0, 0],
	[1, 1, 0, 0, 0]
    ],
    'R':
    [
        [1, 1, 1, 1, 1],
	[1, 1, 0, 0, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 0, 1, 0],
	[1, 1, 0, 1, 1]
    ],
    'S':
    [
	[1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1]
    ],
    'T':
    [
        [1, 1, 1, 1, 1],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0]
    ],
    'W':
    [
	[1, 0, 1, 0, 1], 
	[1, 0, 1 ,0, 1],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0]
    ],
    'Y':
    [
        [1, 0, 0, 0, 1],
	[1, 1, 0, 1, 1],
	[0, 1, 1, 1, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0]
    ],

    '!':
    [
        [0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0]
    ],

    '0':NUMBERS[0],
    '1':NUMBERS[1],
    '2':NUMBERS[2],
    '3':NUMBERS[3],
    '4':NUMBERS[4],
    '5':NUMBERS[5],
    '6':NUMBERS[6],
    '7':NUMBERS[7],
    '8':NUMBERS[8],
    '9':NUMBERS[9],
    0:NUMBERS[0],
    1:NUMBERS[1],
    2:NUMBERS[2],
    3:NUMBERS[3],
    4:NUMBERS[4],
    5:NUMBERS[5],
    6:NUMBERS[6],
    7:NUMBERS[7],
    8:NUMBERS[8],
    9:NUMBERS[9],
    ' ':
    [
        [0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
    ]
}


