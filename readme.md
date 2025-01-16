  SpaConfig get_current_config();
  SpaState get_current_state();

  //float get_setup_priority() const override;

  void on_set_temp(int temp);
  void on_set_hour(int hour);
  void on_set_minute(int minute);
  void on_toggle_light();
  void on_toggle_jet1() ;
  void on_toggle_jet2();

private:
  void read_serial();
  uint8_t crc8(CircularBuffer<uint8_t, 35> &data);
  void ID_request();
  void ID_ack();
  void rs485_send();
  void print_msg(CircularBuffer<uint8_t, 35> &data);
  void decodeSettings();
  void decodeState();
  void decodeFilterSettings();
  void decodeFault();




  : 
esphome::UARTDevice(parent)
{

}