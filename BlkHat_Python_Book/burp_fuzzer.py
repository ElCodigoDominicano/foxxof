"""
* FOR DEMONSTATIONAL PURPOSES ONLY *
A Simple Burp Suite extension <Fuzzer>

Note: Burp Suite, Java, and the Jython 2.7 standalone are required on your machine for this to work.
Burp Suite -> http://www.portswigger.net/ 

-AERivas
"""

from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

from java.util import List, ArrayList

import random


class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.registerIntruderPayloadGeneratorFactory(self)

        return

    def getGeneratorName(self):
        return "Simple Payload Generator"

    def createNewInstance(self, attack):
        return Fuzzer(self, attack)
    
# extends the IIntruderPayloadGenerator class
class Fuzzer(IIntruderPayloadGenerator):
    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payloads = 10
        self.num_iterations = 0
        
        return
    
    def hasMorePayloads(self):
        """ This method checks if max iterations have been reached """
        if self.num_iterations == self.max_payloads:
            return False
        else:
            return True

    def getNextPayload(self, current_payload):
        # Convert into string
        payload = "".join(chr(x) for x in current_payload)
        
        # Call the simple mutator to fuzz the POST
        payload = self.mutate_payload(payload)

        # increase the number of fuzzing attempts
        self.num_iterations += 1

        return payload
    
    def reset(self):
        self.num_iterations = 0
        return

    
    def mutate_payload(self, original_payload):
        # pick a simple mutatator or call an external script
        picker = random.randint(1,3)
        
        # select a random offset in the payload to mutate
        offset = random.randint(0, len(original_payload)-1)

        front, back = original_payload[:offset], original_payload[offset:]

        # random offset insert a SQL injection attempt
        if picker == 1:
            front += "'"

        # jam an XSS attempt
        elif picker == 2:
            front += "<script>alert('Simple_Fuzz!');</script>"

        # repeat a random chunck of the original payload
        elif picker == 3:
            chuck_length = random.randint(0, len(back)-1)
            repeater = random.randint(1,10)
            for _ in range(repeater):
                front += original_payload[:offset + chunck_length]
        
        return front + back