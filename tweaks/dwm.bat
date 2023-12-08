Reg.exe add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MinAnimate" /t REG_SZ /d "0" /f
    Reg.exe add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MaxAnimate" /t REG_SZ /d "0" /f
    Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ExtendedUIHoverTime" /t REG_DWORD /d "196608" /f
    Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DontPrettyPath" /t REG_DWORD /d "1" /f
    Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ListviewShadow" /t REG_DWORD /d "0" /f
    Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "TaskbarAnimations" /t REG_DWORD /d "0" /f
    Reg.exe add "HKCU\Software\Microsoft\Windows\DWM" /v "EnableAeroPeek" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DWM" /v "DWMWA_TRANSITIONS_FORCEDISABLED" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DWM" /v "DisallowAnimations" /t REG_DWORD /d "1" /f
    Reg.exe add "HKCR\Paint.Picture\DefaultIcon" /ve /t REG_SZ /d "%%1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "DisableTaggedEnergyLogging" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxApplication" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxTagPerApplication" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "EnergyEstimationEnabled" /t REG_DWORD /d "0" /f
    Reg.exe add "HKCU\Control Panel\Desktop" /v "FontSmoothing" /t REG_SZ /d "2" /f
    Reg.exe add "HKCU\Control Panel\Desktop" /v "FontSmoothingType" /t REG_DWORD /d "2" /f
    Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView" /v "AllUpView" /t REG_DWORD /d "0" /f
    Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView" /v "Remove TaskView" /t REG_DWORD /d "1" /f
    Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer" /v "AltTabSettings" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel" /v "DisableExceptionChainValidation" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel" /v "KernelSEHOPEnabled" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel" /v "UseNormalStack" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel" /v "UseNewEaBuffering" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel" /v "StackSubSystemStackSize" /t REG_DWORD /d "65536" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel" /v "SystemResponsivenessReserved" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnableUserModeCache" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnableLowLatencyIo" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnableFsCacheHost" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableSystemPTEWriteBack" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "KernelStackSize" /t REG_DWORD /d "8192" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "PfnMaxLookahead" /t REG_DWORD /d "16" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "LatencyMode" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnableLowMemoryKiller" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "CpuRelaxedSpeculation" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableDynamicTick" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DynamicTick" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnergyDriverPolicy" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnergyDriverPolicyVideo" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TimerBResolution" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TimerMinResolution" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TimerReliability" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "KernelIoPriority" /t REG_DWORD /d "3" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableLowQosTimerResolution" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "SerializeTimerExpiration" /t REG_DWORD /d "2" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TimerCheckFlags" /t REG_DWORD /d "8" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "SplitLargeCaches" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "SchedulerAssistThreadFlagOverride" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "GlobalTimerResolutionRequests" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "EnablePerCpuClockTickScheduling" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "CacheErrataOverride" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "CacheAwareScheduling" /t REG_DWORD /d "5" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ForceApicPhysicalDestinationMode" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TscInvariant" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ForceClockSync" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TscSyncPolicy" /t REG_DWORD /d "2" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "TscAdjustDisable" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ContextNoPatchMode" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableTsx" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableLowQosTimerResolution" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "KernelSEHOPEnabled" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "CoalescingTimerInterval" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DebugPollInterval" /t REG_DWORD /d "1000" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "RebalanceMinPriority" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "MaxDynamicTickDuration" /t REG_DWORD /d "10" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "MaximumDpcQueueDepth" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "MaximumDpcRate" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "MaximumSharedReadyQueueSize" /t REG_DWORD /d "128" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "BufferSize" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "IoQueueWorkItem" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "IoQueueWorkItemToNode" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "IoQueueWorkItemEx" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "IoQueueThreadIrp" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ExTryQueueWorkItem" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ExQueueWorkItem" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "IoEnqueueIrp" /t REG_DWORD /d "32" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableVsyncLatencyUpdate" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "ExitLatencyCheckEnabled" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "LatencyToleranceVSyncEnabled" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableLowQosTimerResolution" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "XMMIZeroingEnable" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "EnableDWMShaderIntercept" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "AllowFlipInModal" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DwmTearingPolicy" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "MsaaQualityMode" /t REG_DWORD /d "3" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DwmMaxQueuedBuffers" /t REG_DWORD /d "6" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "MaxD3D9BatchSize" /t REG_DWORD /d "4132" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "UseDDIForRendering" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "UseOcclusion" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DisallowMouseDirectionOptin" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "ForceDirectDrawSuppression" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DwmIommuEnabled" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "ForceVBlankFlipEx" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DWMUseAlternateSolutionForRefreshIncrements" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DWMUseGPUForWindowAnimations" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "UseDesktopDuplicationAPIs" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DWMInputBoosted" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "ParallelModePolicy" /t REG_DWORD /d "2" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "ImageProcessing8bit" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "InteractionOutputPredictionDisabled" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "EnableImageProcessing" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "EnableFrontBufferRenderChecks" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "ResampleModeOverride" /t REG_DWORD /d "2" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "ResampleInLinearSpace" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "OverlayTestMode" /t REG_DWORD /d "5" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "DwmPresentationInterval" /t REG_DWORD /d "2" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "CompositionPolicy" /t REG_DWORD /d "0" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "UseDefaultComposition" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm" /v "UseHWInput" /t REG_DWORD /d "1" /f
    Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\Dwm\ExtendedComposition" /v "ExclusiveModeFramerateThresholdPercent" /t REG_DWORD /d "250" /f