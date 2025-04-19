import sys
import requests
from xxx import GradientBanner
import time
import sys
import click


def main():
    os_platform = str(sys.platform)

    if "linux" in os_platform.lower():

        if len(sys.argv)<2:
            print("\n python3 xx.py <argument> or use the -h flag to see the help menu")
            sys.exit(1)
        else:
            banner = GradientBanner()
            banner.start(cycles=500)  # This will start the banner animation in the background
            

            print(f"Your OS is running on {os_platform}")


            



            
            
        
        
        # Create and start the banner
       # This will start the banner animation in the background


        try:
           
            # Your program output will appear below the banner
            print("\nStarting main program...")
            time.sleep(2)
            print("Doing some work...")
            time.sleep(2)
            print("Still processing...")
            time.sleep(2)
            print("Almost done...")
            time.sleep(2)
            print("Completed!")
        finally:
            # Make sure to stop the banner when we're done
            banner.stop()
    else:
        print("This tool is designed for linux")

if __name__ == "__main__":
    main()