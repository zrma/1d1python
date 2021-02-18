from src.hacker_rank.python.strings import capitalize
from src.hacker_rank.python.strings import count_substring
from src.hacker_rank.python.strings import designer_door_mat
from src.hacker_rank.python.strings import merge_the_tools
from src.hacker_rank.python.strings import minion_game
from src.hacker_rank.python.strings import mutations
from src.hacker_rank.python.strings import print_formatted
from src.hacker_rank.python.strings import print_rangoli
from src.hacker_rank.python.strings import split_and_join
from src.hacker_rank.python.strings import swap_case
from src.hacker_rank.python.strings import text_alignment
from src.hacker_rank.python.strings import validate_string
from src.hacker_rank.python.strings import what_s_your_name
from src.hacker_rank.python.strings import wrap


class TestStrings:
    # noinspection SpellCheckingInspection
    # https://www.hackerrank.com/challenges/swap-case/problem
    def test_swap_case(self):
        assert swap_case("Www.HackerRank.com") == "wWW.hACKERrANK.COM"
        assert swap_case("Pythonist 2") == "pYTHONIST 2"
        assert swap_case('HackerRank.com presents "Pythonist 2".') \
               == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'

    # https://www.hackerrank.com/challenges/python-string-split-and-join/problem
    def test_split_and_join(self):
        assert split_and_join("this is a string") == "this-is-a-string"

    # https://www.hackerrank.com/challenges/whats-your-name/problem
    # noinspection SpellCheckingInspection
    def test_what_s_your_name(self, capsys):  # noqa
        what_s_your_name("Ross", "Taylor")
        captured = capsys.readouterr()
        assert captured.out == "Hello Ross Taylor! You just delved into python.\n"

    # https://www.hackerrank.com/challenges/python-mutations/problem
    def test_mutations(self):
        # noinspection SpellCheckingInspection
        assert mutations("abracadabra", 5, "k") == "abrackdabra"

    # https://www.hackerrank.com/challenges/find-a-string/problem
    def test_count_substring(self):
        # noinspection SpellCheckingInspection
        assert count_substring("ABCDCDC", "CDC") == 2

    # https://www.hackerrank.com/challenges/string-validators/problem
    # noinspection SpellCheckingInspection
    def test_validate_string(self, capsys):  # noqa
        validate_string("qA2")
        captured = capsys.readouterr()
        assert captured.out == "True\nTrue\nTrue\nTrue\nTrue\n"

    # https://www.hackerrank.com/challenges/text-alignment/problem
    # noinspection SpellCheckingInspection
    def test_text_alignment(self, capsys):  # noqa
        text_alignment(5, "H")
        captured = capsys.readouterr()

        expected = """
    H    .
   HHH   .
  HHHHH  .
 HHHHHHH .
HHHHHHHHH.
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHHHHHHHHHHHHHHHHHHHHHH   .
  HHHHHHHHHHHHHHHHHHHHHHHHH   .
  HHHHHHHHHHHHHHHHHHHHHHHHH   .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
  HHHHH               HHHHH             .
                    HHHHHHHHH .
                     HHHHHHH  .
                      HHHHH   .
                       HHH    .
                        H     .
"""

        assert captured.out == expected

    # https://www.hackerrank.com/challenges/text-wrap/problem
    # noinspection SpellCheckingInspection
    def test_wrap(self):
        expected = """ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"""
        assert wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4) == expected

    # https://www.hackerrank.com/challenges/designer-door-mat/problem
    # noinspection SpellCheckingInspection
    def test_designer_door_mat(self, capsys):  # noqa
        expected = """---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""
        designer_door_mat(7, 21)
        captured = capsys.readouterr()
        assert captured.out == expected

        expected = """---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
"""
        designer_door_mat(11, 33)
        captured = capsys.readouterr()
        assert captured.out == expected

        expected = """------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
        designer_door_mat(9, 27)
        captured = capsys.readouterr()
        assert captured.out == expected

    # https://www.hackerrank.com/challenges/python-string-formatting/problem
    # noinspection SpellCheckingInspection
    def test_print_formatted(self, capsys):  # noqa
        expected = """    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

        print_formatted(17)
        captured = capsys.readouterr()
        assert captured.out == expected

        expected = """     1      1      1      1
     2      2      2     10
     3      3      3     11
     4      4      4    100
     5      5      5    101
     6      6      6    110
     7      7      7    111
     8     10      8   1000
     9     11      9   1001
    10     12      A   1010
    11     13      B   1011
    12     14      C   1100
    13     15      D   1101
    14     16      E   1110
    15     17      F   1111
    16     20     10  10000
    17     21     11  10001
    18     22     12  10010
    19     23     13  10011
    20     24     14  10100
    21     25     15  10101
    22     26     16  10110
    23     27     17  10111
    24     30     18  11000
    25     31     19  11001
    26     32     1A  11010
    27     33     1B  11011
    28     34     1C  11100
    29     35     1D  11101
    30     36     1E  11110
    31     37     1F  11111
    32     40     20 100000
    33     41     21 100001
    34     42     22 100010
    35     43     23 100011
    36     44     24 100100
    37     45     25 100101
    38     46     26 100110
    39     47     27 100111
    40     50     28 101000
    41     51     29 101001
    42     52     2A 101010
    43     53     2B 101011
    44     54     2C 101100
    45     55     2D 101101
    46     56     2E 101110
    47     57     2F 101111
    48     60     30 110000
    49     61     31 110001
    50     62     32 110010
    51     63     33 110011
    52     64     34 110100
    53     65     35 110101
    54     66     36 110110
    55     67     37 110111
    56     70     38 111000
    57     71     39 111001
    58     72     3A 111010
    59     73     3B 111011
    60     74     3C 111100
    61     75     3D 111101
    62     76     3E 111110
    63     77     3F 111111
"""

        print_formatted(63)
        captured = capsys.readouterr()
        assert captured.out == expected

    # https://www.hackerrank.com/challenges/alphabet-rangoli/problem
    # noinspection SpellCheckingInspection
    def test_print_rangoli(self, capsys):  # noqa
        expected = """----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

        print_rangoli(3)
        captured = capsys.readouterr()
        assert captured.out == expected

        expected = """--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

        print_rangoli(5)
        captured = capsys.readouterr()
        assert captured.out == expected

        expected = """------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""

        print_rangoli(10)
        captured = capsys.readouterr()
        assert captured.out == expected

    # https://www.hackerrank.com/challenges/capitalize/problem
    def test_capitalize(self):
        assert capitalize("chris alan") == "Chris Alan"
        assert capitalize("hello world lol") == "Hello World Lol"
        assert capitalize("132 456 Wq m e") == "132 456 Wq M E"

    # https://www.hackerrank.com/challenges/the-minion-game/problem
    # noinspection SpellCheckingInspection
    def test_minion_game(self, capsys):  # noqa
        minion_game("BANANA")
        captured = capsys.readouterr()
        assert captured.out == "Stuart 12\n"

        minion_game("BAANANAS")
        captured = capsys.readouterr()
        assert captured.out == "Kevin 19\n"

        minion_game("BANANANAAAS")
        captured = capsys.readouterr()
        assert captured.out == "Draw\n"

    # https://www.hackerrank.com/challenges/merge-the-tools/problem
    # noinspection SpellCheckingInspection
    def test_merge_the_tools(self, capsys):  # noqa
        merge_the_tools("AABCAAADA", 3)
        captured = capsys.readouterr()
        assert captured.out == "AB\nCA\nAD\n"
