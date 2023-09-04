"""
    This program sends a message to a queue on the RabbitMQ server.
    I've updated the code to hold a variable that contains both what is sent in the message as well as what displays to the user.

    Author: Kim Leach
    Date: 09/03/2023
"""

# Add imports at the beginning of the file
import pika

# Define the message you want to send as a variable
message = "Refactoring"

# Create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))  # Use lowercase "localhost" here

# Use the connection to create a communication channel
ch = conn.channel()

# Use the channel to declare a queue
ch.queue_declare(queue="hello")

# Use the channel to publish the message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)

# Print the message to the console for the user
print(f" [x] Sent '{message}'")

# Close the connection to the server
conn.close()

