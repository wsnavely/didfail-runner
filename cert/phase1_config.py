import time
import threading
import subprocess
import os.path
import logging

# Misc
phase1_base = os.path.abspath("..")
phase1_lib = phase1_base + "/lib"
sdk_platforms = phase1_lib + "/platforms"
java_bin = "/usr/bin/java" 
log_level = logging.DEBUG 

# Soot configuration
soot_base = phase1_base + "/soot"
soot_cp_list = [
"/jasmin/classes",
"/jasmin/lib/*",
"/heros/bin",
"/heros/*",
"/soot/classes",
"/soot/libs/*"]
soot_classpath = ":".join([soot_base + x for x in soot_cp_list])

# Extract Manifest configuration
manifest_jarpath = phase1_lib + "/AXMLPrinter2.jar"

# Transform configuration
rt_jar = "/usr/lib/jvm/default-java/jre/lib/rt.jar"
apk_transform_bin = phase1_base + "/cert/transformApk/bin"
android_jar = sdk_platforms + "/android-16/android.jar"
transform_classpath = ":".join([soot_classpath, android_jar, rt_jar, apk_transform_bin])
transform_jvm_flags = ["-Xmx2048m"]
transform_timeout = 60 * 15
transform_monitor = True

# FlowDroid Configuration 
fd_base=phase1_base + "/flowdroid"
fd_android_base=fd_base + "/soot-infoflow-android-latest"
fd_cp_list=[
"/soot-infoflow-latest/bin",
"/soot-infoflow-latest/lib/*",
"/soot-infoflow-android-latest/lib/*",
"/soot-infoflow-android-latest/bin"]
fd_classpath = ":".join([fd_base + x for x in fd_cp_list])
fd_classpath = ":".join([fd_classpath, soot_classpath])
fd_jvm_flags = ["-Xmx8192m"]
fd_timeout = 60 * 15
fd_monitor = True

# epicc Configuration
epicc_base = phase1_base + "/epicc"
epicc_classpath = epicc_base + "/android.jar"
epicc_jar = epicc_base + "/epicc-0.1.jar"
epicc_timeout = 60*10
epicc_monitor = False
epicc_jvm_flags = ["-Xmx512m"]

# dare Configuration
dare_base = phase1_base + "/dare-1.1.0-linux"
dare_timeout = 60*10
dare_monitor = False
dare_exec = dare_base + "/dare"
