# To use Anvil, you typically use the Anvil editor online.
import anvil.server

# Replace with your actual Uplink key from the Anvil web editor
# anvil.server.connect("YOUR_UPLINK_KEY_HERE")

@anvil.server.callable
def get_welcome_message(name):
    return f"Hello, {name}! Welcome to the Anvil website."

if __name__ == '__main__':
    print("Anvil background task started (uncomment connect to run).")
    # anvil.server.wait_forever()
