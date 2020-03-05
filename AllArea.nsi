!define PRODUCT_NAME "AllArea"
!define PRODUCT_VERSION "1.3"
!define PRODUCT_PUBLISHER "Dynamic Programming"
!define PRODUCT_WEB_SITE "http://burnedtoast.cu.cc"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\AllArea.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor bzip2

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "AllArea.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
;!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
;!define MUI_WELCOMEPAGE_BITMAP "AllArea-welcome.bmp"
;!define MUI_HEADERIMAGE
;!define MUI_HEADERIMAGE_BITMAP "AllArea-header.bmp"
; License page
!define MUI_LICENSEPAGE_RADIOBUTTONS
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
; Components page
!insertmacro MUI_PAGE_COMPONENTS
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\GUIAllArea.exe"
!insertmacro MUI_PAGE_FINISH

; Branding
BrandingText "Dynamic Programming"
; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; Reserve files
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "AllArea.exe"
InstallDir "$PROGRAMFILES\AllArea"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Function .onInit
  SetOutPath $TEMP
  File /oname=spltmp.bmp "AllAreaSplash.bmp"

; optional
; File /oname=spltmp.wav "my_splash.wav"

  splash::show 1000 $TEMP\spltmp

  Pop $0 ; $0 has '1' if the user closed the splash screen early,
     ; '0' if everything closed normally, and '-1' if some error occurred.

  Delete $TEMP\spltmp.bmp
;  Delete $TEMP\spltmp.wav
FunctionEnd

