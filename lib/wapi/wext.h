/*
 * wext.h — External declarations for wapi library
 * Reconstructed from WING Remote Protocols V3.1.0-3 documentation
 */

#ifndef WEXT_H_
#define WEXT_H_

#include "wapi.h"
#include "wdef.h"

// Open and Close
int          wOpen(char* wip);
void         wClose();
unsigned int wVer();

// Setting Values
int wSetTokenFloat(wtoken token, float fval);
int wSetTokenInt(wtoken token, int ival);
int wSetTokenString(wtoken token, char* str);
int wToggleTokenInt(wtoken token);
int wClickTokenByte(wtoken token, char ival);

// Getting Values
wtype  wGetType(wtoken token);
char*  wGetName(wtoken token);
whash  wGetHash(wtoken token);
int    wGetToken(wtoken token, wtype *type, wvalue *value);
int    wGetTokenFloat(wtoken token, float* fval);
int    wGetTokenInt(wtoken token, int* ival);
int    wGetTokenString(wtoken token, char* str);
int    wGetTokenDef(wtoken token, int *num, unsigned char* str);
int    wGetTokenTimed(wtoken token, wtype *type, wvalue *value, int timeout);
int    wGetTokenFloatTimed(wtoken token, float *fval, int timeout);
int    wGetTokenIntTimed(wtoken token, int *ival, int timeout);
int    wGetTokenStringTimed(wtoken token, char* str, int timeout);

// Event-driven updates
int wKeepAlive();
int wGetParsedEvents(wTV *tv, int maxevents);
int wGetParsedEventsTimed(wTV *tv, int maxevents, int timeout);

// Nodes
int wGetNode(wtoken node, char *str);
int wSetNode(char *str);
int wGetNodeToTVArray(wtoken node, wTV *array);
int wSetNodeFromTVArray(wTV *array, int nTV);
int wGetBinaryNode(wtoken node, unsigned char *array);
int wSetBinaryNode(unsigned char *array, int len);
int wGetBinaryData(wtoken node, unsigned char *array);

// Utility
wtoken wGetTokenFromName(char* name);
wtoken wGetTokenFromHash(whash h);
char*  wGetNameFromToken(wtoken token);
char*  wGetNameFromHash(whash h);
whash  wGetHashFromToken(wtoken token);
whash  wGetHashFromName(char* name);
int    wSizeMap();

// Network
int wTCPConnect();
int wSearchWING();
int wSend(unsigned char* buf, int len);
int wRecv(unsigned char* buf, int len);
int wSendEscapes(unsigned char* buf, int len);
int wRecvEscapes(unsigned char* buf, int len);
int wMRecv(unsigned char* buf, int len);
int wMeterUDPPort(int port);
int wGetMeters(unsigned char* buf, int maxlen, int timeout);
int wRenewMeters(int reqID);
int wSetMetersRequest(int reqID, unsigned char* wMid);
void wDumpBuffer(unsigned char* buf, int len);

#endif /* WEXT_H_ */
