import base64, zlib, json
from pprint import pprint

print("Colle le code d'invitation Base64 :")
code = input("> ").strip()

if not code.startswith("dc"):
    print("Code invalide : préfixe incorrect")
    exit(1)

try:
    raw = base64.b64decode(code, validate=True)
    data = json.loads(zlib.decompress(raw, -15).decode("utf-8"))
    if not all(k in data for k in ("HostName", "HostUuid", "ServerName", "Candidates")):
        raise ValueError("Structure JSON inattendue")
    pprint(data, sort_dicts=False)
except Exception as e:
    print("Code invalide ou corrompu :", e)
