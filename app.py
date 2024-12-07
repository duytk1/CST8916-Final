import time
import random
from azure.iot.device import IoTHubDeviceClient, Message
from datetime import datetime
import json

def get_stock_data(symbol):
    return {
        'symbol': symbol,
        'price': random.uniform(30.0, 100.0), 
        'timestamp': time.time(),
    }
    
def create_client(connection_string):
    return IoTHubDeviceClient.create_from_connection_string(connection_string)
    
def send_message_azure(client, symbol):
    stock_data = get_stock_data(symbol)
    event_data_batch = client.create_batch()
    event_data_batch.add(Message(json.dumps(stock_data)))
    client.send_batch(event_data_batch) 
    print(f'Sent stock data: {stock_data}')
    
if __name__ == '__main__':
    print('Sending stock data to IoT Hub...')
    # client = create_client('HostName=iothubforassignment.azure-devices.net;DeviceId=Device1;SharedAccessKey=urkO3O+R6tYV0yWCz7wbiDujmzrN28TvY45GjKa1WL8=')
    client = IoTHubDeviceClient.create_from_connection_string("connection_string")
    try:
        while True:
            send_message_azure(client1, 'Dow\'s Lake')
            time.sleep(10)
    except KeyboardInterrupt:
        print('Stopped sending messages.')
    finally:
        client.disconnect()