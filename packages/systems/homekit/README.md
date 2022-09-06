# HomeKit

Exposes Home Assistant Entities to HomeKit.

Some things link themselves directly.
eg. Hue
So this only exposes non-HomeKit entities.

They are split into multiple bridges for performance reasons.
Each Camera is on a bridge of their own.

SkyQ integration now exposes it's buttons directly, so the automation in this folder is not required.
