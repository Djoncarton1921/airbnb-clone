from typing import List, Tuple, NamedTuple, Union


class ImageOrder(NamedTuple):
    image_id: Union[int, str]
    order: int


def convert_response_to_orders(response: List[Tuple[str, int]]) -> List[ImageOrder]:
    """Convert response to list of ImageOrders"""
    return [ImageOrder(image_id=item[0], order=item[1]) for item in response if item[0].isdigit()]
