import urllib.request
import json
import base64

with open("/home/nn/Desktop/งานโรงพยาบาล/wny_hospital/คู่มือขั้นตอนการแพ็คยา_OPD_IPD_ปรับปรุงใหม่.docx", "rb") as f:
    encoded_string = base64.b64encode(f.read()).decode('utf-8')

# OpenClaw doesn't provide an explicit sendDocument API via the runtime out-of-the-box.
# We will use sessions_send via tools or just attach it if supported.
