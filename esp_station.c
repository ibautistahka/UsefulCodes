 wifi_station_get_config(&station_cfg);  //DECLARA LA ESTRUCTURA station_cfg PARA CONFIGURAR EL MODO STATION


  station_cfg.bssid_set=1;

//Nombre y contraseña del router que se conectara
  os_strcpy((char *)station_cfg.ssid,(const char *)valorwifi.con_ssid); //NOMBRE DEL ROUTER A CONECTAR
  os_strcpy((char *)station_cfg.password,(const char *)valorwifi.con_pass); //CLAVE DEL ROUTER A CONECTAR

  wifi_station_set_config(&station_cfg);  //CONFIGURADO EL MODO STATION

  //os_printf("\r\nCONF PASS: %s\r\n",station_cfg.password);
  //os_printf("\r\nCONF SSID: %s\r\n",station_cfg.ssid);