Section "Executables" SEC01
  SectionIn RO
  SetOutPath "$INSTDIR"
  SetOverwrite try
  File "dist\AllArea.exe"
  File "dist\AllVolume.exe"
  File "dist\bz2.pyd"
  File "dist\GUIAllArea.exe"
  CreateDirectory "$SMPROGRAMS\AllArea"
  CreateShortCut "$SMPROGRAMS\AllArea\AllArea.lnk" "$INSTDIR\GUIAllArea.exe"
  CreateShortCut "$DESKTOP\AllArea.lnk" "$INSTDIR\GUIAllArea.exe"
  CreateShortCut "$STARTMENU\AllArea.lnk" "$INSTDIR\GUIAllArea.exe"
  File "dist\GUIAllVolume.exe"
  CreateShortCut "$DESKTOP\AllVolume.lnk" "$INSTDIR\GUIAllVolume.exe"
  CreateShortCut "$SMPROGRAMS\AllArea\AllVolume.lnk" "$INSTDIR\GUIAllVolume.exe"
  CreateShortCut "$STARTMENU\AllVolume.lnk" "$INSTDIR\GUIAllVolume.exe"
  File "dist\library.zip"
  File "dist\python26.dll"
  File "dist\select.pyd"
  SetOutPath "$INSTDIR\tcl\tcl8.5"
  File "dist\tcl\tcl8.5\auto.tcl"
  File "dist\tcl\tcl8.5\clock.tcl"
  File "dist\tcl\tcl8.5\history.tcl"
  File "dist\tcl\tcl8.5\init.tcl"
  File "dist\tcl\tcl8.5\package.tcl"
  File "dist\tcl\tcl8.5\parray.tcl"
  File "dist\tcl\tcl8.5\safe.tcl"
  File "dist\tcl\tcl8.5\tclIndex"
  File "dist\tcl\tcl8.5\tm.tcl"
  File "dist\tcl\tcl8.5\word.tcl"
  SetOutPath "$INSTDIR\tcl\tk8.5"
  File "dist\tcl\tk8.5\bgerror.tcl"
  File "dist\tcl\tk8.5\button.tcl"
  File "dist\tcl\tk8.5\choosedir.tcl"
  File "dist\tcl\tk8.5\clrpick.tcl"
  File "dist\tcl\tk8.5\comdlg.tcl"
  File "dist\tcl\tk8.5\console.tcl"
  File "dist\tcl\tk8.5\dialog.tcl"
  File "dist\tcl\tk8.5\entry.tcl"
  File "dist\tcl\tk8.5\focus.tcl"
  File "dist\tcl\tk8.5\license.terms"
  File "dist\tcl\tk8.5\listbox.tcl"
  File "dist\tcl\tk8.5\menu.tcl"
  File "dist\tcl\tk8.5\mkpsenc.tcl"
  File "dist\tcl\tk8.5\msgbox.tcl"
  File "dist\tcl\tk8.5\obsolete.tcl"
  File "dist\tcl\tk8.5\optMenu.tcl"
  File "dist\tcl\tk8.5\palette.tcl"
  File "dist\tcl\tk8.5\panedwindow.tcl"
  File "dist\tcl\tk8.5\pkgIndex.tcl"
  File "dist\tcl\tk8.5\safetk.tcl"
  File "dist\tcl\tk8.5\scale.tcl"
  File "dist\tcl\tk8.5\scrlbar.tcl"
  File "dist\tcl\tk8.5\spinbox.tcl"
  File "dist\tcl\tk8.5\tclIndex"
  File "dist\tcl\tk8.5\tearoff.tcl"
  File "dist\tcl\tk8.5\text.tcl"
  File "dist\tcl\tk8.5\tk.tcl"
  File "dist\tcl\tk8.5\tkfbox.tcl"
  SetOutPath "$INSTDIR\tcl\tk8.5\ttk"
  File "dist\tcl\tk8.5\ttk\altTheme.tcl"
  File "dist\tcl\tk8.5\ttk\aquaTheme.tcl"
  File "dist\tcl\tk8.5\ttk\button.tcl"
  File "dist\tcl\tk8.5\ttk\clamTheme.tcl"
  File "dist\tcl\tk8.5\ttk\classicTheme.tcl"
  File "dist\tcl\tk8.5\ttk\combobox.tcl"
  File "dist\tcl\tk8.5\ttk\cursors.tcl"
  File "dist\tcl\tk8.5\ttk\defaults.tcl"
  File "dist\tcl\tk8.5\ttk\entry.tcl"
  File "dist\tcl\tk8.5\ttk\fonts.tcl"
  File "dist\tcl\tk8.5\ttk\menubutton.tcl"
  File "dist\tcl\tk8.5\ttk\notebook.tcl"
  File "dist\tcl\tk8.5\ttk\panedwindow.tcl"
  File "dist\tcl\tk8.5\ttk\progress.tcl"
  File "dist\tcl\tk8.5\ttk\scale.tcl"
  File "dist\tcl\tk8.5\ttk\scrollbar.tcl"
  File "dist\tcl\tk8.5\ttk\sizegrip.tcl"
  File "dist\tcl\tk8.5\ttk\treeview.tcl"
  File "dist\tcl\tk8.5\ttk\ttk.tcl"
  File "dist\tcl\tk8.5\ttk\utils.tcl"
  File "dist\tcl\tk8.5\ttk\winTheme.tcl"
  File "dist\tcl\tk8.5\ttk\xpTheme.tcl"
  SetOutPath "$INSTDIR\tcl\tk8.5"
  File "dist\tcl\tk8.5\unsupported.tcl"
  File "dist\tcl\tk8.5\xmfbox.tcl"
  SetOutPath "$INSTDIR"
  File "dist\tcl85.dll"
  File "dist\tk85.dll"
  File "dist\unicodedata.pyd"
  File "dist\w9xpopen.exe"
  File "dist\_ctypes.pyd"
  File "dist\_tkinter.pyd"
SectionEnd

Section "Development" SEC02
  SetOverwrite ifnewer
  File "AllArea.py"
  File "AllVolume.py"
  File "GUIAllArea.py"
  File "GUIAllVolume.py"
  File "setup.py"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\AllArea\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\AllArea\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\AllArea.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\AllArea.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

