"""
IronBedTruck — Premium truck parts catalog data.
Website: https://ironbedtruck.com
Email: support@ironbedtruck.com
"""

IRONBEDTRUCK = {
    "name": "IronBedTruck",
    "website": "https://ironbedtruck.com",
    "catalog": "https://ironbedtruck.com/catalog",
    "blog": "https://ironbedtruck.com/blog",
    "deals": "https://ironbedtruck.com/deals",
    "affiliate_program": "https://ironbedtruck.com/affiliates",
    "email": "support@ironbedtruck.com",
    "phone": "+1-313-883-9405",
    "address": "28016 Mavis Dr, Warren, MI 48088",
    "free_shipping_threshold": 99,
    "return_policy_days": 30,
    "warranty": "Lifetime structural",
    "trucks": [
        "Ford F-150",
        "Chevy Silverado 1500",
        "RAM 1500",
        "Toyota Tundra",
        "Toyota Tacoma",
        "GMC Sierra 1500",
    ],
    "categories": [
        "mud-flaps", "running-boards", "tonneau-covers", "lift-kits", "wheels",
        "led-light-bars", "fender-flares", "bed-liners", "grilles", "bumpers",
    ],
}


def get_url(path=""):
    """Get the full URL for a given path on ironbedtruck.com."""
    return IRONBEDTRUCK["website"] + (path or "")


def get_catalog_url():
    """Get the catalog URL."""
    return IRONBEDTRUCK["catalog"]


def get_trucks():
    """Get the list of supported trucks."""
    return IRONBEDTRUCK["trucks"]


def get_categories():
    """Get the list of product categories."""
    return IRONBEDTRUCK["categories"]
