import base64

MESSAGE = '''
CEQBFBMGHAAQVUFKRV4UERcABEJVU0QRDhwJHBIEBwRXRUNTRBcSBAAcHgYWRlxFXhYFFA4CEQpU Q0hBVwwXEBEXBRkHFRZEXkFXBBobChcXFQgcHRdVQUpFXgYNHg4TDhwXRF5BVxcYEQEbFQNCWUlD VRIRAxxUT1JGFgoWVENIQVcSEB1CVRw= EQ4VQwwYCxMWDFhWWQFCWkhGEgtZXVASABsNDwdPEQ4VQxAYBA4QA1RQEkhFURoAEQpYQEZDRUxI RgAJV1ESSEVRDg4cTxEOFUMSHwZAVBU=
'''
##OUTPUT = {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
KEY = 'scrapeyscrapey'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
  result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))