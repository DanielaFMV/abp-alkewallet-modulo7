from django import template

register = template.Library()

@register.filter
def pesos(value):
    try:
        amount = int(round(float(value)))
        return f"${amount:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
