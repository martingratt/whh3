#ifndef _LIBINETSEC_H_
#define _LIBINETSEC_H_
#include <stdbool.h>

typedef unsigned char byte;

void init_canary(byte *canary, char *user, char *pass);
bool check_canary(byte *canary1, byte *canary2);
int auth_user(char *user, char *pass);
bool check_usr(char *user, char *pass);

#endif
