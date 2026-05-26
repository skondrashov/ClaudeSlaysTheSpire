import json, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(30)
sock.connect(('127.0.0.1', 19284))
sock.sendall(json.dumps({'type': 'command', 'command': 'state'}).encode() + b'\n')
data = b''
while True:
    chunk = sock.recv(8192)
    if not chunk:
        break
    data += chunk
    if b'\n' in data:
        break
sock.close()
resp = json.loads(data.decode().strip())
gs = resp.get('game_state', {})
combat = gs.get('combat_state', {})
print('Screen:', gs.get('screen_type'))
print('HP:', gs.get('current_hp'), '/', gs.get('max_hp'))
print('Gold:', gs.get('gold'))
relics = gs.get('relics', [])
print('Relics (%d):' % len(relics))
for r in relics:
    print('  -', r.get('name', r.get('id', '?')))
print('Potions:', [p.get('name', p.get('id', '?')) for p in gs.get('potions', [])])
deck = gs.get('deck', [])
print('Deck (%d):' % len(deck))
for c in deck:
    print('  -', c.get('name', c.get('id', '?')))
print()
print('Energy:', combat.get('energy', 'N/A'))
print('Block:', combat.get('block', 'N/A'))
hand = combat.get('hand', [])
print('Hand (%d cards):' % len(hand))
for i, c in enumerate(hand):
    print('  [%d] %s (cost=%s)' % (i, c['name'], c.get('cost', '?')))
monsters = combat.get('monsters', [])
print('Enemies (%d):' % len(monsters))
for m in monsters:
    intent = m.get('intent', {})
    pows = m.get('powers', [])
    pow_str = ', '.join('%s %s' % (p['name'], p['amount']) for p in pows)
    idx = m.get('monster_index', m.get('index', '?'))
    print('  [%s] %s HP:%d/%d Block:%d Intent:%s Dmg:%s Powers:%s' % (
        idx, m['name'], m['current_hp'], m['max_hp'],
        m.get('block', 0), intent.get('type', '?'), intent.get('damage', '-'),
        pow_str))
