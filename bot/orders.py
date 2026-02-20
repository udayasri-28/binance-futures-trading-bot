import logging


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(
            f"Placing order: Symbol={symbol}, Side={side}, Type={order_type}, Quantity={quantity}, Price={price}"
        )

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

        logging.info(f"Order response: {response}")

        return response

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise