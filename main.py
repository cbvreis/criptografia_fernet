from flask import Flask, request, jsonify
from loguru import logger
from cryptography.fernet import Fernet

app= Flask(__name__)

@app.route('/cripto', methods=['GET','POST'])
def cripto():
    if(request.args.get("token")):
        try:
            logger.info(f'Request data {request.args.get("token")}...')
            key = b'V-appOSV9wyaBdpMcq4yw47CDU9FSFSl09bg8OiLAn8='
            f = Fernet(key)
            token = f.encrypt(request.args.get("token").encode())
            logger.info(f'Encrypted Data {token}...')
            return jsonify({"status": "success", "message" : "data retrieved successfully", "data": token.decode() })
        except:
            return jsonify({"status": "error", "message" : "data not encrypted"})
    else:
        return jsonify({"status": "error", "message": "not parameter data"})


@app.route('/decode', methods=['GET','POST'])
def decode():
    if (request.args.get("token")):
        try:
            logger.info(f'Request data {request.args.get("token")}...')
            key = b'V-appOSV9wyaBdpMcq4yw47CDU9FSFSl09bg8OiLAn8='
            f = Fernet(key)
            data = f.decrypt(request.args.get("token").encode())
            logger.info(f'Decrypted Data {data}...')
            return jsonify({"status": "success", "message" : "data retrieved successfully", "data": data.decode() })
        except:
            return jsonify({"status": "error", "message" : "data not decrypted"})
    else:
        return jsonify({"status": "error", "message": "not parameter data"})


@app.route('/', methods=['GET','POST'])
def main():
    return jsonify({"status": "error", "message": "404 - Data not Found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)