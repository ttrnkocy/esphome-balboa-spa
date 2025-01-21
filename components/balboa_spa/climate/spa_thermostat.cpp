#include "esphome.h"
#include "esphome/core/log.h"
#include "spa_thermostat.h"

namespace esphome {
namespace balboa_spa {

climate::ClimateTraits BalboaSpaThermostat::traits()
{
    auto traits = climate::ClimateTraits();
    traits.add_supported_mode(climate::CLIMATE_MODE_HEAT);

    return traits;
}

void BalboaSpaThermostat::set_parent(BalboaSpa *parent) { spa = parent; }

}
}