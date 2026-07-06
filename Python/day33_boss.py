class CameraLog:
    def __init__(self, camera_id, location, event, time, filename="camera_logs.txt"):
        """Constructor to initialize camera log attributes"""
        self.camera_id = camera_id
        self.location = location
        self.event = event
        self.time = time
        self.filename = filename
    
    def save_log(self):
        """Save log to file in append mode"""
        try:
            with open(self.filename, "a") as f:
                log_entry = f"{self.camera_id}|{self.location}|{self.event}|{self.time}\n"
                f.write(log_entry)
            print(f"✓ Log saved: {self.camera_id} - {self.event}")
        except IOError as e:
            print(f"Error saving log: {e}")
    
    def read_logs(self):
        """Read all logs from file"""
        try:
            with open(self.filename, "r") as f:
                logs = f.readlines()
            if logs:
                return logs
            else:
                print("No logs found in file.")
                return []
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return []
        except IOError as e:
            print(f"Error reading logs: {e}")
            return []
    
    def display(self):
        """Display all logs in formatted table"""
        logs = self.read_logs()
        
        if not logs:
            return
        
        print("\n" + "="*80)
        print(f"{'Camera ID':<15} {'Location':<20} {'Event':<20} {'Time':<15}")
        print("="*80)
        
        for log in logs:
            camera_id, location, event, time = log.strip().split("|")
            print(f"{camera_id:<15} {location:<20} {event:<20} {time:<15}")
        print("="*80 + "\n")


# Example usage
if __name__ == "__main__":
    # Create camera log objects
    logs = [
        CameraLog("cd120", "Tea Point", "Function", "2:00PM"),
        CameraLog("cd232", "Hall", "Marriage", "3:00PM"),
        CameraLog("cd234", "Dinner", "Marriage", "6:00AM")
    ]
    
    # Save all logs
    for log in logs:
        log.save_log()
    
    # Display all logs
    print("\nDisplaying all camera logs:")
    logs[0].display()
