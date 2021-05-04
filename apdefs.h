/*
    MakeMKV GUI - Graphics user interface application for MakeMKV

    Written by GuinpinSoft inc <makemkvgui@makemkv.com>

    This file is hereby placed into public domain,
    no copyright is claimed.

*/
#ifndef APDEFS_H_INCLUDED
#define APDEFS_H_INCLUDED

static const unsigned int AP_MaxCdromDevices=16;
static const unsigned int AP_Progress_MaxValue=65536;
static const unsigned int AP_Progress_MaxLayoutItems=10;
static const unsigned int AP_UIMSG_BOX_MASK=3854;
static const unsigned int AP_UIMSG_BOXOK=260;
static const unsigned int AP_UIMSG_BOXERROR=516;
static const unsigned int AP_UIMSG_BOXWARNING=1028;
static const unsigned int AP_UIMSG_BOXYESNO=776;
static const unsigned int AP_UIMSG_BOXYESNO_ERR=1288;
static const unsigned int AP_UIMSG_YES=0;
static const unsigned int AP_UIMSG_NO=1;
static const unsigned int AP_UIMSG_DEBUG=32;
static const unsigned int AP_UIMSG_HIDDEN=64;
static const unsigned int AP_UIMSG_EVENT=128;
static const unsigned int AP_UIMSG_HAVE_URL=131072;
static const unsigned int AP_UIMSG_VITEM_BASE=5200;
static const unsigned int AP_MMBD_DISC_FLAG_BUSENC=2;
static const unsigned int AP_MMBD_MMBD_DISC_FLAG_AACS=4;
static const unsigned int AP_MMBD_MMBD_DISC_FLAG_BDPLUS=8;
static const unsigned int AP_vastr_Name=0;
static const unsigned int AP_vastr_Version=1;
static const unsigned int AP_vastr_Platform=2;
static const unsigned int AP_vastr_Build=3;
static const unsigned int AP_vastr_KeyType=4;
static const unsigned int AP_vastr_KeyFeatures=5;
static const unsigned int AP_vastr_KeyExpiration=6;
static const unsigned int AP_vastr_EvalState=7;
static const unsigned int AP_vastr_ProgExpiration=8;
static const unsigned int AP_vastr_LatestVersion=9;
static const unsigned int AP_vastr_RestartRequired=10;
static const unsigned int AP_vastr_ExpertMode=11;
static const unsigned int AP_vastr_ProfileCount=12;
static const unsigned int AP_vastr_ProgExpired=13;
static const unsigned int AP_vastr_OutputFolderName=14;
static const unsigned int AP_vastr_OutputBaseName=15;
static const unsigned int AP_vastr_CurrentProfile=16;
static const unsigned int AP_vastr_OpenFileFilter=17;
static const unsigned int AP_vastr_WebSiteURL=18;
static const unsigned int AP_vastr_OpenDVDFileFilter=19;
static const unsigned int AP_vastr_DefaultSelectionString=20;
static const unsigned int AP_vastr_DefaultOutputFileName=21;
static const unsigned int AP_vastr_ExternalAppItem=22;
static const unsigned int AP_vastr_InterfaceLanguage=23;
static const unsigned int AP_vastr_ProfileString=24;
//
typedef enum _AP_ItemAttributeId
{
  ap_iaUnknown=0,
  ap_iaType=1,
  ap_iaName=2,
  ap_iaLangCode=3,
  ap_iaLangName=4,
  ap_iaCodecId=5,
  ap_iaCodecShort=6,
  ap_iaCodecLong=7,
  ap_iaChapterCount=8,
  ap_iaDuration=9,
  ap_iaDiskSize=10,
  ap_iaDiskSizeBytes=11,
  ap_iaStreamTypeExtension=12,
  ap_iaBitrate=13,
  ap_iaAudioChannelsCount=14,
  ap_iaAngleInfo=15,
  ap_iaSourceFileName=16,
  ap_iaAudioSampleRate=17,
  ap_iaAudioSampleSize=18,
  ap_iaVideoSize=19,
  ap_iaVideoAspectRatio=20,
  ap_iaVideoFrameRate=21,
  ap_iaStreamFlags=22,
  ap_iaDateTime=23,
  ap_iaOriginalTitleId=24,
  ap_iaSegmentsCount=25,
  ap_iaSegmentsMap=26,
  ap_iaOutputFileName=27,
  ap_iaMetadataLanguageCode=28,
  ap_iaMetadataLanguageName=29,
  ap_iaTreeInfo=30,
  ap_iaPanelTitle=31,
  ap_iaVolumeName=32,
  ap_iaOrderWeight=33,
  ap_iaOutputFormat=34,
  ap_iaOutputFormatDescription=35,
  ap_iaSeamlessInfo=36,
  ap_iaPanelText=37,
  ap_iaMkvFlags=38,
  ap_iaMkvFlagsText=39,
  ap_iaAudioChannelLayoutName=40,
  ap_iaOutputCodecShort=41,
  ap_iaOutputConversionType=42,
  ap_iaOutputAudioSampleRate=43,
  ap_iaOutputAudioSampleSize=44,
  ap_iaOutputAudioChannelsCount=45,
  ap_iaOutputAudioChannelLayoutName=46,
  ap_iaOutputAudioChannelLayout=47,
  ap_iaOutputAudioMixDescription=48,
  ap_iaComment=49,
  ap_iaOffsetSequenceId=50,
  ap_iaMaxValue
} AP_ItemAttributeId;

