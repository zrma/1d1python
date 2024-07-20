import attrs
from pytest import CaptureFixture

from src.hacker_rank.python.strings import (
    capitalize,
    count_substring,
    designer_door_mat,
    merge_the_tools,
    minion_game,
    mutations,
    print_formatted,
    print_pattern,
    split_and_join,
    swap_case,
    text_alignment,
    validate_string,
    what_s_your_name,
    wrap,
)


def test_swap_case() -> None:
    """
    https://www.hackerrank.com/challenges/swap-case/problem
    sWAP cASE
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        s: str
        want: str

    # noinspection SpellCheckingInspection
    test_cases = (
        TestCase(s="Www.HackerRank.com", want="wWW.hACKERrANK.COM"),
        TestCase(s="Pythonist 2", want="pYTHONIST 2"),
        TestCase(s='HackerRank.com presents "Pythonist 2".', want='hACKERrANK.COM PRESENTS "pYTHONIST 2".'),
    )

    for tt in test_cases:
        got = swap_case(tt.s)
        assert got == tt.want


def test_split_and_join() -> None:
    """
    https://www.hackerrank.com/challenges/python-string-split-and-join/problem
    String Split and Join
    """
    want = "this-is-a-string"
    give = "this is a string"
    got = split_and_join(give)
    assert got == want


def test_what_s_your_name(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/whats-your-name/problem
    What's Your Name?
    """
    what_s_your_name("Ross", "Taylor")

    want = """Hello Ross Taylor! You just delved into python.
"""
    got = capsys.readouterr().out
    assert got == want


def test_mutations() -> None:
    """
    https://www.hackerrank.com/challenges/python-mutations/problem
    Mutations
    """
    # noinspection SpellCheckingInspection
    want = "abrackdabra"
    got = mutations("abracadabra", 5, "k")
    assert got == want


def test_count_substring() -> None:
    """
    https://www.hackerrank.com/challenges/find-a-string/problem
    Find a string
    """
    want = 2
    # noinspection SpellCheckingInspection
    got = count_substring("ABCDCDC", "CDC")
    assert got == want


def test_validate_string(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/string-validators/problem
    String Validators
    """
    validate_string("qA2")

    want = """True
True
True
True
True
"""
    got = capsys.readouterr().out
    assert got == want


def test_text_alignment(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/text-alignment/problem
    Text Alignment
    """
    text_alignment(5, "H")

    # noinspection SpellCheckingInspection
    want = """
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
    got = capsys.readouterr().out
    assert got == want


def test_wrap() -> None:
    """
    https://www.hackerrank.com/challenges/text-wrap/problem
    Text Wrap
    """
    # noinspection SpellCheckingInspection
    give = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    # noinspection SpellCheckingInspection
    want = """ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"""
    assert wrap(give, 4) == want


def test_designer_door_mat(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/designer-door-mat/problem
    Designer Door Mat
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        n: int
        m: int
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                n=7,
                m=21,
                want="""---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
""",
            ),
            TestCase(
                n=11,
                m=33,
                want="""---------------.|.---------------
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
""",
            ),
            TestCase(
                n=9,
                m=27,
                want="""------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
""",
            ),
        )
    ):
        designer_door_mat(tt.n, tt.m)

        got = capsys.readouterr().out
        assert got == tt.want, f"{i}/{tt.n}/{tt.m}"


def test_print_formatted(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/python-string-formatting/problem
    String Formatting
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        n: int
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                n=17,
                want="""    1     1     1     1
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
""",
            ),
            TestCase(
                n=63,
                want="""     1      1      1      1
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
""",
            ),
        ),
    ):
        print_formatted(tt.n)

        got = capsys.readouterr().out
        assert got == tt.want, f"{i}/{tt.n}"


def test_print_pattern(capsys: CaptureFixture[str]) -> None:
    # noinspection SpellCheckingInspection
    """
    https://www.hackerrank.com/challenges/alphabet-rangoli/problem
    Alphabet Rangoli
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        n: int
        want: str

    for i, tt in enumerate(
        (
            TestCase(
                n=3,
                want="""----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
""",
            ),
            TestCase(
                n=5,
                want="""--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
""",
            ),
            TestCase(
                n=10,
                want="""------------------j------------------
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
""",
            ),
        ),
    ):
        print_pattern(tt.n)

        got = capsys.readouterr().out
        assert got == tt.want, f"{i}/{tt.n}"


def test_capitalize() -> None:
    """
    https://www.hackerrank.com/challenges/capitalize/problem
    Capitalize!
    """
    assert capitalize("chris alan") == "Chris Alan"
    assert capitalize("hello world lol") == "Hello World Lol"
    assert capitalize("132 456 Wq m e") == "132 456 Wq M E"


def test_minion_game(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/the-minion-game/problem
    The Minion Game
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        s: str
        want: str

    # noinspection SpellCheckingInspection
    test_cases = (
        TestCase(s="BANANA", want="Stuart 12\n"),
        TestCase(s="BAANANAS", want="Kevin 19\n"),
        TestCase(s="BANANANAAAS", want="Draw\n"),
    )
    for i, tt in enumerate(test_cases):
        minion_game(tt.s)

        got = capsys.readouterr().out
        assert got == tt.want, f"{i}/{tt.s}"


def test_merge_the_tools(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/merge-the-tools/problem
    Merge the Tools!
    """
    # noinspection SpellCheckingInspection
    merge_the_tools("AABCAAADA", 3)

    want = """AB
CA
AD
"""
    got = capsys.readouterr().out
    assert got == want
