# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2013 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#
# This leverages the loki_patch utility created by djrbliss which allows us
# to bypass the bootloader checks on jfltecdma and jflteatt
# See here for more information on loki: https://github.com/djrbliss/loki
#

"""Custom OTA commands for jf devices with locked bootloaders"""

def FullOTA_InstallEnd(info):
  info.script.script = [cmd for cmd in info.script.script if not "boot.img" in cmd]
  info.script.script = [cmd for cmd in info.script.script if not "show_progress(0.100000, 0);" in cmd]
  info.script.Print("Running Loki...");
  info.script.Print(" ");
  info.script.Mount("/system")
  info.script.AppendExtra('package_extract_file("boot.img", "/tmp/boot.img");')
  info.script.AppendExtra('assert(run_program("/sbin/sh", "/tmp/install/bin/loki.sh") == 0);')
  info.script.AppendExtra('ifelse(is_substring("I545", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /tmp/install/vzw/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("L720", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /tmp/install/spr/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("R970", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /tmp/install/r970/* /system/"));')
  info.script.AppendExtra('set_metadata("/system/bin/efsks", "uid", 0, "gid", 0, "mode", 0755);')
  info.script.AppendExtra('set_metadata("/system/bin/ks", "uid", 0, "gid", 0, "mode", 0755);')
  info.script.AppendExtra('set_metadata("/system/bin/qcks", "uid", 0, "gid", 0, "mode", 0755);')
  info.script.AppendExtra('set_metadata("/system/lib/libreference-ril.so", "uid", 0, "gid", 0, "mode", 0644);')
  info.script.AppendExtra('set_metadata("/system/lib/libril.so", "uid", 0, "gid", 0, "mode", 0644);')
  info.script.AppendExtra('set_metadata("/system/lib/libsec-ril.so", "uid", 0, "gid", 0, "mode", 0644);')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libqmi.so", "uid", 0, "gid", 0, "mode", 0644);')
  info.script.AppendExtra('set_metadata("/system/vendor/lib/libqmiservices.so", "uid", 0, "gid", 0, "mode", 0644);')
  info.script.Unmount("/system")
