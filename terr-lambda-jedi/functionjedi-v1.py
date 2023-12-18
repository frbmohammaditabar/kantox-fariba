import json

# Example usage
manifest_path = '/home/user01/terr-lambda-jedi/manifest.json'
jedi_id_to_locate = '63421'

def locate_and_safeguard(manifest_path, jedi_id):
    # Load the current manifest from the specified path
    with open(manifest_path, 'r') as manifest_file:
        manifest = json.load(manifest_file)

    # Check if the requested Jedi ID is in the manifest
    if jedi_id in manifest:
        jedi_info = manifest[jedi_id]
        # Safeguard the Jedi's ID as your own encrypted secret
        your_secret = encrypt(jedi_id)
        
        # Log the Jedi information requested by the Council
        print(f"Mission Log - Jedi ID: {your_secret}")
        print(f"Name: {jedi_info['name']}")
        print(f"Planet: {jedi_info['planet']}")
        print(f"Power Level: {jedi_info['power_level']}")
        print("\nMay the Force be with you, Jedi Protector!\n")
    else:
        print(f"Jedi with ID {jedi_id} not found in the manifest.")

# Placeholder function for encryption (you can replace this with your own encryption method)
def encrypt(data):
    return f"Encrypted_{data}"


def main(event, context):
    locate_and_safeguard(manifest_path, jedi_id_to_locate)
