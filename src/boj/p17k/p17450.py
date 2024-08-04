from typing import Final, TextIO


def solve17450(reader: TextIO, writer: TextIO) -> None:
    s_price, s_weight = map(int, reader.readline().split())
    n_price, n_weight = map(int, reader.readline().split())
    u_price, u_weight = map(int, reader.readline().split())

    coupon_discount: Final[int] = 500
    min_purchase_for_discount: Final[int] = 5000
    batch_size: Final[int] = 10

    def calculate_total_price(price: int) -> int:
        total = price * batch_size
        return total if total < min_purchase_for_discount else total - coupon_discount

    def cost_effectiveness(weight: int, total_price: int) -> float:
        return float(weight * batch_size) / float(total_price)

    s_total_price = calculate_total_price(s_price)
    n_total_price = calculate_total_price(n_price)
    u_total_price = calculate_total_price(u_price)

    s_cost_effectiveness = cost_effectiveness(s_weight, s_total_price)
    n_cost_effectiveness = cost_effectiveness(n_weight, n_total_price)
    u_cost_effectiveness = cost_effectiveness(u_weight, u_total_price)

    to_buy = max(
        ("S", s_cost_effectiveness), ("N", n_cost_effectiveness), ("U", u_cost_effectiveness), key=lambda item: item[1]
    )[0]

    writer.write(f"{to_buy}")
