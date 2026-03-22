/*
 * wingctl — CLI tool for controlling the Behringer Wing via wapi
 *
 * Usage:
 *   wingctl info                       — Show Wing connection info
 *   wingctl get <path>                 — Get a parameter value
 *   wingctl set <path> <value>         — Set a parameter value
 *   wingctl node <path>                — Dump all children of a node
 *   wingctl gets <path>                — Get as string
 *   wingctl geti <path>                — Get as int
 *   wingctl getf <path>                — Get as float
 *
 * Paths use OSC-style notation: /ch/1/fdr, /io/in/USR/1/user/grp
 * Converted to wapi tokens:    CH_1_FDR, IO_IN_USR_1_USER_GRP
 *
 * Environment:
 *   WING_IP — Wing IP address (default: 192.168.2.2)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include "../lib/wapi/wapi.h"
#include "../lib/wapi/wext.h"

#define WING_DEFAULT_IP "192.168.2.2"
#define STR_BUF 256
#define NODE_BUF 65536
#define METER_BUF 4096
#define METER_UDP_PORT 14135

// Convert OSC path to wapi dot notation: /ch/1/fdr → ch.1.fdr (case-preserved)
static void path_to_token_name(const char *path, char *out, int maxlen) {
    const char *p = path;
    int i = 0;
    // Skip leading /
    if (*p == '/') p++;
    while (*p && i < maxlen - 1) {
        if (*p == '/') {
            out[i++] = '.';
        } else {
            out[i++] = *p;
        }
        p++;
    }
    out[i] = '\0';
}

static int wing_open(void) {
    char *ip_env = getenv("WING_IP");
    char wingip[24];
    if (ip_env && *ip_env) {
        strncpy(wingip, ip_env, sizeof(wingip) - 1);
        wingip[sizeof(wingip) - 1] = '\0';
    } else {
        strcpy(wingip, WING_DEFAULT_IP);
    }
    if (wOpen(wingip) != WSUCCESS) {
        fprintf(stderr, "error: cannot connect to Wing at %s\n", wingip);
        return -1;
    }
    return 0;
}

static void usage(void) {
    fprintf(stderr,
        "Usage: wingctl <command> [path] [value]\n"
        "\n"
        "Commands:\n"
        "  info              Show Wing connection info\n"
        "  get  <path>       Get parameter (auto-detect type)\n"
        "  gets <path>       Get parameter as string\n"
        "  geti <path>       Get parameter as int\n"
        "  getf <path>       Get parameter as float\n"
        "  set  <path> <val> Set parameter (auto-detect type)\n"
        "  node <path>       Dump node children\n"
        "  meter <ch>        Read live input/output levels (e.g. /ch/17 or 17)\n"
        "\n"
        "Paths: /ch/1/fdr, /io/in/USR/1/user/grp, etc.\n"
        "Env:   WING_IP (default: 192.168.2.2)\n"
    );
}

static int cmd_info(void) {
    if (wing_open() < 0) return 1;
    unsigned int v = wVer();
    printf("version=%u.%u\n", v / 256, v & 15);
    wClose();
    return 0;
}

static wtoken resolve_token(const char *path) {
    char tname[256];
    path_to_token_name(path, tname, sizeof(tname));
    wtoken t = wGetTokenFromName(tname);
    if ((int)t < 0) {
        fprintf(stderr, "error: unknown path %s (token %s)\n", path, tname);
    }
    return t;
}

static int cmd_get(const char *path) {
    if (wing_open() < 0) return 1;
    wtoken t = resolve_token(path);
    if ((int)t < 0) { wClose(); return 1; }

    wtype type = wGetType(t);
    int rc;
    switch (type) {
        case I32: {
            int ival;
            rc = wGetTokenInt(t, &ival);
            if (rc == WSUCCESS) printf("%d\n", ival);
            else fprintf(stderr, "error: get failed (%d)\n", rc);
            break;
        }
        case F32: {
            float fval;
            rc = wGetTokenFloat(t, &fval);
            if (rc == WSUCCESS) printf("%.6g\n", fval);
            else fprintf(stderr, "error: get failed (%d)\n", rc);
            break;
        }
        case S32: {
            char str[STR_BUF] = {0};
            rc = wGetTokenString(t, str);
            if (rc == WSUCCESS) printf("%s\n", str);
            else fprintf(stderr, "error: get failed (%d)\n", rc);
            break;
        }
        case NODE: {
            char buf[NODE_BUF] = {0};
            rc = wGetNode(t, buf);
            if (rc == WSUCCESS) printf("%s\n", buf);
            else fprintf(stderr, "error: node get failed (%d)\n", rc);
            break;
        }
        default:
            fprintf(stderr, "error: unknown type %d for path %s\n", type, path);
            break;
    }
    wClose();
    return (rc == WSUCCESS) ? 0 : 1;
}

static int cmd_gets(const char *path) {
    if (wing_open() < 0) return 1;
    wtoken t = resolve_token(path);
    if ((int)t < 0) { wClose(); return 1; }
    char str[STR_BUF] = {0};
    int rc = wGetTokenString(t, str);
    if (rc == WSUCCESS) printf("%s\n", str);
    else fprintf(stderr, "error: get string failed (%d)\n", rc);
    wClose();
    return (rc == WSUCCESS) ? 0 : 1;
}

static int cmd_geti(const char *path) {
    if (wing_open() < 0) return 1;
    wtoken t = resolve_token(path);
    if ((int)t < 0) { wClose(); return 1; }
    int ival;
    int rc = wGetTokenInt(t, &ival);
    if (rc == WSUCCESS) printf("%d\n", ival);
    else fprintf(stderr, "error: get int failed (%d)\n", rc);
    wClose();
    return (rc == WSUCCESS) ? 0 : 1;
}

static int cmd_getf(const char *path) {
    if (wing_open() < 0) return 1;
    wtoken t = resolve_token(path);
    if ((int)t < 0) { wClose(); return 1; }
    float fval;
    int rc = wGetTokenFloat(t, &fval);
    if (rc == WSUCCESS) printf("%.6g\n", fval);
    else fprintf(stderr, "error: get float failed (%d)\n", rc);
    wClose();
    return (rc == WSUCCESS) ? 0 : 1;
}

static int cmd_set(const char *path, const char *value) {
    if (wing_open() < 0) return 1;
    wtoken t = resolve_token(path);
    if ((int)t < 0) { wClose(); return 1; }

    wtype type = wGetType(t);
    int rc;
    switch (type) {
        case I32: {
            int ival = atoi(value);
            rc = wSetTokenInt(t, ival);
            break;
        }
        case F32: {
            float fval = atof(value);
            rc = wSetTokenFloat(t, fval);
            break;
        }
        case S32: {
            rc = wSetTokenString(t, (char*)value);
            break;
        }
        default:
            // Try string as fallback
            rc = wSetTokenString(t, (char*)value);
            break;
    }
    if (rc == WSUCCESS) printf("OK\n");
    else fprintf(stderr, "error: set failed (%d)\n", rc);
    wClose();
    return (rc == WSUCCESS) ? 0 : 1;
}

static int cmd_node(const char *path) {
    if (wing_open() < 0) return 1;
    wtoken t = resolve_token(path);
    if ((int)t < 0) { wClose(); return 1; }

    char buf[NODE_BUF] = {0};
    int rc = wGetNode(t, buf);
    if (rc == WSUCCESS) printf("%s\n", buf);
    else fprintf(stderr, "error: node failed (%d)\n", rc);
    wClose();
    return (rc == WSUCCESS) ? 0 : 1;
}

// Meter command: read input level for a channel
// Channel meter data layout per channel: inL, inR, outL, outR, gateKey, gateGain, dynKey, dynGain
// Each value is signed 16-bit big-endian, in 1/256th dB
static int cmd_meter(const char *path) {
    // Parse channel number from path like /ch/17
    int ch = 0;
    if (strncmp(path, "/ch/", 4) == 0) {
        ch = atoi(path + 4);
    } else {
        ch = atoi(path);
    }
    if (ch < 1 || ch > 40) {
        fprintf(stderr, "error: channel must be 1-40, got %d\n", ch);
        return 1;
    }

    if (wing_open() < 0) return 1;

    // Set up meter UDP port
    int rc = wMeterUDPPort(METER_UDP_PORT);
    if (rc != WSUCCESS) {
        fprintf(stderr, "error: wMeterUDPPort failed (%d)\n", rc);
        wClose();
        return 1;
    }

    // Build meter request bitmap (30 bytes)
    // Bytes 0-4 = channels 1-40 (5 bytes, 8 channels per byte)
    unsigned char mbits[30] = {0};
    int byte_idx = (ch - 1) / 8;
    int bit_idx = (ch - 1) % 8;
    mbits[byte_idx] = (unsigned char)(1 << bit_idx);

    rc = wSetMetersRequest(1, mbits);
    if (rc != WSUCCESS) {
        fprintf(stderr, "error: wSetMetersRequest failed (%d)\n", rc);
        wClose();
        return 1;
    }

    // Read meter data — Wing sends every ~50ms after a valid request
    unsigned char buf[METER_BUF] = {0};
    int got = wGetMeters(buf, METER_BUF, 500000);

    if (got <= 0) {
        fprintf(stderr, "error: no meter data received (got=%d)\n", got);
        wClose();
        return 1;
    }

    // Data format: <4 byte reqID> <meter data groups>
    // Each channel has 8 x 16-bit values: inL, inR, outL, outR, gateKey, gateGain, dynKey, dynGain
    // Skip 4-byte reqID
    if (got < 4 + 16) {
        fprintf(stderr, "error: meter data too short (%d bytes)\n", got);
        wClose();
        return 1;
    }

    // Dump raw bytes for debugging
    fprintf(stderr, "raw (%d bytes):", got);
    for (int i = 0; i < got && i < 40; i++) {
        fprintf(stderr, " %02x", buf[i]);
    }
    fprintf(stderr, "\n");

    unsigned char *mdata = buf + 4; // skip reqID
    // Each meter is 2 bytes big-endian signed
    int16_t inL  = (int16_t)((mdata[0] << 8) | mdata[1]);
    int16_t inR  = (int16_t)((mdata[2] << 8) | mdata[3]);
    int16_t outL = (int16_t)((mdata[4] << 8) | mdata[5]);
    int16_t outR = (int16_t)((mdata[6] << 8) | mdata[7]);

    float inL_dB  = inL / 256.0f;
    float inR_dB  = inR / 256.0f;
    float outL_dB = outL / 256.0f;
    float outR_dB = outR / 256.0f;

    printf("ch%d inL=%.1fdB inR=%.1fdB outL=%.1fdB outR=%.1fdB\n",
           ch, inL_dB, inR_dB, outL_dB, outR_dB);

    wClose();
    return 0;
}

int main(int argc, char *argv[]) {
    if (argc < 2) { usage(); return 1; }

    const char *cmd = argv[1];

    if (strcmp(cmd, "info") == 0) {
        return cmd_info();
    }
    if (strcmp(cmd, "get") == 0 && argc >= 3) {
        return cmd_get(argv[2]);
    }
    if (strcmp(cmd, "gets") == 0 && argc >= 3) {
        return cmd_gets(argv[2]);
    }
    if (strcmp(cmd, "geti") == 0 && argc >= 3) {
        return cmd_geti(argv[2]);
    }
    if (strcmp(cmd, "getf") == 0 && argc >= 3) {
        return cmd_getf(argv[2]);
    }
    if (strcmp(cmd, "set") == 0 && argc >= 4) {
        return cmd_set(argv[2], argv[3]);
    }
    if (strcmp(cmd, "node") == 0 && argc >= 3) {
        return cmd_node(argv[2]);
    }
    if (strcmp(cmd, "meter") == 0 && argc >= 3) {
        return cmd_meter(argv[2]);
    }

    usage();
    return 1;
}
