import subprocess
from datetime import datetime
import os 


timestamp = str(datetime.now())

try:
    absolute_path = os.path.expanduser("~/XXX/{time}")


    main_dir = os.mkdir(absolute_path)
    print(f"path created at {absolute_path}")


except:
    pass




try:
    subfinder = subprocess.run("subfinder", capture_output=True,  )
    with open(timestamp, 'w+') as f:
        f.seek(0)
        for line in subfinder:
            f.write(subfinder.stdout)
            
    
    
except FileNotFoundError:
    print(f"Failed to write {timestamp}")

except Exception as e:
    print(f"Failed {str(e)}")