; Section descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC01} "The Windows executables for AllArea."
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC02} "The development files for AllArea. To use them you must have Python."
!insertmacro MUI_FUNCTION_DESCRIPTION_END


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\setup.py"
  Delete "$INSTDIR\GUIAllVolume.py"
  Delete "$INSTDIR\GUIAllArea.py"
  Delete "$INSTDIR\AllVolume.py"
  Delete "$INSTDIR\AllArea.py"
  Delete "$INSTDIR\_tkinter.pyd"
  Delete "$INSTDIR\_ctypes.pyd"
  Delete "$INSTDIR\w9xpopen.exe"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\tk85.dll"
  Delete "$INSTDIR\tcl85.dll"
  Delete "$INSTDIR\tcl\tk8.5\xmfbox.tcl"
  Delete "$INSTDIR\tcl\tk8.5\unsupported.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\xpTheme.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\winTheme.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\utils.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\ttk.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\treeview.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\sizegrip.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\scrollbar.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\scale.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\progress.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\panedwindow.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\notebook.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\menubutton.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\fonts.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\entry.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\defaults.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\cursors.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\combobox.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\classicTheme.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\clamTheme.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\button.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\aquaTheme.tcl"
  Delete "$INSTDIR\tcl\tk8.5\ttk\altTheme.tcl"
  Delete "$INSTDIR\tcl\tk8.5\tkfbox.tcl"
  Delete "$INSTDIR\tcl\tk8.5\tk.tcl"
  Delete "$INSTDIR\tcl\tk8.5\text.tcl"
  Delete "$INSTDIR\tcl\tk8.5\tearoff.tcl"
  Delete "$INSTDIR\tcl\tk8.5\tclIndex"
  Delete "$INSTDIR\tcl\tk8.5\spinbox.tcl"
  Delete "$INSTDIR\tcl\tk8.5\scrlbar.tcl"
  Delete "$INSTDIR\tcl\tk8.5\scale.tcl"
  Delete "$INSTDIR\tcl\tk8.5\safetk.tcl"
  Delete "$INSTDIR\tcl\tk8.5\pkgIndex.tcl"
  Delete "$INSTDIR\tcl\tk8.5\panedwindow.tcl"
  Delete "$INSTDIR\tcl\tk8.5\palette.tcl"
  Delete "$INSTDIR\tcl\tk8.5\optMenu.tcl"
  Delete "$INSTDIR\tcl\tk8.5\obsolete.tcl"
  Delete "$INSTDIR\tcl\tk8.5\msgbox.tcl"
  Delete "$INSTDIR\tcl\tk8.5\mkpsenc.tcl"
  Delete "$INSTDIR\tcl\tk8.5\menu.tcl"
  Delete "$INSTDIR\tcl\tk8.5\listbox.tcl"
  Delete "$INSTDIR\tcl\tk8.5\license.terms"
  Delete "$INSTDIR\tcl\tk8.5\focus.tcl"
  Delete "$INSTDIR\tcl\tk8.5\entry.tcl"
  Delete "$INSTDIR\tcl\tk8.5\dialog.tcl"
  Delete "$INSTDIR\tcl\tk8.5\console.tcl"
  Delete "$INSTDIR\tcl\tk8.5\comdlg.tcl"
  Delete "$INSTDIR\tcl\tk8.5\clrpick.tcl"
  Delete "$INSTDIR\tcl\tk8.5\choosedir.tcl"
  Delete "$INSTDIR\tcl\tk8.5\button.tcl"
  Delete "$INSTDIR\tcl\tk8.5\bgerror.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\word.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\tm.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\tclIndex"
  Delete "$INSTDIR\tcl\tcl8.5\safe.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\parray.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\package.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\init.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\history.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\clock.tcl"
  Delete "$INSTDIR\tcl\tcl8.5\auto.tcl"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\python26.dll"
  Delete "$INSTDIR\library.zip"
  Delete "$INSTDIR\GUIAllVolume.exe"
  Delete "$INSTDIR\GUIAllArea.exe"
  Delete "$INSTDIR\bz2.pyd"
  Delete "$INSTDIR\AllVolume.exe"
  Delete "$INSTDIR\AllArea.exe"

  Delete "$SMPROGRAMS\AllArea\Uninstall.lnk"
  Delete "$SMPROGRAMS\AllArea\Website.lnk"
  Delete "$STARTMENU\AllVolume.lnk"
  Delete "$SMPROGRAMS\AllArea\AllVolume.lnk"
  Delete "$DESKTOP\AllVolume.lnk"
  Delete "$STARTMENU\AllArea.lnk"
  Delete "$DESKTOP\AllArea.lnk"
  Delete "$SMPROGRAMS\AllArea\AllArea.lnk"

  RMDir "$SMPROGRAMS\AllArea"
  RMDir "$INSTDIR\tcl\tk8.5\ttk"
  RMDir "$INSTDIR\tcl\tk8.5"
  RMDir "$INSTDIR\tcl\tcl8.5"
  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd