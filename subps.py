#!/usr/bin/env  python3
import subprocess



def main():


    try:
        proc = subprocess.run(["cat", "output.txt"], capture_output=True , text = True) #we are using the cat command line tool to view ooutput.txt

        if proc.returncode != 0:
            print(f"The command didnt ran returned ({proc.returncode})")
            print(f"The error: {proc.stderr}")
    
        else:
            try:
                grep = subprocess.run(["grep", "-n" , "POC"], capture_output=True, text = True, input=proc.stdout ) #we have piped the command using the input parameter 

                if grep.returncode == 0:
                    print(grep.stdout)

                elif grep.returncode == 1:
                    print("NO MATCHES")

                else:
                    print(grep.error)

            except subprocess.CalledProcessError as f:
                print (grep.stderr)

    except subprocess.CalledProcessError as e:
        print(grep.stderr)



    




if __name__ == "__main__":
    main()