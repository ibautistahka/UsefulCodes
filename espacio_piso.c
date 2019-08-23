if(cmd9==0){
  char word1[32];
  os_strncpy(cadena,pdata,30);
  cadena[30]='\0';
  char *token=strtok((char *)cadena," =");

  //os_printf("%s\r\n",token);

  token=strtok(NULL," =");
  token=strtok(NULL," =");

  strcpy(word1,token);
  word1[32]='\0';
  for(int i = 0; i < strlen(word1); i++){
    if(word1[i] == '_')
        word1[i] = ' ';
}
//  os_printf("%s\r\n",word1);

  if (os_strcmp(word1,"null")==0){
    strcpy(sta_ssid,"");
    sta_ssid[32]='\0';
  } else {
    strcpy(sta_ssid,word1);
    sta_ssid[32]='\0';
  }

  os_strcpy((char *)valorwifi.con_ssid,(char *)sta_ssid); //CLAVE DEL ROUTER A CONECTAR
  espconn_sent((struct espconn *)arg,(uint8 *)respuesta1,strlen(respuesta1));
}


if(cmd10==0){
  char word1[64];
  os_strncpy(cadena,pdata,30);
  cadena[30]='\0';
  char *token=strtok((char *)cadena," =");

  token=strtok(NULL," =");
  token=strtok(NULL," =");
  strcpy(word1,token);
  word1[20]='\0';
  for(int i = 0; i < strlen(word1); i++){
    if(word1[i] == '_')
        word1[i] = ' ';
}
  //os_printf("%s\r\n",word1);

  if (os_strcmp(word1,"null")==0){
    strcpy(sta_pass,"");
    sta_pass[64]='\0';
  } else {
    strcpy(sta_pass,word1);
    sta_pass[64]='\0';
  }

  os_strcpy((char *)valorwifi.con_pass,(char *)sta_pass); //CLAVE DEL ROUTER A CONECTAR

  //espconn_delete(pespconn);
  espconn_sent((struct espconn *)arg,(uint8 *)respuesta1,strlen(respuesta1));
  borrar=true;
  espconn_disconnect(pespconn);
}
