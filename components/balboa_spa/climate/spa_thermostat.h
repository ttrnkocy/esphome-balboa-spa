#pragma once

#include "esphome/core/component.h"
#include "esphome/components/climate/climate.h"
#include "../balboaspa.h"

namespace esphome {
namespace balboa_spa {

class BalboaSpaThermostat : public climate::Climate, public Component {
 public:
  void setup() override;
  void loop() override;
  void set_parent(BalboaSpa *parent);

 protected:
  void control(const climate::ClimateCall &call) override;
  climate::ClimateTraits traits() override;

 private:
  BalboaSpa *spa;
};

}  // namespace balboa_spa
}  // namespace esphome
