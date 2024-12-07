import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

def get_stock_data(name):
    return {
        'name': name,
        'price': random.uniform(30.0, 100.0), 
        'timestamp': time.time(),
    }

def send_message_azure(client, symbol):
    stock_data = get_stock_data(symbol)
    message = Message(str(stock_data))
    client.send_message(message)
    print(f'Sent stock data: {stock_data}')
    
if __name__ == '__main__':
    print('Sending stock data to IoT Hub...')
    client = IoTHubDeviceClient.create_from_connection_string("HostName=iothubfinal.azure-devices.net;DeviceId=Device1;SharedAccessKey=n0ap3gt1E/xXFx8wkYj22CVdwfDPM2CsQI13pm4PgPA=")
    try:
        while True:
            send_message_azure(client, 'Algonquin College')
            time.sleep(10)
    except KeyboardInterrupt:
        print('Stopped sending messages.')
    finally:
        client.disconnect()