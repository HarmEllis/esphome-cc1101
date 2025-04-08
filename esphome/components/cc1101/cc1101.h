#pragma once

#include "esphome/core/component.h"
#include "esphome/core/gpio.h"

// Libraries for CC1101 module
#include <ELECHOUSE_CC1101_SRC_DRV.h>

// #define EMITTER_GPIO 2

// // Set custom spi pins (byte sck, byte miso, byte mosi, byte ss)
// #define SCK_PIN 14
// #define MISO_PIN 39
// #define MOSI_PIN 12
// #define SS_PIN 15

// #define CC1101_FREQUENCY 433.42

namespace esphome {
namespace cc1101 {

class CC1101 : public Component {
 public:
  void setup() override;
  // void loop() override;
  void dump_config() override;

  // Set time based cover values
  void set_clk_pin(InternalGPIOPin *clk) { this->clk_pin_ = clk; }
  void set_mosi_pin(InternalGPIOPin *mosi) { this->mosi_pin_ = mosi; }
  void set_miso_pin(InternalGPIOPin *miso) { this->miso_pin_ = miso; }
  void set_cs_pin(InternalGPIOPin *cs) { this->cs_pin_ = cs; }
  void set_emitter_pin(InternalGPIOPin *emitter) { this->emitter_pin_ = emitter; }
  void set_cc1101_frequency(double frequency) { this->cc1101_frequency_ = frequency; }

  uint8_t get_emitter_pin();

  template<typename Func> void sent_command(Func &&action) {
    if (ELECHOUSE_cc1101.getCC1101()) {  // Check the CC1101 Spi connection.
      ESP_LOGI("cc1101", "Connection OK");
    } else {
      ESP_LOGE("cc1101", "Connection Error");
    }
    ELECHOUSE_cc1101.SetTx();
    action();
    ELECHOUSE_cc1101.setSidle();
  }

 protected:
  InternalGPIOPin *clk_pin_{nullptr};
  InternalGPIOPin *mosi_pin_{nullptr};
  InternalGPIOPin *miso_pin_{nullptr};
  InternalGPIOPin *cs_pin_{nullptr};
  InternalGPIOPin *emitter_pin_{nullptr};
  double cc1101_frequency_{433.42};
};

}  // namespace cc1101
}  // namespace esphome
