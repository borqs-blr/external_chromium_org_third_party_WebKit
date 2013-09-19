{
  'variables': {
    # Experimental hooks for embedder to provide extra IDL and source files.
    #
    # Note: this is not a supported API. If you rely on this, you will be broken
    # from time to time as the code generator changes in backward incompatible
    # ways.
    'extra_blink_module_idl_files': [],
    'extra_blink_module_files': [],
    'modules_idl_files': [
      '<@(extra_blink_module_idl_files)',
      'crypto/AesCbcParams.idl',
      'crypto/AesKeyGenParams.idl',
      'crypto/Algorithm.idl',
      'crypto/Crypto.idl',
      'crypto/HmacKeyParams.idl',
      'crypto/HmacParams.idl',
      'crypto/Key.idl',
      'crypto/KeyPair.idl',
      'crypto/RsaKeyGenParams.idl',
      'crypto/RsaSsaParams.idl',
      'crypto/SubtleCrypto.idl',
      'crypto/WindowCrypto.idl',
      'crypto/WorkerCrypto.idl',
      'crypto/WorkerGlobalScopeCrypto.idl',
      'device_orientation/DeviceAcceleration.idl',
      'device_orientation/DeviceMotionEvent.idl',
      'device_orientation/DeviceOrientationEvent.idl',
      'device_orientation/DeviceRotationRate.idl',
      'donottrack/NavigatorDoNotTrack.idl',
      'encoding/TextDecoder.idl',
      'encoding/TextEncoder.idl',
      'encryptedmedia/MediaKeyMessageEvent.idl',
      'encryptedmedia/MediaKeyNeededEvent.idl',
      'encryptedmedia/MediaKeySession.idl',
      'encryptedmedia/MediaKeys.idl',
      'filesystem/DOMFileSystem.idl',
      'filesystem/DOMFileSystemSync.idl',
      'filesystem/DataTransferItemFileSystem.idl',
      'filesystem/DirectoryEntry.idl',
      'filesystem/DirectoryEntrySync.idl',
      'filesystem/DirectoryReader.idl',
      'filesystem/DirectoryReaderSync.idl',
      'filesystem/EntriesCallback.idl',
      'filesystem/Entry.idl',
      'filesystem/EntryCallback.idl',
      'filesystem/EntrySync.idl',
      'filesystem/ErrorCallback.idl',
      'filesystem/FileCallback.idl',
      'filesystem/FileEntry.idl',
      'filesystem/FileEntrySync.idl',
      'filesystem/FileSystemCallback.idl',
      'filesystem/FileWriter.idl',
      'filesystem/FileWriterCallback.idl',
      'filesystem/FileWriterSync.idl',
      'filesystem/HTMLInputElementFileSystem.idl',
      'filesystem/Metadata.idl',
      'filesystem/MetadataCallback.idl',
      'filesystem/WindowFileSystem.idl',
      'filesystem/WorkerGlobalScopeFileSystem.idl',
      'gamepad/Gamepad.idl',
      'gamepad/GamepadList.idl',
      'gamepad/NavigatorGamepad.idl',
      'geolocation/Coordinates.idl',
      'geolocation/Geolocation.idl',
      'geolocation/Geoposition.idl',
      'geolocation/NavigatorGeolocation.idl',
      'geolocation/PositionCallback.idl',
      'geolocation/PositionError.idl',
      'geolocation/PositionErrorCallback.idl',
      'imagebitmap/ImageBitmapFactories.idl',
      'imagebitmap/WindowImageBitmapFactories.idl',
      'indexeddb/IDBAny.idl',
      'indexeddb/IDBCursor.idl',
      'indexeddb/IDBCursorWithValue.idl',
      'indexeddb/IDBDatabase.idl',
      'indexeddb/IDBFactory.idl',
      'indexeddb/IDBIndex.idl',
      'indexeddb/IDBKeyRange.idl',
      'indexeddb/IDBObjectStore.idl',
      'indexeddb/IDBOpenDBRequest.idl',
      'indexeddb/IDBRequest.idl',
      'indexeddb/IDBTransaction.idl',
      'indexeddb/IDBVersionChangeEvent.idl',
      'indexeddb/WindowIndexedDatabase.idl',
      'indexeddb/WorkerGlobalScopeIndexedDatabase.idl',
      'mediasource/MediaSource.idl',
      'mediasource/SourceBuffer.idl',
      'mediasource/SourceBufferList.idl',
      'mediasource/URLMediaSource.idl',
      'mediasource/WebKitMediaSource.idl',
      'mediasource/WebKitSourceBuffer.idl',
      'mediasource/WebKitSourceBufferList.idl',
      'mediasource/WindowMediaSource.idl',
      'mediastream/MediaStream.idl',
      'mediastream/MediaStreamEvent.idl',
      'mediastream/MediaStreamTrack.idl',
      'mediastream/MediaStreamTrackEvent.idl',
      'mediastream/MediaStreamTrackSourcesCallback.idl',
      'mediastream/NavigatorMediaStream.idl',
      'mediastream/NavigatorUserMediaError.idl',
      'mediastream/NavigatorUserMediaErrorCallback.idl',
      'mediastream/NavigatorUserMediaSuccessCallback.idl',
      'mediastream/RTCDTMFSender.idl',
      'mediastream/RTCDTMFToneChangeEvent.idl',
      'mediastream/RTCDataChannel.idl',
      'mediastream/RTCDataChannelEvent.idl',
      'mediastream/RTCErrorCallback.idl',
      'mediastream/RTCIceCandidate.idl',
      'mediastream/RTCIceCandidateEvent.idl',
      'mediastream/RTCPeerConnection.idl',
      'mediastream/RTCSessionDescription.idl',
      'mediastream/RTCSessionDescriptionCallback.idl',
      'mediastream/RTCStatsCallback.idl',
      'mediastream/RTCStatsReport.idl',
      'mediastream/RTCStatsResponse.idl',
      'mediastream/SourceInfo.idl',
      'mediastream/URLMediaStream.idl',
      'navigationcontroller/NavigationController.idl',
      'navigationcontroller/NavigatorNavigationController.idl',
      'navigatorcontentutils/NavigatorContentUtils.idl',
      'notifications/Notification.idl',
      'notifications/NotificationCenter.idl',
      'notifications/NotificationPermissionCallback.idl',
      'notifications/WindowNotifications.idl',
      'notifications/WorkerGlobalScopeNotifications.idl',
      'performance/WorkerGlobalScopePerformance.idl',
      'performance/WorkerPerformance.idl',
      'quota/NavigatorStorageQuota.idl',
      'quota/StorageErrorCallback.idl',
      'quota/StorageInfo.idl',
      'quota/StorageQuota.idl',
      'quota/StorageQuotaCallback.idl',
      'quota/StorageUsageCallback.idl',
      'quota/WindowQuota.idl',
      'quota/WorkerNavigatorStorageQuota.idl',
      'speech/SpeechGrammar.idl',
      'speech/SpeechGrammarList.idl',
      'speech/SpeechRecognition.idl',
      'speech/SpeechRecognitionAlternative.idl',
      'speech/SpeechRecognitionError.idl',
      'speech/SpeechRecognitionEvent.idl',
      'speech/SpeechRecognitionResult.idl',
      'speech/SpeechRecognitionResultList.idl',
      'speech/SpeechSynthesis.idl',
      'speech/SpeechSynthesisEvent.idl',
      'speech/SpeechSynthesisUtterance.idl',
      'speech/SpeechSynthesisVoice.idl',
      'speech/WindowSpeechSynthesis.idl',
      'vibration/NavigatorVibration.idl',
      'webaudio/AnalyserNode.idl',
      'webaudio/AudioBuffer.idl',
      'webaudio/AudioBufferCallback.idl',
      'webaudio/AudioBufferSourceNode.idl',
      'webaudio/AudioContext.idl',
      'webaudio/AudioDestinationNode.idl',
      'webaudio/AudioListener.idl',
      'webaudio/AudioNode.idl',
      'webaudio/AudioParam.idl',
      'webaudio/AudioProcessingEvent.idl',
      'webaudio/AudioSourceNode.idl',
      'webaudio/BiquadFilterNode.idl',
      'webaudio/ChannelMergerNode.idl',
      'webaudio/ChannelSplitterNode.idl',
      'webaudio/ConvolverNode.idl',
      'webaudio/DelayNode.idl',
      'webaudio/DynamicsCompressorNode.idl',
      'webaudio/GainNode.idl',
      'webaudio/MediaElementAudioSourceNode.idl',
      'webaudio/MediaStreamAudioDestinationNode.idl',
      'webaudio/MediaStreamAudioSourceNode.idl',
      'webaudio/OfflineAudioCompletionEvent.idl',
      'webaudio/OfflineAudioContext.idl',
      'webaudio/OscillatorNode.idl',
      'webaudio/PannerNode.idl',
      'webaudio/PeriodicWave.idl',
      'webaudio/ScriptProcessorNode.idl',
      'webaudio/WaveShaperNode.idl',
      'webdatabase/Database.idl',
      'webdatabase/DatabaseCallback.idl',
      'webdatabase/DatabaseSync.idl',
      'webdatabase/SQLError.idl',
      'webdatabase/SQLResultSet.idl',
      'webdatabase/SQLResultSetRowList.idl',
      'webdatabase/SQLStatementCallback.idl',
      'webdatabase/SQLStatementErrorCallback.idl',
      'webdatabase/SQLTransaction.idl',
      'webdatabase/SQLTransactionCallback.idl',
      'webdatabase/SQLTransactionErrorCallback.idl',
      'webdatabase/SQLTransactionSync.idl',
      'webdatabase/SQLTransactionSyncCallback.idl',
      'webdatabase/WindowWebDatabase.idl',
      'webdatabase/WorkerGlobalScopeWebDatabase.idl',
      'webmidi/MIDIAccess.idl',
      'webmidi/MIDIAccessPromise.idl',
      'webmidi/MIDIConnectionEvent.idl',
      'webmidi/MIDIErrorCallback.idl',
      'webmidi/MIDIInput.idl',
      'webmidi/MIDIMessageEvent.idl',
      'webmidi/MIDIOutput.idl',
      'webmidi/MIDIPort.idl',
      'webmidi/MIDISuccessCallback.idl',
      'webmidi/NavigatorWebMIDI.idl',
      'websockets/CloseEvent.idl',
      'websockets/WebSocket.idl',
    ],
    'modules_files': [
      '<@(extra_blink_module_files)',
      'crypto/AesCbcParams.cpp',
      'crypto/AesCbcParams.h',
      'crypto/AesKeyGenParams.cpp',
      'crypto/AesKeyGenParams.h',
      'crypto/Algorithm.cpp',
      'crypto/Algorithm.h',
      'crypto/Crypto.cpp',
      'crypto/Crypto.h',
      'crypto/CryptoResult.cpp',
      'crypto/CryptoResult.h',
      'crypto/DOMWindowCrypto.cpp',
      'crypto/DOMWindowCrypto.h',
      'crypto/HmacKeyParams.cpp',
      'crypto/HmacKeyParams.h',
      'crypto/HmacParams.cpp',
      'crypto/HmacParams.h',
      'crypto/Key.cpp',
      'crypto/Key.h',
      'crypto/KeyPair.cpp',
      'crypto/KeyPair.h',
      'crypto/NormalizeAlgorithm.cpp',
      'crypto/NormalizeAlgorithm.h',
      'crypto/RsaKeyGenParams.cpp',
      'crypto/RsaKeyGenParams.h',
      'crypto/RsaSsaParams.cpp',
      'crypto/RsaSsaParams.h',
      'crypto/SubtleCrypto.cpp',
      'crypto/SubtleCrypto.h',
      'crypto/WorkerCrypto.cpp',
      'crypto/WorkerCrypto.h',
      'crypto/WorkerGlobalScopeCrypto.cpp',
      'crypto/WorkerGlobalScopeCrypto.h',
      'device_orientation/DeviceAcceleration.cpp',
      'device_orientation/DeviceAcceleration.h',
      'device_orientation/DeviceMotionController.cpp',
      'device_orientation/DeviceMotionController.h',
      'device_orientation/DeviceMotionData.cpp',
      'device_orientation/DeviceMotionData.h',
      'device_orientation/DeviceMotionDispatcher.cpp',
      'device_orientation/DeviceMotionDispatcher.h',
      'device_orientation/DeviceMotionEvent.cpp',
      'device_orientation/DeviceMotionEvent.h',
      'device_orientation/DeviceOrientationDispatcher.cpp',
      'device_orientation/DeviceOrientationDispatcher.h',
      'device_orientation/DeviceOrientationData.cpp',
      'device_orientation/DeviceOrientationData.h',
      'device_orientation/DeviceOrientationEvent.cpp',
      'device_orientation/DeviceOrientationEvent.h',
      'device_orientation/DeviceRotationRate.cpp',
      'device_orientation/DeviceRotationRate.h',
      'device_orientation/DeviceSensorEventController.cpp',
      'device_orientation/DeviceSensorEventController.h',
      'device_orientation/DeviceSensorEventDispatcher.cpp',
      'device_orientation/DeviceSensorEventDispatcher.h',
      'device_orientation/NewDeviceOrientationController.cpp',
      'device_orientation/NewDeviceOrientationController.h',
      'donottrack/NavigatorDoNotTrack.cpp',
      'donottrack/NavigatorDoNotTrack.h',
      'encoding/TextDecoder.cpp',
      'encoding/TextDecoder.h',
      'encoding/TextEncoder.cpp',
      'encoding/TextEncoder.h',
      'encryptedmedia/MediaKeyMessageEvent.cpp',
      'encryptedmedia/MediaKeyMessageEvent.h',
      'encryptedmedia/MediaKeyNeededEvent.cpp',
      'encryptedmedia/MediaKeyNeededEvent.h',
      'encryptedmedia/MediaKeys.cpp',
      'encryptedmedia/MediaKeys.h',
      'encryptedmedia/MediaKeySession.cpp',
      'encryptedmedia/MediaKeySession.h',
      'filesystem/DOMFilePath.cpp',
      'filesystem/DOMFilePath.h',
      'filesystem/DOMFileSystem.cpp',
      'filesystem/DOMFileSystem.h',
      'filesystem/DOMFileSystemBase.cpp',
      'filesystem/DOMFileSystemBase.h',
      'filesystem/DOMFileSystemSync.cpp',
      'filesystem/DOMFileSystemSync.h',
      'filesystem/DOMWindowFileSystem.cpp',
      'filesystem/DOMWindowFileSystem.h',
      'filesystem/DataTransferItemFileSystem.cpp',
      'filesystem/DataTransferItemFileSystem.h',
      'filesystem/DirectoryEntry.cpp',
      'filesystem/DirectoryEntry.h',
      'filesystem/DirectoryEntrySync.cpp',
      'filesystem/DirectoryEntrySync.h',
      'filesystem/DirectoryReader.cpp',
      'filesystem/DirectoryReader.h',
      'filesystem/DirectoryReaderBase.h',
      'filesystem/DirectoryReaderSync.cpp',
      'filesystem/DirectoryReaderSync.h',
      'filesystem/DraggedIsolatedFileSystem.cpp',
      'filesystem/DraggedIsolatedFileSystem.h',
      'filesystem/EntriesCallback.h',
      'filesystem/Entry.cpp',
      'filesystem/Entry.h',
      'filesystem/EntryBase.cpp',
      'filesystem/EntryBase.h',
      'filesystem/EntryCallback.h',
      'filesystem/EntrySync.cpp',
      'filesystem/EntrySync.h',
      'filesystem/ErrorCallback.h',
      'filesystem/FileCallback.h',
      'filesystem/FileEntry.cpp',
      'filesystem/FileEntry.h',
      'filesystem/FileEntrySync.cpp',
      'filesystem/FileEntrySync.h',
      'filesystem/FileSystemCallback.h',
      'filesystem/FileSystemCallbacks.cpp',
      'filesystem/FileSystemCallbacks.h',
      'filesystem/FileSystemClient.h',
      'filesystem/FileSystemFlags.h',
      'filesystem/FileSystemType.h',
      'filesystem/FileWriter.cpp',
      'filesystem/FileWriter.h',
      'filesystem/FileWriterBase.cpp',
      'filesystem/FileWriterBase.h',
      'filesystem/FileWriterBaseCallback.h',
      'filesystem/FileWriterCallback.h',
      'filesystem/FileWriterSync.cpp',
      'filesystem/FileWriterSync.h',
      'filesystem/HTMLInputElementFileSystem.cpp',
      'filesystem/HTMLInputElementFileSystem.h',
      'filesystem/LocalFileSystem.cpp',
      'filesystem/LocalFileSystem.h',
      'filesystem/Metadata.h',
      'filesystem/MetadataCallback.h',
      'filesystem/SyncCallbackHelper.h',
      'filesystem/WorkerGlobalScopeFileSystem.cpp',
      'filesystem/WorkerGlobalScopeFileSystem.h',
      'filesystem/WorkerLocalFileSystem.cpp',
      'filesystem/WorkerLocalFileSystem.h',
      'gamepad/Gamepad.cpp',
      'gamepad/Gamepad.h',
      'gamepad/GamepadList.cpp',
      'gamepad/GamepadList.h',
      'gamepad/NavigatorGamepad.cpp',
      'gamepad/NavigatorGamepad.h',
      'geolocation/Coordinates.cpp',
      'geolocation/Geolocation.cpp',
      'geolocation/GeolocationController.cpp',
      'geolocation/NavigatorGeolocation.cpp',
      'geolocation/NavigatorGeolocation.h',
      'imagebitmap/ImageBitmapFactories.cpp',
      'imagebitmap/ImageBitmapFactories.h',
      'indexeddb/DOMWindowIndexedDatabase.cpp',
      'indexeddb/DOMWindowIndexedDatabase.h',
      'indexeddb/IDBAny.cpp',
      'indexeddb/IDBAny.h',
      'indexeddb/IDBCallbacks.h',
      'indexeddb/IDBCursor.cpp',
      'indexeddb/IDBCursor.h',
      'indexeddb/IDBCursorBackendInterface.h',
      'indexeddb/IDBCursorWithValue.cpp',
      'indexeddb/IDBCursorWithValue.h',
      'indexeddb/IDBDatabase.cpp',
      'indexeddb/IDBDatabase.h',
      'indexeddb/IDBDatabaseBackendInterface.h',
      'indexeddb/IDBDatabaseCallbacks.h',
      'indexeddb/IDBDatabaseCallbacks.h',
      'indexeddb/IDBDatabaseCallbacksImpl.cpp',
      'indexeddb/IDBDatabaseCallbacksImpl.h',
      'indexeddb/IDBEventDispatcher.cpp',
      'indexeddb/IDBEventDispatcher.h',
      'indexeddb/IDBFactory.cpp',
      'indexeddb/IDBFactory.h',
      'indexeddb/IDBFactoryBackendInterface.h',
      'indexeddb/IDBHistograms.h',
      'indexeddb/IDBIndex.cpp',
      'indexeddb/IDBIndex.h',
      'indexeddb/IDBKey.cpp',
      'indexeddb/IDBKey.h',
      'indexeddb/IDBKeyPath.cpp',
      'indexeddb/IDBKeyPath.h',
      'indexeddb/IDBKeyRange.cpp',
      'indexeddb/IDBKeyRange.h',
      'indexeddb/IDBMetadata.h',
      'indexeddb/IDBObjectStore.cpp',
      'indexeddb/IDBObjectStore.h',
      'indexeddb/IDBOpenDBRequest.cpp',
      'indexeddb/IDBOpenDBRequest.h',
      'indexeddb/IDBPendingTransactionMonitor.cpp',
      'indexeddb/IDBPendingTransactionMonitor.h',
      'indexeddb/IDBRequest.cpp',
      'indexeddb/IDBRequest.h',
      'indexeddb/IDBTracing.h',
      'indexeddb/IDBTransaction.cpp',
      'indexeddb/IDBTransaction.h',
      'indexeddb/IDBVersionChangeEvent.cpp',
      'indexeddb/IDBVersionChangeEvent.h',
      'indexeddb/IndexedDB.h',
      'indexeddb/PageGroupIndexedDatabase.cpp',
      'indexeddb/PageGroupIndexedDatabase.h',
      'indexeddb/WorkerGlobalScopeIndexedDatabase.cpp',
      'indexeddb/WorkerGlobalScopeIndexedDatabase.h',
      'indexeddb/chromium/IDBFactoryBackendInterfaceChromium.cpp',
      'indexeddb/chromium/IDBFactoryBackendInterfaceChromium.h',
      'mediasource/MediaSource.cpp',
      'mediasource/MediaSource.h',
      'mediasource/MediaSourceBase.cpp',
      'mediasource/MediaSourceBase.h',
      'mediasource/MediaSourceRegistry.cpp',
      'mediasource/MediaSourceRegistry.h',
      'mediasource/SourceBuffer.cpp',
      'mediasource/SourceBuffer.h',
      'mediasource/SourceBufferList.cpp',
      'mediasource/SourceBufferList.h',
      'mediasource/URLMediaSource.cpp',
      'mediasource/URLMediaSource.h',
      'mediasource/WebKitMediaSource.cpp',
      'mediasource/WebKitMediaSource.h',
      'mediasource/WebKitSourceBuffer.cpp',
      'mediasource/WebKitSourceBuffer.h',
      'mediasource/WebKitSourceBufferList.cpp',
      'mediasource/WebKitSourceBufferList.h',
      'mediastream/MediaConstraintsImpl.cpp',
      'mediastream/MediaConstraintsImpl.h',
      'mediastream/MediaStream.cpp',
      'mediastream/MediaStream.h',
      'mediastream/MediaStreamEvent.cpp',
      'mediastream/MediaStreamEvent.h',
      'mediastream/MediaStreamRegistry.cpp',
      'mediastream/MediaStreamRegistry.h',
      'mediastream/MediaStreamTrack.cpp',
      'mediastream/MediaStreamTrack.h',
      'mediastream/MediaStreamTrackEvent.cpp',
      'mediastream/MediaStreamTrackEvent.h',
      'mediastream/MediaStreamTrackSourcesCallback.h',
      'mediastream/MediaStreamTrackSourcesRequest.cpp',
      'mediastream/MediaStreamTrackSourcesRequest.h',
      'mediastream/NavigatorMediaStream.cpp',
      'mediastream/NavigatorMediaStream.h',
      'mediastream/NavigatorUserMediaError.h',
      'mediastream/NavigatorUserMediaErrorCallback.h',
      'mediastream/NavigatorUserMediaSuccessCallback.h',
      'mediastream/RTCDTMFSender.cpp',
      'mediastream/RTCDTMFSender.h',
      'mediastream/RTCDTMFToneChangeEvent.cpp',
      'mediastream/RTCDTMFToneChangeEvent.h',
      'mediastream/RTCDataChannel.cpp',
      'mediastream/RTCDataChannel.h',
      'mediastream/RTCDataChannelEvent.cpp',
      'mediastream/RTCDataChannelEvent.h',
      'mediastream/RTCErrorCallback.h',
      'mediastream/RTCIceCandidate.cpp',
      'mediastream/RTCIceCandidate.h',
      'mediastream/RTCIceCandidateEvent.cpp',
      'mediastream/RTCIceCandidateEvent.h',
      'mediastream/RTCPeerConnection.cpp',
      'mediastream/RTCPeerConnection.h',
      'mediastream/RTCSessionDescription.cpp',
      'mediastream/RTCSessionDescription.h',
      'mediastream/RTCSessionDescriptionCallback.h',
      'mediastream/RTCSessionDescriptionRequestImpl.cpp',
      'mediastream/RTCSessionDescriptionRequestImpl.h',
      'mediastream/RTCStatsReport.cpp',
      'mediastream/RTCStatsReport.h',
      'mediastream/RTCStatsRequestImpl.cpp',
      'mediastream/RTCStatsRequestImpl.h',
      'mediastream/RTCStatsResponse.cpp',
      'mediastream/RTCStatsResponse.h',
      'mediastream/RTCVoidRequestImpl.cpp',
      'mediastream/RTCVoidRequestImpl.h',
      'mediastream/SourceInfo.cpp',
      'mediastream/SourceInfo.h',
      'mediastream/UserMediaClient.h',
      'mediastream/UserMediaController.cpp',
      'mediastream/UserMediaController.h',
      'mediastream/UserMediaRequest.cpp',
      'mediastream/UserMediaRequest.h',
      'mediastream/URLMediaStream.cpp',
      'mediastream/URLMediaStream.h',
      'mediastream/WebMediaStreamTrackSourcesRequest.cpp',
      'navigationcontroller/CallbackPromiseAdapter.h',
      'navigationcontroller/NavigationController.cpp',
      'navigationcontroller/NavigationController.h',
      'navigationcontroller/NavigatorNavigationController.cpp',
      'navigationcontroller/NavigatorNavigationController.h',
      'navigatorcontentutils/NavigatorContentUtils.cpp',
      'navigatorcontentutils/NavigatorContentUtils.h',
      'navigatorcontentutils/NavigatorContentUtilsClient.h',
      'notifications/DOMWindowNotifications.cpp',
      'notifications/DOMWindowNotifications.h',
      'notifications/Notification.cpp',
      'notifications/Notification.h',
      'notifications/NotificationCenter.cpp',
      'notifications/NotificationCenter.h',
      'notifications/NotificationController.cpp',
      'notifications/NotificationController.h',
      'notifications/NotificationPermissionCallback.h',
      'notifications/WorkerGlobalScopeNotifications.cpp',
      'notifications/WorkerGlobalScopeNotifications.h',
      'performance/WorkerGlobalScopePerformance.cpp',
      'performance/WorkerGlobalScopePerformance.h',
      'performance/WorkerPerformance.cpp',
      'performance/WorkerPerformance.h',
      'quota/DOMWindowQuota.cpp',
      'quota/DOMWindowQuota.h',
      'quota/NavigatorStorageQuota.cpp',
      'quota/NavigatorStorageQuota.h',
      'quota/StorageInfo.cpp',
      'quota/StorageInfo.h',
      'quota/StorageErrorCallback.cpp',
      'quota/StorageErrorCallback.h',
      'quota/StorageQuota.cpp',
      'quota/StorageQuota.h',
      'quota/StorageQuotaCallback.h',
      'quota/StorageUsageCallback.h',
      'quota/WebStorageQuotaCallbacksImpl.cpp',
      'quota/WebStorageQuotaCallbacksImpl.h',
      'quota/WorkerNavigatorStorageQuota.cpp',
      'quota/WorkerNavigatorStorageQuota.h',
      'speech/DOMWindowSpeechSynthesis.cpp',
      'speech/DOMWindowSpeechSynthesis.h',
      'speech/SpeechGrammar.cpp',
      'speech/SpeechGrammar.h',
      'speech/SpeechGrammarList.cpp',
      'speech/SpeechGrammarList.h',
      'speech/SpeechRecognition.cpp',
      'speech/SpeechRecognition.h',
      'speech/SpeechRecognitionAlternative.cpp',
      'speech/SpeechRecognitionAlternative.h',
      'speech/SpeechRecognitionClient.h',
      'speech/SpeechRecognitionController.cpp',
      'speech/SpeechRecognitionController.h',
      'speech/SpeechRecognitionError.cpp',
      'speech/SpeechRecognitionError.h',
      'speech/SpeechRecognitionEvent.cpp',
      'speech/SpeechRecognitionEvent.h',
      'speech/SpeechRecognitionResult.cpp',
      'speech/SpeechRecognitionResult.h',
      'speech/SpeechRecognitionResultList.cpp',
      'speech/SpeechRecognitionResultList.h',
      'speech/SpeechSynthesis.cpp',
      'speech/SpeechSynthesis.h',
      'speech/SpeechSynthesisEvent.cpp',
      'speech/SpeechSynthesisEvent.h',
      'speech/SpeechSynthesisUtterance.cpp',
      'speech/SpeechSynthesisUtterance.h',
      'speech/SpeechSynthesisVoice.cpp',
      'speech/SpeechSynthesisVoice.h',
      'vibration/NavigatorVibration.cpp',
      'vibration/NavigatorVibration.h',
      'webaudio/AudioBasicInspectorNode.cpp',
      'webaudio/AudioBasicInspectorNode.h',
      'webaudio/AudioBasicProcessorNode.cpp',
      'webaudio/AudioBasicProcessorNode.h',
      'webaudio/AudioBuffer.cpp',
      'webaudio/AudioBuffer.h',
      'webaudio/AudioBufferCallback.h',
      'webaudio/AudioBufferSourceNode.cpp',
      'webaudio/AudioBufferSourceNode.h',
      'webaudio/ChannelMergerNode.cpp',
      'webaudio/ChannelMergerNode.h',
      'webaudio/ChannelSplitterNode.cpp',
      'webaudio/ChannelSplitterNode.h',
      'webaudio/AudioContext.cpp',
      'webaudio/AudioContext.h',
      'webaudio/AudioDestinationNode.cpp',
      'webaudio/AudioDestinationNode.h',
      'webaudio/GainNode.cpp',
      'webaudio/GainNode.h',
      'webaudio/AudioListener.cpp',
      'webaudio/AudioListener.h',
      'webaudio/AudioNode.cpp',
      'webaudio/AudioNode.h',
      'webaudio/AudioNodeInput.cpp',
      'webaudio/AudioNodeInput.h',
      'webaudio/AudioNodeOutput.cpp',
      'webaudio/AudioNodeOutput.h',
      'webaudio/PannerNode.cpp',
      'webaudio/PannerNode.h',
      'webaudio/AudioParam.cpp',
      'webaudio/AudioParam.h',
      'webaudio/AudioParamTimeline.cpp',
      'webaudio/AudioParamTimeline.h',
      'webaudio/AudioProcessingEvent.cpp',
      'webaudio/AudioProcessingEvent.h',
      'webaudio/AudioScheduledSourceNode.cpp',
      'webaudio/AudioScheduledSourceNode.h',
      'webaudio/AudioSourceNode.h',
      'webaudio/AudioSummingJunction.cpp',
      'webaudio/AudioSummingJunction.h',
      'webaudio/AsyncAudioDecoder.cpp',
      'webaudio/AsyncAudioDecoder.h',
      'webaudio/BiquadDSPKernel.cpp',
      'webaudio/BiquadDSPKernel.h',
      'webaudio/BiquadFilterNode.cpp',
      'webaudio/BiquadFilterNode.h',
      'webaudio/BiquadProcessor.cpp',
      'webaudio/BiquadProcessor.h',
      'webaudio/ConvolverNode.cpp',
      'webaudio/ConvolverNode.h',
      'webaudio/DefaultAudioDestinationNode.cpp',
      'webaudio/DefaultAudioDestinationNode.h',
      'webaudio/DelayDSPKernel.cpp',
      'webaudio/DelayDSPKernel.h',
      'webaudio/DelayNode.cpp',
      'webaudio/DelayNode.h',
      'webaudio/DelayProcessor.cpp',
      'webaudio/DelayProcessor.h',
      'webaudio/DynamicsCompressorNode.cpp',
      'webaudio/DynamicsCompressorNode.h',
      'webaudio/ScriptProcessorNode.cpp',
      'webaudio/ScriptProcessorNode.h',
      'webaudio/MediaElementAudioSourceNode.cpp',
      'webaudio/MediaElementAudioSourceNode.h',
      'webaudio/MediaStreamAudioDestinationNode.cpp',
      'webaudio/MediaStreamAudioDestinationNode.h',
      'webaudio/MediaStreamAudioSourceNode.cpp',
      'webaudio/MediaStreamAudioSourceNode.h',
      'webaudio/OfflineAudioCompletionEvent.cpp',
      'webaudio/OfflineAudioCompletionEvent.h',
      'webaudio/OfflineAudioContext.cpp',
      'webaudio/OfflineAudioContext.h',
      'webaudio/OfflineAudioDestinationNode.cpp',
      'webaudio/OfflineAudioDestinationNode.h',
      'webaudio/OscillatorNode.cpp',
      'webaudio/OscillatorNode.h',
      'webaudio/PeriodicWave.cpp',
      'webaudio/PeriodicWave.h',
      'webaudio/RealtimeAnalyser.cpp',
      'webaudio/RealtimeAnalyser.h',
      'webaudio/AnalyserNode.cpp',
      'webaudio/AnalyserNode.h',
      'webaudio/WaveShaperDSPKernel.cpp',
      'webaudio/WaveShaperDSPKernel.h',
      'webaudio/WaveShaperNode.cpp',
      'webaudio/WaveShaperNode.h',
      'webaudio/WaveShaperProcessor.cpp',
      'webaudio/WaveShaperProcessor.h',
      'webdatabase/AbstractDatabaseServer.h',
      'webdatabase/AbstractSQLStatement.h',
      'webdatabase/AbstractSQLStatementBackend.h',
      'webdatabase/ChangeVersionData.h',
      'webdatabase/ChangeVersionWrapper.cpp',
      'webdatabase/ChangeVersionWrapper.h',
      'webdatabase/Database.cpp',
      'webdatabase/DatabaseAuthorizer.cpp',
      'webdatabase/DatabaseAuthorizer.h',
      'webdatabase/DatabaseBackend.cpp',
      'webdatabase/DatabaseBackend.h',
      'webdatabase/DatabaseBackendBase.cpp',
      'webdatabase/DatabaseBackendBase.h',
      'webdatabase/DatabaseBackendContext.cpp',
      'webdatabase/DatabaseBackendContext.h',
      'webdatabase/DatabaseBackendSync.cpp',
      'webdatabase/DatabaseBackendSync.h',
      'webdatabase/DatabaseBase.cpp',
      'webdatabase/DatabaseBase.h',
      'webdatabase/DatabaseBasicTypes.h',
      'webdatabase/DatabaseCallback.h',
      'webdatabase/DatabaseContext.cpp',
      'webdatabase/DatabaseContext.h',
      'webdatabase/DatabaseError.h',
      'webdatabase/DatabaseManager.cpp',
      'webdatabase/DatabaseManager.h',
      'webdatabase/DatabaseObserver.h',
      'webdatabase/DatabaseServer.cpp',
      'webdatabase/DatabaseServer.h',
      'webdatabase/DatabaseSync.cpp',
      'webdatabase/DatabaseSync.h',
      'webdatabase/DatabaseTask.cpp',
      'webdatabase/DatabaseTask.h',
      'webdatabase/DatabaseThread.cpp',
      'webdatabase/DatabaseThread.h',
      'webdatabase/DatabaseTracker.cpp',
      'webdatabase/DatabaseTracker.h',
      'webdatabase/DOMWindowWebDatabase.cpp',
      'webdatabase/DOMWindowWebDatabase.h',
      'webdatabase/QuotaTracker.cpp',
      'webdatabase/QuotaTracker.h',
      'webdatabase/SQLCallbackWrapper.h',
      'webdatabase/SQLError.cpp',
      'webdatabase/SQLError.h',
      'webdatabase/SQLResultSet.cpp',
      'webdatabase/SQLResultSetRowList.cpp',
      'webdatabase/SQLStatement.cpp',
      'webdatabase/SQLStatement.h',
      'webdatabase/SQLStatementBackend.cpp',
      'webdatabase/SQLStatementBackend.h',
      'webdatabase/SQLStatementSync.cpp',
      'webdatabase/SQLStatementSync.h',
      'webdatabase/SQLTransaction.cpp',
      'webdatabase/SQLTransaction.h',
      'webdatabase/SQLTransactionBackend.cpp',
      'webdatabase/SQLTransactionBackend.h',
      'webdatabase/SQLTransactionBackendSync.cpp',
      'webdatabase/SQLTransactionBackendSync.h',
      'webdatabase/SQLTransactionClient.cpp',
      'webdatabase/SQLTransactionClient.h',
      'webdatabase/SQLTransactionCoordinator.cpp',
      'webdatabase/SQLTransactionCoordinator.h',
      'webdatabase/SQLTransactionState.h',
      'webdatabase/SQLTransactionStateMachine.cpp',
      'webdatabase/SQLTransactionStateMachine.h',
      'webdatabase/SQLTransactionSync.cpp',
      'webdatabase/SQLTransactionSync.h',
      'webdatabase/SQLTransactionSyncCallback.h',
      'webdatabase/WorkerGlobalScopeWebDatabase.cpp',
      'webdatabase/WorkerGlobalScopeWebDatabase.h',
      'webmidi/MIDIAccess.cpp',
      'webmidi/MIDIAccess.h',
      'webmidi/MIDIAccessPromise.cpp',
      'webmidi/MIDIAccessPromise.h',
      'webmidi/MIDIClient.h',
      'webmidi/MIDIController.cpp',
      'webmidi/MIDIController.h',
      'webmidi/MIDIConnectionEvent.h',
      'webmidi/MIDIErrorCallback.h',
      'webmidi/MIDIInput.cpp',
      'webmidi/MIDIInput.h',
      'webmidi/MIDIMessageEvent.h',
      'webmidi/MIDIOptions.h',
      'webmidi/MIDIOutput.cpp',
      'webmidi/MIDIOutput.h',
      'webmidi/MIDIPort.cpp',
      'webmidi/MIDIPort.h',
      'webmidi/MIDISuccessCallback.h',
      'webmidi/NavigatorWebMIDI.cpp',
      'webmidi/NavigatorWebMIDI.h',
      'websockets/CloseEvent.h',
      'websockets/MainThreadWebSocketChannel.cpp',
      'websockets/MainThreadWebSocketChannel.h',
      'websockets/NewWebSocketChannelImpl.cpp',
      'websockets/NewWebSocketChannelImpl.h',
      'websockets/ThreadableWebSocketChannelClientWrapper.cpp',
      'websockets/ThreadableWebSocketChannelClientWrapper.h',
      'websockets/WebSocket.cpp',
      'websockets/WebSocket.h',
      'websockets/WebSocketChannel.cpp',
      'websockets/WebSocketChannel.h',
      'websockets/WebSocketChannelClient.h',
      'websockets/WebSocketDeflateFramer.cpp',
      'websockets/WebSocketDeflateFramer.h',
      'websockets/WebSocketDeflater.cpp',
      'websockets/WebSocketDeflater.h',
      'websockets/WebSocketExtensionDispatcher.cpp',
      'websockets/WebSocketExtensionDispatcher.h',
      'websockets/WebSocketExtensionProcessor.h',
      'websockets/WebSocketExtensionParser.cpp',
      'websockets/WebSocketExtensionParser.h',
      'websockets/WebSocketFrame.cpp',
      'websockets/WebSocketFrame.h',
      'websockets/WebSocketHandshake.cpp',
      'websockets/WebSocketHandshake.h',
      'websockets/WebSocketHandshakeRequest.cpp',
      'websockets/WebSocketHandshakeRequest.h',
      'websockets/WebSocketHandshakeResponse.cpp',
      'websockets/WebSocketHandshakeResponse.h',
      'websockets/WebSocketPerMessageDeflate.cpp',
      'websockets/WebSocketPerMessageDeflate.h',
      'websockets/WorkerThreadableWebSocketChannel.cpp',
      'websockets/WorkerThreadableWebSocketChannel.h',
    ],
    'modules_unittest_files': [
      'indexeddb/IDBDatabaseTest.cpp',
      'indexeddb/IDBKeyPathTest.cpp',
      'indexeddb/IDBRequestTest.cpp',
      'indexeddb/IDBTransactionTest.cpp',
      'websockets/WebSocketDeflaterTest.cpp',
      'websockets/WebSocketExtensionDispatcherTest.cpp',
      'websockets/WebSocketExtensionParserTest.cpp',
      'websockets/WebSocketPerMessageDeflateTest.cpp',
    ],
  },
}
