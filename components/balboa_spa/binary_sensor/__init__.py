import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor

from esphome.const import (
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_FAN,
    ICON_LIGHTBULB,
)

from .. import (
    CONF_SPA_ID,
    BalboaSpa
)

CONF_JET1 = "jet1"
CONF_JET2 = "jet2"
CONF_LIGHTS = "lights"

SENSOR_TYPES = {
    CONF_JET1: binary_sensor.binary_sensor_schema(
        icon=ICON_FAN,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    CONF_JET2: binary_sensor.binary_sensor_schema(
        icon=ICON_FAN,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
    CONF_LIGHTS: binary_sensor.binary_sensor_schema(
        icon=ICON_LIGHTBULB,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    ),
}

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_SPA_ID): cv.use_id(BalboaSpa),
    }
).extend({cv.Optional(type): schema for type, schema in SENSOR_TYPES.items()})


async def to_code(config):
    paren = await cg.get_variable(config[CONF_SPA_ID])

    if conf := config.get(CONF_JET1):
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(paren.set_jet1_binary_sensor(sens))
    
    if conf := config.get(CONF_JET2):
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(paren.set_jet2_binary_sensor(sens))

    if conf := config.get(CONF_LIGHTS):
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(paren.set_lights_binary_sensor(sens))