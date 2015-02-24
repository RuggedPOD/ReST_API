
import RPi.GPIO as GPIO
from lxml import etree

ledTable={'1' : 7,
          '2' : 12
         }

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    # Set all led in Output
    for led in ledTable:
        GPIO.setup(ledTable[ led ], GPIO.OUT)

def SetBladeAttentionLEDOn( bladeId ):
    GPIO.output( ledTable[ bladeId ], True)
    response = etree.Element('BladeResponse')
    etree.SubElement(response, 'CompletionCode').text = 'Success'
    etree.SubElement(response, 'statusDescription').text = ''
    etree.SubElement(response, 'apiVersion').text = '1'
    etree.SubElement(response, 'bladeNumber').text = bladeId
    return etree.tostring(response, pretty_print=True)


def SetBladeAttentionLEDOff( bladeId ):
    GPIO.output( ledTable[ bladeId ], False)
    response = etree.Element('BladeResponse')
    etree.SubElement(response, 'CompletionCode').text = 'Success'
    etree.SubElement(response, 'statusDescription').text = ''
    etree.SubElement(response, 'apiVersion').text = '1'
    etree.SubElement(response, 'bladeNumber').text = bladeId
    return etree.tostring(response, pretty_print=True)

