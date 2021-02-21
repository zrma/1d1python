# -*- coding: utf-8 -*-

from typing import List


def process_normal(arr: List[int], tokens: str, repeat: bool, repeat_num: int) -> None:
    last_token: str = str()

    # 작은 수 일괄 카운트
    for token in tokens:
        last_token = token
        arr[int(token) - 1] += 1

    if repeat:
        assert last_token, "Repeat is True, but Last Token is None"
        arr[int(last_token) - 1] += repeat_num


def process_big_number(
    results: List[int], token_by_paren: str, repeat: bool, repeat_num: int
) -> None:
    tokens_by_sharp: List[str] = token_by_paren.split("#")

    # 마지막 토큰이 큰 수(#)인가?
    is_big_last_token = tokens_by_sharp[-1] == ""
    if is_big_last_token:
        tokens_by_sharp.remove("")

    *tokens_by_sharp, last_token = tokens_by_sharp

    # split 했으므로, 마지막 토큰 이외의 나머지는 무조건 큰 수 or 큰 수 + alpha
    for sub_tokens in tokens_by_sharp:

        # 마지막 큰 수만 뽑아내자
        other, last_big_token = sub_tokens[:-2], sub_tokens[-2:]

        for token in other:
            results[int(token) - 1] += 1

        results[int(last_big_token) - 1] += 1

    # 마지막 토큰이 큰 수라면...
    if is_big_last_token:
        # 마지막 큰 수만 뽑아내자
        other, last_big_token = last_token[:-2], last_token[-2:]
        process_normal(results, other, False, 0)

        results[int(last_big_token) - 1] += 1
        if repeat:
            assert last_big_token, "Repeat is True, but Last Token is None"
            results[int(last_big_token) - 1] += repeat_num

    # 아니라면 일반적인 처리
    else:
        process_normal(results, last_token, repeat, repeat_num)


def parse_token(results: List[int], token_by_paren: str) -> None:
    # 반복 처리 해야 할 경우 맨 마지막 토큰을 해당 횟수만큼 반복하자
    repeat = "(" in token_by_paren
    repeat_num = 0

    if repeat:
        token_by_paren, repeat_num_str = token_by_paren.split("(")
        repeat_num = int(repeat_num_str) - 1

    # 큰 수(#)가 포함 된 경우
    exist_big = "#" in token_by_paren

    if exist_big:
        process_big_number(results, token_by_paren, repeat, repeat_num)

    # 큰 수(#)가 포함 안 된 경우
    else:
        process_normal(results, token_by_paren, repeat, repeat_num)


def frequency(s: str) -> List[int]:
    results: List[int] = [0 for _ in range(26)]

    tokens_by_paren = s.split(")")
    if "" in tokens_by_paren:
        tokens_by_paren.remove("")

    for token_by_paren in tokens_by_paren:
        parse_token(results, token_by_paren)

    return results
