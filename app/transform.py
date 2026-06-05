from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP

from app.schemas import SalesTransaction


TAX_RATE = Decimal("0.07")


def round_money(value: Decimal) -> float:
    """
    Round monetary values to 2 decimal places.
    """
    return float(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def transform_transaction(transaction: SalesTransaction) -> dict:
    """
    Transform a validated sales transaction into a cleaned analytical record.
    """

    unit_price = Decimal(str(transaction.unit_price))
    quantity = Decimal(transaction.quantity)

    subtotal = quantity * unit_price
    tax_amount = subtotal * TAX_RATE
    total_amount = subtotal + tax_amount

    transformed_record = {
        "transaction_id": transaction.transaction_id,
        "customer_id": transaction.customer_id,
        "product_id": transaction.product_id,
        "quantity": transaction.quantity,
        "unit_price": round_money(unit_price),
        "currency": transaction.currency,
        "transaction_timestamp": transaction.transaction_timestamp.isoformat(),
        "subtotal": round_money(subtotal),
        "tax_amount": round_money(tax_amount),
        "total_amount": round_money(total_amount),
        "processed_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    return transformed_record
