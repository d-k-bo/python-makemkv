"""This module provides more information about makemkvcon's codes.

It includes mappings for message ids to loglevels and mappings for
codes to human readable strings.
"""

from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING

KEY_CODES = {
    1: "type",
    2: "name",
    3: "langcode",
    4: "language",
    5: "codec",
    8: "chapter_count",
    9: "length",
    10: "size_human",
    11: "size",
    13: "bitrate",
    15: "video_angle",
    17: "samplerate",
    19: "dimensions",
    20: "aspect_ratio",
    21: "framerate",
    27: "file_output",
    30: "information",
}

SPECIAL_VALUES = {
    6201: "video",
    6202: "audio",
    6203: "subtitles",
    6206: "DVD",
    6209: "BD",
    6212: "HDDVD",
    6213: "MKV",
}

# Loglevel for each messsage from makemkvcon
# the messsages can be found in makemkvgui/src/str/en_utf16.cpp
# (in makemkv-oss-1.16.1.tar.gz)
MESSAGE_CODES = {
    1000: DEBUG,
    1001: DEBUG,
    1002: DEBUG,
    1003: DEBUG,
    1004: DEBUG,
    1005: DEBUG,
    1006: DEBUG,
    1007: WARNING,
    1008: ERROR,
    1009: ERROR,
    1010: ERROR,
    1011: DEBUG,
    1012: DEBUG,
    2001: ERROR,
    2003: ERROR,
    2004: ERROR,
    2006: ERROR,
    2007: ERROR,
    2008: WARNING,
    2009: WARNING,
    2010: INFO,
    2011: WARNING,
    2012: WARNING,
    2013: ERROR,
    2014: INFO,
    2015: WARNING,
    2016: ERROR,
    2017: WARNING,
    2018: ERROR,
    2019: ERROR,
    2020: WARNING,
    2021: WARNING,
    2022: ERROR,
    2023: ERROR,
    2024: WARNING,
    2200: ERROR,
    2201: WARNING,
    2202: WARNING,
    2203: WARNING,
    2204: ERROR,
    2205: ERROR,
    2206: ERROR,
    2207: ERROR,
    2208: WARNING,
    2209: ERROR,
    2210: ERROR,
    2211: WARNING,
    2300: ERROR,
    2301: ERROR,
    2302: ERROR,
    2303: ERROR,
    2304: ERROR,
    2400: ERROR,
    2401: ERROR,
    2402: ERROR,
    2404: ERROR,
    3000: ERROR,
    3001: WARNING,
    3002: WARNING,
    3003: WARNING,
    3004: WARNING,
    3005: WARNING,
    3006: INFO,
    3007: INFO,
    3008: WARNING,
    3009: WARNING,
    3010: ERROR,
    3011: INFO,
    3012: INFO,
    3013: INFO,
    3014: INFO,
    3015: WARNING,
    3016: INFO,
    3017: INFO,
    3018: INFO,
    3019: WARNING,
    3020: WARNING,
    3021: WARNING,
    3022: WARNING,
    3023: WARNING,
    3024: WARNING,
    3025: INFO,
    3026: WARNING,
    3027: INFO,
    3028: INFO,
    3029: INFO,
    3030: INFO,
    3031: WARNING,
    3032: WARNING,
    3033: WARNING,
    3034: INFO,
    3035: WARNING,
    3036: WARNING,
    3037: INFO,
    3038: INFO,
    3039: WARNING,
    3040: INFO,
    3041: WARNING,
    3042: WARNING,
    3043: WARNING,
    3100: DEBUG,
    3101: DEBUG,
    3102: DEBUG,
    3103: DEBUG,
    3104: DEBUG,
    3105: DEBUG,
    3106: DEBUG,
    3107: DEBUG,
    3108: DEBUG,
    3109: DEBUG,
    3110: DEBUG,
    3111: DEBUG,
    3200: DEBUG,
    3201: DEBUG,
    3202: DEBUG,
    3203: DEBUG,
    3210: DEBUG,
    3220: INFO,
    3221: WARNING,
    3300: INFO,
    3301: WARNING,
    3302: INFO,
    3303: WARNING,
    3304: INFO,
    3305: INFO,
    3306: WARNING,
    3307: INFO,
    3308: INFO,
    3309: INFO,
    3310: WARNING,
    3311: WARNING,
    3312: WARNING,
    3313: WARNING,
    3314: WARNING,
    3315: WARNING,
    3316: WARNING,
    3317: INFO,
    3318: WARNING,
    3319: WARNING,
    3320: WARNING,
    3321: WARNING,
    3322: INFO,
    3323: ERROR,
    3324: INFO,
    3325: ERROR,
    3326: INFO,
    3327: WARNING,
    3328: INFO,
    3329: WARNING,
    3330: WARNING,
    3331: ERROR,
    3332: INFO,
    3333: WARNING,
    3334: WARNING,
    3335: WARNING,
    3336: WARNING,
    3337: WARNING,
    3338: INFO,
    3339: WARNING,
    3340: WARNING,
    3341: INFO,
    3342: WARNING,
    3343: WARNING,
    3344: INFO,
    3345: WARNING,
    3346: WARNING,
    3347: WARNING,
    3400: DEBUG,
    3401: DEBUG,
    3402: DEBUG,
    3403: DEBUG,
    3404: DEBUG,
    3405: DEBUG,
    3406: DEBUG,
    3407: DEBUG,
    4001: INFO,
    4002: INFO,
    4003: WARNING,
    4004: WARNING,
    4007: WARNING,
    4008: WARNING,
    4009: WARNING,
    4020: WARNING,
    4021: WARNING,
    4022: WARNING,
    4023: WARNING,
    4024: WARNING,
    4025: WARNING,
    4026: WARNING,
    4027: WARNING,
    4028: WARNING,
    4040: WARNING,
    4041: ERROR,
    4042: ERROR,
    4043: ERROR,
    4044: ERROR,
    4045: ERROR,
    4046: WARNING,
    4047: WARNING,
    4048: WARNING,
    4049: WARNING,
    4050: WARNING,
    4051: WARNING,
    4052: INFO,
    4053: WARNING,
    4054: ERROR,
    4055: WARNING,
    4060: WARNING,
    4061: WARNING,
    4062: WARNING,
    5000: WARNING,
    5001: WARNING,
    5002: INFO,
    5003: ERROR,
    5004: WARNING,
    5005: INFO,
    5006: ERROR,
    5007: ERROR,
    5008: ERROR,
    5009: ERROR,
    5010: CRITICAL,
    5011: INFO,
    5012: INFO,
    5013: WARNING,
    5014: INFO,
    5015: INFO,
    5016: ERROR,
    5017: INFO,
    5018: INFO,
    5019: INFO,
    5020: ERROR,
    5021: ERROR,
    5022: ERROR,
    5024: INFO,
    5025: DEBUG,
    5026: DEBUG,
    5027: DEBUG,
    5028: DEBUG,
    5029: DEBUG,
    5030: DEBUG,
    5031: DEBUG,
    5033: DEBUG,
    5036: INFO,
    5037: WARNING,
    5038: WARNING,
    5039: WARNING,
    5040: WARNING,
    5041: WARNING,
    5042: WARNING,
    5043: ERROR,
    5044: DEBUG,
    5045: DEBUG,
    5046: DEBUG,
    5047: DEBUG,
    5048: DEBUG,
    5049: DEBUG,
    5050: DEBUG,
    5051: WARNING,
    5052: WARNING,
    5053: WARNING,
    5054: WARNING,
    5055: WARNING,
    5056: WARNING,
    5057: DEBUG,
    5058: WARNING,
    5060: DEBUG,
    5061: DEBUG,
    5062: DEBUG,
    5063: DEBUG,
    5064: DEBUG,
    5065: DEBUG,
    5066: DEBUG,
    5067: DEBUG,
    5068: WARNING,
    5069: ERROR,
    5070: INFO,
    5071: WARNING,
    5072: INFO,
    5073: WARNING,
    5074: INFO,
    5075: WARNING,
    5076: WARNING,
    5077: WARNING,
    5078: WARNING,
    5079: WARNING,
    5080: CRITICAL,
    5081: INFO,
    5082: WARNING,
    5083: WARNING,
    5084: WARNING,
    5085: DEBUG,
    5086: DEBUG,
    5087: DEBUG,
    5088: DEBUG,
    5089: DEBUG,
    5090: DEBUG,
    5091: DEBUG,
    5092: DEBUG,
    5093: DEBUG,
    5094: INFO,
    5100: DEBUG,
    5101: WARNING,
}