static const unsigned int AP_DskFsFlagDvdFilesPresent=1;
static const unsigned int AP_DskFsFlagHdvdFilesPresent=2;
static const unsigned int AP_DskFsFlagBlurayFilesPresent=4;
static const unsigned int AP_DskFsFlagAacsFilesPresent=8;
static const unsigned int AP_DskFsFlagBdsvmFilesPresent=16;


static const unsigned int AP_DriveStateNoDrive=256;
static const unsigned int AP_DriveStateUnmounting=257;
static const unsigned int AP_DriveStateEmptyClosed=0;
static const unsigned int AP_DriveStateEmptyOpen=1;
static const unsigned int AP_DriveStateInserted=2;
static const unsigned int AP_DriveStateLoading=3;


static const unsigned int AP_Notify_UpdateLayoutFlag_NoTime=1;
static const unsigned int AP_ProgressCurrentIndex_SourceName=65280;
static const unsigned int AP_BackupFlagDecryptVideo=1;
static const unsigned int AP_OpenFlagManualMode=1;
static const unsigned int AP_UpdateDrivesFlagNoScan=1;
static const unsigned int AP_UpdateDrivesFlagNoSingleDrive=2;


static const unsigned int AP_AVStreamFlag_DirectorsComments=1;
static const unsigned int AP_AVStreamFlag_AlternateDirectorsComments=2;
static const unsigned int AP_AVStreamFlag_ForVisuallyImpaired=4;
static const unsigned int AP_AVStreamFlag_CoreAudio=256;
static const unsigned int AP_AVStreamFlag_SecondaryAudio=512;
static const unsigned int AP_AVStreamFlag_HasCoreAudio=1024;
static const unsigned int AP_AVStreamFlag_DerivedStream=2048;
static const unsigned int AP_AVStreamFlag_ForcedSubtitles=4096;
static const unsigned int AP_AVStreamFlag_ProfileSecondaryStream=16384;
static const unsigned int AP_AVStreamFlag_OffsetSequenceIdPresent=32768;


static const unsigned int AP_APP_LOC_MAX=7000;


