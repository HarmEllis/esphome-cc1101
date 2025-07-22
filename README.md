# ESPHome CC1101 rf transceiver component
This is an external component for [ESPHOME](https://esphome.io/), to use a cc1101 rf transceiver module.   
Check the [somfy rts controller repo](https://github.com/HarmEllis/esphome-somfy-cover-remote) for an example how to use this component.

## Required hardware
- ESP32
- CC1101 RF module

## Setup
Use the following ESPHome yaml as a base for this component.

```
esphome:
  name: CC1101 remote

external_components:
  - source: github://HarmEllis/esphome-cc1101@main
    components: [ cc1101 ]

esp32:
  board: esp32dev
  framework:
    type: arduino

# Enable logging
logger:

# Enable Home Assistant API
api:

ota:
  platform: esphome
  password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Remote Fallback Hotspot"
    password: !secret fallback_hotspot

# For the WT32-ETH01 ESP module, you can use these pins
cc1101:
  id: "cc1101_module"
  cc1101_frequency: 433.42
  mosi_pin: 12
  miso_pin: 39
  clk_pin: 14
  cs_pin: 15
  cc1101_emitter_pin: 2

```

## Changes to SmartRC-CC1101-Driver-Lib
The changes are all related to a change in ESP32 Arduino Framework 3.x, to which ESPHome switched from 2.x in version 2025.7.
In this version you are not allowed to use `digitalRead()` or `digitalWrite()` on pins that are claimed for SPI and pins that you did not set the mode for explicitly with the `pinMode()` finction.

## Acknowledgements
This project is based on the [SmartRC-CC1101-Driver-Lib](https://github.com/LSatan/SmartRC-CC1101-Driver-Lib) by LSatan, which itself includes code from the ELECHOUSE CC1101 library by Michael (2010). Permission to modify and distribute was granted by Wilson Shen (ELECHOUSE).

All modifications in this repository are made by Harm Ellis, and are provided under the MIT License. See the LICENSE file for details.
