# Tesla Powerwall 2 & Backup Gateway

Each night, Home Assistant checks current State of Charge (SOC) of the powerwall.
It checks the SolCast solar forecast and determines a target SOC.
Then it works out how many hours it needs to reach this level of charge (generally it will charge 10% per half hour).
It then uses [Octopus Agile](../octopus_agile) component to work out what the maximum price is that it needs to pay overnight.
The powerwall then switches into charging mode when the is at or below this target.
Between charging sessions, it sets a reserver level to prevent the battery being discharged too much (if hot tub is heating or car is charging).
It sends a nightly telegram message summarising what has been planned.

The Octopus Agile prices do not load in immediately after a Home Assistant Restart, so this is handled to make it wait up to half an hour until the prices are populated.