static const unsigned long APP_DUMP_DONE_PARTIAL=5004;
static const unsigned long APP_DUMP_DONE=5005;
static const unsigned long APP_INIT_FAILED=5009;
static const unsigned long APP_ASK_FOLDER_CREATE=5013;
static const unsigned long APP_FOLDER_INVALID=5016;
static const unsigned long PROGRESS_APP_SAVE_MKV_FREE_SPACE=5033;
static const unsigned long PROT_DEMO_KEY_EXPIRED=5021;
static const unsigned long APP_EVAL_TIME_NEVER=5067;
static const unsigned long APP_BACKUP_FAILED=5069;
static const unsigned long APP_BACKUP_COMPLETED=5070;
static const unsigned long APP_BACKUP_COMPLETED_HASHFAIL=5079;
static const unsigned long PROFILE_NAME_DEFAULT=5086;
static const unsigned long VITEM_NAME=5202;
static const unsigned long VITEM_TIMESTAMP=5223;
static const unsigned long APP_IFACE_TITLE=6000;
static const unsigned long APP_CAPTION_MSG=6001;
static const unsigned long APP_ABOUTBOX_TITLE=6002;
static const unsigned long APP_IFACE_OPENFILE_TITLE=6003;
static const unsigned long APP_SETTINGDLG_TITLE=6135;
static const unsigned long APP_BACKUPDLG_TITLE=6136;
static const unsigned long APP_IFACE_OPENFILE_FILTER_TEMPLATE1=6007;
static const unsigned long APP_IFACE_OPENFILE_FILTER_TEMPLATE2=6008;
static const unsigned long APP_IFACE_OPENFOLDER_TITLE=6005;
static const unsigned long APP_IFACE_OPENFOLDER_INFO_TITLE=6006;
static const unsigned long APP_IFACE_PROGRESS_TITLE=6038;
static const unsigned long APP_IFACE_PROGRESS_ELAPSED_ONLY=6039;
static const unsigned long APP_IFACE_PROGRESS_ELAPSED_ETA=6040;
static const unsigned long APP_IFACE_ACT_OPENFILES_NAME=6010;
static const unsigned long APP_IFACE_ACT_OPENFILES_SKEY=6011;
static const unsigned long APP_IFACE_ACT_OPENFILES_STIP=6012;
static const unsigned long APP_IFACE_ACT_OPENFILES_DVD_NAME=6024;
static const unsigned long APP_IFACE_ACT_OPENFILES_DVD_STIP=6026;
static const unsigned long APP_IFACE_ACT_CLOSEDISK_NAME=6013;
static const unsigned long APP_IFACE_ACT_CLOSEDISK_STIP=6014;
static const unsigned long APP_IFACE_ACT_SETFOLDER_NAME=6015;
static const unsigned long APP_IFACE_ACT_SETFOLDER_STIP=6016;
static const unsigned long APP_IFACE_ACT_SAVEALLMKV_NAME=6017;
static const unsigned long APP_IFACE_ACT_SAVEALLMKV_STIP=6018;
static const unsigned long APP_IFACE_ACT_CANCEL_NAME=6036;
static const unsigned long APP_IFACE_ACT_CANCEL_STIP=6037;
static const unsigned long APP_IFACE_ACT_STREAMING_NAME=6131;
static const unsigned long APP_IFACE_ACT_STREAMING_STIP=6132;
static const unsigned long APP_IFACE_ACT_BACKUP_NAME=6133;
static const unsigned long APP_IFACE_ACT_BACKUP_STIP=6134;
static const unsigned long APP_IFACE_ACT_QUIT_NAME=6019;
static const unsigned long APP_IFACE_ACT_QUIT_SKEY=6020;
static const unsigned long APP_IFACE_ACT_QUIT_STIP=6021;
static const unsigned long APP_IFACE_ACT_ABOUT_NAME=6022;
static const unsigned long APP_IFACE_ACT_ABOUT_STIP=6023;
static const unsigned long APP_IFACE_ACT_SETTINGS_NAME=6042;
static const unsigned long APP_IFACE_ACT_SETTINGS_STIP=6043;
static const unsigned long APP_IFACE_ACT_HELPPAGE_NAME=6045;
static const unsigned long APP_IFACE_ACT_HELPPAGE_STIP=6046;
static const unsigned long APP_IFACE_ACT_REGISTER_NAME=6047;
static const unsigned long APP_IFACE_ACT_REGISTER_STIP=6048;
static const unsigned long APP_IFACE_ACT_PURCHASE_NAME=6145;
static const unsigned long APP_IFACE_ACT_PURCHASE_STIP=6146;
static const unsigned long APP_IFACE_ACT_CLEARLOG_NAME=6110;
static const unsigned long APP_IFACE_ACT_CLEARLOG_STIP=6111;
static const unsigned long APP_IFACE_ACT_EJECT_NAME=6052;
static const unsigned long APP_IFACE_ACT_EJECT_STIP=6053;
static const unsigned long APP_IFACE_ACT_REVERT_NAME=6105;
static const unsigned long APP_IFACE_ACT_REVERT_STIP=6106;
static const unsigned long APP_IFACE_ACT_NEWINSTANCE_NAME=6107;
static const unsigned long APP_IFACE_ACT_NEWINSTANCE_STIP=6108;
static const unsigned long APP_IFACE_ACT_OPENDISC_DVD=6062;
static const unsigned long APP_IFACE_ACT_OPENDISC_HDDVD=6063;
static const unsigned long APP_IFACE_ACT_OPENDISC_BRAY=6064;
static const unsigned long APP_IFACE_ACT_OPENDISC_LOADING=6065;
static const unsigned long APP_IFACE_ACT_OPENDISC_UNKNOWN=6099;
static const unsigned long APP_IFACE_ACT_OPENDISC_NODISC=6109;
static const unsigned long APP_IFACE_ACT_TTREE_TOGGLE=6066;
static const unsigned long APP_IFACE_ACT_TTREE_SELECT_ALL=6067;
static const unsigned long APP_IFACE_ACT_TTREE_UNSELECT_ALL=6068;
static const unsigned long APP_IFACE_MENU_FILE=6030;
static const unsigned long APP_IFACE_MENU_VIEW=6031;
static const unsigned long APP_IFACE_MENU_HELP=6032;
static const unsigned long APP_IFACE_MENU_TOOLBAR=6034;
static const unsigned long APP_IFACE_MENU_SETTINGS=6044;
static const unsigned long APP_IFACE_MENU_DRIVES=6035;
static const unsigned long APP_IFACE_CANCEL_CONFIRM=6041;
static const unsigned long APP_IFACE_FATAL_COMM=6050;
static const unsigned long APP_IFACE_FATAL_MEM=6051;
static const unsigned long APP_IFACE_GUI_VERSION=6054;
static const unsigned long APP_IFACE_LATEST_VERSION=6158;
static const unsigned long APP_IFACE_LICENSE_TYPE=6055;
static const unsigned long APP_IFACE_EVAL_STATE=6056;
static const unsigned long APP_IFACE_EVAL_EXPIRATION=6057;
static const unsigned long APP_IFACE_PROG_EXPIRATION=6142;
static const unsigned long APP_IFACE_WEBSITE_URL=6159;
static const unsigned long APP_IFACE_VIDEO_FOLDER_NAME_WIN=6058;
static const unsigned long APP_IFACE_VIDEO_FOLDER_NAME_MAC=6059;
static const unsigned long APP_IFACE_VIDEO_FOLDER_NAME_LINUX=6060;
static const unsigned long APP_IFACE_DEFAULT_FOLDER_NAME=6061;
static const unsigned long APP_IFACE_MAIN_FRAME_INFO=6069;
static const unsigned long APP_IFACE_MAIN_FRAME_MAKE_MKV=6070;
static const unsigned long APP_IFACE_MAIN_FRAME_PROFILE=6180;
static const unsigned long APP_IFACE_MAIN_FRAME_PROPERTIES=6181;
static const unsigned long APP_IFACE_EMPTY_FRAME_INFO=6075;
static const unsigned long APP_IFACE_EMPTY_FRAME_SOURCE=6071;
static const unsigned long APP_IFACE_EMPTY_FRAME_TYPE=6072;
static const unsigned long APP_IFACE_EMPTY_FRAME_LABEL=6073;
static const unsigned long APP_IFACE_EMPTY_FRAME_PROTECTION=6074;
static const unsigned long APP_IFACE_EMPTY_FRAME_DVD_MANUAL=6084;
static const unsigned long APP_IFACE_REGISTER_TEXT=6076;
static const unsigned long APP_IFACE_REGISTER_CODE_INCORRECT=6077;
static const unsigned long APP_IFACE_REGISTER_CODE_NOT_SAVED=6078;
static const unsigned long APP_IFACE_REGISTER_CODE_SAVED=6079;
static const unsigned long APP_IFACE_SETTINGS_IO_OPTIONS=6080;
static const unsigned long APP_IFACE_SETTINGS_IO_AUTO=6081;
static const unsigned long APP_IFACE_SETTINGS_IO_READ_RETRY=6082;
static const unsigned long APP_IFACE_SETTINGS_IO_READ_BUFFER=6083;
static const unsigned long APP_IFACE_SETTINGS_IO_NO_DIRECT_ACCESS=6150;
static const unsigned long APP_IFACE_SETTINGS_IO_DARWIN_K2_WORKAROUND=6151;
static const unsigned long APP_IFACE_SETTINGS_IO_SINGLE_DRIVE=6168;
static const unsigned long APP_IFACE_SETTINGS_DVD_AUTO=6085;
static const unsigned long APP_IFACE_SETTINGS_DVD_MIN_LENGTH=6086;
static const unsigned long APP_IFACE_SETTINGS_DVD_SP_REMOVE=6087;
static const unsigned long APP_IFACE_SETTINGS_AACS_KEY_DIR=6088;
static const unsigned long APP_IFACE_SETTINGS_BDP_MISC=6129;
static const unsigned long APP_IFACE_SETTINGS_BDP_DUMP_ALWAYS=6130;
static const unsigned long APP_IFACE_SETTINGS_DEST_TYPE_NONE=6089;
static const unsigned long APP_IFACE_SETTINGS_DEST_TYPE_AUTO=6090;
static const unsigned long APP_IFACE_SETTINGS_DEST_TYPE_SEMIAUTO=6091;
static const unsigned long APP_IFACE_SETTINGS_DEST_TYPE_CUSTOM=6092;
static const unsigned long APP_IFACE_SETTINGS_DESTDIR=6093;
static const unsigned long APP_IFACE_SETTINGS_GENERAL_MISC=6094;
static const unsigned long APP_IFACE_SETTINGS_LOG_DEBUG_MSG=6095;
static const unsigned long APP_IFACE_SETTINGS_DATA_DIR=6167;
static const unsigned long APP_IFACE_SETTINGS_EXPERT_MODE=6169;
static const unsigned long APP_IFACE_SETTINGS_SHOW_AVSYNC=6170;
static const unsigned long APP_IFACE_SETTINGS_GENERAL_ONLINE_UPDATES=6188;
static const unsigned long APP_IFACE_SETTINGS_ENABLE_INTERNET_ACCESS=6187;
static const unsigned long APP_IFACE_SETTINGS_PROXY_SERVER=6189;
static const unsigned long APP_IFACE_SETTINGS_TAB_GENERAL=6096;
static const unsigned long APP_IFACE_SETTINGS_MSG_FAILED=6097;
static const unsigned long APP_IFACE_SETTINGS_MSG_RESTART=6098;
static const unsigned long APP_IFACE_SETTINGS_TAB_LANGUAGE=6152;
static const unsigned long APP_IFACE_SETTINGS_LANG_INTERFACE=6153;
static const unsigned long APP_IFACE_SETTINGS_LANG_PREFERRED=6154;
static const unsigned long APP_IFACE_SETTINGS_LANGUAGE_AUTO=6156;
static const unsigned long APP_IFACE_SETTINGS_LANGUAGE_NONE=6157;
static const unsigned long APP_IFACE_SETTINGS_TAB_IO=6164;
static const unsigned long APP_IFACE_SETTINGS_TAB_STREAMING=6165;
static const unsigned long APP_IFACE_SETTINGS_TAB_PROT=6166;
static const unsigned long APP_IFACE_SETTINGS_TAB_ADVANCED=6172;
static const unsigned long APP_IFACE_SETTINGS_ADV_DEFAULT_PROFILE=6173;
static const unsigned long APP_IFACE_SETTINGS_ADV_DEFAULT_SELECTION=6174;
static const unsigned long APP_IFACE_SETTINGS_ADV_EXTERN_EXEC_PATH=6175;
static const unsigned long APP_IFACE_SETTINGS_PROT_JAVA_PATH=6177;
static const unsigned long APP_IFACE_SETTINGS_ADV_OUTPUT_FILE_NAME_TEMPLATE=6178;
static const unsigned long APP_IFACE_SETTINGS_TAB_INTEGRATION=6190;
static const unsigned long APP_IFACE_SETTINGS_INT_TEXT=6191;
static const unsigned long APP_IFACE_SETTINGS_INT_HDR_PATH=6192;
static const unsigned long APP_IFACE_BACKUPDLG_TEXT_CAPTION=6137;
static const unsigned long APP_IFACE_BACKUPDLG_TEXT=6138;
static const unsigned long APP_IFACE_BACKUPDLG_FOLDER=6139;
static const unsigned long APP_IFACE_BACKUPDLG_OPTIONS=6147;
static const unsigned long APP_IFACE_BACKUPDLG_DECRYPT=6148;
static const unsigned long APP_IFACE_DRIVEINFO_LOADING=6100;
static const unsigned long APP_IFACE_DRIVEINFO_UNMOUNTING=6112;
static const unsigned long APP_IFACE_DRIVEINFO_WAIT=6101;
static const unsigned long APP_IFACE_DRIVEINFO_NODISC=6102;
static const unsigned long APP_IFACE_DRIVEINFO_DATADISC=6103;
static const unsigned long APP_IFACE_DRIVEINFO_NONE=6104;
static const unsigned long APP_IFACE_FLAGS_DIRECTORS_COMMENTS=6125;
static const unsigned long APP_IFACE_FLAGS_ALT_DIRECTORS_COMMENTS=6126;
static const unsigned long APP_IFACE_FLAGS_SECONDARY_AUDIO=6127;
static const unsigned long APP_IFACE_FLAGS_FOR_VISUALLY_IMPAIRED=6128;
static const unsigned long APP_IFACE_FLAGS_CORE_AUDIO=6143;
static const unsigned long APP_IFACE_FLAGS_FORCED_SUBTITLES=6144;
static const unsigned long APP_IFACE_FLAGS_PROFILE_SECONDARY_STREAM=6171;
static const unsigned long APP_IFACE_ITEMINFO_SOURCE=6119;
static const unsigned long APP_IFACE_ITEMINFO_TITLE=6120;
static const unsigned long APP_IFACE_ITEMINFO_TRACK=6121;
static const unsigned long APP_IFACE_ITEMINFO_ATTACHMENT=6122;
static const unsigned long APP_IFACE_ITEMINFO_CHAPTER=6123;
static const unsigned long APP_IFACE_ITEMINFO_CHAPTERS=6124;
static const unsigned long APP_TTREE_TITLE=6200;
static const unsigned long APP_TTREE_VIDEO=6201;
static const unsigned long APP_TTREE_AUDIO=6202;
static const unsigned long APP_TTREE_SUBPICTURE=6203;
static const unsigned long APP_TTREE_ATTACHMENT=6214;
static const unsigned long APP_TTREE_CHAPTERS=6215;
static const unsigned long APP_TTREE_CHAPTER=6216;
static const unsigned long APP_TTREE_FORCED_SUBTITLES=6211;
static const unsigned long APP_TTREE_HDR_TYPE=6204;
static const unsigned long APP_TTREE_HDR_DESC=6205;
static const unsigned long DVD_TYPE_DISK=6206;
static const unsigned long BRAY_TYPE_DISK=6209;
static const unsigned long HDDVD_TYPE_DISK=6212;
static const unsigned long MKV_TYPE_FILE=6213;
static const unsigned long APP_TTREE_CHAP_DESC=6207;
static const unsigned long APP_TTREE_ANGLE_DESC=6210;
static const unsigned long APP_DVD_MANUAL_TITLE=6220;
static const unsigned long APP_DVD_MANUAL_TEXT=6225;
static const unsigned long APP_DVD_TITLES_COUNT=6221;
static const unsigned long APP_DVD_COUNT_CELLS=6222;
static const unsigned long APP_DVD_COUNT_PGC=6223;
static const unsigned long APP_DVD_BROKEN_TITLE_ENTRY=6224;
static const unsigned long APP_SINGLE_DRIVE_TITLE=6226;
static const unsigned long APP_SINGLE_DRIVE_TEXT=6227;
static const unsigned long APP_SINGLE_DRIVE_ALL=6228;
static const unsigned long APP_SINGLE_DRIVE_CAPTION=6229;
static const unsigned long APP_SI_DRIVEINFO=6300;
static const unsigned long APP_SI_PROFILE=6301;
static const unsigned long APP_SI_MANUFACTURER=6302;
static const unsigned long APP_SI_PRODUCT=6303;
static const unsigned long APP_SI_REVISION=6304;
static const unsigned long APP_SI_SERIAL=6305;
static const unsigned long APP_SI_FIRMWARE=6306;
static const unsigned long APP_SI_FIRDATE=6307;
static const unsigned long APP_SI_BECFLAGS=6308;
static const unsigned long APP_SI_HIGHEST_AACS=6309;
static const unsigned long APP_SI_DISCINFO=6320;
static const unsigned long APP_SI_NODISC=6321;
static const unsigned long APP_SI_DISCLOAD=6322;
static const unsigned long APP_SI_CAPACITY=6323;
static const unsigned long APP_SI_DISCTYPE=6324;
static const unsigned long APP_SI_DISCSIZE=6325;
static const unsigned long APP_SI_DISCRATE=6326;
static const unsigned long APP_SI_DISCLAYERS=6327;
static const unsigned long APP_SI_DISCCBL=6329;
static const unsigned long APP_SI_DISCCBL25=6330;
static const unsigned long APP_SI_DISCCBL27=6331;
static const unsigned long APP_SI_DEVICE=6332;


