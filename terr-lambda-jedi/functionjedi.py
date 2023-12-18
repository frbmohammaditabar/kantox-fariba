import json
import os

def main(event, context):
#    manifest_path = 's3://jedibucketfariba/manifest.json'
  #  manifest_path = "/home/user01/terr-lambda-jedi/manifest.json"
    #jedi_id_to_locate = event['jedi_id']
  # Get the path to the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Specify the full path to manifest.json
    manifest_path = os.path.join(current_dir, 'manifest.json')
    jedi_id_to_locate = '63421' 
    # Placeholder function for encryption (replace with your own encryption method)
    def encrypt(data):
        return f"Encrypted_{data}"

    # Load the current manifest from the specified path
    with open(manifest_path, 'r') as manifest_file:
        manifest = json.load(manifest_file)

    # Check if the requested Jedi ID is in the manifest
    if jedi_id_to_locate in manifest:
        jedi_info = manifest[jedi_id_to_locate]
        # Safeguard the Jedi's ID as your own encrypted secret
        your_secret = encrypt(jedi_id_to_locate)
        
        # Log the Jedi information requested by the Council
        result = {
            "message": "Jedi located and safeguarded.",
            "jedi_id": your_secret,
            "name": jedi_info['name'],
            "planet": jedi_info['planet'],
            "power_level": jedi_info['power_level']
        }
    else:
        result = {"message": f"Jedi with ID {jedi_id_to_locate} not found in the manifest."}

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

