# This file is generated by gyp; do not edit.

include $(CLEAR_VARS)

LOCAL_MODULE_CLASS := GYP
LOCAL_MODULE := third_party_WebKit_Source_core_generate_test_support_idls_gyp
LOCAL_MODULE_STEM := generate_test_support_idls
LOCAL_MODULE_SUFFIX := .stamp
LOCAL_MODULE_TAGS := optional
gyp_intermediate_dir := $(call local-intermediates-dir)
gyp_shared_intermediate_dir := $(call intermediates-dir-for,GYP,shared)

# Make sure our deps are built first.
GYP_TARGET_DEPENDENCIES :=

### Rules for action "Settings":
$(gyp_shared_intermediate_dir)/blink/SettingsMacros.h: gyp_local_path := $(LOCAL_PATH)
$(gyp_shared_intermediate_dir)/blink/SettingsMacros.h: gyp_intermediate_dir := $(abspath $(gyp_intermediate_dir))
$(gyp_shared_intermediate_dir)/blink/SettingsMacros.h: gyp_shared_intermediate_dir := $(abspath $(gyp_shared_intermediate_dir))
$(gyp_shared_intermediate_dir)/blink/SettingsMacros.h: export PATH := $(subst $(ANDROID_BUILD_PATHS),,$(PATH))
$(gyp_shared_intermediate_dir)/blink/SettingsMacros.h: $(LOCAL_PATH)/third_party/jinja2/__init__.py $(LOCAL_PATH)/third_party/markupsafe/__init__.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/hasher.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/in_file.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/in_generator.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/license.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/name_macros.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/name_utilities.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/template_expander.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/macros.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/make_settings.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/InternalSettingsGenerated.idl.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/InternalSettingsGenerated.cpp.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/InternalSettingsGenerated.h.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/SettingsMacros.h.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/core/frame/Settings.in $(GYP_TARGET_DEPENDENCIES)
	@echo "Gyp action: third_party_WebKit_Source_core_core_derived_sources_gyp_generate_test_support_idls_target_Settings ($@)"
	$(hide)cd $(gyp_local_path)/third_party/WebKit/Source/core; mkdir -p $(gyp_shared_intermediate_dir)/blink; python ../build/scripts/make_settings.py frame/Settings.in --output_dir "$(gyp_shared_intermediate_dir)/blink"

$(gyp_shared_intermediate_dir)/blink/InternalSettingsGenerated.idl: $(gyp_shared_intermediate_dir)/blink/SettingsMacros.h ;
$(gyp_shared_intermediate_dir)/blink/InternalSettingsGenerated.cpp: $(gyp_shared_intermediate_dir)/blink/SettingsMacros.h ;
$(gyp_shared_intermediate_dir)/blink/InternalSettingsGenerated.h: $(gyp_shared_intermediate_dir)/blink/SettingsMacros.h ;

### Rules for action "InternalRuntimeFlags":
$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl: gyp_local_path := $(LOCAL_PATH)
$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl: gyp_intermediate_dir := $(abspath $(gyp_intermediate_dir))
$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl: gyp_shared_intermediate_dir := $(abspath $(gyp_shared_intermediate_dir))
$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl: export PATH := $(subst $(ANDROID_BUILD_PATHS),,$(PATH))
$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl: $(LOCAL_PATH)/third_party/jinja2/__init__.py $(LOCAL_PATH)/third_party/markupsafe/__init__.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/hasher.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/in_file.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/in_generator.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/license.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/name_macros.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/name_utilities.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/template_expander.py $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/macros.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/make_internal_runtime_flags.py $(LOCAL_PATH)/third_party/WebKit/Source/platform/RuntimeEnabledFeatures.in $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/InternalRuntimeFlags.h.tmpl $(LOCAL_PATH)/third_party/WebKit/Source/build/scripts/templates/InternalRuntimeFlags.idl.tmpl $(GYP_TARGET_DEPENDENCIES)
	@echo "Gyp action: third_party_WebKit_Source_core_core_derived_sources_gyp_generate_test_support_idls_target_InternalRuntimeFlags ($@)"
	$(hide)cd $(gyp_local_path)/third_party/WebKit/Source/core; mkdir -p $(gyp_shared_intermediate_dir)/blink; python ../build/scripts/make_internal_runtime_flags.py ../platform/RuntimeEnabledFeatures.in --output_dir "$(gyp_shared_intermediate_dir)/blink"

$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.h: $(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl ;


GYP_GENERATED_OUTPUTS := \
	$(gyp_shared_intermediate_dir)/blink/SettingsMacros.h \
	$(gyp_shared_intermediate_dir)/blink/InternalSettingsGenerated.idl \
	$(gyp_shared_intermediate_dir)/blink/InternalSettingsGenerated.cpp \
	$(gyp_shared_intermediate_dir)/blink/InternalSettingsGenerated.h \
	$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.idl \
	$(gyp_shared_intermediate_dir)/blink/InternalRuntimeFlags.h

# Make sure our deps and generated files are built first.
LOCAL_ADDITIONAL_DEPENDENCIES := $(GYP_TARGET_DEPENDENCIES) $(GYP_GENERATED_OUTPUTS)

### Rules for final target.
# Add target alias to "gyp_all_modules" target.
.PHONY: gyp_all_modules
gyp_all_modules: third_party_WebKit_Source_core_generate_test_support_idls_gyp

# Alias gyp target name.
.PHONY: generate_test_support_idls
generate_test_support_idls: third_party_WebKit_Source_core_generate_test_support_idls_gyp

LOCAL_MODULE_PATH := $(PRODUCT_OUT)/gyp_stamp
LOCAL_UNINSTALLABLE_MODULE := true

include $(BUILD_SYSTEM)/base_rules.mk

$(LOCAL_BUILT_MODULE): $(LOCAL_ADDITIONAL_DEPENDENCIES)
	$(hide) echo "Gyp timestamp: $@"
	$(hide) mkdir -p $(dir $@)
	$(hide) touch $@
