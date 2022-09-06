"""Aliases for manufacturers and model IDs."""

from __future__ import annotations

MANUFACTURER_SIGNIFY = "Signify Netherlands B.V."
MANUFACTURER_IKEA = "IKEA of Sweden"
MANUFACTURER_MULLER_LIGHT = "Müller Licht"
MANUFACTURER_YEELIGHT = "Yeelight"
MANUFACTURER_TUYA = "TuYa"
MANUFACTURER_AQARA = "Aqara"
MANUFACTURER_LEXMAN = "Lexman"
MANUFACTURER_MELITECH = "MeLiTec"
MANUFACTURER_WIZ = "WiZ"
MANUFACTURER_OSRAM = "OSRAM"
MANUFACTURER_LEDVANCE = "LEDVANCE"
MANUFACTURER_FEIBIT = "Feibit Inc co.  "

MANUFACTURER_ALIASES = {
    "Philips": MANUFACTURER_SIGNIFY,
    "IKEA": MANUFACTURER_IKEA,
    "Xiaomi": MANUFACTURER_AQARA,
    "LUMI": MANUFACTURER_AQARA,
    "ADEO": MANUFACTURER_LEXMAN,
    "MLI": MANUFACTURER_MULLER_LIGHT,
    "LightZone": MANUFACTURER_MELITECH,
}

MANUFACTURER_DIRECTORY_MAPPING = {
    MANUFACTURER_IKEA: "ikea",
    MANUFACTURER_FEIBIT: "jiawen",
    MANUFACTURER_LEDVANCE: "ledvance",
    MANUFACTURER_MULLER_LIGHT: "mueller-licht",
    MANUFACTURER_OSRAM: "osram",
    MANUFACTURER_SIGNIFY: "signify",
    MANUFACTURER_AQARA: "aqara",
    MANUFACTURER_LEXMAN: "lexman",
    MANUFACTURER_YEELIGHT: "yeelight",
    MANUFACTURER_TUYA: "tuya",
    MANUFACTURER_MELITECH: "melitec",
    MANUFACTURER_WIZ: "wiz",
}