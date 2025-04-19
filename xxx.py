from colorama import Fore, Style, init, Cursor
import itertools
import os
import time
import threading

# Initialize colorama
init(autoreset=True)

class GradientBanner:
    def __init__(self):
        self.colors = [
            Fore.RED, Fore.YELLOW, Fore.GREEN,
            Fore.CYAN, Fore.BLUE, Fore.MAGENTA
        ]
        self.running = False
        self.thread = None
        self.ascii_art = '''
                  xXx
                   |  
                   |
           ;       |        ,           
         ,;        |         '.         
        ;:         |          :;        
       ::          |           ::       
       ::          |           ::       
       ':          |           :        
        :.         |           :        
     ;' ::         |          ::  '     
    .'  ';         |          ;'  '.    
   ::    :;        |         ;:    ::   
   ;      :;.      |       ,;:     ::   
   :;      :;:     |      ,;"      ::   
   ::.      ':;  ..,.;  ;:'     ,.;:   
    "'"...   '::,::::: ;:   .;.;""'    
        '"""....;:::::;,;.;"""         
    .:::.....'"':::::::'",...;::::;.   
   ;:' '""'"";.,;:::::;.'""""""  ':;   
  ::'         ;::;:::;::..       "SHHHH"  
 ::         ,;:::::::::::;:..       :: 
 ;'     ,;;:;::::::::::::::;";..    ':. 
::     ;:"  ::::::"""'::::::  ":     :: 
 :.    ::   ::::::;  :::::::   :     ; 
  ;    ::   :::::::  :::::::   :    ;  
   '   ::   ::::::....:::::'  ,:   '   
    '  ::    :::::::::::::"   ::       
       ::     ':::::::::"'    ::       
       ':       """""""'      ::       
        ::                   ;:        
        ':;                 ;:"        
-hrr-     ';              ,;'          
            "'           '"     
        '''
        # Calculate banner height for cursor positioning
        self.banner_height = len(self.ascii_art.strip('\n').split('\n'))

    def display(self, cycles=30, delay=0.3):
        lines = self.ascii_art.strip('\n').split('\n')
        color_cycle = itertools.cycle(self.colors)

        # Clear screen once at start and move to top
        print('\033[2J')  # Clear screen
        print('\033[H')   # Move to top
        # Print empty lines for the banner space
        print('\n' * (self.banner_height + 2))
        
        while self.running and cycles > 0:
            # Move cursor to top of console
            print('\033[H', end='')
            
            # Print the banner
            current_colors = list(itertools.islice(color_cycle, len(lines)))
            for line, color in zip(lines, current_colors):
                print(color + line)
            
            # Move cursor below banner for program output
            print('\033[' + str(self.banner_height + 2) + ';0H', end='')
            
            time.sleep(delay)
            cycles -= 1
        
        self.running = False

    def start(self, cycles=30, delay=0.3):
        """Start the banner animation in a separate thread"""
        if self.thread and self.thread.is_alive():
            return  # Already running
        
        self.running = True
        self.thread = threading.Thread(target=self.display, args=(cycles, delay))
        self.thread.daemon = True  # Thread will stop when main program exits
        self.thread.start()

    def stop(self):
        """Stop the banner animation"""
        self.running = False
        if self.thread:
            self.thread.join()  # Wait for the thread to finish

# 🧪 Run it
if __name__ == "__main__":
    banner = GradientBanner()
    banner.start()  # Start the banner animation
    
    # Your other code can run here while the banner is displaying
    # For example:
    time.sleep(5)  # Simulate some work
    print("Your output will appear here!")
    time.sleep(5)  # More work
    
    banner.stop()  # Stop the banner when you're done

