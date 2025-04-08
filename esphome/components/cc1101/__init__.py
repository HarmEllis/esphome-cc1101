from esphome import pins
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import (
    CONF_CLK_PIN,
    CONF_CS_PIN,
    CONF_ID,
    CONF_MISO_PIN,
    CONF_MOSI_PIN,
    PLATFORM_ESP32,
    PLATFORM_ESP8266,
    PLATFORM_RP2040,
)

CODEOWNERS = ["@HarmEllis"]

cc1101_ns = cg.esphome_ns.namespace("cc1101")
CC1101 = cc1101_ns.class_("CC1101", cg.Component)

CONF_CC1101_FREQUENCY = "cc1101_frequency"
CONF_EMITTER_PIN = "cc1101_emitter_pin"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(CC1101),
            cv.Required(CONF_CLK_PIN): pins.internal_gpio_output_pin_schema,
            cv.Required(CONF_MISO_PIN): pins.internal_gpio_input_pin_schema,
            cv.Required(CONF_MOSI_PIN): pins.internal_gpio_output_pin_schema,
            cv.Required(CONF_CS_PIN): pins.internal_gpio_output_pin_schema,
            cv.Required(CONF_EMITTER_PIN): pins.internal_gpio_output_pin_schema,
            cv.Required(CONF_CC1101_FREQUENCY): cv.float_range(min=300, max=928),
        }
    ).extend(cv.COMPONENT_SCHEMA),
    cv.only_on([PLATFORM_ESP32, PLATFORM_ESP8266, PLATFORM_RP2040]),
    cv.only_with_arduino,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add_library("SPI", None)
    cg.add_library("EEPROM", None)
    cg.add_library("SmartRC-CC1101-Driver-Lib", None)
    await cg.register_component(var, config)

    clk_pin = await cg.gpio_pin_expression(config[CONF_CLK_PIN])
    cg.add(var.set_clk_pin(clk_pin))

    miso_pin = await cg.gpio_pin_expression(config[CONF_MISO_PIN])
    cg.add(var.set_miso_pin(miso_pin))

    mosi_pin = await cg.gpio_pin_expression(config[CONF_MOSI_PIN])
    cg.add(var.set_mosi_pin(mosi_pin))

    cs_pin = await cg.gpio_pin_expression(config[CONF_CS_PIN])
    cg.add(var.set_cs_pin(cs_pin))

    emitter_pin = await cg.gpio_pin_expression(config[CONF_EMITTER_PIN])
    cg.add(var.set_emitter_pin(emitter_pin))

    cg.add(var.set_cc1101_frequency(config[CONF_CC1101_FREQUENCY]))
