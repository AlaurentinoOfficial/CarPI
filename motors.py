import smbus

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

def setVelocity(left, right):
    bus.write_i2c_block_data(SLAVE_ADDRESS, 0x01, [left, right, 0b10101010])
