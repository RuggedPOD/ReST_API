from flask import Flask, request
app = Flask(__name__)

mock=1

if mock == 1:
    import service_mock as service
else:
    import service_gpio as service


@app.route("/SetBladeAttentionLEDOn")
def SetBladeAttentionLEDOn():
    if 'bladeId' in request.args:
        return service.SetBladeAttentionLEDOn( request.args['bladeId'] )
    else:
        return 'Set bladeId'

@app.route("/SetBladeAttentionLEDOff")
def SetBladeAttentionLEDOff():
    if 'bladeId' in request.args:
        return service.SetBladeAttentionLEDOff( request.args['bladeId'] )
    else:
        return 'Set bladeId'


if __name__ == "__main__":
    service.init()

    app.run(host= '0.0.0.0')
    app.run()