typedef enum _ApSettingId
{
  apset_Unknown=0,
  apset_dvd_MinimumTitleLength ,
  apset_dvd_TestMTL ,
  apset_dvd_SPRemoveMethod ,
  apset_app_DataDir ,
  apset_app_Key ,
  apset_app_KeyHash ,
  apset_io_ErrorRetryCount ,
  apset_io_IgnoreReadErrors ,
  apset_io_RBufSizeMB ,
  apset_io_TIPS_Server ,
  apset_app_ExpertMode ,
  apset_io_DarwinK2Workaround ,
  apset_fs_ForceIsoForUDF102 ,
  apset_app_DestinationType ,
  apset_app_DestinationDir ,
  apset_app_ShowDebug ,
  apset_app_DebugKey ,
  apset_app_PreferredLanguage ,
  apset_app_BackupDecrypted ,
  apset_app_InterfaceLanguage ,
  apset_app_UpdateEnable ,
  apset_app_UpdateLastCheck ,
  apset_io_SingleDrive ,
  apset_app_ShowAVSyncMessages ,
  apset_bdplus_DumpAlways ,
  apset_deprecated_s_EnableUPNP ,
  apset_deprecated_s_BindIp ,
  apset_deprecated_s_BindPort ,
  apset_screen_geometry ,
  apset_screen_state ,
  apset_app_DefaultProfileName ,
  apset_app_DefaultSelectionString ,
  apset_app_Java ,
  apset_app_ccextractor ,
  apset_app_SiteInfoString ,
  apset_path_OpenFile ,
  apset_path_DestDir ,
  apset_path_BackupDirMRU ,
  apset_path_DestDirMRU ,
  apset_app_DefaultOutputFileName ,
  apset_sdf_Stop ,
  apset_app_Proxy ,
  apset_MaxValue
} ApSettingId;

#endif // APDEFS_H_INCLUDED

